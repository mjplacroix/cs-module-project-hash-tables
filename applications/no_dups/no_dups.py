def no_dups(s):
    # Your code here

    # split up words into a list
    s = s.split()
    # empty cache
    cache = {}
    remove = []
    # if word exists in cache
    for i in range(len(s)):
        if s[i] in cache:
            cache[s[i]] += 1
        else:
            cache[s[i]] = 1

    s.reverse()

    for key, value in cache.items():
        for i in range(value-1):
            s.remove(key)

    s.reverse()

    s = " ".join(s)

    return s
    



    # # delete from string
    #         remove.append(i)
    # # else, add word to cache
    #     else:
    #         cache[s[i]] = 1
    
    # for num in remove

    # unsplit the words
    # return 



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))