# count-min-sketch
Count-Min Sketch algorithm implementation using Python.

Count-min sketch approach was proposed by Graham Cormode and S. Muthukrishnan. in the paper approximating data with the count-min sketch [Link](https://ieeexplore.ieee.org/document/6042851).

It is a useful algorithm for probabilistically estimate the frequency of an item/element in a stream of data.

## To activate virtual environment
`poetry shell`

## To install dependencies
`poetry install`

## To run linter
`poetry run flake8 --ignore=E501 src/*`
`poetry run flake8 --ignore=E501 tests/*`

## To build project
`poetry build`

## To test project
`poetry run pytest -v`

## Usage
- Define a Python class using the Item as the base class and override the `repr` method.  The objects of the defined class can now be counted by initializing a CMS instance.
- To see an example of how to use CMS, check out the files in the tests folder.