# -*- coding: utf-8 -*-

from win32com.client import constants
from win32com.client.gencache import EnsureDispatch as Dispatch
outlook = Dispatch("Outlook.Application")
mapi = outlook.GetNamespace("MAPI")
print (mapi.GetDefaultFolder(6))
class Oli():
    def __init__(self, outlook_object):
        self._obj = outlook_object
    def items(self):
        array_size = self._obj.Count
        for item_index in range(1,array_size+1):
            print("OK")
            print(item_index, self._obj[item_index])
            yield (item_index, self._obj[item_index])

    def prop(self):
        return sorted( self._obj._prop_map_get_.keys() )


for inx, folder in Oli(mapi.Folders).items():
    # iterate all Outlook folders (top level)
    print (inx,folder.Name)
    print ("|----------|")
    # for inx,subfolder in Oli(folder.Folders).items():
    #     print ("(%i)" % inx, subfolder.Name,"=> ", type(subfolder))