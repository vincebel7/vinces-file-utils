import re, sys, os

def longest(l):
    longestlist = max(len(elem) for elem in l)
    print("longest list: " + longestlist)
    return l[longestlist]

def diff(argv):
    if(len(argv) < 4):
        print("usage: vfu diff item1 item2")
        return

    item1 = argv[2]
    item2 = argv[3]
    if(os.path.isdir(item1) and os.path.isdir(item2)):
        print("Comparing directories...")
        diffdir(item1, item2)

    elif(os.path.isfile(item1) and os.path.isfile(item2)):
        print("Comparing files...")

    else:
        print("Error: Items must both be files, or both be directories")

def diffdir(dir1, dir2): # recursive
    dir1_list = os.listdir(dir1)
    dir2_list = os.listdir(dir2)
    dir1_list.sort()
    dir2_list.sort()

    if((not dir1_list) and (not dir2_list)):
        return

    for i in dir1_list:
        #print("TESTING WITH I: " + str(i))
        if((not isdir(i, dir1)) and (not isfile(i, dir2))):
            print("(vfu) Only in " + dir1 + ": " + i)
        
        if((isdir(i, dir1)) and (not isdir(i, dir2))):
            print("(vfu) Only in " + dir1 + ": " + i)
            
        if(isdir(i, dir1) and isdir(i, dir2)):
            diffdir((str(dir1) + "/" + str(i)), (str(dir2) + "/" + str(i)))
            dir2_list.remove(i)

        if(isfile(i, dir1) and isfile(i, dir2)):
            dir2_list.remove(i)

    for j in dir2_list:
        #print("TESTING WITH J: " + str(j))
        if((not isdir(j, dir2)) and (not isfile(j, dir1))):
            print("(vfu) Only in " + dir2 + ": " + j)

        if((isdir(j, dir2)) and (not isdir(j, dir1))):
            print("(vfu) Only in " + dir2 + ": " + j)
        
def difffile():
    return

def isdir(d, parent):
    path = str(parent) + "/" + str(d)
    return os.path.isdir(path)

def isfile(f, d):
    path = str(d) + "/" + str(f)
    return os.path.isfile(path)
