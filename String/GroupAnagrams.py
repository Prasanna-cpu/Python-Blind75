

def groupAnagrams(strs):
    groups={}

    for word in strs:
        sorted_word=" ".join(sorted(word))

        if sorted_word in groups:
            groups[sorted_word].append(word)

        else:
            groups[sorted_word]=word

    return list(groups.values())