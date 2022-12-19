# 14. LONGEST COMMON PREFIX


---


## DESRIPTION

Difficulty: Easy

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`. E.g. "".

 
**Example 1**:
```
Input: strs = ["flower","flow","flight"]
Output: "fl"
```


**Example 2**:
```
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```
 

**Constraints**:

`1 <= strs.length <= 200`
`0 <= strs[i].length <= 200`
`strs[i]` consists of only lowercase English letters.



---


## STATISTICS

Accepted: 2.1M
Submissions: 5M
Acceptance Rate: 40.8%



---



## START CODE

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
```


```cs
public class Solution {
    public string LongestCommonPrefix(string[] strs) {
        
    }
}
```



---



## NOTES

A `prefix` is an affix which is placed before the stem of a word. Adding it to the beginning of one word changes it into another word.

For example,

re- turn    >>  return
re- sult    >>  result
re- search  >>  research
re- port    >>  report
re- member  >>  remember
re- ason    >>  reason
re- ally    >>  really
re- al      >>  real
re- ad      >>  read