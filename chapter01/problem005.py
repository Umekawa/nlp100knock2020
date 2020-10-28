def word_ngram(n, s):
  li = []
  for i in range(len(s) - n + 1):
    li.append(s[i:i+n])
  return li

def sentence_ngram(n,s):
  words = s.split(' ')
  li = []
  for i in range(len(words) - n + 1):
    li.append(words[i:i+n])
  return li

s = 'I am an NLPer'
print(word_ngram(2, s))
print(sentence_ngram(2, s))