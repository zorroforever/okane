from tortoise.contrib.sanic import register_tortoise
from config import configs

# mysql database url
SQLALCHEMY_DATABASE_URL = "mysql://{}:{}@{}:{}/{}?charset=utf8".format(
    configs.MYSQL_USER,
    configs.MYSQL_PASSWORD,
    configs.MYSQL_SERVER,
    configs.MYSQL_PORT,
    configs.MYSQL_DB_NAME
)

# tortoise orm json config
TORTOISE_ORM = {
    "connections": {"default": SQLALCHEMY_DATABASE_URL},
    "apps": {
        "models": {
            "models": ["app.models.model"],
            "default_connection": "default",
        },
    },
    "use_tz": False,
    "timezone": "Asia/Shanghai"
}


def db_init(app):
    register_tortoise(
        app,
        config=TORTOISE_ORM,
        generate_schemas=False
    )
