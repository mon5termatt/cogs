from .core import RoleManagement

__red_end_user_data_statement__ = (
    "This cog does not persistently store end user data. "
    "This cog does store discord IDs as needed for operation."
)


async def setup(bot):
    await bot.send_to_owners(
        "Thanks For Installing My Cog! "
    )
    cog = RoleManagement(bot)
    bot.add_cog(cog)
    cog.init()
