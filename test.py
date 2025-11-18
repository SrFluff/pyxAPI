print("PyXAPI tester v1.0.0\n")

import time
import api
import os

fs_exists = os.path.exists("fs.py")

if fs_exists:
    os.remove("fs.py")

api.fsInit()

api.fsWrite("test","test file",0)
import fs

print("Filesystem tests\n")

if fs.names[0] == "test":
    print("1.  OK")
else:
    print("1.  NO")

if fs.cont[0] == "test file":
    print("2.  OK")
else:
    print("2.  NO")

if fs.perm[0] == 0:
    print("3.  OK")
else:
    print("3.  NO")

if api.fsRead("test") == "test file":
    print("4.  OK")
else:
    print("4.  NO")

del fs

if api.fsAbout("test") == (0,9,0):
    print("5.  OK")
else:
    print("5.  NO")

if api.fsRemovable("test",0):
    print("6.  OK")
else:
    print("6.  NO")

if api.fsExists("test"):
    print("7.  OK")
else:
    print("7.  OK")

if api.fsList() == ["test"]:
    print("8.  OK")
else:
    print("8.  NO")

api.fsCopy("test")
import fs
if fs.names[1] == "test.copy":
    print("9.  OK")
else:
    print("9.  NO")

del fs

api.fsRename("test.copy","copy_of_test")
import fs
if fs.names[1] == "copy_of_test":
    print("10. OK")
else:
    print("10. NO")

del fs

api.fsRemove("copy_of_test",0)

import fs

if len(fs.names) == 1 and len(fs.cont) == 1 and len(fs.perm) == 1:
    print("11. OK")
else:
    print("11. NO")

del fs

api.fsRemove("test",0)

import fs

if len(fs.names) == 0 and len(fs.cont) == 0 and len(fs.perm) == 0:
    print("12. OK")
else:
    print("12. NO")

del fs

api.fsWrite("test","chown test file",1)
api.fsChown("test",0)
if api.fsAbout("test")[2] == 0:
    print("13. OK")
else:
    print("13. NO")

os.remove("fs.py")

print("\nEncryption tests\n")

if api.enEncrypt("AAABBBDDD") == "0 0 0 1 1 1 3 3 3":
    print("1. OK")
else:
    print("2. NO")

if api.enDecrypt("0 0 0 1 1 1 3 3 3") == "aaabbbddd":
    print("2. OK")
else:
    print("2. NO")
