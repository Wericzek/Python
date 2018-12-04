def replace_word(string):


    string = string.replace("nigdy", "prawie nigdy ")
    string = string.replace("i", "ii")
    string = string.replace("oraz", "i")
    string = string.replace("iiiiiiiii", "oraz")
    string = string.replace("dlaczego", "czemu")
    return string


exampl = "dlaczego ja nigdy oraz jestem i oraz i ja nigdy czemu dlaczego "
print(replace_word(exampl))