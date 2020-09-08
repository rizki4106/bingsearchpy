from bingsearchpy import engine
import logging
query = input('search > ')
for i in engine.search(query):
    print(i['title'])