import logging
import random
import sys
import time
from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import paho.mqtt.client as mqtt

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

FIRST_RECONNECT_DELAY = 1
RECONNECT_RATE = 2
MAX_RECONNECT_COUNT = 12
MAX_RECONNECT_DELAY = 60

broker = '192.168.0.19'
tcp_port = 1883
websocket_port = 8083
ssl_tls_port = 8883
secure_websocket_port = 8084
topic = "sensor/basil"
client_id = f'python-mqtt-{random.randint(0,1000)}'

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    db_path = os.path.join(BASE_DIR, 'data.sqlite')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    db.init_app(app)

    from . import models
    from .routes import routes

    app.register_blueprint(routes)

    with app.app_context():
        db.create_all()

    return app


class MQTTBroker:
    def on_disconnect(self, client, userdata, reason_code):
        logging.info(f"Disconnected with code: {reason_code}")
        reconnect_count, reconnect_delay = 0, FIRST_RECONNECT_DELAY
        while reconnect_count < MAX_RECONNECT_COUNT:
            logging.info(f"Reconnecting in {reconnect_delay} seconds...")
            time.sleep(reconnect_delay)

            try:
                client.reconnect()
                logging.info(f"Reconnected at {datetime.now}")
                return
            except Exception as e:
                logging.error(f"Reconnect failed with {e}, retrying...")

            reconnect_delay *= RECONNECT_RATE
            reconnect_delay = min(reconnect_delay, MAX_RECONNECT_DELAY)
            reconnect_count += 1

        logging.info(f"Reconnect failed after {reconnect_count} attempts. Terminating...")


    def connect_mqtt(self):
        def on_connect(connecting_client, userdata, flags, reason_code, properties):
            if reason_code == 0:
                print("Connected to broker")
                connecting_client.subscribe(topic)
            else:
                print("Connection failed, code %d\n", reason_code)

        client = mqtt.Client(
            client_id=client_id,
            callback_api_version=mqtt.CallbackAPIVersion.VERSION2
        )
        client.on_connect = on_connect
        client.on_message = self.on_message
        client.connect(broker, tcp_port)
        client.on_disconnect = self.on_disconnect
        return client

    def on_message(self, subscribing_client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}`")


    def run(self):
        client = self.connect_mqtt()
        client.loop_forever()

