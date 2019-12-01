from github import Github. InputGit

token = 'e33eeb41a8a264e5c2e737db2383a37b494a32af'
g = Github(token)

repo = g.get_user().get_repo('soilsensor')
file = '/data/sensordata.csv'

commit_message = 'New data'
master_ref = repo.get_git_ref('heads/master')
master_sha = master_ref.object.sha
base_tree = repo.get_git_tree(master_sha)

with open(file, 'rb') as input_file
