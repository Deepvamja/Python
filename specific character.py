char_list = ["a", "b" ,"c"]
string = "abcd"
matched_list = [characters in char_list for characters in string]
print(matched_list)
OUTPUT
[True, True, True, False]
string_contains_chars = all(matched_list)
print(string_contains_chars)