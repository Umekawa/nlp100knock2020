s = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
words = s.replace(',','').replace('.', '').split(' ')
head = [0,4,5,6,7,8,14,15,18]
dic = {}
for i in range(len(words)):
  c = words[i][0] if i in head else words[i][0:2]
  dic[i] = c

print(dic)
