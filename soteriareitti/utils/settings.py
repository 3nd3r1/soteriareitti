# soteriareitti/settings.py

import logging

logging.basicConfig(format='%(asctime)s,%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d:%H:%M:%S',
                    level=logging.DEBUG)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class Settings:
    osm_file = "data/finland-latest.osm.pbf"
    max_size = None
    timeout = 30
