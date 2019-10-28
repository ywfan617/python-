def palindrome_str(strs):
    res="".join(list(reversed(strs)))
    if res==strs:
        return "Yes"
    else:
        return "No"
if __name__=="__main__":
    res=palindrome_str("1 + 2 = 2 + 1")
    print(res)