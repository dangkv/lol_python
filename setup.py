from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='lol_python',
    version='0.0.0a',
    description='A Python API Wrapper for Riot League of Legends API Endpoints.',
    url="https://github.com/dangkv/lol_python",
    author="Dang Khoi Vo",
    author_email="dangkv@gmail.com",
    py_modules=['lol_python'],
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: GPL-3.0-or-later",
        "Operating System :: Mac OS",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "certifi == 2022.12.7",
        "charset - normalizer == 2.1.1",
        "idna == 3.4",
        "requests == 2.28.1",
        "urllib3 == 1.26.13",
    ],
    extras_require={
        "dev": [],
    },

)
