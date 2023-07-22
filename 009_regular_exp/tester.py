import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa HaHaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
example.com
example,company
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
900-555-123
900-555-123456
Mr. Jones
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
abc
абвгд
wall mall hall ball tall
'''

sentence = 'Start a sentence and then bring it to an end'

emails = '''
SampleMaiL@example.com
john.sample@my-work.net
jack-125-production@colledge.edu
bob.Samples@example.co.uk
example@example.org
'''

urls = '''
https://www.google.com
http://www.wordpress.org
https://www.nasa.gov
https://example.net
www.example.net
example.net
'''

# pattern = re.compile(r'(\d{3}[-.]\d{3}[-.]\d{3,5})')
# pattern = re.compile(r'[1-3-]')
# pattern = re.compile(r'M(r|s|rs)\.? [A-Z][a-z]*')

# pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-.]+\.[a-zA-Z0-9-.]+')

# pattern = re.compile(r'(http://|https://)?(www\.)?([a-zA-Z0-9-]+)([a-zA-Z.]+)')

# matches = pattern.finditer(text_to_search)
#
# for match in matches:
#     print(match)

# pattern = re.compile(r'a', re.IGNORECASE)
pattern = re.compile(r'abc#I am a comment')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)