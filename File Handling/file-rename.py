import os

folderPath = r'C:\Users\Rohit Gadekar\Desktop\New folder'
os.chdir(r"C:\Users\Rohit Gadekar\Desktop\New folder")
for i in os.listdir(folderPath):
    oldname = i
    newname = i[15:]
    os.rename(oldname, newname)
