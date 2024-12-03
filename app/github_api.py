from github import Github

def fetch_repo_files(token, repo_name):
    g = Github(token)
    repo = g.get_repo(repo_name)
    files = repo.get_contents("")
    return [file.path for file in files if file.type == "file"]