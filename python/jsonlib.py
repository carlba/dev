import json

class MyJson:
    def __init__(self, pyobj=None, filename=None):
        self.pyobj = pyobj
        self.filename = filename
    def dumps_to_file(self,pyobj, filename, **kwargs):
        """Dumps python object in json format to a file"""
        if pyobj:
            self.pyobj = pyobj
        if filename:
            self.filename = filename
        if "indent" in kwargs:
            indent = kwargs["indent"]
        else:
            indent = 4       
        
        with open(self.filename,'w+') as f:
            f.write(json.dumps(self.pyobj, indent, **kwargs))
            
    #def loads(self,pystring, **kwargs):
    #    if pystring:
    #        self.pystring = pystring
    #    if self.filename:
    #        with open(self.filename,'w+') as f:
    #            f.write(json.dumps(self.pyobj, indent=4))
    #    else:
    #        return json.dumps(self.pyobj, indent=4)
        
    
if __name__ == '__main__':
    myjson = MyJson()
    testdict= {"namn" : "calle"}
    myjson.dumps_to_file(testdict,"test.json", encoding="ascii", indent=1)