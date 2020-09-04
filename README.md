## bingsearchpy
bing search engine for python.

### installation

```python 
pip install bingsearchpy
```
#### how to use

- get random data

```python
from bingsearchpy.bingsearch import engine

for i in engine.search('the most beautiful place in the world'):
    print(i['title'], i['link'])
```

- get image

```python
from bingsearchpy.bingsearch import engine

for i in engine.search_image('bali'):
    print(i['link'])
```
that's it all 😎
