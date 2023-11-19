from Exception.logger import logging
from Exception.exception import CustomException
import sys
from fastapi.responses import JSONResponse
from Scripts.db_helper import db_connection
from Scripts.generic_helper import get_str_from_food_dict


inprogrss_order = {}
def add_to_order(parameters, section_id : str):
    try:
        logging.info("Lets Add to Order start")
        food_items = parameters["food-items"]
        food_quantity = parameters["number"]

        if len(food_items) != len(food_quantity):
            fulfillment = "Please add a quantity of all items(e.g i want 2 plates of baryani and 1 juice)"
        else:
            food_dict = dict(zip(food_items , food_quantity))
            logging.info(f"Convert the food_items into dict: {food_dict}")
            # inprogrss_order = {section_id:food_dict}
            

            if section_id in inprogrss_order:
                current_food_dict = inprogrss_order[section_id]
                current_food_dict.update(food_dict)
                inprogrss_order[section_id] = current_food_dict
                logging.info("Update dict and adding more items")
            else:
                inprogrss_order.update({section_id: food_dict})
                logging.info("Lets Adding 1st Order to a dict")
            
            order_str = get_str_from_food_dict(inprogrss_order[section_id])
            fulfillment = f"So far you have: {order_str}. Do you need anything else?"
        
        logging.info(f"Your food_items and food_quantity is successfully added")
        return JSONResponse(content={
                'fulfillmentText': fulfillment
            })
    except Exception as e:
        logging.info(f"An exception has occurred : {e}")
        raise CustomException(e, sys)