import json, urllib.request

def tester(sort_type:str):
    '''A script for testing code used in other parts of the module'''

    f = [{'year':'2000', 'size':'4', 'landed':'down'},{'year':'1600', 'size':'200', 'landed':'down'}]

    for dicts in f:
        for keys in dicts:

            try:
                dicts[keys] = int(dicts[keys])
            except:
                dicts[keys] = str(dicts[keys])

    print(sorted(f, key = lambda x:x[sort_type]))

def websearch(search_address:str):
    '''This funtion is for pulling a valid url and converting from .json to a list, as well as printing keys in the dictionaries'''

    global x
    
    x = json.load(urllib.request.urlopen(search_address))

    for keys in x[0]:
            
            #prints all valid keys
            
            print(keys)


def puller(sorter:str):
    '''This function is for sorting the list with keywords obtained from "websearch()"'''

    for dicts in x:
        for keys in dicts:
            
            #converts values from str to int where possible
            
            try:
                dicts[keys] = int(float(dicts[keys]))
            except:
                dicts[keys] = str(dicts[keys])

    #sorting by kywrd

    z = sorted(x, key = lambda x:x[sorter])

    #outputs only the first ten entries to avoid terminal overflow
    
    for out in range(10):
        print(z[out])
    