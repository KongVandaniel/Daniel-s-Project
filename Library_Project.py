# Lending Library Books at BBU

from datetime import datetime

from Daniel_Project.Projects_D.utils import (
    typewriter_print,
    get_safe_input,
    colorize,
    BOLD,
    RED
)


# ==========================================
# LIBRARY STOCK
# ==========================================

library_books = [
    {"name": "C++ Programming", "status": "Available"},
    {"name": "Magnificient", "status": "Available"},
    {"name": "Harry Potter", "status": "Available"},
    {"name": "Python Coding Book", "status": "Available"},
    {"name": "Han Velsing", "status": "Available"},
    {"name": "Hotel Transylvania 1", "status": "Available"},
    {"name": "Hotel Transylvania 2", "status": "Available"},
    {"name": "Hotel Transylvania 3", "status": "Available"},
    {"name": "Hotel Transylvania 4", "status": "Available"},
]


def main_menu():

    while True:

        print()
        print()

        typewriter_print("===== Welcome to BBU's Library! =====")

        print()

        typewriter_print(
            "What are you looking forward to do today?"
        )

        print()

        typewriter_print("1. Lend Book")
        typewriter_print("2. Return Book")

        print()

        choice = get_safe_input(
            colorize(
                "Select an option (1 or 2 (or type 'stop')): ",
                BOLD
            )
        )

        try:

            # ==========================================
            # LEND BOOK
            # ==========================================

            if choice == "1":

                print()

                typewriter_print(
                    "===== Please Confirm Your Identity Before Lending Books! ====="
                )

                student_id = input("Enter ID: ")
                student_name = input("Enter Full-Name: ")

                # ------------------------------------------
                # DATE VALIDATION
                # ------------------------------------------

                while True:

                    try:

                        lend_date = input(
                            "Enter lend date (DD-MM-YYYY): "
                        )

                        return_date = input(
                            "Enter return date (DD-MM-YYYY): "
                        )

                        lend_date_obj = datetime.strptime(
                            lend_date,
                            "%d-%m-%Y"
                        )

                        return_date_obj = datetime.strptime(
                            return_date,
                            "%d-%m-%Y"
                        )

                        # Return date cannot be before
                        # or equal to lend date
                        if return_date_obj <= lend_date_obj:

                            raise ValueError(
                                "Return date must be later than lend date."
                            )

                        # Calculate duration
                        lend_duration_days = (
                            return_date_obj - lend_date_obj
                        ).days

                        # Maximum = 28 days
                        if lend_duration_days > 28:

                            raise ValueError(
                                "Lending duration cannot be more than 4 weeks (28 days)."
                            )

                        weeks = lend_duration_days // 7
                        days = lend_duration_days % 7

                        if weeks > 0 and days > 0:

                            duration_text = (
                                f"{weeks} week(s) and {days} day(s)"
                            )

                        elif weeks > 0:

                            duration_text = (
                                f"{weeks} week(s)"
                            )

                        else:

                            duration_text = (
                                f"{days} day(s)"
                            )

                        # Date is valid
                        break

                    except ValueError as err:

                        print()

                        typewriter_print(
                            colorize(
                                f"⚠️ Date Error: {err}",
                                RED
                            )
                        )

                        print()

                # ------------------------------------------
                # SELECT BOOKS
                # ------------------------------------------

                book_names = []

                print()

                typewriter_print(
                    "===== Books Currently In Stock ====="
                )

                number = 1

                for book in library_books:

                    if book["status"] == "Available":

                        typewriter_print(
                            f"{number}. {book['name']}"
                        )

                        number += 1

                print()

                while True:

                    book_name = input(
                        "Enter Book's name (or type 'stop'): "
                    )

                    # Stop entering books
                    if book_name.lower() == "stop":
                        break

                    book_found = None

                    # Find book
                    for book in library_books:

                        if book["name"].lower() == book_name.lower():

                            book_found = book
                            break

                    # Book doesn't exist
                    if book_found is None:

                        raise ValueError(
                            f"Book '{book_name}' does not exist in the library."
                        )

                    # Book already borrowed
                    if book_found["status"] == "Unavailable":

                        raise ValueError(
                            f"Book '{book_found['name']}' is currently unavailable."
                        )

                    # Prevent duplicate lending
                    if book_found["name"] in book_names:

                        raise ValueError(
                            f"Book '{book_found['name']}' has already been selected."
                        )

                    # Change status
                    book_found["status"] = "Unavailable"

                    # Add ONLY the name to invoice
                    book_names.append(
                        book_found["name"]
                    )

                # Must lend at least one book
                if not book_names:

                    raise ValueError(
                        "You must lend at least one book."
                    )

                book_count = len(book_names)

                # ------------------------------------------
                # LENDING INVOICE
                # ------------------------------------------

                print()

                typewriter_print(
                    f"Total books lent: {book_count}"
                )

                print()

                typewriter_print(
                    "===== Student Invoice ====="
                )

                print()

                typewriter_print(
                    f"Stu. ID: {student_id}"
                )

                typewriter_print(
                    f"Stu. Name: {student_name}"
                )

                print()

                typewriter_print(
                    f"Lend Date: {lend_date}"
                )

                typewriter_print(
                    f"Return Date: {return_date}"
                )

                typewriter_print(
                    f"Lend Duration: {duration_text}"
                )

                print()

                typewriter_print(
                    "Book's Name:"
                )

                for number, book in enumerate(
                    book_names,
                    start=1
                ):

                    typewriter_print(
                        f"{number}. {book}"
                    )

                print()

                typewriter_print(
                    f"Amount of Book: {book_count}"
                )

                print()

                typewriter_print(
                    "===== Thank You For Your Cooperation! "
                    "Hope To See You Again Soon! ====="
                )


            # ==========================================
            # RETURN BOOK
            # ==========================================

            elif choice == "2":

                print()

                typewriter_print(
                    "===== Please Confirm Your Identity Before Returning Books! ====="
                )

                student_id = input(
                    "Enter ID: "
                )

                student_name = input(
                    "Enter Full-Name: "
                )

                # ------------------------------------------
                # RETURN DATE
                # ------------------------------------------

                while True:

                    try:

                        return_date = input(
                            "Enter return date (DD-MM-YYYY): "
                        )

                        return_date_obj = datetime.strptime(
                            return_date,
                            "%d-%m-%Y"
                        )

                        break

                    except ValueError:

                        typewriter_print(
                            colorize(
                                "⚠️ Invalid date. Please use DD-MM-YYYY.",
                                RED
                            )
                        )

                # ------------------------------------------
                # SELECT BOOKS TO RETURN
                # ------------------------------------------

                book_names = []

                print()

                typewriter_print(
                    "===== Books Currently Borrowed ====="
                )

                number = 1

                for book in library_books:

                    if book["status"] == "Unavailable":

                        typewriter_print(
                            f"{number}. {book['name']}"
                        )

                        number += 1

                print()

                while True:

                    book_name = input(
                        "Enter Book's name (or type 'stop'): "
                    )

                    if book_name.lower() == "stop":
                        break

                    book_found = None

                    # Find book
                    for book in library_books:

                        if book["name"].lower() == book_name.lower():

                            book_found = book
                            break

                    # Doesn't exist
                    if book_found is None:

                        raise ValueError(
                            f"Book '{book_name}' does not exist in the library."
                        )

                    # Already available
                    if book_found["status"] == "Available":

                        raise ValueError(
                            f"Book '{book_found['name']}' is already available."
                        )

                    # Prevent duplicate return
                    if book_found["name"] in book_names:

                        raise ValueError(
                            f"Book '{book_found['name']}' has already been returned."
                        )

                    # Return book
                    book_found["status"] = "Available"

                    book_names.append(
                        book_found["name"]
                    )

                # Must return at least one book
                if not book_names:

                    raise ValueError(
                        "You must return at least one book."
                    )

                book_count = len(book_names)

                # ------------------------------------------
                # RETURN INVOICE
                # ------------------------------------------

                print()

                typewriter_print(
                    f"Total books returned: {book_count}"
                )

                print()

                typewriter_print(
                    "===== Student Invoice ====="
                )

                print()

                typewriter_print(
                    f"Stu. ID: {student_id}"
                )

                typewriter_print(
                    f"Stu. Name: {student_name}"
                )

                print()

                typewriter_print(
                    f"Return Date: {return_date}"
                )

                print()

                typewriter_print(
                    "Book's Name:"
                )

                for number, book in enumerate(
                    book_names,
                    start=1
                ):

                    typewriter_print(
                        f"{number}. {book}"
                    )

                print()

                typewriter_print(
                    f"Amount of Book: {book_count}"
                )

                print()

                typewriter_print(
                    "===== Thank You For Your Cooperation! "
                    "Hope To See You Again Soon! ====="
                )


            # ==========================================
            # STOP PROGRAM
            # ==========================================

            elif choice.lower() == "stop":

                print()

                typewriter_print(
                    "===== Thank You For Choosing BBU's Library! ====="
                )

                print()

                break


            # ==========================================
            # INVALID MENU OPTION
            # ==========================================

            else:

                raise ValueError(
                    "Option must be 1 or 2."
                )


        except ValueError as err:

            print()

            typewriter_print(
                colorize(
                    f"⚠️ Menu Error: {err}",
                    RED
                )
            )


main_menu()