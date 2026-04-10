import argparse
import getpass
from .config import save_credentials, get_credentials
import logging

# from logger import setup_logger

log = logging.getLogger(f"gis_tool.{__name__}")


def main():
    parser = argparse.ArgumentParser(description="GIS CLI Tool")
    subparsers = parser.add_subparsers(dest="command")

    # --- FIX STARTS HERE ---
    # Create a dedicated parser for the 'configure' command
    conf_parser = subparsers.add_parser(
        "configure",
        help="Saves/Sets up credentials. You must provide both --url and --user.",
    )

    # Add arguments specifically to the 'configure' sub-command
    conf_parser.add_argument(
        "--url", type=str, required=True, help="ArcGIS or Enterprise/Portal URL"
    )
    conf_parser.add_argument(
        "--user", type=str, required=True, help="Username for authentication"
    )

    # Add Main Args (These will be available globally)
    parser.add_argument(
        "--sys-env",
        dest="system_environment",  # Added dest to match your 'profile' line below
        type=str,
        required=True,
        help="Specify system environment (e.g., portal, agol)",
    )
    parser.add_argument(
        "--search-user", type=str, help="Enter email or username to search for a user"
    )

    args = parser.parse_args()

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
