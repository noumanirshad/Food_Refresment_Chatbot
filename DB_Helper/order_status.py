import mysql.connector as con
from Exception.logger import logging
import sys
from Exception.exception import CustomException

class StatusOrderId:
    def __init__(self):
        self.connection = con.connect(
            host='localhost',
            port=3305,
            user='root',
            password='Numi9585@',
            database='pandeyji_eatery',
            auth_plugin='mysql_native_password'
        )

    def fetch_order_details(self, order_id):
        try:
            logging.info("Let's start to fetch order details from MySQL order table.")
            if self.connection.is_connected():
                cursor = self.connection.cursor(dictionary=True)  # Using dictionary cursor for easier data retrieval

                query = f"SELECT * FROM orders WHERE order_id = {order_id}"
                cursor.execute(query)

                result = cursor.fetchall()  # Use fetchall() to get all rows

                if result:
                    logging.info("Successfully Fetch  the order details from MySQL order table.")
                    return result
                else:
                    return None

                cursor.close()
            else: 
                logging.info("Connection is not connected from DB.") 
        except Exception as e:
            logging.info(f"An exception has occurred: {e}")
            raise CustomException(e, sys)

    
    def fetch_item_id(self, item_id):
        try:
            logging.info("Let's start to fetch item_name using item_Id from MySQL item_id table.")
            if self.connection.is_connected():
                cursor = self.connection.cursor(dictionary=True)  # Using dictionary cursor for easier data retrieval

                query = f"SELECT * FROM food_items WHERE item_id = {item_id}"
                cursor.execute(query)

                result = cursor.fetchall()  # Use fetchall() to get all rows

                if result:
                    logging.info("Successfully Fetch  the item_name using item_Id from MySQL item_id table.")
                    return result
                else:
                    return None

                cursor.close()
        except Exception as e:
            logging.info(f"An exception has occurred: {e}")
            raise CustomException(e, sys)
    
    def get_order_status(self, order_id):
        try:
            logging.info("Let's start the db connection. Let's start to track the order from MySQL order_tracking table.")

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
                    logging.info("Db connection is successfully connected and Successfully track the order from MySQL order_tracking table.")
                    return status

                

        except Exception as e:
            logging.info(f"An exception has occurred: {e}")
            raise CustomException(e, sys)

        