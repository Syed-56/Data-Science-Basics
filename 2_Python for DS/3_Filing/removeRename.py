import os

if os.path.exists("writing_reading_lists.txt"):
    print("File Exists")
    os.rename("writing_reading_lists.txt", "writingReadingLists.txt")
    #os.remove("writingReadlingLists.txt")  removes files

else:
    print("File Dont Exist")