# (BETA) GitlabGroupExporter 
Export group with all projects and subgroups

# Requirements  

* python >=3.6
* admin rights over gitlab (owner role to export groups and projects, admin rights to create groups, projects...)
* API token on both Gitlab (asigned to your gitlab user)

# Install  
1. Install requirements

```sh
pip3 install -r requirements.txt
```

# Usage  

## Configuration file (config.yml)

Set your configuration with config.yml (on root path)

```
vim config.yml
```

```yaml
OLD_GITLAB_URL: https://oldgitlab.com
OLD_TOKEN: XXXX
NEW_GITLAB_URL: http://newgitlab.com
NEW_TOKEN: XXXXX
OLD_GROUP_ID: XXXXX
NEW_GROUP_NAME: MyNewImportedGroup
```

### Variables description
 * **OLD_GITLAB_URL**: Gitlab url from you want to export the group
 * **OLD_TOKEN**: Gitlab token with API access from old gitlab instance
 * **NEW_GITLAB_URL**: Gitlab url where you want to import that new group
 * **NEW_TOKEN**: Gitlab token with API access from new gitlab instance
 * **OLD_GROUP_ID**: Group Id from the group that you want to export (on old gitlab instance)
 * **NEW_GROUP_NAME**: New group name that you will create (import) over that new gitlab instance

## Example command  

```
mkdir /tmp/gitlab 
python3 main.py -p /tmp/gitlab/ -l INFO
```
**Note:** Directory must be created and need to be empty. When you set the directory on the command, need to end with slash '/'

# Examples  

# Group to be exported  

![Old group](/img/old_gitlab.png)

# New group imported from old gitlab instance  

![New group](/img/new_gitlab.png)

# Command
![Command example](/img/command-example.png)

# Config  

![Config example](/img/config-example.png)

# Result
![Result]()


Then, delete the directory if you no longer need it.

```sh
rmdir /tmp/gitlab
```

# About code

* This code written in python possibly has many unanticipated improvements. It is not a program designed at a productive level contemplating all the possible errors that may exist.

* It is only a functional program designed to automate.

* As for the python code itself, possible improvements are welcome. I am not a 100% experienced python programmer, but I am having fun. Enjoy :)