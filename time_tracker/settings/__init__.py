from .base import *  # noqa
try:
    from .local import *  # noqa
except ImportError as exc:
    message = '{} (Did you forget to create symlink to local.py?)'
    exc.args = (message.format(exc.args[0]), )
    exc.msg = message.format(exc.msg)
    raise exc
