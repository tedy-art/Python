File Handling:-
    1) open a file
    2) perform operation on a file
    3) close a file

Type of file
1) Text file - Plain text, Human readable
        e.g. name, marks

2) Binary File- Binary file machine readable
        e.g. mp3, jpeg, mp4

opening file:-
    python provides an in-buit function "open()" a file
    syntax:
        var_name = open("file_name", mode= "r/w/a", buffering,
                          encoding=None, error=None, newline = None, closefd = True)

e.g.
f = open("hello.txt")
if f:
    print("File is successfully opened!!")

1) file_name = file to accessed
2) mode = access mode(perpose of opening file)
3) f = file handler, File pointer
4) buffering = * Positive Interger value used to set buffer size for
                a file.
               * In text mode, buffer size should be 1 or more than 1.
               * In binary mode, buffer size can be 0
               * Default size- 4096-8192 bytes
5) encoding = * Encoding type used to decode and encode file.
              * Should be used in text mode only
              * Default value depends on OS
              * For windows - cp1252
6) error = * Represents how encoding and decoding error are to be 
             handled
           * Cannot be used in binary mode
           * some standard value are: strict, ignore, replace etc.

7) newline = * It can be \n,\r,\r\n

e.g.
    f = open("hello.txt", mode="r", buffering = 10, encoding="utf-8")
    if f:
        print("Opened")
    print(f)