from app.logic import logic
from sanic import Blueprint, response
from app.utils.utils import ParseObjToJson
from config import configs

try:
    from ujson import loads as json_loads
except:
    from json import loads as json_loads
view_bp = Blueprint('view_api', url_prefix=configs.API_V1_STR)


# /api/v1/user
@view_bp.route("/user", methods=["GET"])
async def list_all(request):
    users = await logic.list_all()
    return response.json({"Users": [ParseObjToJson(user) for user in users]})


# /api/v1/user/<pk:int>
@view_bp.route("/user/<pk:int>", methods=["GET"])
async def get_user(request, pk):
    users = await logic.list_by_id(pk)
    return response.json({"User": [ParseObjToJson(users)]})


# /api/v1/user/add
@view_bp.route("/user/add", methods=["POST"])
async def add_user(request, **kwargs):
    user_name = request.form.get('user_name')
    if user_name is None:
        return response.json({"User": "wrong param,param is none or other!"})
    await logic.save_user(user_name)
    return response.json({"User": "save ok"})


# /api/v1/user/update
@view_bp.route("/user/update", methods=["POST"])
async def upd_user(request, **kwargs):
    user_name = request.form.get('user_name')
    uid = request.form.get('id')
    if user_name is None or uid is None:
        return response.json({"User": "wrong param,param is none or other!"})
    await logic.update_username(uid, user_name)
    return response.json({"User": "update ok"})