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

    def insert_order_id(self, order_id, item_id, item_quantity, price):
        try:
            logging.info(f"Let's start inserting order items")
            
            if self.connection.is_connected():
                cursor = self.connection.cursor()

                # Provide values for all columns, including item_id
                query = "INSERT INTO orders (order_id, item_id, quantity, total_price) VALUES (%s, %s, %s, %s)"
                values = order_id,  item_id,  item_quantity, price

                cursor.execute(query, values)
                self.connection.commit()
                logging.info(f"Successfully inserted order for Order ID {order_id}")

                cursor.close()
            logging.info("Order inserted successfully")

        except con.Error as err:
            logging.info(f"Error inserting order item: {err}")
            self.connection.rollback()
            return -1

        except Exception as e:
            logging.info(f"An exception has occurred: {e}")
            raise CustomException(e, sys)

    def fetch_item_id_by_name(self, item_name):
            try:
                logging.info("Let's start fetching item_id from food_items table.")
                if self.connection.is_connected():
                    cursor = self.connection.cursor(dictionary=True)  # Using dictionary cursor for easier data retrieval

                    # Execute the query to retrieve the item_id for the given item_name
                    query = f"SELECT item_id FROM food_items WHERE name = '{item_name}'"
                    cursor.execute(query)

                    # Fetch the result
                    result = cursor.fetchone()

                    if result:
                        item_id = result['item_id']
                        logging.info(f"Successfully fetched item_id for {item_name}: {item_id}")
                        return item_id
                    else:
                        logging.info(f"No item found with name: {item_name}")
                        return None

                    cursor.close()

            except con.Error as err:
                logging.info(f"Error fetching item_id: {err}")
                print(f"Error fetching item_id: {err}")
                return None

            except Exception as e:
                logging.info(f"An exception has occurred: {e}")
                raise CustomException(e, sys)
            

    def fetch_price_by_name(self, item_name):
            try:
                logging.info("Let's start fetching price from food_items table.")
                if self.connection.is_connected():
                    cursor = self.connection.cursor(dictionary=True)  # Using dictionary cursor for easier data retrieval

                    # Execute the query to retrieve the price for the given item_name
                    query = f"SELECT price FROM food_items WHERE name = '{item_name}'"
                    cursor.execute(query)

                    # Fetch the result
                    result = cursor.fetchone()

                    if result:
                        price = result['price']
                        logging.info(f"Successfully fetched price for {item_name}: {price}")
                        return price
                    else:
                        logging.info(f"No item found with name: {item_name}")
                        return None

                    cursor.close()

            except con.Error as err:
                logging.info(f"Error fetching price: {err}")
                print(f"Error fetching price: {err}")
                return None

            except Exception as e:
                logging.info(f"An exception has occurred: {e}")
                raise CustomException(e, sys)