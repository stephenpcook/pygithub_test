import json
from github import Github

with open('env.json') as f:
    config = json.load(f)

token = config['github_token']
repo_name = config['repo_name']

g = Github(token)

r = g.get_user().get_repo(repo_name)
print(r.default_branch)

r.edit(default_branch='release')
print(r.default_branch)
