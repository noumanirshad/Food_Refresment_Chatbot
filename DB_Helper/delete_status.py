import mysql.connector as con
from Exception.logger import logging
from Exception.exception import CustomException
import sys

class DatabaseManager:
    def __init__(self):
        self.connection = con.connect(
            host='localhost',
            port=3305,
            user='root',
            password='Numi9585@',
            database='pandeyji_eatery',
            auth_plugin='mysql_native_password'
        )

    def delete_order(self, order_id):
        try:
            logging.info("Let's start the deleting order process.")
            cursor = self.connection.cursor()

            # Use the DELETE statement to remove rows based on the order ID
            delete_query = f"DELETE FROM orders WHERE order_id = {order_id}"
            cursor.execute(delete_query)

            # Commit the changes
            self.connection.commit()

            logging.info(f"Successfully deleted order with ID {order_id} from the database.")

        except con.Error as err:
            logging.info(f"Error deleting order: {err}")
            print(f"Error deleting order: {err}")
            self.connection.rollback()

        except Exception as e:
            logging.info(f"An exception has occurred: {e}")
            raise CustomException(e, sys)

        finally:
            # Close the cursor and connection
            cursor.close()

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()


# # Example of using the delete_order function
# db_manager = DatabaseManager()
# order_id_to_delete = 123  # Replace with the actual order ID you want to delete
# db_manager.delete_order(order_id_to_delete)
# db_manager.close_connection()
