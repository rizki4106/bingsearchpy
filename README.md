## bingsearchpy
bing search engine for python.
<hr/>
installation

```python 
pip install bingsearchpy
```
how to use

```python
from bingsearchpy import bingsearch
for i in bingsearch.engine.search('the most beautiful place in the world'):
    print(i['title'], i['link'], i['description'])
```
that's it all 😎