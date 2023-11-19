from fastapi import FastAPI, Request
from Exception.logger import logging
from Exception.exception import CustomException
import sys
from Scripts.track_order import tracking_order
from Scripts.adding_order import add_to_order
from Scripts.generic_helper import extract_section_id


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


        intent_handler_dict = {
            "order.add-context: ongoing-order" : add_to_order,
            # "order.remove-context-ongoing-order" : remove_order,
            # " order.complete-context: ongoing-order" : complete_order,
            # 'track.order - context: ongoing-tracking' : tracking_order
        }
        logging.info(f"FulfillmentText is successfully connected")  
        
        return intent_handler_dict[intent](parameters, section_id)

        # if intent == 'track.order - context: ongoing-tracking':
        #     return tracking_order(parameters) 
        #     # return parameters['Order_id']
          
        
        
        
    except Exception as e:
        logging.info(f"An exception has occurred : {e}")
        raise CustomException(e, sys)
    


