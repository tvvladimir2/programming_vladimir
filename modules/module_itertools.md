# ITERTOOLS MODULE


---


## LINKS

[Itertools simple clear examples at GeeksforGeeks.org](https://www.geeksforgeeks.org/python-itertools/?ref=gcse)
[itertools — Functions creating iterators for efficient looping¶](https://docs.python.org/3/library/itertools.html#itertools.combinations_with_replacement)


---


## DESCRIPTION

`Itertools` is a standard library that contains several functions that are useful in functional programming.


---


## Infinite iterators:

|   | Iterator |   Arguments   |                     Results                    |                Example                |
|---|:--------:|:-------------:|:----------------------------------------------:|:-------------------------------------:|
| 1 | count()  | start, [step] | start, start+step, start+2*step, …             | count(10) --> 10 11 12 13 14 ...      |
| 2 | cycle()  | p             | p0, p1, … plast, p0, p1, …                     | cycle('ABCD') --> A B C D A B C D ... |
| 3 | repeat() | elem [,n]     | elem, elem, elem, … endlessly or up to n times | repeat(10, 3) --> 10 10 10            |


---


## Iterators terminating on the shortest input sequence:

|    |        Iterator       |          Arguments          |                   Results                   |                          Example                         |
|----|:---------------------:|:---------------------------:|:-------------------------------------------:|:--------------------------------------------------------:|
| 4  | accumulate()          | p [,func]                   | p0, p0+p1, p0+p1+p2, …                      | accumulate([1,2,3,4,5]) --> 1 3 6 10 15                  |
| 5  | chain()               | p, q, …                     | p0, p1, … plast, q0, q1, …                  | chain('ABC', 'DEF') --> A B C D E F                      |
| 6  | chain.from_iterable() | iterable                    | p0, p1, … plast, q0, q1, …                  | chain.from_iterable(['ABC', 'DEF']) --> A B C D E F      |
| 7  | compress()            | data, selectors             | (d[0] if s[0]), (d[1] if s[1]), …           | compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F            |
| 8  | dropwhile()           | pred, seq                   | seq[n], seq[n+1], starting when pred fails  | dropwhile(lambda x: x<5, [1,4,6,4,1]) --> 6 4 1          |
| 9  | filterfalse()         | pred, seq                   | elements of seq where pred(elem) is false   | filterfalse(lambda x: x%2, range(10)) --> 0 2 4 6 8      |
| 10 | groupby()             | iterable[, key]             | sub-iterators grouped by value of key(v)    |                                                          |
| 11 | islice()              | seq, [start,] stop [, step] | elements from seq[start:stop:step]          | islice('ABCDEFG', 2, None) --> C D E F G                 |
| 12 | pairwise()            | iterable                    | (p[0], p[1]), (p[1], p[2])                  | pairwise('ABCDEFG') --> AB BC CD DE EF FG                |
| 13 | starmap()             | func, seq                   | func(*seq[0]), func(*seq[1]), …             | starmap(pow, [(2,5), (3,2), (10,3)]) --> 32 9 1000       |
| 14 | takewhile()           | pred, seq                   | seq[0], seq[1], until pred fails            | takewhile(lambda x: x<5, [1,4,6,4,1]) --> 1 4            |
| 15 | tee()                 | it, n                       | it1, it2, … itn  splits one iterator into n |                                                          |
| 16 | zip_longest()         | p, q, …                     | (p[0], q[0]), (p[1], q[1]), …               | zip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D- |


---


## Combinatoric iterators:

|    |             Iterator            |      Arguments     |                            Results                            |
|----|:-------------------------------:|:------------------:|:-------------------------------------------------------------:|
| 17 | product()                       | p, q, … [repeat=1] | cartesian product, equivalent to a nested for-loop            |
| 18 | permutations()                  | p[, r]             | r-length tuples, all possible orderings, no repeated elements |
| 19 | combinations()                  | p, r               | r-length tuples, in sorted order, no repeated elements        |
| 20 | combinations_with_replacement() | p, r               | r-length tuples, in sorted order, with repeated elements      |

The recursive generators that are used to simplify combinatorial constructs such as permutations, combinations, and Cartesian products are called combinatoric iterators.

---


## 1. itertools.count(start=0, step=1)

Make an iterator that returns evenly spaced values starting with number start. Often used as an argument to map() to generate consecutive data points. Also, used with zip() to add sequence numbers.

**Example 1**: Use for() loop
```python
from itertools import count

for i in count(3, 1.5):
  print(i)
  if i >= 9:
    break
```
```
> 3
> 4.5
> 6.0
> 7.5
> 9.0
```

**Example 1**: Use while() loop in a function
```python
def count(start=3, step=1.5):
    n = start
    while True:
        yield n
        n += step
        if n == 10.5:
            break

set = list(count())
print(list(set))
```
```
> [3, 4.5, 6.0, 7.5, 9.0]
```


---


##  2. itertools.cycle(iterable)

The function cycle infinitely iterates through an iterable (for instance a list or string)
Make an iterator returning elements from the iterable and saving a copy of each. When the iterable is exhausted, return elements from the saved copy. Repeats indefinitely. Roughly equivalent to:

```python
from itertools import cycle

my_set = [1,2,3]

for i in cycle(my_set):
  print(i)
```
```
> 1
> 2
> 3

> 1
> 2
> 3

> 1
> 2
> 3
> ...
```


---


##  3. itertools.repeat(object[, times])

The function `repeat()` repeats an object, either infinitely or a specific number of times.
Make an iterator that returns object over and over again. Runs indefinitely unless the times argument is specified. Used as argument to `map()` for invariant parameters to the called function. Also used with `zip()` to create an invariant part of a tuple record.


Syntax: repeat(val, num)
Parameters:
val: The value to be printed.
num: If the optional keyword num is mentioned, then it repeatedly prints the passed value num number of times, otherwise prints the passed value infinite number of times.


Used for:
- A common use for repeat is to supply a stream of constant values to `map()` or `zip()`:


```python
import itertools

c = list(itertools.repeat(25, 4))
print (c)
```
```
> [25, 25, 25, 25]
```


---


## 4.  itertools.accumulate(iterable[, func, *, initial=None])

Make an iterator that returns accumulated sums, or accumulated results of other binary functions (specified via the optional func argument).

If func is supplied, it should be a function of two arguments. Elements of the input iterable may be any type that can be accepted as arguments to func. (For example, with the default operation of addition, elements may be any addable type including Decimal or Fraction.)

Usually, the number of elements output matches the input iterable. However, if the keyword argument initial is provided, the accumulation leads off with the initial value so that the output has one more element than the input iterable.


Syntax:
itertools.accumulate(iterable[, func]) –> accumulate object


Used for:
- Set to min() for a running minimum.
- Set to max() for a running maximum.
- Set to operator.mul() for a running product.
- Amortization tables can be built by accumulating interest and applying payments.
- First-order recurrence relations can be modeled by supplying the initial value in the iterable and using only the accumulated total in func argument.

**Example**:
```python
import itertools
# import operator to work with operator
import operator

GFG = [1, 2, 3, 4, 5]

# The operator.mul takes two numbers and multiplies them.
result = itertools.accumulate(GFG, operator.mul)

print(result)

# printing each item from list
for each in result:
    print(each)
```
```
<itertools.accumulate object at 0x000001969644F480>
> 2           # operator.mul(1, 2)
> 6           # operator.mul(2, 3)
> 24          # operator.mul(6, 4)
> 120         # operator.mul(24, 5)
```


---


## 5. itertools.chain(*iterables)

It is a function that takes a series of iterables and returns one iterable. It groups all the iterables together and produces a single iterable as output. Its output cannot be used directly and thus explicitly converted into iterables.

Make an iterator that returns elements from the first iterable until it is exhausted, then proceeds to the next iterable, until all of the iterables are exhausted. Used for treating consecutive sequences as a single sequence.

**Example**: Two lists.
```python
from itertools import chain

consonants = ['d1', 'f1', 'k1', 'l1', 'n1', 'p1']
vowels = ['a2', 'e2', 'i2', 'o2', 'u2']

res = list(chain(consonants, vowels))

print(res)
res.sort()
print(res)
```
```
> ['d1', 'f1', 'k1', 'l1', 'n1', 'p1', 'a2', 'e2', 'i2', 'o2', 'u2']

> ['a2', 'd1', 'e2', 'f1', 'i2', 'k1', 'l1', 'n1', 'o2', 'p1', 'u2']
```


**Example**: String as an iterable.
```python
from itertools import chain

consonants = 'abcd'
vowels = ''

res = list(chain(consonants, vowels))

print(res)
```
```
> ['a', 'b', 'c', 'd']
```


---


##  14. itertools.takewhile(predicate, iterable)

Make an iterator that returns elements from the iterable as long as the predicate is true.
This allows considering an item from the iterable until the specified predicate becomes false for the first time. The iterable is a list or string in most of the cases. As the name suggests it “take” the element from the sequence “while” the predicate is “true”. This function come under the category “terminating iterators”. The output cannot be used directly and has to be converted to another iterable form. Mostly they are converted into lists.

General implementation:
```
def takewhile(predicate, iterable):
   for i in iterable:
       if predicate(i):
            return(i)
       else:
            break
```

**Example**: Take elements from a list until one of them is not even (function returns False).
```python
from itertools import takewhile

# function to check whether the number is even
def even_nos(x):
     return(x % 2 == 0)

# iterable (list)
li =[0, 2, 4, 5, 8, 22, 34, 6, 67]

# output list
new_li = list(takewhile(even_nos, li))

print(new_li)
```
```
> [0, 2, 4]
```

**Example**: Take the elements as long as they are digits.
```python
from itertools import takewhile

# function to test the elements
def test_func(x):
    print("Testing:", x)
    return(x.isdigit())

# using takewhile  with for-loop
for i in takewhile(test_func, "14erdg456"):
    print("Output :", i)
    print()
```
```
> Testing: 1
> Output : 1
>
> Testing: 4
> Output : 4
>
> Testing: e
```


**Example**: Using lambda function as a pridicate.
```python
from itertools import takewhile

my_list = [2,4,6,7,9,8]           # value 7 will break the takewhile()

result = takewhile(lambda x: x%2==0, my_list)   # function

print(list(result))
```
```
> [2, 4, 6]
```


---


## 17. itertools.product(*iterables, repeat=1)

In the terms of Mathematics Cartesian Product of two sets is defined as the set of all ordered pairs (a, b) where a belongs to A and b belongs to B. Consider the below example for better understanding.

Input1: arr1 = [1, 2, 3]
Input2: arr2 = [5, 6, 7]
Output : [(1, 5), (1, 6), (1, 7), (2, 5), (2, 6), (2, 7), (3, 5), (3, 6), (3, 7)]

Cartesian product of input iterables.

Roughly equivalent to nested for-loops in a generator expression. For example, product(A, B) returns the same as ((x,y) for x in A for y in B).

The nested loops cycle like an odometer with the rightmost element advancing on every iteration. This pattern creates a lexicographic ordering so that if the input’s iterables are sorted, the product tuples are emitted in sorted order.

To compute the product of an iterable with itself, specify the number of repetitions with the optional repeat keyword argument. For example, product(A, repeat=4) means the same as product(A, A, A, A).


**Example**: Cartesian product.
```python
from itertools import product

arr1 = [1, 2, 3]
arr2 = [5, 6, 7]

result = product(arr1, arr2)
print(result)
print(list(result))
```
```
> <itertools.product object at 0x000001C525A82740>
> [(1, 5), (1, 6), (1, 7), (2, 5), (2, 6), (2, 7), (3, 5), (3, 6), (3, 7)]
```


---


## 18. itertools.permutations(iterable, r=None)

itertool.permutations() method provides us with all the possible arrangements that can be there for an iterator and all elements are assumed to be unique on the basis of there position and not by there value or category. All these permutations are provided in lexicographical order. The function itertool.permutations() takes an iterator and ‘r’ (length of permutation needed) as input and assumes ‘r’ as default length of iterator if not mentioned and returns all possible permutations of length ‘r’ each.

**Example**: All possible arrangements of banana.
```python
from itertools import permutations

my_string = 'ada'

result = permutations(my_string)
result2 = permutations(my_string)

print(result)
print('Number of variations is: ', len(list(result2)))
print(list(result))
```
```
> <itertools.permutations object at 0x0000020B0F055540>
> Number of variations is:  6
> [('a', 'd', 'a'), ('a', 'a', 'd'), ('d', 'a', 'a'), ('d', 'a', 'a'), ('a', 'a', 'd'), ('a', 'd', 'a')]
```
