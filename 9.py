def delete_word( string ):
    string = string.replace("się", " ")
    string = string.replace("oraz", " ")
    string = string.replace("nigdy", " ")
    string = string.replace("i", " ")
    string = string.replace("dlaczego", " ")
    return string


exmpl = "dlaczego ja nigdy oraz jestem i co z tego i ja nigdy"
print(delete_word(exmpl))