def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

this = "        Akshu is a good boy        "
n = remove_and_split(this, "Akshu")
print(n)
