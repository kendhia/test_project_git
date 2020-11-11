import json
import os
import requests
from github import Github

# GitHub API Token
GH_API_TOKEN = '0da2f28e4c68a760bf8697c9d96332eddd471214'
# GitHub User Name
GH_USER = 'Dhia Kennouche'
# Variable to store first argument to setup-repo, the repo name. Will be used as GH repo name, too.
NEW_REPO_NAME = "test_project2"

# Project directory.
PROJECT_DIR = "C:\\Users\\dhiak\\Documents\\pythonprojects\\prototypes"
# GitHub repos Create API call
g = Github(GH_API_TOKEN)
u = g.get_user()
repo = u.create_repo(NEW_REPO_NAME)


init_local_git = f"git init {PROJECT_DIR}"
remote_push = f"git -C {PROJECT_DIR} remote add origin https://github.com/kendhia/{NEW_REPO_NAME}.git"
os.system(init_local_git)
os.system(remote_push)

os.system(f"git -C {PROJECT_DIR} add . & git -C {PROJECT_DIR} commit -a -m 'message' & git -C {PROJECT_DIR} push --set-upstream origin master")
os.system(f"git -C {PROJECT_DIR} push --set-upstream origin master")