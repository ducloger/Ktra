def check_palndrome(s):
    x = 0
    y = len(s)-1
    for i in range(len(s)):
        if s[x] != s[y]:
            return False
        else: 
            x += 1
            y -= 1
            print(f"Loop: {x}")
    return True

print(check_palndrome("tnmpghfjdksla;omnt"))