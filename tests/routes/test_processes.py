from rest_framework import status
from rest_framework.test import APITestCase
from seed.tests.util_test import fill_test_database


class TestProcesses(APITestCase):

    def setUp(self):
        fill_test_database()

        # Create dummy test cases for test characters
        self.client.post('/api/processes/',
                         {"input": 1, "result": "I", "user_id": 1})
        self.client.post('/api/processes/',
                         {"input": 799, "result": "DCCXCIX", "user_id": 1})
        self.client.post('/api/processes/',
                         {"input": 3999, "result": "MMMCMXCIX", "user_id": 1})
        self.client.post('/api/processes/',
                         {"input": 1994, "result": "MCMXCIV", "user_id": 1})

    def test_decimal_to_roman(self):
        input_1 = {"input": 1, "user_id": 1}
        response_1 = self.client.post(
            '/api/processes/decimal_to_roman/', input_1)
        output_1 = "I"
        self.assertEqual(response_1.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_1.data, output_1)

        input_2 = {"input": 799, "user_id": 1}
        response_2 = self.client.post(
            '/api/processes/decimal_to_roman/', input_2)
        output_2 = "DCCXCIX"
        self.assertEqual(response_2.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_2.data, output_2)

        input_3 = {"input": 3999, "user_id": 1}
        response_3 = self.client.post(
            '/api/processes/decimal_to_roman/', input_3)
        output_3 = "MMMCMXCIX"
        self.assertEqual(response_3.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_3.data, output_3)

        input_4 = {"input": 1994, "user_id": 1}
        response_4 = self.client.post(
            '/api/processes/decimal_to_roman/', input_4)
        output_4 = "MCMXCIV"
        self.assertEqual(response_4.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_4.data, output_4)

        input_5 = {"input": "Error", "user_id": 1}
        response_5 = self.client.post(
            '/api/processes/decimal_to_roman/', input_5)
        self.assertEqual(response_5.status_code, status.HTTP_400_BAD_REQUEST)

        input_6 = {"input": 1, "user_id": "Admin"}
        response_6 = self.client.post(
            '/api/processes/decimal_to_roman/', input_6)
        self.assertEqual(response_6.status_code, status.HTTP_400_BAD_REQUEST)


    def test_characters(self):
        input_1 = 2
        response_1 = self.client.get(
            '/api/processes/' + str(input_1) + '/characters/')
        output_1 = ["I"]
        self.assertEqual(response_1.status_code, status.HTTP_200_OK)
        self.assertEqual(response_1.data, output_1)

        input_2 = 3
        response_2 = self.client.get(
            '/api/processes/' + str(input_2) + '/characters/')
        output_2 = ["X", "I", "D", "C"]
        self.assertEqual(response_2.status_code, status.HTTP_200_OK)
        self.assertEqual(response_2.data, output_2)

        input_3 = 4
        response_3 = self.client.get(
            '/api/processes/' + str(input_3) + '/characters/')
        output_3 = ["X", "M", "I", "C"]
        self.assertEqual(response_3.status_code, status.HTTP_200_OK)
        self.assertEqual(response_3.data, output_3)

        input_4 = 5
        response_4 = self.client.get(
            '/api/processes/' + str(input_4) + '/characters/')
        output_4 = ["X", "V", "M", "I", "C"]
        self.assertEqual(response_4.status_code, status.HTTP_200_OK)
        self.assertEqual(response_4.data, output_4)
