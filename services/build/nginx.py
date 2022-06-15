"""Services for hentaistube controller"""
# Retic
from distutils.log import error
from importlib.resources import path
from retic import App as app

# Services
from retic.services.responses import success_response, error_response

# Constants
import services.general.constants as constants


def build_nginx_config_file(
    url_domain,
):
    try:
        _path = "/home/admin/conf/web/{0}.nginx.conf".format(url_domain)
        _nginx_template = constants.NGINX_TEMPLATE.replace("$HOST", app.config.get(
            'VPS_HOST')).replace("$PORT", app.config.get('VPS_PORT')).replace("$DOMAIN", url_domain)

        _file = open(_path, "w")
        _file.write(_nginx_template)
        _file.close()

        _data = {
            u'path': _path,
        }
        return success_response(_data)
    except Exception as e:
        return error_response(msg="Ngnix file error when was updated, error: {0}".format(str(e)))
