""" soteriareitti/utils/file_reader.py """

import os
from pathlib import Path

base_dir = Path(__file__).parents[2]
data_dir = os.path.join(base_dir, "data")
resources_dir = os.path.join(base_dir, "resources")

if not os.path.exists(data_dir):
    os.makedirs(data_dir)


def get_data(file: str) -> str:
    return os.path.join(data_dir, file)


def get_base(file: str) -> str:
    return os.path.join(base_dir, file)


def get_resources(file: str) -> str:
    return os.path.join(resources_dir, file)
