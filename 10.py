def replace_word(word):


    word = word.replace("nigdy", "prawie nigdy ")
    word = word.replace("i", "ii")
    word = word.replace("oraz", "i")
    word = word.replace("iiiiiiiii", "oraz")
    word = word.replace("dlaczego", "czemu")
    return word


exampl = "dlaczego ja nigdy oraz jestem i oraz i ja nigdy czemu dlaczego "
print(replace_word(exampl))