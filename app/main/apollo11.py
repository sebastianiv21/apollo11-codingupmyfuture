from app.models.config_model import ConfigModel


class Apollo11:
    def __init__(self, config: ConfigModel):
        self.config = config

    def run(self):
        print("hola mundo")
