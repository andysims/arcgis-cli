import os
import configparser
from pathlib import Path
import logging

# from .logger import logger

log = logging.getLogger(f"gis_tool.{__name__}")

CONFIG_DIR = Path.home() / ".gis-tool"
CONFIG_FILE = CONFIG_DIR / "config.ini"


def save_credentials(profile_name: str, url: str, username: str, password: str):
    """Writes credentials to the user's home directory."""
    config = configparser.ConfigParser()

    # Load existing config if it exists so we don't overwrite other profiles
    if CONFIG_FILE.exists():
        config.read(CONFIG_FILE)

    if not CONFIG_DIR.exists():
        CONFIG_DIR.mkdir(parents=True, exist_ok=True)

    config[profile_name] = {"url": url, "user": username, "pass": password}

    with open(CONFIG_FILE, "w") as f:
        config.write(f)

    # Set permissions so only the user can read/write (Unix-style)
    if os.name != "nt":
        os.chmod(CONFIG_FILE, 0o600)


def get_credentials(profile_name="default"):
    """
    Retrieves credentials for a specific profile.
    Returns a dictionary or raises a FileNotFoundError/KeyError.
    """
    if not CONFIG_FILE.exists():
        raise FileNotFoundError(
            f"Configuration file not found at {CONFIG_FILE}. Run 'configure' first."
        )

    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)

    if profile_name not in config:
        raise KeyError(f"Profile '{profile_name}' not found in {CONFIG_FILE}")

    return {
        "url": config[profile_name].get("url"),
        "user": config[profile_name].get("user"),
        "pass": config[profile_name].get("pass"),
    }


if __name__ == "__main__":
    save_credentials(
        profile_name="test", url="https://arcgis.com", username="test", password="bogus"
    )
