import mysql.connector as con
from Exception.logger import logging
import sys
from Exception.exception import CustomException

class TrackOrderId:
    def __init__(self):
        self.connection = con.connect(
            host='localhost',
            port=3305,
            user='root',
            password='Numi9585@',
            database='pandeyji_eatery',
            auth_plugin='mysql_native_password'
        )

    def insert_order_tracking(self, order_id, status):
        try:
            logging.info(f"Lets start the inserting_order_tracking")
            cursor = self.connection.cursor()

            # Inserting the record into the order_tracking table
            insert_query = "INSERT INTO order_tracking (order_id, status) VALUES (%s, %s)"
            cursor.execute(insert_query, (order_id, status))

            # Committing the changes
            self.connection.commit()
            # Closing the cursor
            cursor.close()
            logging.info(f"Successfully inserting_order_tracking")

        except Exception as e:
            logging.info(f"An exception has occurred: {e}")
            raise CustomException(e, sys)