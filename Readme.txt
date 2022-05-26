
    It may be that an error occurs on creating a new session.
    This lies in an error of one of the python modules.
    To solve this you either have to update python and the modules to the latest version.
    Or you have go into this folder:
    C:\Users\[YourPCUsername]\AppData\Local\Programs\Thonny\Lib\encodings\
    And into this file:
    cp1252.py
    And comment out the entire line 205:
    '\ufffe'   #  0x9D -> UNDEFINED
    This solves the problem