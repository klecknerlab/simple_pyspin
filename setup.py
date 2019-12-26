from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='simple_pyspin',
    version='0.1.0',
    description='An easy-to-use Pythonic wrapper for the FLIR PySpin Library.  Developed by the Kleckner Lab at UC Merced.',
    url='https://github.com/klecknerlab/simple_pyspin',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Dustin Kleckner',
    author_email='dkleckner@ucmerced.edu',
    license='Apache 2.0 (http://www.apache.org/licenses/LICENSE-2.0)',
    packages=['simple_pyspin'],
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
