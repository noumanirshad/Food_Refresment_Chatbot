from Exception.logger import logging
from Exception.exception import CustomException
import numpy as np
import sys
from fastapi.responses import JSONResponse
from Scripts.adding_order import inprogrss_order
from Scripts.generic_helper import get_str_from_food_dict

def remove_order_item(parameters: dict, section_id: str):
    try:
        logging.info("Let's start Removing order items")
        
        if section_id not in inprogrss_order:
            return JSONResponse(content={
                'fulfillmentText': "I am having trouble finding your order. Can you place a new order again?"
            })
        
            
        current_order = inprogrss_order[section_id]
        food_items = parameters.get("food-items", [])
        food_quantity = parameters.get("number", [])
        logging.info(f'food_quantity in a list:   {food_quantity}')

        # Ensure food_quantity is an iterable
        food_quantity = np.array([food_quantity]) if np.isscalar(food_quantity) else np.array(food_quantity)
        logging.info(f'food_quantity convert list to array: {food_quantity}')


        if not food_items:
            return JSONResponse(content={
                'fulfillmentText': "Please specify the items you want to remove."
            })

        
        remove_item = []
        no_such_item = []
        
        for item in food_items:
            if len(food_quantity) <= 0 or food_quantity is None:
                    remove_item.append(item)
                    del current_order[item]
                    logging.info(f"1.Successfully removed all instances of {item} from the order.")

        for item, quantity_to_remove in zip(food_items, food_quantity):
            logging.info(f"this is food item {item} and quantity {quantity_to_remove}")
            if item not in current_order:
                no_such_item.append(item)
            elif quantity_to_remove is None or quantity_to_remove >= current_order[item]:
                remove_item.append(item)
                del current_order[item]
                logging.info(f"Successfully removed all instances of {item} from the order.")
            else:
                current_order[item] -= quantity_to_remove
                remove_item.append(f"{quantity_to_remove} {item}(s)")
                logging.info(f"Successfully removed {quantity_to_remove} {item}(s) from the order. Current order = {current_order}")
                if current_order[item] == 0:
                    del current_order[item]  # Remove the item if its quantity becomes zero

        fulfillment = ""

        if len(remove_item) > 0:
            fulfillment += f"Removed {', '.join(remove_item)} from your order!\n"

        if no_such_item:
            fulfillment += f"The following items are not in your order: {', '.join(no_such_item)}\n"

        if not current_order:
            fulfillment += "Your order is essentially empty."
        else:
            order_str = get_str_from_food_dict(current_order)
            fulfillment += f"After removing these items, here is your final order:\n [{order_str}]. Do you need anything else?"

        return JSONResponse(content={
            'fulfillmentText': fulfillment
        })


    except Exception as e:
        logging.info(f"An exception has occurred : {e}")
        raise CustomException(e, sys)