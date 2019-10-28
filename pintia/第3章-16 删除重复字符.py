def remove_repeatchar(strs):
    char_list=list(map(str,strs))
    char_list=sorted(set(char_list))
    return "".join(char_list)
if __name__=="__main__":
    res=remove_repeatchar("ad2f3adjfeainzzzv")
    print(res)