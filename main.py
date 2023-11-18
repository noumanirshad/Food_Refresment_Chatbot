from fastapi import FastAPI, Request
from Exception.logger import logging
from Exception.exception import CustomException
import sys
from Scripts.track_order import tracking_order


app = FastAPI()

@app.post("/")
async def handle_request(request : Request):
    try:
        logging.info("Lets Strat my Application")

        payload = await request.json()
        intent = payload['queryResult']['intent']['displayName']
        parameters = payload['queryResult']['parameters']
        outputcontext = payload['queryResult']['outputContexts']
        print(parameters)





        if intent == 'track.order - context: ongoing-tracking':
            return tracking_order(parameters) 
            # return parameters['Order_id']
        logging.info(f"FulfillmentText is successfully connected")    
        
        
        
    except Exception as e:
        logging.info(f"An exception has occurred : {e}")
        raise CustomException(e, sys)
    

