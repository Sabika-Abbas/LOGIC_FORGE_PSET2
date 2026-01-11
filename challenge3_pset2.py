def lps_recursive(s):
    i=0
    j=len(s)-1
    if i > j:
        return 0
    if i == j:
        return 1
    
    if s[i] == s[j]:
        i+=1
        j-=1
        return 2 + lps_recursive(s[i:j+1])
    return max(lps_recursive(s[i+1:j+1]), lps_recursive(s[i:j]))

print(lps_recursive("ABCA")) 