from Exception.logger import logging
from Exception.exception import CustomException
import sys
from Scripts.adding_order import inprogrss_order


def remove_id(remove_id, section_id):
    try:
        logging.info("Let's start the new order")
        if inprogrss_order is not None:
            for id in inprogrss_order:
                del inprogrss_order[id]
                logging.info("New order is successfully empty")
    except Exception as e:
        logging.info(f"An exception has occurred : {e}")
        raise CustomException(e, sys)

