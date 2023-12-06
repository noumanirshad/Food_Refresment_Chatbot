from Exception.logger import logging
from Exception.exception import CustomException
import sys
from fastapi.responses import JSONResponse
from DB_Helper.insert_order_id import InsertOrderId


def Price_Items(parameters, section_id : str):
    try:
        logging.info("Lets strats the function of Price_Items")
        price_item = InsertOrderId()
        food_items = parameters["food-items"]

        price = price_item.fetch_price_by_name(food_items)
        fulfillment = f"Price of 1 {food_items} is {price}$"

        logging.info("Successfully Get the price of Price items.")
        return JSONResponse(content={
            'fulfillmentText': fulfillment
            })
    except Exception as e:
        logging.info(f"An exception has occurred : {e}")
        raise CustomException(e, sys)


