from lxml import html
import requests

f = open('Pages.txt', 'r')
quotes = []
pages = f.read().split('\n')
f.close()
pages.pop()
#print (pages)

for page in pages:
    print (page)
    data = requests.get(page)
    tree = html.fromstring(data.content)
    #print (tree)
    #lines = tree.xpath('//blockquote/text()')
    #print (lines)
    '''lines = len(tree.xpath('//blockquote'))
    print (lines)
    for i in range (lines):
        sentences = len(tree.xpath('//blockquote['+str(i)+']/a'))
        print (sentences)
        quote = ""
        for j in range (sentences):
            sentence = tree.xpath('//blockquote['+str(i)+']/a['+str(j)+']/text()')
            print (sentence)
            quote = quote+sentence+"\n"
        quotes.append(quote)'''
    #quote = tree.xpath('//blockquote/a')

    quotes = quotes + tree.xpath('//blockquote/a/text()')

print (len(quotes))
print (quotes[-1])
f = open('Lines.txt', 'w')
print ("JOINING")
out = "\n".join(quotes)
print (out)
f.write(out)
f.close()
