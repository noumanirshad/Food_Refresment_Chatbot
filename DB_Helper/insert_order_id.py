import mysql.connector as con
from Exception.logger import logging
import sys
from Exception.exception import CustomException

class InsertOrderId:
    def __init__(self):
        self.connection = con.connect(
            host='localhost',
            port=3305,
            user='root',
            password='Numi9585@',
            database='pandeyji_eatery',
            auth_plugin='mysql_native_password'
        )

    def insert_order_id(self, items, item_quantity, order_id):
        try:
            logging.info(f"Let start the Inserting order ")
            if self.connection.is_connected():
                cursor = self.connection.cursor()

                cursor.callproc('insert_order_item', (items, item_quantity, order_id))
                self.connection.commit()
                logging.info(f"Successfully insert {item_quantity} {items} order item and quantity into the table. ")

                cursor.close()
            logging.info(f"Order item inserted successfully")

        except con.Error as err:
            logging.info(f"Error inserting order item: {err}")
            print(f"Error inserting order item: {err}")
            self.connection.rollback()
            return -1

        except Exception as e:
            logging.info(f"An exception has occurred: {e}")
            raise CustomException(e, sys)
