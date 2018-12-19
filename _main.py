import os
import c4d
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
    importpath = (r'\\192.168.3.6\current04\DLL_GAMING\Animatic\c4d\Sc01_Arena')
    files = os.listdir(importpath)

    if files:
        for file in files:
            print('opening file: {}'.format(file))
            path = os.path.join(importpath, file)
            c4d.documents.LoadFile(path)
            # export FBX
            exportpath = os.path.join(r'\\192.168.3.6\current04\DLL_GAMING\Animatic\3dExchange\fromC4D',
                                      '{}.fbx'.format(file))
            if c4d.documents.SaveDocument(doc, exportpath, c4d.SAVEDOCUMENTFLAGS_DONTADDTORECENTLIST, 1026370):
                print('file succesful exported')
                c4d.documents.KillDocument(doc)
            else:
                print('error occured when writing file')
    else:
        print('folder is emtpy')

if __name__ == '__main__':
    main()