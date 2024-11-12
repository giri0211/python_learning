# Running the unit tests in python

1. create tests folder and required test files in this folder.
1. import the `unittest` module `TestCase` class
1. create a class for unit test by the function being tested.

1. Below `test_area` method is testing the `calc_cricle_area` functionality by passing the required input values and comparing the output with given value in the second argument.

```python

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        # test areas
        self.assertAlmostEqual(calc_cricle_area(1), pi)
        self.assertAlmostEqual(calc_cricle_area(0), 0)
        self.assertAlmostEqual(calc_cricle_area(2.1), pi*2.1**2)
```

1. run the tests from root folder using the below `unittest` command.

```cmd
 python -m unittest .\fundamentals\basics\tests\test_circle_area.py
```

1. In the case of expecting an error to be validated, use the `assertRaises` method of `unittest.TestCase` class.

```python
    def test_type(self):
        self.assertRaises(TypeError, calc_cricle_area, 3+5j)
        self.assertRaises(TypeError, calc_cricle_area, True)
        self.assertRaises(TypeError, calc_cricle_area, "radius")
```

1. If you want help about the assert funtions follow the commands below in the python interpreter, se

```Pshell
# open python interpreter
python
# import unittest module
import unittest
# get the documentation on assertRaises method
help(unittest.TestCase.assertRaises)
```Pshell