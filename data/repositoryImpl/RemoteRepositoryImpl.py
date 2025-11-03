import os
from domain.repository.RemoteRepository import RemoteRepository


class RemoteRepositoryImpl(RemoteRepository):
    def __init__(self, client):
        self.client = client

    def get_azkar_urls(self):
        try:
            table_name = os.getenv("AZKAR_URL_TABLE")
            if not table_name:
                raise ValueError("AZKAR_URL_TABLE environment variable not set.")

            response = self.client.table(table_name).select("url").execute()
            print(f"Raw Supabase response: {response.data}")
            if not response.data:
                print("No URLs found in table.")
                return []

            urls = [row["url"] for row in response.data]
            return urls
        except Exception as e:
            print(f"Error fetching azkar URLs: {e}")
            return []