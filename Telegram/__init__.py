from typing import List
import yaml

commands = {}

def get_command(value: str) -> List:
    return commands["command"][value]
