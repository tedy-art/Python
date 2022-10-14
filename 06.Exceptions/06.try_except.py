# import module sys to get the type of exception
import sys
randomList = ['a', 0, 2]
for entry in randomList:
    try:
        print("The entry is ",entry)
        r = 1/int(entry)
        break
    except:
        print("Ooops!", sys.exc_info()[0],"occured.")
        #exc_info():To obtain the execution information for the current thread,format the results & prints the text to a file handle.
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", r)
