def longeststr(str_list):
    str_list.sort(key=lambda x:-len(x))
    return str_list[0]
if __name__=="__main__":
    str_list=["li","wang","zhang","jin","xiang"]
    res=longeststr(str_list)
    print("The longest is:",res)