import inspect
import io
import os


__all__ = ['__version__']


# A simple `from autoslugged import __version__` would trigger a cascading import
# of `autoslugged.fields`, then `django`.  As the latter may not be available
# (being a dependency), we try to work around it.
#
# Cases:
# 1) building the package with a global interpreter and no dependencies
#    installed globally;
# 2) building documentation e.g. on RTFD server (no Django settings available
#    on runtime);
# 3) installing django-autoslugged before Django itself (highly unlikely).
#
__version__ = None
thisfile = inspect.getfile(inspect.currentframe())
path = os.path.join(os.path.abspath(os.path.dirname(thisfile)), 'autoslugged/__init__.py')
with io.open(path, encoding='utf8') as f:
    for line in f:
        if line.startswith('__version__'):
            exec(line)
            break
assert __version__, 'autoslugged.__version__ must be imported correctly'
