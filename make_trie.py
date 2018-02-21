###########################
## Make a trie in python ##
###########################

beneficial = ['a', 'b', 'c', 'aa', 'd']
health = [1, 2, 3, 4, 5, 6]
a, b, c = 1, 5, 'caaab'

print(c.count('aa'))

d = dict(zip(beneficial, health))

print(d.keys(), d.values())
print(list(d.keys())[2:], d.values())

k = list(d.keys())[2:]

_end = '_end_'
def make_trie(d):
    root = dict()
    for word in d:
        current_dict = root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        current_dict[_end] = _end
    return root

def in_trie(trie, word):
    current_dict = trie
    for letter in word:
        if letter in current_dict:
            current_dict = current_dict[letter]
        else:
            return False
    else:
        if _end in current_dict:
            return True
        else:
            return False


print(in_trie(make_trie(beneficial), 'caaab'))