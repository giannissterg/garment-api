from logging import Logger
from typing import Callable 

from usecases.usecase import Usecase


class LoggerUsecase[F, T](Usecase[F, T]):
  def __init__(self, inner_usecase: Usecase[F, T], logger: Logger, logCallback: Callable[[T], str]) -> None:
    self.inner_usecase = inner_usecase
    self.logger = logger
    self.logCallback = logCallback

  async def execute(self, filter: F) -> T:
    result = await self.inner_usecase.execute(filter)
    self.logger.info(self.logCallback(result))
    return result