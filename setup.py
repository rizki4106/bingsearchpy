from distutils.core import setup
setup(
  name = 'bingsearchpy',
  packages = ['bingsearchpy'],
  version = '0.1',
  license='MIT',
  description = 'bing searc engine for python',
  author = 'mrxxx04',
  author_email = 'rizkimaulana348@gmail.com',
  url = 'https://github.com/rizki4106/bingsearchpy',
  download_url = 'https://github.com/rizki4106/bingsearch.py/archive/v_01.tar.gz',
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