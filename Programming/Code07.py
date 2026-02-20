 #Given a list of strings, use a single list comprehension to extract strings that meet two criteria: they must be longer than 5 characters AND they must start with a vowel (a, e, i, o, u).
strings = ["apple", "banana", "orange", "grape", "kiwi", "avocado", "peach"]
result = [
    s for s in strings 
    if len(s) > 5 and s[0].lower() in 'aeiou'
    ]
print(result)
