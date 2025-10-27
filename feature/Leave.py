import nextcord
from nextcord import Interaction
from nextcord.ext import commands

class Leave(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(name="leave", description="الخروج من القناة الصوتية")
    async def leave(self, interaction: Interaction):
        if interaction.guild.voice_client:
            await interaction.guild.voice_client.disconnect()
            await interaction.response.send_message("❌ انا خرجت ")
            print("LOG: Command leave Called")
        else:
            await interaction.response.send_message("❌ ياعم انا مش جوه")