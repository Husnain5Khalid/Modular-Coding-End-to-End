from setuptools import setup, find_packages
from typing import List

PROJECT_NAME="End-to-ENd modular Coding in ML"
VERSION="0.0.1"
DESCRIPTION="This project tell us about industry level coding"
AUTHOR_NAME="Husnain Khalid"
AUTHOR_EMAIL="youcandoit.ml"
REQUIREMENTS_FILE_NAME = "requirements.txt"
HYPEN_E_DOT = "-e ."

# Now below function DO this 3 things
#1. Requrement.txt file open
#2. then read this file
#3. then new line \n replace by ""

def get_requirements_list()->List[str]:
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requriment_name.replace("\n", "") for requriment_name in requirement_list]

        if HYPEN_E_DOT in requirement_list:
            requirement_list.remove(HYPEN_E_DOT)
        return requirement_list
    
setup(name=PROJECT_NAME,
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHOR_NAME,
      author_email=AUTHOR_EMAIL,
      packages=find_packages(),
      install_requires= get_requirements_list()
      )