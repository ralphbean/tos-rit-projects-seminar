
import os
from yaml import load
try:
    # Do this if libYAML is installed.  Its fast.
    from yaml import CLoader as Loader
except ImportError:
    # This is written in pure python.  Not as fast.
    from yaml import Loader

def load_students(fname=None):
    if not fname:
        # If nobody specified, guess at where the student db is stored.
        fname = os.path.sep.join(
            __file__.split(os.path.sep)[:-4] + ['data', 'students.yaml']
        )

    f = open(fname, 'r')
    data = load(f, Loader=Loader)
    f.close()

    return data
