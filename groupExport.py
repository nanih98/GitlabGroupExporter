import gitlab
import time
import logging
import urllib3
urllib3.disable_warnings()
from credentials import old_config_credentials, new_config_credentials
from config import get_config
from validations import group_exists

# Set credentials to Gitlabs
gl_old = old_config_credentials()
gl_new = new_config_credentials()

old_url = get_config()['OLD_GITLAB_URL']
new_url = get_config()['NEW_GITLAB_URL']

def group_export_import(groupId,path):
    # Check if new group exists
    logging.info(f"🔧 - Validationg if group exists")
    group_exists()
    logging.info(f"🆗 - Group don't exists on new instance. Then, can be created")
    
    group = gl_old.groups.get(groupId)
    logging.info(f"🔧 - Exporting group {group.name} with Id {groupId} from {old_url}")
    export = group.exports.create()
    
    logging.info("🔧 - Wait for the export to finish")
    time.sleep(120)

    ## Download the result
    with open(f'{path}/{group.name}.tar.gz', 'wb') as f:
        export.download(streamed=True, action=f.write)
    
    ## Import group
    logging.info(f"🔧 - Importing {group.name} in {new_url}")
    with open(f'{path}/{group.name}.tar.gz', 'rb') as f:
        gl_new.groups.import_group(f, path=get_config()["NEW_GROUP_NAME"].lower().replace(" ", "") ,name=get_config()["NEW_GROUP_NAME"])
    logging.info(f"🆗 - Group {group.name} imported correctly in {new_url}")