import os


for folderNames, subFolders, filenames in os.walk(r'C:\Users\george.dominguez\Downloads\LPL Summer'):
        for file in filenames:
                if ' ' not in file:
                        continue
                else:
                        fileName, fileExt = os.path.splitext(file)
                        name1, name2, name3 = fileName.split('.')
                        newName ='{}{}{}{}'.format(name1.replace(' ', '_'), name2.replace(' ', '_'), name3.replace(' ', '_'), fileExt)
                        os.rename(os.path.join(folderNames, file), os.path.join(folderNames, newName))
                
