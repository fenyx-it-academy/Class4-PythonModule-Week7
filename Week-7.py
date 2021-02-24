#!/usr/bin/env python
# coding: utf-8

# Question 1:
# Write a program that detects the ID number hidden in a text. We know that the format of the ID number is 2 letters, 1 digit, 2 letters, 2 digits, 1 letter, 1 digit (For example: AA4ZA11B1).
# 
# Input : AABZA1111AEGTV5YH678MK4FM53B6
# 
# Output : MK4FM53B6
# 
# Input : AEGTV5VZ4PF94B6YH678
# 
# Output : VZ4PF94B6

# In[ ]:


import re

string = 'AABZA1111AEGTV5YH678MK4FM53B6'
pattern = "\w\w\d\w\w\d\d\w\d"

result = re.findall(pattern, string) 
print(result)


# Question 2:
# Find words that are 8 letter long on this text ;
# 
# Without, the night was cold and wet, but in the small parlour of Laburnum villa the blinds were drawn and the fire burned brightly. Father and son were at chess; the former, who possessed ideas about the game involving radical chances, putting his king into such sharp and unnecessary perils that it even provoked comment from the white-haired old lady knitting placidly by the fire. "Hark at the wind," said Mr. White, "who, having seen a fatal mistake after it was too late, was amiably desirous of preventing his son from seeing it. I'm listening," said the latter grimly surveying the board as he stretched out his hand. "Check." I should hardly think that he's come tonight," said his father, with his hand poised over the board. "Mate," replied the son. "That's the worst of living so far out," balled Mr. White with sudden and unlooked-for violence; "Of all the beastly, slushy, out of the way places to live in, this is the worst. Path's a bog, and the road's a torrent. I don't know what people are thinking about. I suppose because only two houses in the road are let, they think it doesn't matter."

# In[3]:


import re

string = """"Without, the night was cold and wet, but in the small parlour of Laburnum villa the blinds were drawn and the fire burned brightly. Father and son were at chess; the former, who possessed ideas about the game involving radical chances, putting his king into such sharp and unnecessary perils that it even provoked comment from the white-haired old lady knitting placidly by the fire. "Hark at the wind," said Mr. White, "who, having seen a fatal mistake after it was too late, was amiably desirous of preventing his son from seeing it. I'm listening," said the latter grimly surveying the board as he stretched out his hand. "Check." I should hardly think that he's come tonight," said his father, with his hand poised over the board. "Mate," replied the son. "That's the worst of living so far out," balled Mr. White with sudden and unlooked-for violence; "Of all the beastly, slushy, out of the way places to live in, this is the worst. Path's a bog, and the road's a torrent. I don't know what people are thinking about. I suppose because only two houses in the road are let, they think it doesn't matter."""

pattern = "[\W|\s]\w{8}[\s|\W]"

result = re.findall(pattern, string)
print(result)


# Question 3:
# Write a program that list according to email addresses without email domains in a text.
# 
# Example:
# 
# Input:
# 
# The advencements in biomarine studies franky@google.com with the investments necessary and Davos sinatra123@yahoo.com. Then New Yorker article on wind farms...
# 
# Output :
# 
# franky
# 
# sinatra123

# In[ ]:


import re

string = 'The advencements in biomarine studies franky@google.com with the investments necessary and Davos sinatra123@yahoo.com. Then New Yorker article on wind farms...'

pattern = '([\w\d]+)@[\w\d]+'

result = re.findall(pattern, string)

for i in re.findall(pattern, string):
  print (i)

