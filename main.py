from bingsearchpy import engine

for i in engine.search("how to make a bomb"):
    print(i['title'], i['link'])