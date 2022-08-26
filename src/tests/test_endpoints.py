#!/usr/bin/env python3
import unittest
from os import environ

from ..file_client.api.flask_config.flask_setup import app
from ..file_client.api.flask_config.api_setup import add_resources

# Running function to add api endpoints
add_resources()

host = environ.get('FLASK_HOST')
port = environ.get('FLASK_HOST')


class FlaskTestCase(unittest.TestCase):

    def testReadEndpoint(self):
        """
        Tests for Read endpoint - GET MESSAGE - VALID REQUEST
        """
        with app.test_client() as tester:
            try:
                response = tester.get(f"{host}:{port}/read/1", headers={"Content-Type": "application/json"})
                response_message = response.__dict__["_status"] # Response message details
                response_status_code = response.status_code # Status code

                print("\nTest case: Testing Read endpoint - GET MESSAGE - VALID REQUEST")
                print("Reponse message: ", response_message)
                print("Reponse status: ", response_status_code)

                # Assert test to check if we got status code that we expected
                self.assertEqual(response_status_code, 200) # (Status code you got, Status code you expect)

            except AssertionError as e:
                # Print assertion error
                print("Error: ", e)

    def testStatEndpoint(self):
        """
        Tests for Stat endpoint - GET MESSAGE - VALID REQUEST
        """
        with app.test_client() as tester:
            try:
                response = tester.get(f"{host}:{port}/stat/1", headers={"Content-Type": "application/json"})
                response_message = response.__dict__["_status"] # Response message details
                response_status_code = response.status_code # Status code

                print("\nTest case: Testing Stat endpoint - GET MESSAGE - VALID REQUEST")
                print("Reponse message: ", response_message)
                print("Reponse status: ", response_status_code)

                # Assert test to check if we got status code that we expected
                self.assertEqual(response_status_code, 200) # (Status code you got, Status code you expect)

            except AssertionError as e:
                # Print assertion error
                print("Error: ", e)

if __name__ == "__main__":
    unittest.main()
