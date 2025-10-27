import nextcord
from nextcord import Interaction
from nextcord.ext import commands

class Join(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(name="join", description="الدخول للقناة الصوتية")
    async def join(self, interaction: Interaction):
        print("LOG: Command join Called")
        if interaction.user.voice:
            channel = interaction.user.voice.channel
            if not interaction.guild.voice_client:
                await channel.connect()
                await interaction.response.send_message("✅ انا جيت ")
                print("LOG: bot joined to {channel}".format(channel=channel))
            else:
                await interaction.response.send_message("❌ انا بالفعل داخل القناة")
        else:
            await interaction.response.send_message("❌ والله ابدا ادخل انت الأول ")