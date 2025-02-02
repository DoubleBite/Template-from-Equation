# Template from Equation


This library provides functions to create template (make template) from its associated equation (e.g. 2+5 -> n0+n1).


The term "**equation template**" is first introduced in Kushman et al.(2014). It represents the abstraction of equation systems. The concept of it are then used in many following works. We found a tool to create such templates useful but not publicly available. So we tried to write one and share with peers in the area of automatic math word problem solving in NLP.


The template generated would contain "n0, n1, n2, ..." for numbers and "x0, x1, x2, ..." for variables.
For example:  
+ 2+5 -> n0+n1
+ 2+5*60/x = y -> n0 + n1 * n2 / x0 = x1


In some situations, we want to keep some constants in the equation unchanged. For example, to get the template of the equation "2+7\*60 = x"  for the problem *"How many minutes is 2 hours and 7 minutes?"*, we want to keep the constant "60" unchanged. In this situation, our function allows passing a number slot which contains only the numbers we want to substitute for our template. (See the Example Usage below).


To make template from equation, we use the ast trees. When traversing an AST tree, it returns "n0, n1, n2, ..." for the leaf nodes of numbers, and "x0, x1, x2" for variables. Then, an equation of "2+5\*x" can be turned into its template "n0+n1\*x0". (Using AST tree can help us avoid some subtle string matching difficulties of regular expression.)




## Installation
```
pip install template_from_equation
```


## Usage
```python
>>> from template_from_equation import Equation

>>> eq1 = Equation("2+5")
>>> eq1
2 + 5
>>> eq1.get_template()
'n0 + n1'

>>> eq2 = Equation("2+7*60 = x")
>>> eq2
2 + 7 * 60 = x
>>> eq2.get_template()
'n0 + n1 * n2 = x0'
>>> eq2.get_template(num_slot=[2,7])
'n0 + n1 * 60 = x0'

>>> eq3 = Equation("2*x+5*12 = y")
>>> eq3.get_template()
'n0 * x0 + n1 * n2 = x1'
>>> eq3.get_template(num_slot=[2,5])
'n0 * x0 + n1 * 12 = x1'
```


## Todo

- [ ] An option to share tokens for repeated numbers, i.e. 2+5*2 -> n0 +n1 * n0
- [ ] To parse the operator "^"



## References
+ [Kushman, Nate, et al. "Learning to automatically solve algebra word problems." Proceedings of the 52nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers). Vol. 1. 2014.](https://www.aclweb.org/anthology/P14-1026)
+ [codegen](https://github.com/andreif/codegen): Some of the naming styles but not the code are adapted from codegen, which is a library to convert ast tree to python code 


## License
This project is licensed under the terms of the MIT license.