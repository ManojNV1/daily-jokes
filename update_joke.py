import requests
import re

# Fetch a random joke
response = requests.get("https://v2.jokeapi.dev/joke/Any?format=txt&safe-mode")
joke = response.text.strip() if response.status_code == 200 else "Failed to fetch joke 😢"

# Update README
with open("README.md", "r") as f:
    readme = f.read()

updated_readme = re.sub(r"{{JOKE}}", joke, readme)

with open("README.md", "w") as f:
    f.write(updated_readme)