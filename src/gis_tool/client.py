import logging
from logger import logger
from arcgis.gis import GIS
from arcgis.auth._error import ArcGISLoginError

log = logging.getLogger(f"gis_tool.{__name__}")
logging.getLogger("arcgis").setLevel(logging.ERROR)


def gis_connection(org_url: str, username: str, password: str) -> GIS:
    """Returns connection to ArcGIS (Online or Portal). Raises on failure."""

    try:
        log.info(f"Attempting connection to {org_url}")
        gis = GIS(
            url=org_url,
            username=username,
            password=password,
        )
        log.info(f"Successfully connected as {gis.users.me.username}")
        return gis
    except ArcGISLoginError as e:
        log.error(f"Invalid username, password, or both: {e}")
    except RuntimeError as e:
        log.error(f"Failed connecting to {org_url}; runtime error: {e}")
        raise
    except Exception as e:
        log.error(f"Failed connecting to {org_url}: {e}")
        raise
