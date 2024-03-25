import json

class Config:
    def __init__(self, config_path='config.json'):
        self.config_path = config_path
        self.config = self.load_config()

    def load_config(self):
        """Loads the configuration from a JSON file."""
        try:
            with open(self.config_path, 'r') as config_file:
                return json.load(config_file)
        except FileNotFoundError:
            raise Exception(f"Configuration file {self.config_path} not found.")
        except json.JSONDecodeError:
            raise Exception(f"Error decoding the configuration file {self.config_path}.")

    def get(self, key, default=None):
        """Retrieves a configuration value with a specified key."""
        return self.config.get(key, default)

# Usage example:
if __name__ == "__main__":
    config = Config()
    print("Model Name:", config.get('model_name'))
    print("Database Host:", config.get('database').get('host'))
    # For nested dictionaries, ensure to handle the possibility of None values appropriately.
