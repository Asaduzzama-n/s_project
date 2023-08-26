# import string
# import time
# from random import random
#
# import constant as const
#
#
# def run_test_case(password, expected_error, password_field=None, error_message_element=None):
#     password_field.send_keys(password)
#     time.sleep(1)  # Give the page some time to react to the input
#
#     actual_error_message = error_message_element.text
#
#     if expected_error is None:
#         if actual_error_message == "":
#             print(f"Password '{password}' is valid.")
#             return True
#         else:
#             print(f"Password '{password}' is invalid, but no error was expected.")
#             return False
#     else:
#         if expected_error in actual_error_message:
#             print(f"Password '{password}' generated the expected error: '{expected_error}'.")
#             return True
#         else:
#             print(f"Password '{password}' did not generate the expected error. Actual error: '{actual_error_message}'.")
#             return False
