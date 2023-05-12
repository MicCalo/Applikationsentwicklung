# coding: utf8

class InformationBlock:
    def __init__(self, title:str, infos:dict):
        self._title = title
        self._infos = infos

    @property
    def title(self):
        return self._title
    
    @property
    def keys(self):
        return self._infos.keys()
    
    def get_info(self, key:str):
        return self._infos[key]