import requests

from .config import BASE_URL, REQUEST_TIMEOUT


def get_todo(todo_id):

    if not isinstance(todo_id, int) or todo_id <= 0:
        raise ValueError("Todo ID must be a positive integer")

    url = f"{BASE_URL}/todos/{todo_id}"

    try:
        response = requests.get(
            url,
            timeout=REQUEST_TIMEOUT
        )

        response.raise_for_status()

    except requests.exceptions.Timeout as error:
        raise RuntimeError("API request timed out") from error

    except requests.exceptions.HTTPError as error:
        raise RuntimeError(
            f"HTTP error occurred: {error}"
        ) from error

    except requests.exceptions.RequestException as error:
        raise RuntimeError(
            f"API connection failed: {error}"
        ) from error

    try:
        data = response.json()

    except ValueError as error:
        raise RuntimeError(
            "API returned invalid JSON"
        ) from error

    if not isinstance(data, dict):
        raise RuntimeError("Unexpected API response format")

    return data