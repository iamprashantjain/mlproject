import sys
import logging
import logger


def error_message_detail(error, error_detail: sys):
    """Generate a custom error message with details of where the error occurred."""
    _, _, exc_tb = error_detail.exc_info()
    
    # Get file name, line number, and error message
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_no = exc_tb.tb_lineno
    error_msg = str(error)
    
    # Create a detailed error message
    error_message = (
        f"Error occurred in script '{file_name}' "
        f"at line {line_no}: {error_msg}"
    )
    
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        # Initialize the base class with the error message
        super().__init__(error_message)
        # Generate a detailed error message
        self.error_message = error_message_detail(error_message, error_detail)
        
    def __str__(self):
        # Return the detailed error message
        return self.error_message



# if __name__ == "__main__":
#     try:
#         # Some code that may raise an exception
#         x = 1 / 0
#     except Exception as e:
#         # Log the error message
#         logging.error("An error occurred", exc_info=True)
#         # Raise a custom exception with details
#         raise CustomException(e, sys)
