from fastapi import FastAPI, Request
from Exception.logger import logging
from Exception.exception import CustomException
import sys
from Scripts.track_order import tracking_order
from Scripts.adding_order import add_to_order
from Scripts.complete_order import complete_order
from Scripts.price_Item import Price_Items
from Scripts.remove_order import remove_order_item
from Scripts.generic_helper import extract_section_id
from Scripts.delete_order import delete_to_order
from Scripts.new_order import remove_id



app = FastAPI()

@app.post("/")
async def handle_request(request : Request):
    try:
        logging.info("Lets Strat my Application")

        payload = await request.json()
        intent = payload['queryResult']['intent']['displayName']
        parameters = payload['queryResult']['parameters']
        outputcontext = payload['queryResult']['outputContexts']

        section_id = extract_section_id(outputcontext[0]['name'])
        logging.info(f"Extract Features from Dialogflow: Parameter : {parameters}, intent : {intent}, section_id : {section_id}") 

        
        intent_handler_dict = {
            "New Order": remove_id,
            "order.add-context: ongoing-order" : add_to_order,
            "order.remove-context-ongoing-order" : remove_order_item,
            "order.complete-context: ongoing-order" : complete_order,
            "Pricing Intent:" : Price_Items,
            'track.order - context: ongoing-tracking' : tracking_order,
            'delete_order-context: ongoing-order' : delete_to_order
        }
        
        logging.info(f"FulfillmentText is successfully connected")  
        
        return intent_handler_dict[intent](parameters, section_id)

        # if intent == 'track.order - context: ongoing-tracking':
        #     return tracking_order(parameters) 
        #     # return parameters['Order_id']
                 
        
        
    except Exception as e:
        logging.info(f"An exception has occurred : {e}")
        raise CustomException(e, sys)
    


