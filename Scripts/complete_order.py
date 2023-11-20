from Exception.logger import logging
from Exception.exception import CustomException
import sys
from fastapi.responses import JSONResponse
from Scripts.adding_order import inprogrss_order
from Scripts.generic_helper import get_str_from_food_dict
from DB_Helper.insert_order_id import InsertOrderId
from DB_Helper.new_order_id import NextOrderId
from DB_Helper.order_total_price import PriceOrderId
from DB_Helper.order_tracking import TrackOrderId



def complete_order(parameters, section_id : str):
    try:
        logging.info("Lets strats the function of order complete")
        price_id = PriceOrderId()
        if section_id not in inprogrss_order:
            fulfillment = "I'm having a trouble finding your order. Sorry, Can you place an order?"
        else:
            order = inprogrss_order[section_id]
            order_id = save_to_order(order)
            if order_id == -1:
                fulfillment = "Sorry, I couldn't find your order due to backend error. Please try again"
            else:
                order_total = price_id.get_order_total_price(order_id)
                fulfillment = f'''Awesome, We have place your order.
                \nHere is your order_id {order_id}
                \nHere is your order: {get_str_from_food_dict(order)}
                \nTotal Price of your order is:  {int(order_total)}$. \nYou can pay at the time of delivery'''
            del inprogrss_order[section_id]

        logging.info("Successfully Get the order_id and total_price of order.")
        return JSONResponse(content={
            'fulfillmentText': fulfillment
            })
    except Exception as e:
        logging.info(f"An exception has occurred : {e}")
        raise CustomException(e, sys)
    


def save_to_order(order):
    try:
        logging.info("Lets strats the function of save_to_order")
        next_id = NextOrderId()
        insert_id = InsertOrderId()
        track_id = TrackOrderId()
        next_order_id = next_id.get_next_order_id()
        for item , quantity in order.items():
            recode = insert_id.insert_order_id(
                item,
                quantity,
                next_order_id
            )
            if recode == -1:
                return -1
        
        track_id.insert_order_tracking(next_order_id, "in progress")

        return next_order_id
    
            
    except Exception as e:
        logging.info(f"An exception has occurred : {e}")
        raise CustomException(e, sys)