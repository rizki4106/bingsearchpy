from setuptools import setup

def readme():
  with open('README.md') as f:
    README = f.read()
    return README


setup(
  name = 'bingsearchpy',
  packages = ['bingsearchpy'],
  version = '0.6',
  description=('bing search engine for python'),
  long_description=readme(),
  long_description_content_type="text/markdown",
  license='MIT',
  author = 'mrxxx04',
  author_email = 'rizkimaulana348@gmail.com',
  url = 'https://github.com/rizki4106/bingsearchpy',
  download_url = 'https://github.com/rizki4106/bingsearchpy/archive/v.0.1.zip',
  keywords = ['google','msn','searchengine', 'microsoft', 'google'],
  install_requires=[
          'requests',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)