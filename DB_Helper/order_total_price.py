import mysql.connector as con
from Exception.logger import logging
import sys
from Exception.exception import CustomException

class PriceOrderId:
    def __init__(self):
        self.connection = con.connect(
            host='localhost',
            port=3305,
            user='root',
            password='Numi9585@',
            database='pandeyji_eatery',
            auth_plugin='mysql_native_password'
        )

    def get_order_total_price(self, order_id):
        try:
            logging.info(f"Let start the get_order_total_price.")
            cursor = self.connection.cursor()
            query = f"SELECT get_total_order_price({order_id})"

            cursor.execute(query)
                

            # Fetch the result
            result = cursor.fetchone()[0]
            cursor.close()
            logging.info("Successfully fetched the total price of order")
            return result
        
        except Exception as e:
            logging.info(f"An exception has occurred: {e}")
            raise CustomException(e, sys)