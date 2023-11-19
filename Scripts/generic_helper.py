import re
from Exception.logger import logging
from Exception.exception import CustomException
import sys


def extract_section_id(section_id : str):
    try:
        logging.info("Lets extract section")
        match = re.search(r"/sections/(.*?)/context/", section_id)
        if match:
            extract_section_id = match.group(1)
            logging.info(f"Successfully extracted section_id : {extract_section_id}")
            return extract_section_id

    except Exception as e:
        logging.info(f"An exception has occurred : {e}")
        raise CustomException(e, sys)


def get_str_from_food_dict(food_dict):
    return ", ".join([f"{int(value)} {key}" for key , value in food_dict.items()])




