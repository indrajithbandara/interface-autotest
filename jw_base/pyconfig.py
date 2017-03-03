import ConfigParser

class confParse(object):

    def __init__(self,conf_path):
        self.conf_path = conf_path
        self.conf_parser = ConfigParser.ConfigParser()
        self.conf_parser.read(conf_path)

    def get_sections(self):
        return self.conf_parser.sections()

    def get_options(self,section):
        return self.conf_parser.options(section)

    def get_items(self,section):
        return self.conf_parser.items(section)

    def get_val(self,section,option,is_bool = False,is_int = False):
        if is_bool and not is_int:
            #bool类型配置
            val = self.conf_parser.getboolean(section,option)
            return val
        elif not is_bool and is_int:
            val = self.conf_parser.getint(section,option)
            return val

        val = self.conf_parser.get(section,option)
        return val