import jsonschema
import json
import yaml
import logging
import os
from config import get_config
from credentials import new_config_credentials
from exceptions import GroupExists, InvalidPath, EmptyDirectory

def validate_schema():
    '''
    Validate yaml schema (config.yml loadead as a json) and validating with schemas/config.json
    '''
    schema = open("./schemas/config.json","r")
    schema_data = json.loads(schema.read())

    item_data = get_config()
    
    logging.info("🔧 - Validating schema")
    jsonschema.validate(schema=schema_data, instance=item_data)
    logging.info("🆗 - Validation OK")

def validate_config_exists():
    '''
    Validate if config.yml exists in this project
    '''
    logging.info("🔧 - Validating config file exists")
    if os.path.isfile('config.yml') or os.path.isfile('config.yaml'):
        logging.info("🆗 - Config file exists")
    else:
        raise ConfigDontExists

def validate_path(path):
    '''
    When we launch the python3 command main.py -p /folder/, the set directory should end with a slash '/'
    '''
    if path[-1] != '/':
       raise InvalidPath(path)
   
def validate_empty_dir(path):
    '''
    The established directory must be empty since delete operations are performed when the program ends. 
    Files downloaded from Gitlab will be deleted. As a precaution, if there were other files, they would be deleted.
    '''
    if not os.listdir(path):
        logging.info("🆗 - Directory is empty")
    else:
        raise EmptyDirectory(path)


def validate_group_exists():
    '''
    Validate that the group name that we put to the imported group does not exist in the new instance
    '''
    gl_new = new_config_credentials()
    new_url = get_config()['NEW_GITLAB_URL']
    
    logging.info(f"🔧 - Validationg if group exists")
    listGroups = gl_new.groups.list(search=get_config()["NEW_GROUP_NAME"])    
    for group in listGroups:
        if group.attributes['parent_id'] is None and get_config()["NEW_GROUP_NAME"].lower().replace(" ", "") == group.attributes['path']:
            raise GroupExists(get_config()["NEW_GROUP_NAME"],new_url)
    logging.info(f"🆗 - Group don't exists on new instance. Then, can be created")

def validate(path): 
    validate_schema()
    validate_config_exists()
    validate_path(path)
    validate_empty_dir(path)
    validate_group_exists()