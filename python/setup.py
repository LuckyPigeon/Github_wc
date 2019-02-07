from setuptools import setup, find_packages

setup(
  name = 'pywc',
  version = '0.0',
  long_description = 'Linux command \'wc\' implement with github page',
  author = 'LuckyPigeon',
  author_email = 'lucky90322@gmail.com',
  classifier = [
    'Development Status :: 3 - Alpha',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
  keywords = 'github wc',
  py_modules = ['py_wc.py'],
  install_requires = [
    'sys',
    'urllib',
    'pprint',
    'beautifulsoup4'
  ],
  python_requires = '=3.6.*',
  project_urls = {
    'Bug Reports': 'https://github.com/LuckyPigeon/Github_wc/issues',
    'Source': 'https://github.com/LuckyPigeon/Github_wc',
  },
)
