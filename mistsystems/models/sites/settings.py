import json
from mistsystems.models.sites.rogue import Rogue


class Settings:

    def __init__(self):
        self.rogue = Rogue()

        
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)