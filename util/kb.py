import json
from dataclasses import dataclass

@dataclass
class Layout:
    name: str
    board: str
    source: str
    authors: list[str]
    layers: dict[str, list[str]]

    def __init__(self, file: str):
        with open(file, 'r') as f:
            data = json.load(f)

        self.__dict__ = data

    def swap(self, pair: str):
        for name, layer in self.layers.items():
            ll = '\n'.join(layer)
            self.layers[name] = (ll
                .replace(pair[1], '`')
                .replace(pair[0], pair[1])
                .replace('`', pair[0])
            ).split('\n')

    def colswap(self, pair: str):
        A = []
        B = []

        for layer in self.layers.values():
            A += [x for x in zip(*layer) if pair[0] in x][0]
            B += [x for x in zip(*layer) if pair[1] in x][0]

        for pair in [''.join(x) for x in zip(A, B)]:
            self.swap(pair)

    def __str__(self):
        rows = self.layers['main']
        rows = [f'  {x[:9]} {x[9:]}' for x in rows]

        match self.board:
            case 'stagger':
                rows[1] = ' ' + rows[1]
                rows[2] = '  ' + rows[2]
            case 'angle':
                rows[2] = ' ' + rows[2]

        return f'{self.name}\n' + '\n'.join(rows)