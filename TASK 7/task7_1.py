import pprint

def main(sentence):
    sentence = sentence.lower()
    words = sentence.split()
    word_count ={}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

input_sentence = input("Enter a sentence: ")

word_counts = main(input_sentence)

print(word_counts)
