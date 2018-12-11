import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hotAD",
    version="0.0.3",
    author="Anthony Rentsch, Jiayin Lu, Lipika Ramaswamy, Yuanheng Wang",
    author_email="anthony.rentsch@g.harvard.edu",
    description="A Python package for forward mode automatic differentiation for multivariate functions, Jacobian/Hessian matrix computation, root-finding, and optimization routines.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CS207ProjectGroup8/cs207-FinalProject",
    packages=setuptools.find_packages(),
    install_requires=['numpy==1.15.2',
                      'matplotlib==2.2.3'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
