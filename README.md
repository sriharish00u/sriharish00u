# sriharish00u

## About
This repository serves as a personal toolkit, housing a collection of utility scripts designed to streamline various development workflows. It includes tools for automating the update of a GitHub profile README with recent project activity and scripts for leveraging AI to assist with code documentation generation.

## Features
*   **Automated GitHub Profile Update**: Dynamically fetches and lists your latest, non-forked GitHub repositories to keep your profile README fresh.
*   **AI-Powered Code Scanning**: Scans a wide range of code files (Python, JavaScript, HTML, CSS, TypeScript, Java, C++, C) within a repository.
*   **Gemini API Integration**: Utilizes the Google Gemini API for potential AI-driven insights or content generation based on scanned code.
*   **Configurable Directory Skipping**: Intelligently skips common development directories like `.git`, `node_modules`, `__pycache__`, and `.github` during code scans.

## Tech Stack
*   **Core Language**: Python 3.x
*   **External APIs**:
    *   GitHub API (for repository data)
    *   Google Gemini API (for AI capabilities)
*   **Libraries**:
    *   `requests` (for making HTTP requests)
*   **Standard Python Modules**:
    *   `os` (for operating system interactions)
    *   `json` (for JSON data handling)
    *   `datetime` (for date-related operations)

## Getting Started

### Prerequisites
Before you begin, ensure you have the following installed and configured:
*   **Python 3.x**: Download and install from [python.org](https://www.python.org/downloads/).
*   **`requests` library**: Install via pip:
    ```bash
    pip install requests
    ```
*   **GitHub Personal Access Token**:
    *   Generate a token with `repo` scope from your [GitHub Developer Settings](https://github.com/settings/tokens).
    *   Set it as an environment variable: `GITHUB_TOKEN`.
    ```bash
    export GITHUB_TOKEN="YOUR_GITHUB_PERSONAL_ACCESS_TOKEN"
    ```
*   **Google Gemini API Key**:
    *   Obtain an API key from the Google AI Studio or Google Cloud Console.
    *   Set it as an environment variable: `GEMINI_API_KEY`.
    ```bash
    export GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
    ```

### Installation
1.  **Clone the repository**:
    ```bash
    git clone https://github.com/sriharish00u/sriharish00u.git
    cd sriharish00u
    ```

2.  **Verify prerequisites**: Ensure `requests` is installed and environment variables are set as described above.

## Usage

### Updating Your GitHub Profile README
The `update_readme.py` script automatically fetches your latest projects and can be integrated into your profile README.

To run the script:
```bash
python scripts/update_readme.py
```
This script will typically generate content that can be placed into your main `README.md` file (e.g., in your `sriharish00u` profile repository if used for that purpose).

### Generating Code Documentation (AI-Assisted)
The `generate_docs.py` script is designed to scan a codebase and interact with the Gemini API.

To run the script from the root of a project you wish to scan:
```bash
python scripts/generate_docs.py
```
By default, `scan_repo` will scan the current directory (`.`). You can modify the `scan_repo` function in `scripts/generate_docs.py` to specify a different path if needed. The exact output or interaction with the Gemini API depends on further implementation within the `generate_docs.py` script.

## API Reference

### Internal Script Functions
*   **`scan_repo(path=".")`** (in `generate_docs.py`):
    *   Scans all code files within the specified `path` (defaults to current directory).
    *   Collects content from files with extensions like `.py`, `.js`, `.html`, `.css`, `.ts`, `.java`, `.cpp`, `.c`.
    *   Skips directories such as `.git`, `node_modules`, `__pycache__`, and `.github`.

### External API Usage
*   **GitHub API**: `api.github.com/users/{USERNAME}/repos` is used to fetch a user's repositories.
*   **Google Gemini API**: `generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent` is used for AI model interactions.

## Screenshots
_To add screenshots, replace this section with relevant images showcasing the project's functionality (e.g., an updated GitHub profile README, or output from the documentation generator)._

## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, please feel free to:
1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/AmazingFeature`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
5.  Push to the branch (`git push origin feature/AmazingFeature`).
6.  Open a Pull Request.

## License
MIT