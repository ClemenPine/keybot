import os
import json
import glob
from os.path import basename
from jellyfish import damerau_levenshtein_distance as lev

from util import kb
from util.consts import LAYOUT_DIR

def find(target: str, n=1, *, subdir='', fuzzy=False):
    target = target.lower()
    path = f'{LAYOUT_DIR}/{subdir}/**/*.json'

    layouts = {basename(x)[:-5]: x for x in glob.glob(path, recursive=True)}
    names = sorted(layouts.keys(), key=lambda x: len(x))

    if fuzzy:
        results = sorted(names, key=lambda x: lev(x, target))[:n]
    else:
        results = [x for x in names if target in x][:n]

    return [layouts[x] for x in results]


def exists(target: str, subdir=''):
    file = find(target, subdir=subdir, fuzzy=True)[0]
    ll = kb.Layout(file)

    return ll.name.lower() == target.lower()


def move(old_file: str, new_file: str):
    os.rename(old_file, new_file)


def remove(file: str):
    os.remove(file)


def write(file: str, ll: kb.Layout):
    with open(file, 'w') as f:
        json.dump(ll.__dict__, f, indent=4)