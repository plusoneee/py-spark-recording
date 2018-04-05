# Filter
* Filter items out of a sequence
* Return filtered list

Example 1 - over2 : 
* #### Python Function:
```python
# print(3,4)
def over_two(list1):
    new_lsit = [x for x in list1 if x > 2]
    return (new_list)
print(over_two([1,2,3,4]))
```
* ####  PySpark `filter`:
```python
n = [1,2,3,4]
list( filter( (lambda x:x>2,n) ))
```

* You don't necessary use a `lambda` function:
```python
n = [4,3,2,1]
print( [x for x in n if x > 2] )
```
