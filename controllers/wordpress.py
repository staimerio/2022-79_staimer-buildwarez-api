# Retic
from retic import Request, Response, Next, App as app
from retic.services.validations import validate_obligate_fields

# Services
from retic.services.responses import error_response, success_response
from services.build import wordpress


def build_wp_movies(req: Request, res: Response, next: Next):
    """Validate obligate params"""
    _validate = validate_obligate_fields({
        u'db_username': req.param('db_username'),
        u'db_password': req.param('db_password'),
        u'db_name': req.param('db_name'),
        u'url_domain': req.param('url_domain'),
    })

    """Check if has errors return a error response"""
    if _validate["valid"] is False:
        return res.bad_request(
            error_response(
                "The param {} is necesary.".format(_validate["error"])
            )
        )

    """Get all novel from latests page"""
    _result = wordpress.build_wp_movies(
        req.param('db_username'),
        req.param('db_password'),
        req.param('db_name'),
        req.param('db_host', "localhost"),
        req.param('url_domain'),
    )
    """Check if exist an error"""
    if _result['valid'] is False:
        return res.bad_request(_result)
    """Response the data to client"""
    res.ok(_result)
