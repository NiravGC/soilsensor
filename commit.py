''' GitHub push code taken from https://stackoverflow.com/questions/38594717 '''

from github import Github, InputGitTreeElement

token = 'e33eeb41a8a264e5c2e737db2383a37b494a32af'
g = Github(token)

repo = g.get_user().get_repo('soilsensor')
file_list = [
  'data/sensordata.csv',
  'data/notes.txt'
]

commit_message = 'Data update'
master_ref = repo.get_git_ref('heads/master')
master_sha = master_ref.object.sha
base_tree = repo.get_git_tree(master_sha)

element_list = list()
for entry in file_list:
    with open(entry, 'rb') as input_file:
        data = input_file.read()
    element = InputGitTreeElement(entry, '100644', 'blob', data)
    element_list.append(element)
tree = repo.create_git_tree(element_list, base_tree)
parent = repo.get_git_commit(master_sha)
commit = repo.create_git_commit(commit_message, tree, [parent])
master_ref.edit(commit.sha)
