"""
Given two strings. Find the length of the longest subsequence which is common for both strings.
Subsequence is a sequence that made from the original string by removing elements but not changing the orger.
E.g.
string ABCDE has subsequences: AB, AC, AD, AE, ABC, ABE, etc.
"""

str1 = 'elephant'
str2 = 'erepat'


def sequence_length(s1: str, s2: str, ind1: int, ind2: int) -> int:
    if len(s1) <= ind1 or len(s2) <= ind2:
        return 0
    if s1[ind1] == s2[ind2]:
        return 1 + sequence_length(s1, s2, ind1 + 1, ind2 + 1)

    rm_s1 = sequence_length(s1, s2, ind1 + 1, ind2)
    rm_s2 = sequence_length(s1, s2, ind1, ind2 + 1)
    return max(rm_s1, rm_s2)


print(sequence_length(str1, str2, 0, 0))
