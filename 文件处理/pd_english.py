import re


#def delete(listA):
    # return list(set(listA))
 #   return sorted(set(listA), key=listA.index)
def pd(list):
    name = []
    numb = []
    for i in list:
        if bool(re.search('[a-z]', i)) == True:
            name.append(i)
        if bool(re.search('[0-300]', i)) == True:
            numb.append(i)
            
    return name,numb
    