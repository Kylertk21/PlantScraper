import unittest
from app import create_app, db
from flask import json

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_sensor_post(self):
        payload = {
            "sensor_id": "test-123",
            "readings": {
                "sunlight": "Full Sun",
                "water": "Moist"
            }
        }

        response = self.client.post(
            "/api/sensor",
            data=json.dumps(payload),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn("Sensor data saved", response.get_data(as_text=True))

    def test_get_sensor_not_found(self):
        response = self.client.get("/api/sensor/unknown-id")
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
