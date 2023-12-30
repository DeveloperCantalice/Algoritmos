
string1 = 'feliwe'
string2 = 'likefe'


def Solution(str1: str, str2: str):
    
    if len(str1) != len(str2):
        return False
    
    hash1 = {}
    hash2 = {}

    for l1 in str1:

        if l1 not in hash1:
            hash1[l1] = 1
        else:
            hash1[l1] += 1
    
    for l2 in str2:

        if l2 not in hash2:
            hash2[l2] = 1
        else:
            hash2[l2] += 1

    
    for i in hash1.keys():
        if i not in hash1 or i not in hash2 or hash1[i] != hash2[i]:
            return False
    return True


print(Solution(string1, string2))