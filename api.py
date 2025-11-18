def fsWrite(fileName: str,fileCont: str,uid=0):
    import fs
    names = fs.names
    cont = fs.cont
    perm = fs.perm
    if not fileName in names:
        names.append(fileName)
        cont.append(fileCont)
        perm.append(uid)
    else:
        cont[names.index(fileName)] = fileCont
    f = open("fs.py","w")
    f.write("names = " + str(names) + "\ncont = " + str(cont) + "\nperm = " + str(perm) + "\n")
    f.close()
    del fs

def fsRemove(fileName: str,uid: int):
    import fs
    names = fs.names
    cont = fs.cont
    perm = fs.perm

    if fileName in names and uid >= perm[names.index(fileName)]:
        cont.pop(names.index(fileName))
        perm.pop(names.index(fileName))
        names.pop(names.index(fileName))
        f = open("fs.py","w")
        f.write("names = " + str(names) + "\ncont = " + str(cont) + "\nperm = " + str(perm) + "\n")
        f.close()

    del fs

def fsRead(fileName: str):
    import fs
    rType = ""
    if fileName in fs.names:
        rType = fs.cont[fs.names.index(fileName)]
    else:
        rType = "0: No such file"
    del fs
    return rType

def fsExists(fileName: str):
    import fs
    rType = False
    if fileName in fs.names:
        rType = True
    else:
        rType = False
    del fs
    return rType

def fsList():
    import fs
    rType = fs.names
    del fs
    return rType

def fsRename(oldName, newName):
    import fs
    names = fs.names
    cont = fs.cont

    if oldName in names and not newName in names:
        names[names.index(oldName)] = newName
        f = open("fs.py","w")
        f.write("names = " + str(names) + "\ncont = " + str(cont) + "\nperm = " + str(perm) + "\n")
        f.close()
    del fs

def fsCopy(fileName):
    import fs
    names = fs.names
    cont = fs.cont
    perm = fs.perm
    tempName = fileName + ".copy"
    while tempName in names:
        tempName += ".copy"
    if fileName in names:
        names.append(tempName)
        cont.append(cont[names.index(fileName)])
        perm.append(perm[names.index(fileName)])
    f = open("fs.py","w")
    f.write("names = " + str(names) + "\ncont = " + str(cont) + "\nperm = " + str(perm) + "\n")
    f.close()
    del fs

def fsAbout(fileName):
    import fs
    if fileName in fs.names:
        rType = (fs.names.index(fileName),len(fs.cont[fs.names.index(fileName)]),fs.perm[fs.names.index(fileName)])
    else:
        rType = (-1,-1,-1)
    del fs
    return rType

def fsRemovable(fileName: str,uid: int):
    import fs
    rType = False
    if fileName in fs.names and uid >= fs.perm[fs.names.index(fileName)]:
        rType = True
    del fs
    return rType

def enEncrypt(string: str):
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0","!","@","#","$","%","^","&","*","(",")","_","-","=","+","[","]","{","}","\\","|",";",":","'",'"',",","<",".",">","/","?","~","`"," "]
    lStr = string.lower()
    eStr = ""
    for i in lStr:
        eStr += str(alphabet.index(i)) + " "
    eStr = eStr[0:-1]
    return eStr

def enDecrypt(string: str):
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0","!","@","#","$","%","^","&","*","(",")","_","-","=","+","[","]","{","}","\\","|",";",":","'",'"',",","<",".",">","/","?","~","`"," "]
    sString = string.split()
    dString = ""
    for i in sString:
        dString += alphabet[int(i)]
    return dString
