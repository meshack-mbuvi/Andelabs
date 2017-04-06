
def find_missing_num(a,b):
    
    if len(a) == len (b): #if the two lists are of the same size,none has extra number
        return 0
    
    if len(a) > len(b):# if list a has the extra number
        for item in a: 
            if item in b:
                continue
            else:
                return item
    else: # if list b has the extra number
        for item in b:
            if item in a:
                continue
            return item 