# PyX universal API
The universal API, made for (not ready yet) PyX
# Functions
Filesystem functions\
`fsInit() - Creates the fs.py file, needed to write to the system`
`fsWrite(fileName,fileCont,uid) - Writes a file to the system`\
`fsRemove(fileName,uid) - Removes a file if the uid is greater or equal`\
`fsRead(fileName) - Reads a file's contents`\
`fsExists(fileName) - Returns if a file exists`\
`fsList() - Returns all the filenames in the system`\
`fsRename(oldName,newName) - Renames a file`\
`fsCopy(fileName) - Makes a copy of a file`\
`fsAbout(fileName) - Returns the: index, content length, and uid. All in a tuple`\
`fsRemovable(fileName,uid) - Returns whether a uid can remove a file`\
\
Encryption functions\
`enEncrypt(string) - Returns an encrypted string`\
`enDecrypt(string) - Returns a decrypted string`
# Prerequisites
Keep `api.py` in the same directory as `fs.py`
