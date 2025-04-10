from git import Repo

def git_commit_push(message="Auto commit"):
    repo = Repo('.')  # Current directory
    repo.git.add(A=True)
    repo.index.commit(message)
    origin = repo.remote(name='origin')
    origin.push()

git_commit_push("Commit using GitPython")
