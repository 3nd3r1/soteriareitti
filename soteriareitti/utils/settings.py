""" soteriareitti/settings.py """
import os
from dotenv import load_dotenv
from soteriareitti.utils.file_reader import get_base

try:
    load_dotenv(dotenv_path=get_base(".env"))
    load_dotenv(dotenv_path=get_base(".env.local"))
except FileNotFoundError:
    pass


class Settings:
    app_place = os.getenv("APP_PLACE", "Töölö")

    # Cache
    caching = os.getenv("CACHING", "True") == "True"
    cache_version = "6"  # Change this when cache is deprecated

    # OSM
    max_size = None
    timeout = 30
