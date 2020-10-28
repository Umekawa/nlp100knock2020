import random
def random_except_head_and_tail(s):
  if len(s)<=4:
    return s # もっと良いアーリーリターンの書き方がある気がする
  sorted_s = s[0]
  tail = s[-1]
  rand =  random.sample(range(len(s)-2), len(s)-2)
  for i in rand:
    sorted_s+=s[i+1]
  return sorted_s + tail

s = 'I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'
words = s.split(' ')
randomed_word_list = []
for word in words:
  randomed_word_list.append(random_except_head_and_tail(word))

print(' '.join(randomed_word_list))
