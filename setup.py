import setuptools
from distutils.command.install import INSTALL_SCHEMES
for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']
    

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="INLD", 
    version="0.0.1",
    author="Jagmanjot",
    author_email="jagmanjotsingh.becse17@pec.edu.in",
    description="A package to detect Indian natural languages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jagman32/INLD",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    data_files=[('', ['LICENSE']),('',['INLD/vectorizer.pkl']),('',['INLD/lang_detect.model'])],
    include_package_data=True,
    python_requires='>=3.6',
)