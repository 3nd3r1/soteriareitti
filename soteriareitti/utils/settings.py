""" soteriareitti/settings.py """


class Settings:
    app_place = "Helsinki"

    # Cache
    caching = True
    cache_version = "3"  # Change this when cache is deprecated

    # OSM
    max_size = None
    timeout = 30
