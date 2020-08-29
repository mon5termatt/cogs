from .antimentionspam import AntiMentionSpam

__red_end_user_data_statement__ = (
    "This cog does not persistently store data or metadata about users. "
    "Discord IDs of users may occasionally be logged to file "
    "as part of exception logging."
)


async def setup(bot):
    await bot.send_to_owners(
        "Thanks For Installing My Cog! "
    )
    bot.add_cog(AntiMentionSpam(bot))
