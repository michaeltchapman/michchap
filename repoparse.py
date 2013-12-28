# Generate web assets from template

import json
import yaml
import os
import subprocess
import requests
import codecs
from jinja2 import Template

repos = []

sf_repos = {}
os_repos = {}
my_repos = {}

userpass = ('michaeltchapman', '29fb0e5cbeb0913b63ee5bba8dbf41d3a334f02f')

languages = { 'Python' : 'python_logo.png',
              'Ruby'   : 'ruby_logo.png',
              'Shell'  : 'shell_logo.png',
              'Puppet' : 'puppet_logo.png'
            }

for f in os.listdir('repos'):
    with open('repos/' + f, 'r') as r:
        repos.append(json.loads(r.read()))

icon_url = repos[0]['owner']['avatar_url']

os.chdir('clones')
for repo in repos:
    os.chdir(repo['name'])
    output = subprocess.check_output(['git', 'log', '--author=Michael\ Chapman', '--oneline', '--all'])
    lines = output.split('\n')
    if (lines > 0):
        for commit in lines:
            c = commit.split(' ')
            if len(c) > 1 and c[1] != 'Merge':
                if 'my_commits' not in repo:
                    repo['my_commits'] = 1
                else:
                    repo['my_commits'] = repo['my_commits'] + 1
    os.chdir('..')

os.chdir('..')
def print_repo(name, repos):
    print '  <div class="openstack_repos">'
    print '    <div>'
    print '      <img src="' + icon_url + '"/>'
    print '    </div>'
    print '    <div>'
    print "      <h4>" + name.title() + " Commits</h4>"
    print '    </div>'
    print "    <table>"
    for repo, count in repos.items():
        print "      <tr>"
        print "".join(['        ', '<td>',repo,'</td>'])
        print "".join(['        ','<td>',str(count),'</td>'])
        print "      </tr>"
    print "    </table>"
    print "  </div>"

def jinja_template(name):
    personal_repos = {}
    os_repos = []
    sf_repos = []
    for repo in repos:
        if repo['owner']['login'] == name:
            if not repo['fork']:
                repo['languages'] = map(lambda l:l.lower(), repo['languages'])
                personal_repos[repo['name']] = repo
        if repo['owner']['login'] == 'stackforge' and 'my_commits' in repo:
            sf_repos.append(repo)
        if repo['owner']['login'] == 'openstack' and 'my_commits' in repo:
            os_repos.append(repo)

    with open('resume/index.html', 'r') as temp_file:
        template = Template(temp_file.read().decode('utf-8'))
        print template.render(personal_repos=personal_repos, os_repos=os_repos, sf_repos=sf_repos).encode('utf-8')

jinja_template('michaeltchapman')
