from abc import ABC, abstractmethod

class Usecase[F, T](ABC):
    """Usecase interface"""

    @abstractmethod
    def execute(self, filter: F) -> T:
        """To be implemented"""
        pass

class AsyncUsecase[F, T](ABC):
    """Usecase interface"""

    @abstractmethod
    async def execute(self, filter: F) -> T:
        """To be implemented"""
        pass
