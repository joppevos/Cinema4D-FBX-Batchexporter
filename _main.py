import os
import c4d
import time
"""
# LOOK FOR IN A DIRECTORY WITH MULTIPLE FOLDERS, FIND THE C4D FILES IN THOSE FOLDERS. PLACE THEM IN EXACT THE 
SAME NAME TYPE OF FOLDERS. 

Grab only .c4d files path.split == .c4d?

get the highest version number only. 

"""

def main():
    """
    export all c4d files in given directory to FBX
    """
    importpath = (r'\\192.168.3.6\current04\DLL_GAMING\Animatic\3dExchange\fromC4D\arena_collect')
    files = os.listdir(importpath)
    if files:
        for afile in files:
            print('opening file: {}'.format(afile))
            path = os.path.join(importpath, afile)
            c4d.documents.LoadFile(path)
            exportpath = os.path.join(r'\\192.168.3.6\current04\DLL_GAMING\Animatic\3dExchange\fromC4D\arena_fbx',
                                      '{}.fbx'.format(afile.split('.')[0]))
            doc = c4d.documents.GetActiveDocument()
            if c4d.documents.SaveDocument(doc, exportpath, c4d.SAVEDOCUMENTFLAGS_DONTADDTORECENTLIST, 1026370):
                print('file succesful exported')
            else:
                print('error occured when writing file')
        c4d.documents.CloseAllDocuments()
    else:
        print('folder is emtpy')

if __name__ == '__main__':
    main()