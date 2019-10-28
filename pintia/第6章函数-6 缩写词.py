def acronym(phrase):
    words=phrase.split()
    res=""
    for i in words:
        res+=i[0].upper()
    return res
if __name__ == '__main__':
    phrase="central  processing  unit"
    res=acronym(phrase)
    print(res)