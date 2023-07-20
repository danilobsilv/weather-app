from setuptools import setup
from setuptools import find_packages

setup(
      name = "Weather App",
    
      version = "1.0.0",
    
      author = "Danilo Bruno da Silva",

      author_email = "danilobsilv@gmail.com",
    
      description = "Weather checking application",

      install_requires = [],

      packages = find_packages(),

      classifiers = [
            "Programming Language :: Python :: 3.9.13",
            "License :: MIT license",
            "Operating System :: Windows 11"
      ]
)