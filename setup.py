from setuptools import find_packages,setup
from typing import List
# from pip.req.req_file import parse_requirements

hyphen_e_dot="-e ."

def get_requirements(file_path:str)->List[str]:
    # This function returns the list of requirements
    requirements=[]
    with open (file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements] # so that '\n' is ignored while reading requirements.txt    
        # This is ListComprehension

        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot) # so that '-e .' is ignored while reading requirements.txt

    return requirements





# def get_requirements(file_path: str) -> List[str]:
#     requirements = []
    
#     for req in parse_requirements(file_path, session=""):
#         if not req.requirement.startswith("-e"):
#             requirements.append(str(req.requirement))
    
#     return requirements




setup(

    name='Student_Performance_Indicator',
    version='0.0.1',
    author='Nitin',
    author_email='bcs.animesh@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    



)