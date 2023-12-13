# role.py

class Role:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    # Function to return colored text
    def colored_text(self, text):
        return f'\033[{self.color}m{text}\033[0m'

