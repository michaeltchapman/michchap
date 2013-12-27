# Download repositories from github 

import requests
import json
import os
import subprocess

from requests_oauthlib import OAuth2Session

userpass = ('michaeltchapman', '29fb0e5cbeb0913b63ee5bba8dbf41d3a334f02f')

def get_repos(user):
    page = 1
    while (True):
        r = requests.get('https://api.github.com/users/' + user + '/repos', params={'page' : str(page) })
        print 'requested page ' + str(page)
        if (r.ok):
            j = json.loads(r.text)
            reps = json.loads(r.text)
            for r in reps:
                print r['name']
                langs = requests.get(r['languages_url'], auth=userpass)
                r['languages'] = json.loads(langs.text)
                with open(str('repos/' + r['name']), 'w') as wf:
                    wf.write(json.dumps(r, indent=4, sort_keys=True))
            if len(reps) < 30:
                break
            page = page + 1

get_repos('michaeltchapman')
get_repos('stackforge')
get_repos('openstack')

repos = []

for f in os.listdir('repos'):
    with open('repos/' + f, 'r') as r:
        repos.append(json.loads(r.read()))

for repo in repos:
    if repo['name'] not in os.listdir('clones'):
        print repo['name']
        print repo['clone_url']
        subprocess.call(['git', 'clone', repo['clone_url'], 'clones/' + repo['name']])
    else:
        os.chdir('clones/' + repo['name'])
        subprocess.call(['git', 'fetch', 'origin'])
        os.chdir('../..')
