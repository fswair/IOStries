from libs.main import IOStries, IOAnySEO, IOSEOMetrics, IOArticles

obj = IOStries("Test")


def find_similar(query:str, stack:list | tuple, return_types=False) -> int | dict:
    similartypes, iotypes = {}, {}
    counter = 0
    for s in stack:
        if __similar__(query, s) > 50:
            counter+=1
            similartypes[f"[RELATIVE] {count_chars(s, True)}"] = (__similar__(query, s, return_types=True))
            iotypes[f"{count_chars(s, True)}"] = IOStries(s).types
        else:
            similartypes[f"{count_chars(s, True)}"] = (__similar__(query, s, return_types=True))
            iotypes[f"{count_chars(s, True)}"] = IOStries(s).types
    if not return_types:
        return counter
    return {"similaritys":similartypes, "IOTypes":iotypes}


def count_chars(string:str, return_chars=False):
    if not return_chars:
        return obj.get_length([x for x in string if x in obj.shuffle])
    return "".join([x for x in string if x in obj.shuffle])




def __similar__(query: str, stack_part: str, return_types=False):
    q_types = IOStries(query).types
    s_types = IOStries(stack_part).types
    equivalent = (q_types["n_lower"] + q_types["n_upper"]) == (s_types["n_upper"] + s_types["n_lower"]) == count_chars(query)
    
    q = count_chars(query, True)
    s  = count_chars(stack_part, True)
    tr = "aeıAEIiİÜUOÖuüoö"
    includes_same_chars = ("".join(sorted(list(set([x for x in count_chars(query.lower(), True)]))))).strip() == ("".join(sorted(list(set([x for x in count_chars(stack_part.lower(), True)]))))).strip()
    vowel_n_consonant = IOStries(query).get_char_types()["vowels"] == IOStries(stack_part).get_char_types()["vowels"] and IOStries(query).get_char_types()["consonant"] == IOStries(stack_part).get_char_types()["consonant"]
    begin_with_vowel = (q[0] in tr and (s[0] in tr)
    begin_with_consonant = not begin_with_vowel
    ends_with_consonant = q not in tr and s not in tr
    ends_with_vowel = not ends_with_consonant
    _ = {"equivalent":0 if not equivalent else 40, "vowel_n_consonant": 0 if not vowel_n_consonant else 20, "begin_with_vowel":0 if not begin_with_vowel else 5, "begin_with_consonant":0 if not begin_with_consonant else 5, "ends_with_consonant":0 if not ends_with_consonant else 5, "ends_with_vowel":0 if not ends_with_vowel else 5, "same_chars_score": 0 if not includes_same_chars else 20 }
    __ = {"percentage":sum([x for x in _.values()]), "equivalent":0 if not equivalent else 1, "vowel_n_consonant": 0 if not vowel_n_consonant else 1, "begin_with_vowel":0 if not begin_with_vowel else 5, "begin_with_consonant":0 if not begin_with_consonant else 1, "ends_with_consonant":0 if not ends_with_consonant else 1, "ends_with_vowel":0 if not ends_with_vowel else 1, "same_chars_score": 0 if not includes_same_chars else 1 }
    if not return_types:
        return sum([x for x in _.values()])
    return __

print(f'Percentage of similarity: {__similar__("helloguys", "HeLlo,,%4+GuYs")}')
