from util import kb, memory
from util.session import Session
from util.consts import LAYOUT_DIR

def exec(id: int, layout_name: str, *args):
    if memory.exists(layout_name):
        return f'Error: `{layout_name}` is already taken'

    session = Session(id)

    ll = kb.Layout(session.file)
    ll.name = layout_name

    file = f'{LAYOUT_DIR}/{session.name}/{layout_name.lower()}.json'
    memory.write(file, ll)

    return 'Success!'