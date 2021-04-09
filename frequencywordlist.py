
string = ['a', 'A', 'b']
counter = dict()

for word in string:
        word = word.lower()
        if word in counter:
            counter[word] = counter[word] + 1
        else:
            counter[word] = 1

for key in list(counter.keys()):
    print(key, ":", counter[key]/len(string))

#calculate the length of a string

def string_length(str1):
    count = 0
    for char in str1:
        count += 1
    return count

print(string_length('HelloWorld'))

#count the number of characters in a string

def char_frequency(str1):
    dict={}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_frequency('HelloWorld'))

#validity of a string of parantheses

def is_valid_parenthese(str1):
    stack, pchar = [], {"(": ")","{":"}","[":"]"}
    for parenthese in str1:
        if parenthese in pchar:
            stack.append(parenthese)
        elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
            return False
    return len(stack) == 0

print(is_valid_parenthese("(){}[]"))
print(is_valid_parenthese("()[}"))

#get a single string from two given strings separated by a space and swap the two chars of each string

def chars_mix_up(a, b):
    new_a = b[:2] + a[2:]
    new_b = a[:2] + b[2:]
    return new_a + ' ' + new_b
print(chars_mix_up('abc' , 'xyz'))

#return the length of the longest word

def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][0], word_len[-1][1]
result = find_longest_word(("PHP", "Python","Ruby"))
print("\nLongest word :", result[1] + "\nLength : ",result[0])

#reverse a string
def reverse_string(str1):
    return ''.join(reversed(str1))
print(reverse_string('python'))

#convert string to all uppercase
def change_case(str1):
    for letter in str1:
        if letter.upper() == letter:
            return str1.lower()
        else:
            return str1.upper()
print(change_case('Python'))

#reverse words in string
def reverse_words_in_string(str1):
    for line in str1.split('\n'):
        return(' '.join(line.split()[::-1]))
print(reverse_words_in_string("The quick brown fox jumps over the lazy dog"))

#strip chars from string

def strip_chars(str, chars):
    return "".join(c for c in str if c not in chars)
print(strip_chars("The quick brown fox jumps over the lazy dog", "aeiou"))

