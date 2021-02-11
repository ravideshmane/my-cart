from setuptools import setup

setup(name='MyCartApp',
      version='1.0',
      py_modules=['mycart'],
      install_requires=['Click', 'pandas', 'pyfiglet'],
      entry_points='''
      [console_scripts]
      mycart=mycart:mycart
      ''',
      )