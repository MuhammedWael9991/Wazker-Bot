import os
import aiohttp
from urllib.parse import urlparse
from domain.repository.LocalRepository import LocalRepository


class LocalRepositoryImpl(LocalRepository):
    def __init__(self, cache_dir="cache/audio"):
        self.cache_dir = cache_dir
        os.makedirs(self.cache_dir, exist_ok=True)

    async def cache_azkar_files(self, urls, cache_dir=None):
        cache_dir = cache_dir or self.cache_dir
        os.makedirs(cache_dir, exist_ok=True)

        local_paths = []
        async with aiohttp.ClientSession() as session:
            for url in urls:
                parsed = urlparse(url)
                file_name = os.path.basename(parsed.path)
                local_path = os.path.join(cache_dir, file_name)

                if os.path.exists(local_path):
                    print(f"⚡ Cached: {file_name}")
                    local_paths.append(local_path)
                    continue

                try:
                    async with session.get(url) as response:
                        if response.status == 200:
                            with open(local_path, "wb") as f:
                                f.write(await response.read())
                            print(f"✅ Downloaded: {file_name}")
                            local_paths.append(local_path)
                        else:
                            print(f"❌ Failed to download: {url} (Status {response.status})")
                except Exception as e:
                    print(f"⚠️ Error downloading {url}: {e}")

        return local_paths