from numpy import min_scalar_type


def longestCommonPrefix(strs) :
    """
    strs: list of strings 
    """
    res = ""
    map = {}
    for word in strs:
        map[len(word)] = word
    min_word = map[min(map.keys())]
    leng = len(min_word)
    i = 0
    while i < leng:
        set1 = set([word[i] for word in strs])
        if len(set1) == 1: ## only one common letter
            res += min_word[i]
            i += 1
        else: 
            break 
    return res 
