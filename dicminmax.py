def keywithmaxval(d):
    """ a) create a list of the dict's keys and values;
    b) return the key with the max value"""
    
    v = list(d.values())
    k = list(d.keys())
    max_v = max(v)
    min_v = min(v)
    print(v)
    print(k)
    #print(k[v.index(max(v))]) 
    #print(max(d, key = lambda k : d.get(k)))
    #print(type(v))
    max_k = []
    min_k = []
    for item in d:
        if max_v == d[item]:
            max_k.append(item)
        elif min_v == d[item]:
            min_k.append(item)
    print(max_k)
    print(min_k)
    return


#test
d={'a': 1, 'b': 2, 'c': 0, 'd': 2, 'e':0}
keywithmaxval(d)
