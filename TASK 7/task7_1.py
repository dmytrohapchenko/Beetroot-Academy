import string


sentence = input()

sentence = sentence.translate(str.maketrans('', '', string.punctuation)) # видаляє пунктуацію
sentence = sentence.lower().split(' ')
key_words = []
l_list = {}

for i in sentence:
    sentence.count(i)
    if sentence.count(i)>1:
        key_words.append(i)

for i in range(len(key_words)):
    l_list[key_words[i]] = sentence.count(key_words[i])

print(l_list)