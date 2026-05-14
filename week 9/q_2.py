# class InvalidMarksError(Exception):
#     pass

# try:
#     marks = int(input("Enter student marks: "))
#     if marks < 0 or marks > 100:
#         raise InvalidMarksError("Marks must be between 0 and 100.")
#     print(f"Marks entered: {marks}")
# except InvalidMarksError as e:
#     print(f"Custom Error: {e}")
# except ValueError:
#     print("Error: Please enter a valid integer.")