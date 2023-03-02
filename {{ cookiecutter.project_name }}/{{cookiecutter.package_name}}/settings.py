# -*- coding: utf-8 -*-
# (c) Nelen & Schuurmans

from pydantic import AnyUrl
from pydantic_settings_yaml import YamlBaseSettings

class Settings(YamlBaseSettings):
    environment: str
    debug: bool = False
    database_url: AnyUrl

settings = Settings()
