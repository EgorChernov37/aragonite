try:
    import configparser
    class AttrDict(dict):
        def __init__(self, *args, **kwargs):
            super(AttrDict, self).__init__(*args, **kwargs)
            self.__dict__ = self
    config = configparser.ConfigParser(dict_type=AttrDict)
    config.read('VERSION.ini')
    ver = config._sections.general.ver
except Exception:
    print("[ERROR] Reader program damaged. Please update it in 'https://github.com/EgorChernov37/proplus6'!")
