# it helps in building our application as a package 

from setuptools import setup, find_packages


HYPHEN_E_DOT = '-e .'
#meta data information about our package
def get_requirements(file_path):
    with open(file_path) as f:
        requirements = f.read().splitlines()
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
    return requirements 



setup(
    name="mlproject1",
    version="0.1",
    packages=find_packages(),
    author="deepanshu agarwal",
    author_email="deepanshuagarwal946@gmail.com",
    # packages=find_packages(),
    install_requires=get_requirements("requirements.txt")   
)