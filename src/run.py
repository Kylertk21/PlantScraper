from app import create_app
from app import MQTTBroker
import threading

app = create_app()

if __name__ == '__main__':
    broker = MQTTBroker()
    threading.Thread(target=broker.run, daemon=True).start()
    app.run(debug=True, host='0.0.0.0')
