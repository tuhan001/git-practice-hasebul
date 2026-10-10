from datetime import date

from utils import add, divide, multiply, subtract


def show_result(label, operation):
    try:
        print(f"{label} = {operation()}")
    except (TypeError, ZeroDivisionError) as error:
        print(f"Calculation error: {error}")


def main():
    print("Name: Hasebul")
    print(f"Today's date: {date.today()}")
    show_result("5 + 3", lambda: add(5, 3))
    show_result("5 - 3", lambda: subtract(5, 3))
    show_result("5 * 3", lambda: multiply(5, 3))
    show_result("5 / 0", lambda: divide(5, 0))


if __name__ == "__main__":
    main()
