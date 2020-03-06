# Remove repeated underscore characters.
# Uses a list comprehension with a conditional expression.
s = 'a_b_c__d___ef___g'
print(s)
print(s.split('_'))
print([ x  for x in s.split('_') ])
print([ x  for x in s.split('_') if len(x) > 0 ])
print('_'.join([ x  for x in s.split('_') if len(x) > 0 ]))
