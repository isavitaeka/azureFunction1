import unittest
import requests

class TestAzureFunction(unittest.TestCase):

    def test_get_details_with_query_params(self):
        response = requests.get('http://localhost:7071/api/GetDetails', params={'name': 'John', 'job': 'Developer'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Hello, John with job as Developer. This HTTP triggered function executed successfully.")

    def test_get_details_without_query_params(self):
        response = requests.get('http://localhost:7071/api/GetDetails')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "This HTTP triggered function executed successfully. Pass a name and job in the query string or in the request body for a personalized response.")

if __name__ == '__main__':
    unittest.main()