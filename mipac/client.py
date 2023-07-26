from typing import Self

from mipac.config import Config, IMisskeyVersions, config
from mipac.http import HTTPClient
from mipac.manager.client import ClientManager
from mipac.utils.log import LOGING_LEVEL_TYPE, setup_logging


class Client:
    def __init__(
        self,
        url: str,
        token: str | None = None,
        *,
        log_level: LOGING_LEVEL_TYPE | None = 'INFO',
        use_version: IMisskeyVersions = 12,
        use_version_autodetect: bool = True
    ) -> None:
        if log_level is not None:
            setup_logging(level=log_level)
        config.from_dict(use_version=use_version, use_version_autodetect=use_version_autodetect)
        self.config: Config = config
        self.http: HTTPClient = HTTPClient(url, token)

    async def __aenter__(self) -> Self:
        await self.http.login()
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        await self.close_session()

    @property
    def api(self) -> ClientManager:
        return ClientManager(self.http, self.config)

    async def close_session(self) -> None:
        await self.http.close_session()
