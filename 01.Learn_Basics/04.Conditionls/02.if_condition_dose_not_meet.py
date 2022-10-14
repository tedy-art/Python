def main():
    x, y = 8, 4
    if(x<y):
        st = "x is less than y"
    print(st)
if __name__=="__main__":
    main()
"""
Error 
UnboundLocalError:local variabe 'st' referenced before assignment
"""