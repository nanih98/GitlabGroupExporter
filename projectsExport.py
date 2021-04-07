import gitlab
import time
import logging
import urllib3
from credentials import old_config_credentials, new_config_credentials
from config import get_config
from groupExport import get_new_group_id
urllib3.disable_warnings()

# Set credentials to Gitlabs
gl_old = old_config_credentials()
gl_new = new_config_credentials()

old_projects_ids = {}
new_projects_ids = {}

## Search projects from oldGroupId
def project_export_import(oldGroupId,path,newGroupId):
    '''
    Export project from groupId on old gitlab instance. Then import into the new gitlab instance in the respective group
    '''
    group = gl_old.groups.get(oldGroupId)
    projects = group.projects.list()
    
    old_url = get_config()['OLD_GITLAB_URL']
    new_url = get_config()['NEW_GITLAB_URL']

    for project in projects:
        p = gl_old.projects.get(project.id)
        logging.info(f"🔧 - Exporting project {project.name} from {old_url}")
        export = p.exports.create()
    
        # Wait for the 'finished' status
        export.refresh()
        while export.export_status != 'finished':
            time.sleep(1)
            export.refresh()
    
        # Download the result
        with open(f'{path}/project_export_'+project.name+'.tar.gz', 'wb') as f:
            export.download(streamed=True, action=f.write)

        logging.info(f"🔧 - Importing project {project.name} on {new_url}")
        output = gl_new.projects.import_project(file=open(f'{path}/project_export_'+project.name+'.tar.gz', 'rb'), path=project.path, name=project.name, namespace=f"{newGroupId}")
        # Get a ProjectImport object to track the import status
        project_import = gl_new.projects.get(output['id'], lazy=True).imports.get()
        while project_import.import_status != 'finished':
            time.sleep(1)
            project_import.refresh()
        logging.info("🆗 - Next project")

def get_old_subgroups(oldGroupId):
    '''
    Recursive function to retrieve all subgroups of a parent group from old instance. We add the name of the subgroups and their id to a dictionary
    '''
    group = gl_old.groups.get(oldGroupId)
    subgroups = group.subgroups.list()
    
    for subgroup in subgroups:
        slash = subgroup.full_path.find('/')
        length = len(subgroup.full_path)
        old_projects_ids[subgroup.full_path[slash:length]] = subgroup.id
        get_old_subgroups(subgroup.id)


def get_new_subgroups(newGroupId):
    '''
    Recursive function to retrieve all subgroups of a parent group from new instance. We add the name of the subgroups and their id to a dictionary
    '''
    group = gl_new.groups.get(newGroupId)
    subgroups = group.subgroups.list()
    
    for subgroup in subgroups:
        slash = subgroup.full_path.find('/')
        length = len(subgroup.full_path)
        new_projects_ids[subgroup.full_path[slash:length]] = subgroup.id
        get_new_subgroups(subgroup.id)

def migrate_projects(path):
    '''
    Encapsulate project migration functions
    '''
    # First migrate projects from parent group
    get_old_subgroups(get_config()["OLD_GROUP_ID"])
    get_new_subgroups(get_new_group_id())
    project_export_import(get_config()["OLD_GROUP_ID"],path,get_new_group_id())
    
    # Then, migrate projects from subgroups
    for k, v in old_projects_ids.items():
        project_export_import(v,path,new_projects_ids[k])
