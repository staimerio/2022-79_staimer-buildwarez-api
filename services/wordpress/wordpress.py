"""Services for hentaistube controller"""
# Retic
from retic import App as app

# Requests
import requests

# bs4
from bs4 import BeautifulSoup
from retic.services.responses import success_response

# Time
from datetime import datetime

# Time
from time import sleep

# services
import services.general.wordpress as wordpress

import services.general.constants as constants

# Constants


def build_wp_movies(
    db_username,
    db_password,
    db_name,
    url_site,
):
    """Set nginx config file"""
    pass