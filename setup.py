from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(filepath: str) -> List[str]:
    """
    This function returns a list of requirements.
    """
    requirements = []
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # Remove newline characters

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='mlproject',
    version='0.1',
    author='Prashant Jain',
    author_email='iamprashantjain2601@gmail.com',
    description='A brief description of my ML project',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/my_ml_project',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
