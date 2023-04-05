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
	print("Reader program was damaged, please get a new one.")
