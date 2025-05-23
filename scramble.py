# Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

# Notes:

# Only lower case letters will be used (a-z). No punctuation or digits will be included.
# Performance needs to be considered.
# Examples
# scramble('rkqodlw', 'world') ==> True
# scramble('cedewaraaossoqqyt', 'codewars') ==> True
# scramble('katas', 'steak') ==> False


def scramble(s1, s2):
    
    s1_count = {}
    s2_count = {}
    
   
    for char in s1:
        if char in s1_count:
            s1_count[char] += 1
        else:
            s1_count[char] = 1
    
   
    for char in s2:
        if char in s2_count:
            s2_count[char] += 1
        else:
            s2_count[char] = 1
    
   
    for char, count in s2_count.items():
        if s1_count.get(char, 0) < count:
            return False  
    
    return True  



#scramble('cedewaraaossoqqyt', 'codewars')
#scramble('katas', 'steak')
print(scramble('rkqodlw', 'world'))