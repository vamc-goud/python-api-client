import unittest
import requests

from unittest.mock import Mock, patch

from app.api_client import get_todo
from app.config import BASE_URL, REQUEST_TIMEOUT


class TestGetTodo(unittest.TestCase):

    @patch("app.api_client.requests.get")
    def test_returns_todo_when_request_succeeds(self, mock_get):

        expected_data = {
            "userId": 1,
            "id": 1,
            "title": "delectus aut autem",
            "completed": False
        }

        fake_response = Mock()

        fake_response.json.return_value = expected_data

        mock_get.return_value = fake_response

        result = get_todo(1)

        self.assertEqual(result, expected_data)

        mock_get.assert_called_once_with(
            f"{BASE_URL}/todos/1",
            timeout=REQUEST_TIMEOUT
        )

    @patch("app.api_client.requests.get")
    def test_rejects_invalid_ids(self, mock_get):

        invalid_ids = [0, -1, "1", True, None]

        for todo_id in invalid_ids:

            with self.subTest(todo_id=todo_id):

                with self.assertRaises(ValueError):
                    get_todo(todo_id)

        mock_get.assert_not_called()

    @patch("app.api_client.requests.get")
    def test_handles_timeout(self, mock_get):

        mock_get.side_effect = requests.exceptions.Timeout(
            "Request took too long"
        )

        with self.assertRaisesRegex(
            RuntimeError,
            "API request timed out"
        ):
            get_todo(1)

    @patch("app.api_client.requests.get")
    def test_handles_http_error(self, mock_get):

        fake_response = Mock()

        fake_response.raise_for_status.side_effect = (
            requests.exceptions.HTTPError("404 Client Error")
        )

        mock_get.return_value = fake_response

        with self.assertRaisesRegex(
            RuntimeError,
            "HTTP error occurred"
        ):
            get_todo(1)

    @patch("app.api_client.requests.get")
    def test_handles_invalid_json(self, mock_get):

        fake_response = Mock()

        fake_response.json.side_effect = ValueError(
            "Invalid JSON"
        )

        mock_get.return_value = fake_response

        with self.assertRaisesRegex(
            RuntimeError,
            "API returned invalid JSON"
        ):
            get_todo(1)

    @patch("app.api_client.requests.get")
    def test_rejects_unexpected_response_format(self, mock_get):

        fake_response = Mock()

        fake_response.json.return_value = []

        mock_get.return_value = fake_response

        with self.assertRaisesRegex(
            RuntimeError,
            "Unexpected API response format"
        ):
            get_todo(1)


if __name__ == "__main__":
    unittest.main()