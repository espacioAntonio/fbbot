import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with open('requeriments.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='fbbot',
    version=open("fbbot/_version.py").readlines()[-1].split()[-1].strip("\"'"),
    install_requires=requirements,
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description="fbbot is a sim1ple bot class to showcasing the Facebook Messenger Platform",
    long_description=README,
    url='https://github.com/espacioAntonio/fbbot',
    author='espacioAntonio',
    author_email='espacio.antonio@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Development Status :: 3 - Alpha',
        'Topic :: Communications :: Chat',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
