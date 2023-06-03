"""
Given a string. Find the length of the longest palindromic subsequence
E.g. ELRMENMENT -> 5 (EMEME)
"""

str = 'ELRMENMENT'
#      0123456789


def sequence_length(s: str, ind1: int, ind2: int) -> int:
    if ind1 > ind2:
        return 0
    if ind1 == ind2:
        return 1
    if s[ind1] == s[ind2]:
        return 2 + sequence_length(s, ind1 + 1, ind2 - 1)

    rm_s1 = sequence_length(s, ind1 + 1, ind2)
    rm_s2 = sequence_length(s, ind1, ind2 - 1)
    return max(rm_s1, rm_s2)


print(sequence_length(str, 0, len(str) - 1))

