from threading import Lock

_instances = {}
_lock: Lock = Lock()


def _has_method(cls, method):
    """Check if the class has the given method."""
    return any(method in ancestor.__dict__ for ancestor in cls.__mro__[:-1])


def _has_new(cls):
    """Check if the class has __new__ implemented."""
    return _has_method(cls, '__new__')


def _has_init(cls):
    """Check if the class has __init__ implemented."""
    return _has_method(cls, '__init__')


def singleton(scope: str = 'Global'):
    """Class decorator to indicate singleton implementation."""
    with _lock:
        _instances.setdefault(scope, {})

    def singleton_wrapper(real_class):
        """Wraps the class to be a scoped singleton."""

        def get_instance(*args, **kwargs):
            with _lock:
                _instances[scope].setdefault(
                    real_class,
                    real_class(*args, **kwargs))
                return _instances[scope][real_class]

        return get_instance

    return singleton_wrapper
