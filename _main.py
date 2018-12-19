import os
import c4d
from c4d import gui


def main():
    """
    export all c4d files in given directory to FBX
    """
    try:

        importpath = c4d.gui.InputDialog('Insert path of the C4D files directory', 'C:\example_path')
        newfolder = str(importpath + '\\FBX_export')
        if not os.path.exists(newfolder):  # check if path exist
            os.makedirs(newfolder)

        files = os.listdir(importpath)
        if files:
            for afile in files:
                if afile.endswith('.c4d'):
                    print('opening file: {}'.format(afile))
                    path = os.path.join(importpath, afile)
                    c4d.documents.LoadFile(path)
                    exportpath = os.path.join(newfolder, '{}.fbx'.format(afile.split('.')[0]))
                    doc = c4d.documents.GetActiveDocument()
                    if c4d.documents.SaveDocument(doc, exportpath, c4d.SAVEDOCUMENTFLAGS_DONTADDTORECENTLIST, 1026370):
                        print('file successful exported')
                    else:
                        print('error occurred writing file')
        else:
            gui.MessageDialog('No c4d files found in given folder!')

    finally:
        c4d.documents.CloseAllDocuments()


if __name__ == '__main__':
    main()