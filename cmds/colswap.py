from util import kb, memory
from util.session import Session

def exec(id: int, letter_pair: str, *args):
    session = Session(id)

    temp_file = f'.layouts/{session.name}.json'
    
    ll = kb.Layout(session.file)
    
    ll.authors = []
    ll.source = ''
    ll.colswap(letter_pair)

    memory.write(temp_file, ll)

    session.file = temp_file
    session.update()
    
    ll.name += ' (edited)'
    return '```\n' + str(ll) + '\n```'