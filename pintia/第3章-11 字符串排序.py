def f(str_list):
    str_list.sort()
    return str_list
if __name__=="__main__":
    res=f(["red","yellow","blue","green","white","bluo"])
    print("After sorted:")
    print(res)