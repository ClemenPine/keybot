import os
import json
from dataclasses import dataclass

@dataclass
class Session:
    id: int

    name: str
    file: str
    corpus: str

    def __init__(self, id: int):
        file = f'sessions/{id}.json'

        # default values
        self.file = ''
        self.corpus = 'monkeyracer'

        if os.path.exists(file):
            with open(file, 'r') as f:
                data = json.load(f)

            self.__dict__ |= data
            
        self.id = id

    def update(self):
        file = f'sessions/{self.id}.json'

        del self.__dict__['id']

        with open(file, 'w') as f:
            json.dump(self.__dict__, f, indent=4)