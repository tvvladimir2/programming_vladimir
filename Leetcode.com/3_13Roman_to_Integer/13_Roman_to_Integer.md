# 13. ROMAN TO INTEGER


---



## LINKS

[13. Roman to Integer](https://leetcode.com/problems/roman-to-integer/)
[Roman Numeral Converter](https://www.calculatorsoup.com/calculators/conversions/roman-numeral-converter.php)



---



## DESCRIPTION

Difficulty: Easy

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

**Symbol**       **Value**
I                1
V                5
X                10
L                50
C                100
D                500
M                1000

For example, 2 is written as `II` in Roman numeral, just two ones added together. `12` is written as `XII`, which is simply `X + II`. The number `27` is written as `XXVII`, which is `XX + V + II`.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as `IX`. There are six instances where subtraction is used:

`I` can be placed before `V` (5) and `X` (10) to make 4 and 9. 
`X` can be placed before `L` (50) and `C` (100) to make 40 and 90. 
`C` can be placed before `D` (500) and `M` (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.



---



## EXAMPLES

**Example 1**:
```
Input: s = "III"
Output: 3
Explanation: III = 3.
```


**Example 2**:
```
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
```


**Example 3**:
```
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
```
 


---



## CONSTRAINTS:

`1 <= s.length <= 15`
`s` contains only the characters `('I', 'V', 'X', 'L', 'C', 'D', 'M')`.
It is **guaranteed** that s is a valid roman numeral in the range **[1, 3999]**. 3999 = MMM



---



## PERSONAL NOTES

**Symbol**  **Value**
I           1
II          2
III         3
IV          4
V           5
VI          6
VII         7
VIII        8
IX          9


**Symbol**  **Value**
X           10
XX          20
XXX         30
XL          40
L           50
LX          60
LXX         70
LXXX        80
XC          90


**Symbol**  **Value**
C           100
CC          200
CCC         300
CD          400
D           500
DC          600
DCC         700
DCCC        800
CM          900


**Symbol**  **Value**
M           1000
MM          2000
MMM         3000
---------------------------------------------------------
'3999 = MMM' is a maximum problem value
V, X and I will have a top underline beginning with 4000.
This underline can not be typed in a text edito.
---------------------------------------------------------
IV          4000
V           5000
DC          6000
DCC         7000
DCCC        8000
CM          9000


