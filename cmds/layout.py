from util import kb, memory
from util.session import Session

def exec(id: int, layout_name: str=None, *args):
    session = Session(id)
    
    if layout_name:
        file = memory.find(layout_name, fuzzy=True)[0]
    else:
        file = session.file

    ll = kb.Layout(file)

    session.file = file
    session.update()

    return '```\n' + str(ll) + '\n```'