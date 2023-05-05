from util import kb, memory
from util.session import Session

def exec(id: int, layout_name: str, *args):
    session = Session(id)

    if not memory.exists(layout_name, subdir=session.name):
        return f'Error: Layout `{layout_name}` not found in your list'

    file = memory.find(layout_name, subdir=session.name)[0]
    memory.remove(file)

    return f'Removed `{layout_name}`'