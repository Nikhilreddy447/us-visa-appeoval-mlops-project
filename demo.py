import sys
from us_visa.logger import logging
from us_visa.exception import CustomExeption

try:
    a = 1
    b = 0
    print(a / b)
except Exception as e:
    raise CustomExeption(e,sys)