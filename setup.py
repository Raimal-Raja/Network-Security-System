'''
The setup.py file is an essential part of packaging and distribution Python Projects. It is used by setup tools(or distutils in older Python versions) to define the configuration of your project , such as its metadata, dependencies, and more

'''

from setuptools import find_packages, setup
from typing import List


def get_requirements() ->List[str]:
    '''
    this function will return list of requirements
    '''
    requirement_list:list[str]=[]
    
    try:
        with open(r'D:\GitHub\MLOPs-ETL-Pipelines-Network-Security-System\requirements.txt', 'r') as file:
            #read lines from the file
            lines = file.readlines()
            
            #Process each line
            for line in lines:
                requirement =line.strip()
                # ignore empty lines and -e .
                if requirement and requirement!= '-e .':
                    requirement_list.append(requirement)
    except  FileNotFoundError:
        print('Requirements.txt file not found')
        
    return requirement_list
# print(get_requirements())

setup(
    name = 'NetworkSecurity',
    version='0.0.1',
    author="Raimal Raja",
    author_email='raimalraja@gmail.com',
    packages=find_packages(),
    install_reguires=get_requirements(),
)
