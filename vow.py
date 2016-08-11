n = raw_input()
def check(a):
    x=['a','e','i','o','u']
    for k in x:
        if ( k == a ):
            return "Vowel"
    return "Consonant"

print check(n)
