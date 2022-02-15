# Default Markdown:
---


## Used Links
> [Basic writing and formatting syntax (Github - Markdown README files)](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

> [Markdown Python course files](https://github.com/programiz/python-course)


## Create empty line & comment:
```
<br/><br/>  <!-- Create empty line & comment it -->
```



## HTML Supported links:
<p align="center">
    <a href="https://github.com/mathLab/EZyRB/blob/master/LICENSE.rst" target="_blank">
        <img alt="Software License" src="https://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat-square">
    </a>
    <a href="https://travis-ci.org/mathLab/pydata" target="_blank">
        <img alt="Build Status" src="https://travis-ci.org/mathLab/pydata.svg">
    </a>
    <a href="https://coveralls.io/github/mathLab/pydata" target="_blank">
        <img alt="Coverage Status" src="https://coveralls.io/repos/github/mathLab/pydata/badge.svg">
    </a>
</p>


## SVG links:
[![PyPI version](https://badge.fury.io/py/unix-ar.svg )](https://pypi.python.org/pypi/unix_ar/)
[![Build Status](https://travis-ci.com/getninjas/unix_ar.svg?branch=master)](https://travis-ci.org/getninjas/unix_ar)
[![Read The Docs](https://readthedocs.org/projects/unix_ar/badge/?version=latest)](https://unix_ar.readthedocs.io/en/latest/?badge=latest)


# Headings & paragraphs:
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6
This is a paragraph with `highlighted word 1`, `word2`, `word3`

<!-- Italics -->
*This text* is italic

_This text_ is italic

<!-- Strong -->
**This text** is italic

__This text__ is italic

<!-- Strikethrough -->
~~This text~~ is strikethrough

<!-- Blockquote -->
> This is a quote


<!-- Horizontal Rule -->
## Horizontal rule:
---
___


## Links:
<!-- Links -->
[`Highlighted link`](http://www.traversymedia.com)

[Traversy Media](http://www.traversymedia.com)

[Traversy Media](http://www.traversymedia.com "Traversy Media")

[LICENSE file with relative path](LICENSE.rst)


## UL list:
* Item 1
* Item 2
* Item 3
  * Nested Item 1
  * Nested Item 2


## UL list:
1. Item 1
1. Item 2
1. Item 3
2.


## Inline Code Block:
`<p>This is a paragraph</p>`


## Images:
![Markdown Logo](https://markdown-here.com/img/icon256.png)
<br/></br>

---
# Github Markdown:
---
## Bash code block
<!-- Code Blocks -->
```bash
  npm install

  npm start
```

## Javascript code block
```javascript
  function add(num1, num2) {
    return num1 + num2;
  }
```

## Python code block
```python
  def add(num1, num2):
    return num1 + num2
```

## Tables
| Name     | Email          |
| -------- | -------------- |
| John Doe | john@gmail.com |
| Jane Doe | jane@gmail.com |


## Task List
* [x] Task 1
* [x] Task 2
* [ ] Task 3


## Ignoring Markdown formatting

You can tell GitHub to ignore (or escape) Markdown formatting by using **\** before the Markdown character.

```
Let's rename \*our-new-project\* to \*our-old-project\*.
```

## Footnotes (only displays inm Github)
Here is a simple footnote[^1].

A footnote can also have multiple lines[^2].  

You can also use words, to fit your writing style more closely[^note].

[^1]: My reference.
[^2]: Every new line should be prefixed with 2 spaces.  
  This allows you to have a footnote with multiple lines.
