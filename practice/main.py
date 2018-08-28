
import os

repodir = '.repo'               # name of repo's private directory

S_repo = 'repo'                 # special repo repository

REPO_MAIN = S_repo + '/main.py' # main script

 

def _FindRepo():

  """Look for a repo installation, starting at the current directory.

  """

  curdir = os.getcwd()
  print (curdir)

  repo = None

 

  olddir = None

  while curdir != '/' and curdir != olddir and not repo:

    repo = os.path.join(curdir, repodir, REPO_MAIN)
    print(repo)

    if not os.path.isfile(repo):

      repo = None

      olddir = curdir

      curdir = os.path.dirname(curdir)

  return (repo, os.path.join(curdir, repodir))

print (_FindRepo())
