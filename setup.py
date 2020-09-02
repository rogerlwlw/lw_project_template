# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 14:09:32 2020

@author: rogerluo
"""

# for 'xxx' project replace 'projectlibxx' with project name 'xxx'

# build dist
# source dist
# setup.py bdist_wheel bdist_egg  sdist



# # 'dev'
# setup.py alias --global-config dev egg_info --tag-build=DEV --tag-date bdist_wheel sdist bdist_egg
# # 正式发布版，无后缀添加
# # 'release'
# setup.py alias --global-config release egg_info -Db "" bdist_wheel sdist bdist_egg
# # 仅仅保留最近3此更新
# # 'keep3'
# setup.py alias --global-config keep3 rotate --match=.tar.gz,.egg,.whl,.msi --keep=3 

# setup.py dev
# setup.py release
# setup.py keep3

import re
from setuptools import setup, find_packages

for line in open('projectlibxx/__init__.py'):
    match = re.match("__version__ *= *'(.*)'", line)
    if match:
        __version__, = match.groups()

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="projectlibxx",
    version=__version__,
    packages=find_packages(),
    # This tells setuptools to install any data files it finds in your packages.
    # The data files must be specified via the distutils’ MANIFEST.in file.
    # data files not contained in pkg folder will not be included
    inlcude_package_data=True,

    # Specify additional patterns to match files that may or may
    # not be matched by MANIFEST.in or found in source control
    package_data={
        # include all files under data subdirectory for all pkgs
        "": ['data/*'],
        # # And include any *.msg files found in the "pkg_A" package, too
        # "pkg_A": ["*.msg"]        
        },

    # exclude README.txt from all packages
    exclude_package_data={"": ["README.md", ]},

    # Dynamic Discovery of Services and Plugins
    
    # Automatic Script Creation: add script entry points that could be called
    # through cmd
    entry_points={
        'console_scripts': ['projectlibxx = projectlibxx.__main__:run_main'],
    },
    install_requires=[
        'numpy>=1.15.0',
        'pandas>=1.0.0',
        'scikit-learn>=0.22.1',
        'scipy>=1.1. 0',
        'matplotlib>=3.2.2'
        'setuptools>=46.1.3',
    ],
    
    extras_require={
        "yapf":  ['yapf>=0.25.0'],
        "plotly": ["plotly>=4.6.0"],
        },
    
    author="rogerluo",
    author_email="coolww@outlook.com",
    description=
    "short description",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='GNU/LGPLv3',
    url='https://github.com/rogerlwlw',
    classifiers=[
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering :: Artificial Intelligence'
    ],
    keywords=[
        'pipeline optimization', 
        'hyperparameter optimization', 
        'data science',
        'machine learning', 
        'Bayesian optimization',
        'data mining',
    ],
)


