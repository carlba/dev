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

    def loads_from_file(self,filename, **kwargs):
        if filename:
            self.filename = filename

        try:
            with open(filename,'r') as jsonfile:
                return json.loads(jsonfile.read())
        except IOError as e:
            print repr(e)

if __name__ == '__main__':
    myjson = MyJson()
    testdict= {"namn" : "calle"}
    myjson.dumps_to_file(testdict,"test.json", encoding="ascii", indent=1)
    print myjson.loads_from_file("test.json")
    print myjson.loads_from_file("bog.json")