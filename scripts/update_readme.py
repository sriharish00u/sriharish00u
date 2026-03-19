import os
import requests
from datetime import date

# your github username
USERNAME = "sriharish00u"
TOKEN = os.environ["GITHUB_TOKEN"]

# fetch your repos from github api
headers = {"Authorization": f"token {TOKEN}"}
url = f"https://api.github.com/users/{USERNAME}/repos?sort=updated&per_page=6"
repos = requests.get(url, headers=headers).json()

# build the projects list
lines = []
for repo in repos:
    if repo["fork"]:          # skip forked repos
        continue
    name = repo["name"]
    desc = repo["description"] or "no description yet"
    link = repo["html_url"]
    lines.append(f"- [{name}]({link}) — {desc}")

# build the block to inject
block = "\n".join(lines)
block += f"\n\n_auto updated: {date.today()}_"

# read current readme
with open("README.md", "r") as f:
    readme = f.read()

# find the markers and replace content between them
start_marker = "<!-- PROJECTS:START -->"
end_marker   = "<!-- PROJECTS:END -->"

start_idx = readme.find(start_marker) + len(start_marker)
end_idx   = readme.find(end_marker)

new_readme = readme[:start_idx] + "\n" + block + "\n" + readme[end_idx:]

# write back
with open("README.md", "w") as f:
    f.write(new_readme)

print("README updated successfully")

