# What is this
- this is a simple libary representing logical sentences

# Usage
- just include the logic_classes.py file in your project and import all needed classes

### Currently supported classes and examples
- Value: Represents a simple boolean
```python
a = Value(False,"a")
```
- And: Represents a simple logical and
```python
testone = And(a, b, c)
```
- Or: Represents a simple logical or
```python
testone = Or(a, b, c)
```
- Not: Represents a not
```python
a = Not(Value(False,"a"))
```
- Impl: Represents an implication
```python
testone =Impl(And(a, b, c), Not(Value(False, "d")))
```
- each clas has two functions
    - ```print```: prints the logical sentence
    - ```evaluate```: evaluates the sentence
- accessing values directly is possible but leads to undefined behaviour and is **NOT** the correct way to retrive values

