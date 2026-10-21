import re
from urllib.parse import urlparse


def analyze_github_url(github_url: str) -> dict:
    """
    Validate a public GitHub profile or repository URL.
    This does not fetch live GitHub statistics.
    """

    github_url = github_url.strip()

    if not github_url:
        return {
            "valid": False,
            "message": "Please provide a GitHub URL."
        }

    parsed_url = urlparse(github_url)

    if (
        parsed_url.scheme not in ("http", "https")
        or parsed_url.hostname not in ("github.com", "www.github.com")
    ):
        return {
            "valid": False,
            "message": "Please provide a valid GitHub URL."
        }

    path_parts = [
        part for part in parsed_url.path.strip("/").split("/")
        if part
    ]

    if not path_parts:
        return {
            "valid": False,
            "message": "GitHub username or repository is missing."
        }

    username = path_parts[0]

    if not re.fullmatch(r"[A-Za-z0-9-]{1,39}", username):
        return {
            "valid": False,
            "message": "The GitHub username format is invalid."
        }

    result = {
        "valid": True,
        "username": username,
        "profile_url": f"https://github.com/{username}",
        "repository": None,
        "message": "GitHub URL format is valid."
    }

    if len(path_parts) >= 2:
        result["repository"] = path_parts[1]

    return result