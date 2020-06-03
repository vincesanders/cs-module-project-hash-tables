def no_dups(s):
    arr = s.split(' ')
    words = {}
    for word in arr:
        if word in words:
            continue
        else:
            words[word] = True
    return ' '.join(words)



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))