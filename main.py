def main():
    path_to_book = './books/frankenstein.txt'
    frankenstein = openBook(path_to_book)
    frankensteinSplit = frankenstein.split()
    print(f"number of words: {len(frankensteinSplit)}")
    num_char_list_sorted = numberOfCharacters(frankenstein)
    for i in num_char_list_sorted:
        print(f"The {i['char']} character was found: {i['num']} times")

def openBook(path_to_book):
    with open(path_to_book) as f:
        return f.read()
    
def numberOfCharacters(text):
    char_list = []
    for i in text:
        char_lower = i.lower()
        if char_lower.isalpha():
            char_dict = checkCharList(char_lower, char_list)
            if char_dict:
                char_dict["num"] += 1
            else:
                char_dict["num"] = 1
                char_dict["char"] = char_lower
                char_list.append(char_dict)
    
    char_list.sort(reverse=True, key=sort_on)

    return char_list

def checkCharList(char, char_list):
    for dict in char_list:
        if dict["char"] == char:
            return dict
    return {}

def sort_on(char_dict):
    return char_dict['num']

main()