# Big O Notation & Time Complexity


---


## LINKS:

[The Origin of Graphs](https://www.youtube.com/watch?v=N4mez69LcxE)

[Yourtube video](https://www.youtube.com/watch?v=D6xkbGLQesk) (studied completely)


---


## DESCRIPTION

**Wrong questions to ask:**
- [ ] `How much time does it take to run this function?`


**Right questions to ask:**
- [x] `How does the runtime of the program grow as the size of the input grows?`


**Time Complexity** = a way of showing how the runtime of a program/function increases


---


## GRAPHS

![](https://miro.medium.com/max/551/1*d-pvBA0dFCMl-Qfpl61wEA.png)

![\pictures\big_O.png](https://media.geeksforgeeks.org/wp-content/cdn-uploads/mypic.png)
<br></br>


---


## TIME COMPLEXITY: LINEAR TIME `O(n)`
```
T = a*n+b           # `a`, `b` are constants, 'n' is the size of the input
```

>  1. Find the fastest growing term >> a*n
>  2. Remove the coefficient >> n
>  3. T = O(n)

```python
x = 1                             # input size
given_array = [*range(1, x, 1)]   # generate list

total = 0
for i in given_array:
    total += 1

print(total)    # T:O(n) linear complexity
```

---


## TIME COMPLEXITY: CONSTANT TIME

Simple calculation, always takes the same amount of time to calculate.

Formula: `T = O(1)`

```
T = a = 0.567 (random number we get from a formula)
T = 0.567 * 1 = O(1)
```


**Adding two constant times.** E.g. using two formulas:
T = O(1) + O(1) = c1 + c2 = c3 = c3*1 = O(1)
>  1. Find the fastest growing term >> c3*1
>  2. Remove the coefficient >> 1
>  3. T = O(1)


```python
given_array = [*range(1, x, 1)] # generate list

total = 0
total = total + given_array[0]  # O(1)
print(total)                    # O(1)
```


---


## ADDING TIME COMPLEXITIES:  linear  + constant `O(n**2)`

```python
x = 1                             # input size
won = 5
lost = 3
given_array = [*range(1, x, 1)]   # generate list

total = won + lost                # O(1)
for i in given_array:             # O(n)
    total += 1                    # O(1)

print(total)                      # O(1)
```


**From the code block above:**
> T = O(1) + n*O(n) + O(1) = c1 + n*c2 = O(n)
>  1. Find the fastest growing term >> n*c2
>  2. Remove the coefficient >> n
>  3. T = O(n)


---


## TIME COMPLEXITY: QUADRATIC TIME

```
`T = O(n**2)`
```

```
T = a*n**2+b*n+c           # where `a`, `b`, 'c' are constants, 'n' is the size of the input
```


```python
array = [[1,2,3,4],
         [3,6,1,6],
         [3,6,1,0]]

totak = 0             # O(1)

for i in array:       # O(n)
  for k in i:         # O(n)
    total += 1        # O(1)

print(total)          # O(1)
```
```
T = O(1) + n*n*O(1) = n**2*c1 + c2 = O(n**2)
```


---


## LET'S SKETCH:

![](https://printsgraphpaper.com/wp-content/uploads/2019/11/Blank-Graph-Paper-With-Axis-For-Maths.png)

**Other Notes:**

Brute force
interate through entire array which is length 10
and do it potentially 'n' times for each number in the array
worst case time complexity is big 'O' of n squared >> `O(n**2)`

time complexity in the worst scenario is big 'O' of n >> T: O(n) (linear algorithm to solve the problem)


---