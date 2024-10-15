def all_variants(text):
    n = len(text)
    x = 0
    while x<=n:
        if x == 0:
            for i in range(n):
                yield text[i]
        elif x<n:
            for j in range(n-x):
                yield text[j:j+x+1]
        x+=1

a = all_variants("abcde")
for i in a:
    print(i)
