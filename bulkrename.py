import os, re

def bulkrename(argv):
    if(len(argv) < 4):
        print("usage: vfu rename <target> <pattern>")
        print("pattern syntax:\nF@ to indicate existing filename including extension,\nX@ for existing filename, excluding extension,\nE@ for extension")
        print("example: vfu rename myfile.py F@.backup ====> myfile.py.backup")
        print("example: vfu rename * X@-revisedE@ ====> myfile-revised.py, myfile-revised.sh")
        return

    target = argv[2]
    pattern = argv[3]

    if(target == "*"): #change this to if target contains *
        #get directory somehow
        os.getcwd()
        #loop entire 
        return

    if(not valid_filename(target)):
        print("Not a valid filename. Please try again.")
        return

    new_filename = parse(target, pattern)
    filemove(target, new_filename)

def filemove(oldname, newname):
    directory = os.getcwd() + "/"
    oldpath = directory + oldname
    newpath = directory + newname
    os.rename(oldpath, newpath)
    return

def parse(filename, pattern):
    filename_full = filename
    filename_exclude = filename.split('.', 1)[0]
    extension = "." + filename.split('.', 1)[1]


    pattern = pattern.replace('F@',filename)
    pattern = pattern.replace('X@',filename_exclude)
    pattern = pattern.replace('E@',extension)
    print(pattern)

    return pattern

def valid_filename(filename):
    filepath = os.getcwd() + "/" + filename
    if(os.path.isfile(filepath)):
        return True

    return False

