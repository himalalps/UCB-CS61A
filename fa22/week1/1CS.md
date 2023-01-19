# What is CS?

what problem, how to solve, what techniques using computation.

# What is this course about?

manage complexity

- Mastering abstraction
- Programming paradigms

intro to programming

- understanding Python
- combining multiple ideas in large projects
- computers interpret prog languages

Different types of languages: Scheme and SQL

# Demos

```python
shakes = open('shakespeare.txt')
text = shakes.read().split()
len(text)
text[:25]
text.count('you')
'draw'[::-1]    # 'ward'
words = set(text)
{w for w in words if len(w) == 4 and w[::-1] in words}

```