from setuptools import find_packages, setup
from typing import List


HYPHEN_EDOT = '-e .'

#returns list of requirements 
def get_requirements(filepath:str)->List[str]:
    requirements = []
    with open(filepath) as fileobj:
        requirements = fileobj.readlines()
        requirements = [r.replace('\n', '') for r in requirements]

    if HYPHEN_EDOT in requirements:
        requirements.remove(HYPHEN_EDOT)

    return requirements

setup(
name='ds_proj',
version='0.0.1',
author='Shinan',
author_email='calzoni.shinan@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)