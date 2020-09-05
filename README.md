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
| data | description |
|------|-------------|
| title | title of websites |
| link | website's link |

- get image

```python
from bingsearchpy.bingsearch import engine

for i in engine.search_image('bali'):
    print(i['title'], i['link'])
```
| data | description |
|------|-------------|
| title | image's name |
| link | image's source |

- get video
```python
from bingsearchpy.bingsearch import engine

for i in engine.search_video('bandung'):
    print(i['title'], i['snippet_video'], i['detail_video'])
```
| data | description |
|------|-------------|
| title | video's name |
| snippet_video | short video |
| detail_video | the place of origin of the video |


that's it all 😎
