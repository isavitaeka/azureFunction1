Sure! Here's how you can write a test case for the provided Azure Function using Python's `unittest` framework and the `requests` library to simulate HTTP requests:

First, ensure you have the `requests` library installed. You can install it using pip if you haven't already:

```bash
pip install requests
```

Next, you can create a test file, for example, `test_function.py`, with the following content:

```python
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
```

In this example:
- The `test_get_details_with_query_params` method tests the function with query parameters `name` and `job`.
- The `test_get_details_without_query_params` method tests the function without any query parameters.

Make sure your Azure Function is running locally on port 7071 before executing these tests. If your function is hosted elsewhere, update the URL accordingly.

To run the tests, simply execute the test file:

```bash
python test_function.py
```

This will run the test cases and provide you with the results.

Would you like any further assistance with this?