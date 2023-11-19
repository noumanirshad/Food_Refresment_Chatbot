import mysql.connector as con
from Exception.logger import logging
import sys
from Exception.exception import CustomException





class db_connection:
    def __init__(self):
        self.connection = con.connect(
            host='localhost',
            port=3305,
            user='root',
            password='Numi9585@',
            database='pandeyji_eatery',
            auth_plugin='mysql_native_password'
        )

    def get_order_status(self, order_id):
        try:
            logging.info("Let's start the db connection")

            if self.connection.is_connected():
                cursor = self.connection.cursor()

                # Execute the query to retrieve the status for the given order_id
                query = f"SELECT status FROM order_tracking WHERE order_id = {order_id}"
                cursor.execute(query)

                # Fetch the result
                result = cursor.fetchone()
                cursor.close()

                if result:
                    status = result[0]
                    return status

                logging.info("Db connection is successfully connected")

        except Exception as e:
            logging.info(f"An exception has occurred: {e}")
            raise CustomException(e, sys)

        finally:
            # Close the database connection
            if self.connection.is_connected():
                cursor.close()
            self.connection.close()