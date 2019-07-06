def repeatedString(s, n):
    if len(s) >= n:
        return s[:n].count('a')
    else:
        
        x = len(s) * (n//len(s))
        if n == x:
            return s.count('a') * (n//len(s))
        else:
            return s.count('a') * (n//len(s)) + s[:n - x].count('a')