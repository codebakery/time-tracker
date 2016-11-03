import os
import importlib

from .base import *  # noqa

setting = os.environ.get('PROJECT_SETTING')
if setting:
    env_settings = importlib.import_module('time_tracker.settings.' + setting)
    globals().update(env_settings.__dict__)
else:
    try:
        from .local import *  # noqa
    except ImportError as exc:
        message = '{} (Did you forget to create symlink to local.py?)'
        exc.args = (message.format(exc.args[0]), )
        exc.msg = message.format(exc.msg)
        raise exc
