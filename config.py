import yaml
import json

def get_config():
    '''
    This function return parsed yaml as a dictionary object (like json)
    '''
    item = open("config.yml","r")
    item_data = yaml.load(item.read(), Loader=yaml.FullLoader)
    return item_data
