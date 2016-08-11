n = int(raw_input())
def check(n):
    if (n > 0):
        return "Positive"
    elif (n < 0):
        return "Negative"
    else:
        return "Zero"

print check(n)
