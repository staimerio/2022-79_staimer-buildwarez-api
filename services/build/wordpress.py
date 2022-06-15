"""Services for hentaistube controller"""
# Retic
from retic import App as app

# services
from retic.services.responses import success_response


# services
import services.build.nginx as nginx

# Constants


def build_wp_movies(
    db_username,
    db_password,
    db_name,
    db_host,
    url_domain,
):
    """Set nginx config file"""
    _nginx_file = nginx.build_nginx_config_file(url_domain=url_domain)
    return _nginx_file
