import json, urllib.request

def tester(sort_type:str):

    f = [{'year':'2000', 'size':'4', 'landed':'down'},{'year':'1600', 'size':'200', 'landed':'down'}]

    for dicts in f:
        for keys in dicts:

            try:
                dicts[keys] = int(dicts[keys])
            except:
                dicts[keys] = str(dicts[keys])

    print(sorted(f, key = lambda x:x[sort_type]))

def websearch():

    global x
    
    x = json.load(urllib.request.urlopen('https://data.nasa.gov/resource/y77d-th95.json'))

    for dicts in x:
        for keys in dicts:
            print(keys)

def puller(sort:str):

    for dicts in x:
        for keys in dicts:
            try:
                dicts[keys] = int(float(dicts[keys]))
            except:
                dicts[keys] = str(dicts[keys])

    z = sorted(x, key = lambda x:x[sort])

    for out in range(10):
        print(z[out])
    