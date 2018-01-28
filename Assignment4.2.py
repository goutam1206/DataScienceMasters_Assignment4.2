def mymap(lst):
    retlst = []
    for word in lst:
        retlst.append(len(word))
    return retlst

mymap(["Hello","I","am","Goutama","Sarma","and","I","am","printing","longest","word"])
    

def isVowel(s):
    if s.upper() in ['A','E','I','O','U']:
        return True
    else:
        return False

print (isVowel('X'))
print (isVowel('a'))
print (isVowel('E'))