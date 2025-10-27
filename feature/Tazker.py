import nextcord
from nextcord import Interaction
from nextcord.ext import commands, tasks
import asyncio

class StartTazker(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.current_index = 0

        self.audio_files_list = [
            "bot_audio/استغفر الله وأتوب اليه.mp3",
            "bot_audio/الحمدلله.mp3",
            "bot_audio/اللهم انت ربي.mp3",
            "bot_audio/اللهم صلي على سيدنا محمد.mp3",
            "bot_audio/بسم الله الذي لايضر مع اسمه شي في الأرض ولا في السماء وهو العلي العظيم.mp3",
            "bot_audio/سبحان الله.mp3",
            "bot_audio/سبحان الله عدد خلقه وزضا نفسه وزنة عرشة.mp3",
            "bot_audio/سبحان الله و بحمده سبحان الله العظيم.mp3",
            "bot_audio/لا اله الا الله.mp3",
            "bot_audio/لا اله الا انت سبحانك اني كنت من الظالمين.mp3",
        ]

    @nextcord.slash_command(name="start_tazker", description="بدء تشغيل التذكير الصوتي الدوري")
    async def start_tazker(self, interaction: Interaction):
        await interaction.response.defer()
        print("LOG: Command start_tazker Called")

        if not interaction.guild.voice_client:
            await interaction.followup.send("❌ البوت ليس في قناة صوتية. استخدم أمر `/join` أولاً!")
            return

        if not self.play_periodic_audio.is_running():
            self.play_periodic_audio.start(interaction.guild.id)
            await interaction.followup.send("✅ بدأ تشغيل التذكير الصوتي كل دقيقة!")
        else:
            await interaction.followup.send("⚠️ التذكير يعمل بالفعل!")

    @tasks.loop(minutes=5)
    async def play_periodic_audio(self, guild_id: int):
        guild = self.bot.get_guild(guild_id)
        vc = guild.voice_client

        if vc and vc.is_connected():
            await self.play_audio(vc)
        else:
            print("❌ لم يتم العثور على اتصال صوتي!")

    async def play_audio(self, vc: nextcord.VoiceClient):
        if not vc.is_connected():
            return

        audio = self.audio_files_list[self.current_index]
        print(f"🎧 Playing: {audio}")

        source = nextcord.FFmpegPCMAudio(audio)
        vc.play(source)

        while vc.is_playing():
            await asyncio.sleep(1)

        self.current_index = (self.current_index + 1) % len(self.audio_files_list)

    @nextcord.slash_command(name="stop_tazker", description="ايقاف التذكير")
    async def stop_tazker(self, interaction: Interaction):
        if self.play_periodic_audio.is_running():
            self.play_periodic_audio.stop()
            print("LOG: Command stop_tazker Called")
            await interaction.response.send_message("✅ تم إيقاف تشغيل التذكير!")
        else:
            await interaction.response.send_message("❌ لم يتم بدء التشغيل حتى الآن!")