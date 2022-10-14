import sys
if not sys.platform.startswith("linux"):
# if not sys.platform.startswith("win32"):
    raise Exception("Opps...")
print("hello")