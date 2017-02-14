import nltk

senStart = "SENTENCE_START"
senEnd = "SENTENCE_END"

f = open('Lines.txt', 'r')
text = f.read()
lines = text.split("--------------")

lines = [line.replace('\n', ' ') for line in lines]
#print (lines)
sentences = [nltk.sent_tokenize(line.lower()) for line in lines]
sentences = ["%s %s %s" % (senStart, sentence, senEnd) for sentence in sentences]

tokenized = [nltk.word_tokenize(sentence) for sentence in sentences]
print (tokenized)
