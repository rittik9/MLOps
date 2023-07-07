#will create my machine learning application as a package & deploy in pypi
#from there anybody can install and anybody can use it
from setuptools import find_packages,setup  #find packages finds all packages present in our application directory
from typing import List


HYPEN_E_DOT = '-e .' #-e . in requirements.txt triggers setup.py
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements
        
        
    
        
    
    
    
    
#like meta data of the entire project
setup(
    name = 'mlops',
    version = '0.0.1',
    author = 'Rittik Panda',
    author_email = 'rittikpanda24@gmail.com',
    packages = find_packages(), #this will go and check how many folders contain __init__.py,then it will consider it as a package and it will build it ,once built you can import it
    install_requires = get_requirements('requirements.txt')
)