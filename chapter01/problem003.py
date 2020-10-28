s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
words = s.replace(',','').replace('.', '').split(' ')
li = []
for word in words:
  li.append(len(word))

print(li)
