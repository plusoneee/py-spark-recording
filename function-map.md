# Map
* Apply same function to each element of sequence.
* Return the modified list.


List `[a,b,c]`,function `f()` -> `map()` -> `new` List `[f(a),f(b),f(c)]`


Example 1 - square:
* #### Python Function:
```python
# want print([16,9,4,1])
def square(list1):
    new_list = []
    for n in list1:
        new_list.append(n**2)
    return (new_list)
print(square([4,3,2,1)])
```
* ####  PySpark `map`:
```python
n = [4,3,2,1]
list( map(lambda x:x**2,n) )
```

* You don't necessary use a `lambda` function:
```python
# 
list( map(square,n) )
# 
n = [4,3,2,1]
print( [x**2 for x in n] )
```