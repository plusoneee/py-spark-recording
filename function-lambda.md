

# Lambda

Example 1 - double: 
* #### Python Function:
```python
# double x
def double(x):
    return (x * 2)
```
* ####  PySpark `lambda`:
```python
lambda x:2 * x
```
* `x` : Parameter(s)
* `x * 2`: Return

Example 2 - add: 
* ### Python Function:
```python
# add x and y
def add(x,y):
    return (x + y)
```
* #### PySpark `lambda`:
```python
lambda x,y:x+y
```
Example 3 - Max: 
* #### Python Function:
```python
# max of x,y
def max(x,y):
    if x > y:
        return (x)
    else: 
        return (y)
```
* ####  PySpark `lambda`:
```python
lambda x,y:x if x>y else y
```


