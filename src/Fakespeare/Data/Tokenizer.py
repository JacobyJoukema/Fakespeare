import nltk

f = open('Lines.txt', 'r')
text = f.read()

tokenized = [nltk.word_tokenize(line) for line in text.split("--------------")]
print (tokenized)
