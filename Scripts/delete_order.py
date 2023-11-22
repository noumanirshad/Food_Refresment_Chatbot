from Exception.logger import logging
from Exception.exception import CustomException
import sys
from fastapi.responses import JSONResponse
from DB_Helper.delete_status import DatabaseManager


inprogrss_order = {}

def delete_to_order(parameters, section_id : str):
    try:
        logging.info("Lets start the process od Order delete")
        id = parameters["delete_id"]
        DatabaseManager.delete_order(id)
        fulfillment = 'Your order has been deleted. Thank you for joining us.'


        return JSONResponse(content={
                'fulfillmentText': fulfillment
            })
    except Exception as e:
        logging.info(f"An exception has occurred : {e}")
        raise CustomException(e, sys)