from tortoise import Tortoise, run_async


async def init():
    await Tortoise.init(
        db_url='mysql://meta:meta123@127.0.0.1:3306/meta?charset=utf8',
        modules={'models': ['app.models.model']},
        timezone="Asia/Shanghai"
    )
    # Generate the schema
    await Tortoise.generate_schemas(safe=False)


run_async(init())
