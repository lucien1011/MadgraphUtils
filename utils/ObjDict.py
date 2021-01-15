import sys

def read_from_file_python3(input_path):
    import importlib
    spec = importlib.util.spec_from_file_location("cfg",input_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    cfg = mod.cfg
    return cfg

def read_from_file_python2(input_path):
    import imp
    f = open(input_path,'r')
    cfg = imp.load_source('cfg',input_path,f)
    return cfg

class ObjDict(dict):
    def __getattr__(self, name):
        if name in self:
            return self[name]
        else:
            raise AttributeError("No such attribute: " + name)

    def __setattr__(self, name, value):
        self[name] = value

    def __delattr__(self, name):
        if name in self:
            del self[name]
        else:
            raise AttributeError("No such attribute: " + name)
