def word_count(s):
    # Your code here
    
    # make string all lowercase
    s = s.lower()
    # split up into a list
    s = s.split()
    # remove none alpha characters
    for w in range(len(s)):
        for l in s[w]:
            if l == "'":
                continue
            elif l.isalpha() == False:
                s[w] = s[w].replace(l, "")


    # split up into a list
    # if already in dictionary, increment value
    word_count = {}
    for word in s:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    print(word_count)
    return word_count
    # else create a dictionary for each new occurance
    # return dicdtionary



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))