import mysql.connector as con
from Exception.logger import logging
import sys
from Exception.exception import CustomException

class NextOrderId:
    def __init__(self):
        self.connection = con.connect(
            host='localhost',
            port=3305,
            user='root',
            password='Numi9585@',
            database='pandeyji_eatery',
            auth_plugin='mysql_native_password'
        )

    def get_next_order_id(self):
        try:
            logging.info('Let\'s get the next order id ')
            
            cursor = self.connection.cursor()

            query = "SELECT MAX(order_id) from orders"
            cursor.execute(query)

            # Fetching the result
            result = cursor.fetchone()[0]
            logging.info(f'Max Order id is fetched: {result}')

            cursor.close()
            if result is None:
                return 1
            else:
                return result + 1
            
        except Exception as e:
            logging.info(f"An exception has occurred: {e}")
            raise CustomException(e, sys)