import glob
from os.path import basename

LAYOUT_DIR = '../KART'

SERVER_COMMANDS = ['layout']
DM_COMMANDS = [basename(x)[:-3] for x in glob.glob('cmds/*.py')]