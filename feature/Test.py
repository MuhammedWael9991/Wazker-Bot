import nextcord
from nextcord import Interaction
from nextcord.ext import commands

class Test(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(name="test", description="اختبار أوامر Slash")
    async def test(self, interaction: Interaction):
        print("LOG: Command test Called")
        await interaction.response.send_message("✅ Slash command يعمل بنجاح!")
