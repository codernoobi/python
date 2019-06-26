"""PIP is a package manager for Python packages, or modules if you like

A package contains all the files you need for a module.
Modules are Python code libraries you can include in your project

check if pip is installed
Navigate your command line to the location of Python's script directory, and type the following
pip --version

Download a Package
Downloading a package is very easy.
Open the command line interface and tell PIP to download the package you want.
Navigate your command line to the location of Python's script directory, and type the following
pip install camelcase

Once the package is installed, it is ready to use.
Import the "camelcase" package into your project
"""

import camelcase
								#using package
c = camelcase.CamelCase()
txt = "hello world"
print(c.hump(txt))

#Find more packages at https://pypi.org/.
#to upgrade the pip - (python -m pip install --upgrade pip)