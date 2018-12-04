def delete_word( string ):
    string = string.replace("się", " ")
    string = string.replace("oraz", " ")
    string = string.replace("nigdy", " ")
    string = string.replace("i", " ")
    string = string.replace("dlaczego", " ")
    return string


exampl = "dlaczego ja nigdy oraz jestem i klkl i ja nigdy"
print(delete_word(exampl))