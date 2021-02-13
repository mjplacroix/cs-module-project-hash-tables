# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

with open("ciphertext.txt") as f:
    s = f.read()

def letter_tally(s):
    tally = {}

    for character in s:
        if character not in tally:
            tally[character] = 1
        else:
            tally[character] += 1

    tally_list = list(tally.items())
    tally_list.sort(key=lambda x: x[1], reverse=True)
    tally = dict(tally_list)

    print(tally)

letter_tally(s)

with open("ciphertext.txt") as f:
    words = f.read()

decode_dict = {'W':'E', 'J':'T', 'M':'A', 'X':'O', 'C':'H', 
'D':'N', 'K':'R', 'I':'I', 'N':'S', 'U':'D', 'S':'L', 'O':'W', 
'G':'U', 'Q':'G', 'B':'F', 'Y':'B', 'E':'M', 'F':'Y', 'A':'C', 
'Z':'P', 'P':'K', 'H':'V', 'V':'Q', 'T':'J', 'L':'X', 'R':'Z'}

def cipher(words):
    new_string = ""
    # iterate through string
    for letter in words:
    # look up each character in dictionary
        if letter in decode_dict:
    # if in dictionary, add value to new string
            new_string += (decode_dict[letter])
    # else add key to new string
        else:
            new_string += letter
    print(new_string)
    # print string

cipher(words)

# Your code here

