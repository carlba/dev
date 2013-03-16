def splitLog(logline):
    splitlog = logline.split("|")   
    
    logtypes = ["time","loglevel","logclass","thread","threadid","function","logdata"]    
    
    logDict ={}
    
    
    
    
    for i in range(len(logtypes)):       
        logDict[logtypes[i]] = splitlog[i].strip()                    
    return logDict
    
        
def HTTPGetToObj(logobj):    
    # for key in logobj:
    #    print file[file.rindex('.')+1:](key,logobj[key]+2)
        # pass
    try:
        logdata = logobj["logdata"]
    except TypeError:
        logdata = logobj        
    
    url = logdata[logdata.rindex('/?')+1:]
    url = url.replace('?','&')
    urlList = url.split("&")
    
    parameters =  {}    
    
    for item in urlList:
        if item:            
            splititem = item.split("=")
            parameters[splititem[0]] =  splititem[1]
    return parameters
    
    
    #print urlObj
    
    
    
    #print file[file.rindex('.')file.rindex('.')+1:]
    
    
 





if __name__ == '__main__':


    logline = "12:28:33_594 | L32 | C08 | BHS CH       | 0x00001528 | ActivationHandler::PerformActivation | Send activation message = https://eagle.becmgr.com/?cid=998001&pid=BEC&imsi=240016008918970&imei=358133031912246&mac=F4:CE:46:97:C7:22&guid=6075838E-5F71-4F15-B3EC-D6A7FCFA079A"    
    
    log = convert(logline)
    parameters = getToObj(log)
    print parameters 
    
    

