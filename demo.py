<<<<<<< HEAD
import sys
from us_visa.logger import logging
from us_visa.exception import CustomExeption

try:
    a = 1
    b = 0
    print(a / b)
except Exception as e:
    raise CustomExeption(e,sys)
=======
mongodb+srv://vnmad:vnmad367@cluster0.6a1uw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
>>>>>>> c10299b85a7a89ae5124fa9f37bdad7820473ab2
