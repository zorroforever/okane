from sanic import Sanic
from app.db.database import db_init
from app.routers import router_init
from app.logs import log_init, sys_log


def conf_init(app):
    from config import configs
    sys_log.info(msg=f'Start app with {configs.ENVIRONMENT} environment')
    if configs.ENVIRONMENT == 'production':
        app.docs_url = None
        app.redoc_url = None
        app.debug = False


def create_app():
    app = Sanic(__name__)
    log_init()
    db_init(app)
    router_init(app)
    return app
