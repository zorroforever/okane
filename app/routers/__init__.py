from app.routers import user_view


# add new blueprint here
def router_init(app):
    app.blueprint(user_view.view_bp)
