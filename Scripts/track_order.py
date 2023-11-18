from Exception.logger import logging
from Exception.exception import CustomException
import sys
from fastapi.responses import JSONResponse
from Scripts.db_helper import db_connection

    


def tracking_order(parameter):
    try:
        logging.info("Let's start tracking the order")
        order_id = int(parameter['Order_id'])
        logging.info(f"your order_id is {order_id}")

        # Create an instance of db_connection
        db_conn = db_connection()

        # Call the get_order_status method on the instance
        status = db_conn.get_order_status(order_id)
        if status:
            fulfilment_text = f"Status for Order ID {order_id}: {status}"
        else:
            fulfilment_text = f"No record found for Order ID {order_id}"

        logging.info(f"Your Order ID {order_id} is successfully connected")
        return JSONResponse(content={
            'fulfillmentText': fulfilment_text
        })

    except Exception as e:
        logging.info(f"An exception has occurred : {e}")
        raise CustomException(e)

