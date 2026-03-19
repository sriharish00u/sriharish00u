import os
import requests
import json

GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"

def scan_repo(path="."):
    """scan all code files in the repo"""
    code_content = []
    extensions = [".py", ".js", ".html", ".css", ".ts", ".java", ".cpp", ".c"]
    skip_dirs = [".git", "node_modules", "__pycache__", ".github"]

    for root, dirs, files in os.walk(path):
        # skip unwanted folders
        dirs[:] = [d for d in dirs if d not in skip_dirs]
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()[:500]  # first 500 chars per file
                        code_content.append(f"### {filepath}\n{content}")
                except:
                    pass

    return "\n\n".join(code_content[:10])  # max 10 files


def generate_readme(repo_name, code_summary):
    """send code to gemini and get a full readme back"""

    prompt = f"""
You are a technical documentation expert.

Based on this code from a GitHub project called "{repo_name}", write a complete professional README.md.

CODE SUMMARY:
{code_summary}

Write the README in this exact structure:

# {repo_name}

## About
(2-3 lines about what this project does)

## Features
(bullet list of key features)

## Tech Stack
(list the technologies used based on the code)

## Getting Started

### Prerequisites
(what needs to be installed)

### Installation
(step by step setup commands)

## Usage
(how to run and use the project)

## API Reference
(if applicable, list endpoints or functions)

## Screenshots
(placeholder section with instructions to add screenshots)

## Contributing
(standard contributing guide)

## License
MIT

Keep it clean, professional, and accurate to the actual code.
Only return the README content, nothing else.
"""

    body = {
        "contents": [{"parts": [{"text": prompt}]}]
    }

    response = requests.post(GEMINI_URL, json=body)
    result = response.json()

    try:
        return result["candidates"][0]["content"]["parts"][0]["text"]
    except:
        print("Gemini error:", json.dumps(result, indent=2))
        return None


def main():
    repo_name = os.path.basename(os.getcwd())
    print(f"Scanning repo: {repo_name}")

    code_summary = scan_repo(".")
    if not code_summary:
        print("No code files found")
        return

    print("Sending to Gemini...")
    readme = generate_readme(repo_name, code_summary)

    if readme:
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(readme)
        print("README.md generated successfully")
    else:
        print("Failed to generate README")


if __name__ == "__main__":
    main()
```

---

Now add the Gemini API key to GitHub secrets:
```
1. Go to your repo → Settings
2. Secrets and variables → Actions
3. New repository secret
4. Name:  GEMINI_API_KEY
5. Value: your key
6. Click Add secret
