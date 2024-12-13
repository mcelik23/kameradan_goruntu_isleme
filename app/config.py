import toml
from dataclasses import dataclass
import numpy as np


@dataclass
class ColorRange:
    lower: np.ndarray
    upper: np.ndarray


@dataclass
class Config:
    red: ColorRange
    yellow: ColorRange
    green: ColorRange


def load_config(file_path: str) -> Config:
    config_data = toml.load(file_path)
    colors = config_data['colors']

    return Config(
        red=ColorRange(np.array(colors['red_lower']), np.array(colors['red_upper'])),
        yellow=ColorRange(np.array(colors['yellow_lower']), np.array(colors['yellow_upper'])),
        green=ColorRange(np.array(colors['green_lower']), np.array(colors['green_upper']))
    )
