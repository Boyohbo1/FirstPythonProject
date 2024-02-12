def tester(sort_type):

    y = [{'year':2000, 'size':4, 'landed':'down'},{'year':1600, 'size':200, 'landed':'down'}]
    
    if sort_type == 'year':
        print(sorted(y, key = lambda x:x['year']))
    elif sort_type == 'size':
        print(sorted(y, key = lambda x:x['size']))
    elif sort_type == 'landed':
        print(sorted(y, key = lambda x:x['landed']))
    else:
        print('Valid sort options are: year, size, landed.')



def puller():
    

    
    print()