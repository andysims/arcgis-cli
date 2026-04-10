import argparse
import getpass
from .config import save_credentials, get_credentials
import logging

# from logger import setup_logger

log = logging.getLogger(f"gis_tool.{__name__}")


def main():
    # ==== Handles Credentials ====
    # Create a parent parser (Global Args)
    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument(
        "--sys-env",
        dest="system_environment",
        type=str,
        required=False,
        help="Specify system env: ArcGIS Online (agol) or Enterprise/Portal (portal) URL",
    )

    # Main parser
    parser = argparse.ArgumentParser(
        parents=[parent_parser], description="GIS CLI Tool"
    )
    subparsers = parser.add_subparsers(dest="command")

    # Sub-command (for configuring)
    conf_parser = subparsers.add_parser(
        "configure",
        help="Saves/Sets up credentials.",
    )
    conf_parser.add_argument("--url", type=str, required=True)
    conf_parser.add_argument("--user", type=str, required=True)

    # Search parser
    search_parser = subparsers.add_parser(
        "search", help="Search the ArcGIS Online/Portal environment"
    )
    search_parser.add_argument("--user", help="User to search for")
    search_parser.add_argument("--group", help="Group to search for")

    args = parser.parse_args()

    # Enforce --sys-env req. after parse
    if not args.system_environment:
        parser.error("the following arguments are required: --sys-env")

    profile = args.system_environment.strip().lower()

    if args.command == "configure":
        log.info(f"Setting up login config file for {args.user} on {args.url}")

        # Prompt for password securely
        password = getpass.getpass(f"Enter password for {args.user}: ")
        save_credentials(profile, args.url, args.user, password)
        log.info(f"Successfully saved credentials for profile: {profile}")

    # Grab creds
    if not args.command == "configure":
        creds = get_credentials(profile_name=profile)
        print(creds)


if __name__ == "__main__":
    main()
