class GetAzkarUseCase:
    def __init__(self, remote_repository, local_repository):
        self.remote_repository = remote_repository
        self.local_repository = local_repository

    async def execute(self):
        azkar_urls = self.remote_repository.get_azkar_urls()
        azkar_sounds = await self.local_repository.cache_azkar_files(azkar_urls, cache_dir="cache/audio/")
        return azkar_sounds
