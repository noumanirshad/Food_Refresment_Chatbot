from Exception.logger import logging
from Exception.exception import CustomException
import sys
from fastapi.responses import JSONResponse
from DB_Helper.order_status import StatusOrderId


def tracking_order(parameter, section_id):
    try:
        logging.info("Let's start tracking the order")
        order_id = int(parameter['number'])
        logging.info(f"your order_id is {order_id}")

        # Create an instance of db_connection
        order_details_fetcher = StatusOrderId()

        # Call the get_order_status method on the instance
        status = order_details_fetcher.get_order_status(order_id)
        order_details = order_details_fetcher.fetch_order_details(order_id)

        current_order = []
        if order_details:
            for item_no in range(len(order_details)):
                item_id = order_details[item_no]['item_id']
                item_quantity = order_details[item_no]['quantity']
                item_food = order_details_fetcher.fetch_item_id(item_id)
                item_name =  item_food[0]['name']
                current_order.append(f"{item_name} : {item_quantity} ")



        # Initialize fulfilment_text
        fulfilment_text = ""
        if current_order is not None:
            fulfilment_text += f"This is your current Order: \n {current_order}. "
        if status:
            fulfilment_text += f"Status for Order ID {order_id} is {status}"
        else:
            fulfilment_text = f"No record found for Order ID {order_id}"

        logging.info(f"Your Order ID {order_id} is successfully connected")
        return JSONResponse(content={
            'fulfillmentText': fulfilment_text
        })

    except Exception as e:
        logging.info(f"An exception has occurred: {e}")
        raise CustomException(e, sys)
