from collections import Counter
def example(**kwargs):
    for key,value in kwargs.items():
        print (key,value)

# example(test="kebrjlhkjl/jrnfl", test2=5)

def makeAnagram(a, b):
    a_dict = {}
    b_dict = {}
    count = 0
    for i in a:
        if i in a_dict.keys():
            a_dict[i] = a_dict[i] + 1
        else: 
            a_dict[i] = 1

    for i in b:
        if i in b_dict.keys():
            b_dict[i] = b_dict[i] + 1
        else: 
            b_dict[i] = 1

    print (a_dict)
    print (b_dict)

    for key, val in a_dict.items():
        if key in b_dict.keys() and val < b_dict[key]:
            count += a_dict[key] - val
        elif key not in b_dict.keys():
            count += val

    for key, val in b_dict.items():
        if key in a_dict.keys() and val < a_dict[key]:
            count += a_dict[key] - val
        elif key not in a_dict.keys():
            count += val

    return count

def makeAnagram2(a, b):
    a_dict = Counter(a)
    b_dict = Counter(b)
    a_dict.subtract(b_dict)
    return sum (abs(i) for i in a_dict.values() )
print(makeAnagram2('fcrxzwscanmligyxyvym','jxwtrhvujlmrpdoqbisbwhmgpmeoke'))