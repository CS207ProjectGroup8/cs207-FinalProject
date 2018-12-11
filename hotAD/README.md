# hotAD

A Python package for forward mode automatic differentiation for multivariate functions, Jacobian/Hessian matrix computation, root-finding, and optimization routines.

[![Build Status](https://travis-ci.org/CS207ProjectGroup8/cs207-FinalProject.svg?branch=master)](https://travis-ci.org/CS207ProjectGroup8/cs207-FinalProject.svg?branch=master)

[![Coverage Status](https://coveralls.io/repos/github/CS207ProjectGroup8/cs207-FinalProject/badge.svg?branch=master)](https://coveralls.io/github/CS207ProjectGroup8/cs207-FinalProject?branch=master)

## Background
Classically, scientists have used symbolic differentiation and finite difference method to compute derivatives of functions, but these approaches face issues of increasing errors and increasing time cost in evaluating the derivatives as dimensions and complexities of the function go up. **Automatic differentiation (AD)** applies the chain rule - a rudimentary differentiation technique - over and over on a series of elementary arithmetic operations that make up any function. As the order increases, the complexity of AD calculation is not worse than the original function, therefore achieving efficiency.

Our Python package employs the forward mode of AD to evaluate the first and second derivatives of functions. Users are welcome to use our forward mode AD module and accompanying the elementary functions module for their own applications or to take advantage of our even more user-friendly Jacobian-calculating and optimization module.

## Installation
To install, users have two options

* **Pip**: `pip install hotAD` *(coming soon)*
* **Download source code**: Find the code under `hotAD/hotAD` and the requirements in the `requirements.txt` file.

## Usage

### AutoDiffObject
Users can instantiate variables they wish to differentiate and then combine these variables into a function, which will now contain the function value and first derivative. To call vector-valued functions, simply create a list of functions. Users can specify an optional argument `H=True` if they wish to compute the second derivative as well.

`x = AutoDiff(3, 'x')`
`y = AutoDiff(4, 'y')`
`f = x*y + x`

### ElementaryFunctions
Users are strongly recommended to use our elementary functions. Currently we have implemented:
* trigonometric functions (`sin`, `cos`, `tan`, `arcsin`, `arccos`, `arctan`)
* power functions (`power`, `sqrt`)
* exponential functions (`log`, `exp`)
* logistic function (`logit`)

`x = AutoDiff(np.pi, 'x')`
`y = AutoDiff(np.pi/4, 'y'`
`f = ef.sin(x) + np.tan(y)`

### ADfun
Users can use the methods in this module to compute the Jacobian matrix of a function, to perform root-finding via Newton's Method, and to perform minimization via `newton`, `quasi-newton-BFGS`, and `gradient-descent` methods.

## More information
For additional information on how to use the package, please see `docs/milestone2.ipynb`.

Our group members are:

* Yuanheng Wang
* Jiayin Lu
* Lipika Ramaswamy
* Anthony Rentsch
