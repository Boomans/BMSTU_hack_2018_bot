from distutils.core import setup, Extension

setup(name='levenshtein', version='1.0',\
      ext_modules=[Extension('levenshtein', ['library.c'])])