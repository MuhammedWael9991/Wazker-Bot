from abc import ABC, abstractmethod

class RemoteRepository(ABC):
    @abstractmethod
    def get_azkar_urls(self):
        pass