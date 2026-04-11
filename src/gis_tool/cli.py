import argparse

# import logging

# log = logging.getLogger(f"gis_tool.{__name__}")


def arg_parser() -> argparse.ArgumentParser:
    # Creates parent parser (Global Args)
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

    return parser.parse_args()
