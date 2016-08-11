def check(a):
    x=['a','e','i','o','u']
    for k in x:
        if ( k == a ):
            return "Vowel"
    return "Consonant"
n = raw_input()
print check(n)
