from .api_client import get_todo


def main():

    try:
        todo_id = int(input("Enter Todo ID: "))

        todo = get_todo(todo_id)

        print("\nTodo Details")
        print("------------")

        print("ID:", todo["id"])
        print("Title:", todo["title"])
        print("Completed:", todo["completed"])
        print("User ID:", todo["userId"])

    except ValueError as error:
        print("Invalid input:", error)

    except RuntimeError as error:
        print("Application error:", error)


if __name__ == "__main__":
    main()