def cipher(s):
  ciphered_s = ''
  for c in s:
    ciphered_c = chr(219-ord(c)) if c.islower() else c
    ciphered_s += ciphered_c
  return ciphered_s

s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
ciphered_s = cipher(s)
print(ciphered_s)
decoded_s = cipher(ciphered_s)
print(decoded_s)
