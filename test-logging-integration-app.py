import sys
import src.logger
from src.exception import CustomException

def example_function():
    try:
        x = 10
        y = 0
        result = x / y
    except Exception as e:
        raise CustomException(e, sys)


if __name__=="__main__":
    try: 
        example_function()
    except CustomException as e:
        print(e)

        