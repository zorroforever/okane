from tortoise import timezone

from app.models.model import OkaneUser


async def list_all():
    users = await OkaneUser.all()
    return users


async def list_by_id(uid):
    users = await OkaneUser.filter(id=uid).first()
    return users


async def save_user(user_name):
    timezone.get_use_tz()
    await OkaneUser.get_or_create(c_name=user_name)


async def update_username(uid, user_name):
    await OkaneUser.filter(id=uid).update(c_name=user_name)
