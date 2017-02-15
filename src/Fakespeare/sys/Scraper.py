from lxml import html
import requests

f = open('Pages.txt', 'r')
quotes = []
pages = f.read().split('\n')
f.close()
pages.pop()

for page in pages:
    print (page)
    data = requests.get(page)
    tree = html.fromstring(data.content)
    lines = len(tree.xpath('//blockquote'))
    for line in range (lines):
        text = tree.xpath('//blockquote['+str(line)+']/a/text()')
        if (text != []):
            quotes.append('\n'.join(text))

print (len(quotes))
f = open('Lines.txt', 'w')
print ("JOINING")
print (type(quotes))
out = "\n--------------\n".join(quotes)
f.write(out)
f.close()
