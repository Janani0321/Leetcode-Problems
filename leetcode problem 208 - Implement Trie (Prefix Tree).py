Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #leetcode problem 208 - Implement Trie (Prefix Tree)
... 
... class Trie(object):
... 
...     def __init__(self):
...         self.root={}
... 
...     def insert(self, word):
...         c=self.root
...         for i in word:
...             if i not in c:
...                 c[i]={}
...             c=c[i]
...         c['end']=''
... 
...     def search(self, word):
...         c=self.root
...         for i in word:
...             if i not in c:
...                 return False
...             c=c[i]
...         return 'end' in c
...         
...     def startsWith(self, prefix):
...                 return False
...             c=c[i]
