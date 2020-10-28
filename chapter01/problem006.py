def word_ngram(n, s):
  li = []
  for i in range(len(s) - n + 1):
    li.append(s[i:i+n])
  return li

paradise = 'paraparaparadise'
paragraph = 'paragraph'

paradise_bi =  word_ngram(2, paradise)
paragraph_bi =  word_ngram(2, paragraph)

set_paradice = set(paradise_bi)
set_paragragh = set(paragraph_bi)

union = set_paragragh | set_paradice
paradice_difference = set_paragragh ^ set_paradice
paragragh_difference = set_paradice ^ set_paragragh
intersection = set_paragragh&set_paradice

print('Union')
print(union)
print('Paradice difference')
print(paradice_difference)
print('Paragragh difference')
print(paragragh_difference)
print('intersection')
print(intersection)

print('Is paraparaparadise include "se"?')
print('se' in set_paradice)
print('Is paragraph include "se"?')
print('se' in set_paragragh)
