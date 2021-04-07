# GitlabGroupExporter
Export group with all projects and subgroups

# Requirements

* python >=3.6
* admin rights over gitlab servers

# Install
1. Install requirements

```sh
pip3 install -r requirements.txt
```

# Usage

## Configuration file (config.yml)

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
 * **OLD_GROUP_ID**: Group Id from the group what you want to export (on old gitlab instance)
 * **NEW_GROUP_NAME**: New group name that you will create (import) over that new gitlab instance

