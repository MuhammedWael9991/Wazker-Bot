from abc import ABC, abstractmethod

class LocalRepository(ABC):

    @abstractmethod
    def cache_azkar_files(self, urls, cache_dir):
        pass