class TestableSettings:

    def __init__(self, settings: tuple[tuple[str, None]]) -> None:
        self._settings = dict((name, value) for name, value in settings)

    def get(self, name):
        return self._settings[name]
    
    def get_or(self, name, default):
        return self._settings[name] if self._settings[name] != None else default
    
    def get_all(self):
        return tuple(setting for setting in self._settings.values())