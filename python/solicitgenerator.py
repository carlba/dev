import gspread
import urllib
import itertools
import json
import hashlib
from jsonlib import MyJson
from getpass import getpass
from convertlog import HTTPGetToObj

from collections import OrderedDict as odict

url = "https://khan.d.birdstep.internal"
prefix = "/?"



def main():
    
    worksheet = init_worksheet("carl.backstrom@birdstep.com")
    sheetdict = convert_sheet_to_json(worksheet)
    
    dump_to_pretty_json_file(sheetdict, "testcases.json")

def init_worksheet(username,password=None,sheet=None):
    if not password:       
        for i in range(1,5):
            password = getpass("Password: ")
            if verify_password(password,["96b9be268fc69f0491a25eee3cca7cbe","3a0a51e24157f6bbe026f94f72cd7510"]):
                break
            else:
                pass
    if not sheet:
        sheet = "SprintEmsUpgrade"
        
    googlespreadsheet = gspread.login('genzorg@gmail.com', password)
    worksheet = googlespreadsheet.open("Solicits").worksheet(sheet)
    return worksheet
    

def verify_password(password, hashed_password):
    if hashlib.md5( password ).hexdigest() in hashed_password:
        return True

def convert_sheet_to_json(worksheet):
    headers = worksheet.row_values(1)
    all_rows = worksheet.get_all_values()
    headers = all_rows[0]
    data = all_rows[1:]
    tcdict = odict()
    
    
    for row in data:
        if row[0] == "":
            continue
        if "TC:" in row[0]:
            tcname = row[0][3:].strip()
            tcdict[tcname] = []
            currentdict = tcname
            continue
        if row[0][0:4] == "http":
            print row
            tcdict[currentdict].append(HTTPGetToObj(row[0]))
            continue
        
        if "xpi" in row[0]:
            continue
        
        if "end" in row[0]:
            break
        tcdict[currentdict].append(odict(itertools.izip(headers, row)))
    return tcdict
    #url = url + prefix + urllib.urlencode(urldict)

def dump_to_pretty_json_file(adict,filename, path=None):
    myjson = MyJson()
    myjson.dumps_to_file(adict,"test.json", encoding="ascii", indent=4)

if __name__ == '__main__':
    main()