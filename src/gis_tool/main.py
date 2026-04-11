import argparse
import getpass
from .config import save_credentials, get_credentials
from .cli import arg_parser
import logging
import sys

# from logger import setup_logger

log = logging.getLogger(f"gis_tool.{__name__}")


def main():
    args = arg_parser()

    # Enforce --sys-env req. after parse
    if not args.system_environment:
        log.error("the following arguments are required: --sys-env")
        sys.exit(1)

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
