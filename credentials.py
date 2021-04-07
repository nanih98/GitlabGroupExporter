import gitlab
import urllib3
import json
import pprint
urllib3.disable_warnings()
from config import get_config

data = get_config()

def old_config_credentials():
    gl_old = gitlab.Gitlab(data["OLD_GITLAB_URL"], private_token=data["OLD_TOKEN"], ssl_verify=True)
    return gl_old

def new_config_credentials():
    gl_new = gitlab.Gitlab(data["NEW_GITLAB_URL"], private_token=data["NEW_TOKEN"], ssl_verify=True)
    return gl_new
