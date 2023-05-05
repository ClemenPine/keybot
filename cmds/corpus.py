from util.session import Session

def exec(id: int, corpus_name: str=None, *args):
    session = Session(id)
    
    if not corpus_name:
        return f'`{session.corpus}` is your selected corpus'

    session.corpus = corpus_name
    session.update()