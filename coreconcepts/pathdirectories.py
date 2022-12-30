from pathlib import Path

#Absolute path - for directories in windows or C:drive
#Relative path  - within project

#creating a path object
path = Path("ecommerce")
print(path.exists())

# path.mkdir : used to create a directory in code.
# path.rmdir : used to remove the directory
path = Path("email")
print(path.rmdir())

# path.glob() allows to search for files or directories and their current path
from pathlib import Path

path = Path()
for file in path.glob("*.py"):
    print(file)

#python package index PYPI
#openpyxl : package used for working with excel spreadsheets : 2.5.14 : pip install openpyxl - pip install is used to install packages
# when __init__.py is added to a folder, is then considered a package, with modules.

#3:56:04