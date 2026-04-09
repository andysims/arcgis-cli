import argparse
import getpass
from .config import save_credentials, get_credentials
import logging

# from logger import setup_logger

log = logging.getLogger(f"gis_tool.{__name__}")


def main():
    parser = argparse.ArgumentParser(description="GIS CLI Tool")
    subparsers = parser.add_subparsers(dest="command")

    # Configure Command
    conf_parser = parser.add_argument("configure", help="Saves credentials")
    # conf_parser.add_argument(
    #    "--profile", default="default", help="Profile name (e.g., portal, agol)"
    # )
    conf_parser.add_argument("--url", type=str, help="ArcGIS URL")
    conf_parser.add_argument("--user", type=str, help="Username")

    # Add Main Args
    parser.add_argument(
        "--sys-env",
        "--system-env",
        "--system-environment",
        type=str,
        help="Specify system environment (e.g., portal, agol)",
    )
    parser.add_argument(
        "--search-user", type=str, help="Enter email or username to search for a user"
    )

    args = parser.parse_args()

    profile = (args.system_environment).strip().lower()

    if args.command == "configure":
        log.info(f"Setting up login config file for {args.user} on {args.url}")

        # Prompt for password securely
        password = getpass.getpass(f"Enter password for {args.user}: ")
        save_credentials(profile, args.url, args.user, password)
        log.info(f"Successfully saved credentials for profile: {profile}")

    # Grab creds
    creds = get_credentials(profile=profile)
    print(creds)


if __name__ == "__main__":
    main()
