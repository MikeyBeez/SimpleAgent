
import json

class Role:
    def __init__(self, name):
        self.name = name
        self.color = self.get_color()

    def get_color(self):
        with open('roles_config.json', 'r') as f:
            config = json.load(f)
        return config.get(self.name, {}).get('color', '0')  # Default to no color if the role name or color is not found

    # Function to return colored text
    def colored_text(self, text):
        return f'\033[{self.color}m{text}\033[0m'

