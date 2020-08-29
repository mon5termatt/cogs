from .general import General

__red_end_user_data_statement__ = (
    "This cog does not persistently store data or metadata about users."
)


async def setup(bot):
    await bot.send_to_owners(
        "Thanks For Installing My Cog! "
    )
    bot.add_cog(General())
