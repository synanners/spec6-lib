from flask import (
    Flask,
    request
)
from app.modules.acquisitions.acquisition_api import acquisitions


app = Flask(__name__)

app.register_blueprint(acquisitions)


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404


@app.errorhandler(500)
def server_error(e):
    """Return a custom 500 error."""
    return 'Error while serving request', 500

