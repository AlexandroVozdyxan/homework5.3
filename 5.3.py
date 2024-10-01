import string


some_text = "hello hello hi g!!o"
string_punctuation = "!@#%^&"

translator = str.maketrans("", "", string_punctuation)
cleand_text = some_text.translate(translator)

hashtag = cleand_text.title()
# print(hashtag)
some_list = hashtag.split()
# print(some_list)
some_str_text = "#".join([str(i) for i in some_list])
# print(some_str_text)
some_text = "#" + some_str_text
# print(some_text)
if len(some_text) > 140:
    some_text1 = some_text[0:141]
    print(some_text1)
else:
    print(some_text)



