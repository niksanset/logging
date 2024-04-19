import logging as log


debug_logger = log.getLogger('debug_logger')
debug_handler = log.FileHandler('debug.log')
debug_formatter = log.Formatter('%(asctime)s - %(levelname)s - %(message)s')
debug_handler.setFormatter(debug_formatter)
debug_logger.addHandler(debug_handler)
debug_logger.setLevel(log.DEBUG)


error_logger = log.getLogger('error_logger')
error_handler = log.FileHandler('errors.log')
error_formatter = log.Formatter('%(asctime)s - %(levelname)s - %(message)s')
error_handler.setFormatter(error_formatter)
error_logger.addHandler(error_handler)
error_logger.setLevel(log.ERROR)

def example_function():
    try:

        result = 10 / 0
    except ZeroDivisionError as e:
      
        error_logger.error(f"An error occurred: {e}", exc_info=True)

def main():

    debug_logger.debug("This is a debug message")

  
    example_function()

if __name__ == "__main__":
    main()