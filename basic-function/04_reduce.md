# Reduce
* Apply same operaction to items of a sequence.
* Users resault of operation as first param of next operation 
* Return an item (not list)


List `[a,b,c]`,function `f()` -> `reduce()` -> `f( f(a,b), c)`


Example 1 - mult:
* #### Python Function:
```python
# want print([16,9,4,1])
def mult(list1):
    prod = list1[0]
    for n in range(1,len(list1)):
        prod = prod * list1[n]
    return prod
print(prod([4,3,2,1]))
```
* ####  PySpark `reduce`:
```python
reduce(lambda x,y:x*y, n)
```
4 * 3 = 12
12 * 2 = 24
24 * 1 = 24
