''' GitHub push code adapated from https://stackoverflow.com/questions/38594717 '''

from github import Github, InputGitTreeElement

token = 'e33eeb41a8a264e5c2e737db2383a37b494a32af'
g = Github(token)

repo = g.get_user().get_repo('soilsensor')
file = 'soilsensor/data/sensordata.csv'

commit_message = 'New data'
master_ref = repo.get_git_ref('heads/master')
master_sha = master_ref.object.sha
base_tree = repo.get_git_tree(master_sha)

with open(file, 'rb') as input_file:
  data = input_file.read()
element = InputGitTreeElement(entry, '100644', 'blob', data)

tree = repo.create_git_tree(element, base_tree)
parent = repo.get_git_commit(master_sha)
commit = repo.create_git_commit(commit_message, tree, [parent])
master_ref.edit(commit.sha)
