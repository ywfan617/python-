def f():
    char_dict={"letter":0,"blank":0,"other":0}
    for i in range(1):
        char=input()
        print(char)
        if "a"<=char<="z" or "A"<=char<="Z":
            char_dict["letter"]+=1

        elif char in [" ",""]:
            char_dict["blank"]+=1
        else:
            char_dict["other"]+=1
    return char_dict
if __name__=="__main__":
    res=f()
    print(res)
    #print("\n")

