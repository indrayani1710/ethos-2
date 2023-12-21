import os
from dotenv import load_dotenv


class EnvConfig:
    def __init__(self, dotenv_path=".env"):
        self.dotenv_path = dotenv_path
        self.load_env_variables()

    def load_env_variables(self):
        if os.path.exists(self.dotenv_path):
            load_dotenv(self.dotenv_path)
            print(f"Environment variables loaded from {self.dotenv_path}")
        else:
            print(
                f"{self.dotenv_path} not found. Make sure to create the file with your configuration.")

    def set_env_variable(self, name, value):
        os.environp[name] = value

    @property
    def db_name(self):
        return os.getenv("DB_NAME")

    @property
    def db_name(self):
        return os.getenv("PORT")

    @property
    def db_name(self):
        return os.getenv("BAUD_RATE")

    @property
    def db_name(self):
        return os.getenv("INTERVAL")
