import importlib.util
import sys
from setuptools import setup, find_packages
import f5_ctlr_agent

def parse_requirements(filename):
    """ Load requirements from a pip requirements file """
    with open(filename) as f:
        lines = f.read().splitlines()
        # Remove comments and empty lines
        reqs = [line for line in lines if line and not line.startswith('#')]
    return reqs

# Parse requirements and dependency links
install_reqs = parse_requirements('./agent-runtime-requirements.txt')
install_links = [req for req in install_reqs if '://' in req]
install_reqs = [req for req in install_reqs if '://' not in req]

print('install requirements:', install_reqs)
print('dependency links:', install_links)

setup(
    name='f5-ctlr-agent',
    description='F5 Networks Controller Agent',
    license='Apache License, Version 2.0',
    version=f5_ctlr_agent.__version__,
    author='F5 Networks',
    url='https://github.com/f5devcentral/f5-ctlr-agent',
    keywords=['F5', 'big-ip'],
    scripts=['f5_ctlr_agent/bigipconfigdriver.py'],
    dependency_links=install_links,
    install_requires=install_reqs,
    packages=find_packages(exclude=['*test', '*.test.*', 'test*', 'test']),
)
