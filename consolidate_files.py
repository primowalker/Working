import os, shutil
 
 
def movefiles():
    x=0
    inputDir=raw_input("please enter the folder where the files are: ")
    outputDir=raw_input("please enter the destination folder")
    for root, dirs, files in os.walk(inputDir topdown=False):
        for name in files:
            newname="%09d"%x+name
            x+=1
            shutil.move(os.path.join(root, name), os.path.join(outputDir,newname))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
