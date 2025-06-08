
### Class used to communicate with other classes in Observer Pattern
class EventBus:
    _subscribers = {}

    @classmethod
    def subscribe(cls, event_name, callback):
        cls._subscribers.setdefault(event_name, []).append(callback)

    @classmethod
    def emit(cls, event_name, *args, **kwargs):
        for callback in cls._subscribers.get(event_name, []):
            callback(*args, **kwargs)