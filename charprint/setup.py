import setuptools

with open("README.md", "r") as fhandle:
    long_description = fhandle.read() # Your README.md file will be used as the long description!

setuptools.setup(
    name="charprint-AverseABFun", 
    version="0.0.1", 
    author="AverseABFun", 
    author_email="arthurebeck@gmail.com", 
    description="Charprint! It prints one character at a time!", 
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AverseABFun/Charprint", 
    packages=setuptools.find_packages(), 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ], 
    python_requires='>=3.6', 
)
