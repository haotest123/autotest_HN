
import json
import os
import yaml

def read_yaml(filename):
    with open(filename,'r',encoding='utf-8')as f:
        return yaml.load(f,Loader=yaml.FullLoader)



def write_sellerId(file,vendor_id):
    with open(file,'a+',encoding='utf-8')as f:
        f.seek(0)
        if f.read()=='':
            datadict={}
        else:
            f.seek(0)
            datadict=json.load(f)
        datadict={"vendor_id":vendor_id}
        f.seek(0)
        f.truncate()
        json.dump(datadict,f,indent=2,ensure_ascii=False)























