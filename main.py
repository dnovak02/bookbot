def count_text(text):
    return len(text.split())

def count_letter(text):
    letter_count = {}
    text = text.lower()
    unique_chars = set(text)
    for char in unique_chars:
        if char.isalpha():
            letter_count[char] = text.count(char)
    return letter_count

def create_report(text,filename):
    text_dict=count_letter(text)
    text_count=count_text(text)
    print("--- Begin report of "+filename+" ---")
    print(str(text_count)+"words found in the document")
    char_count_list = list(text_dict.items())
    char_count_list.sort(key=lambda x: x[1], reverse=True)
    for char, count in char_count_list:
        print("The '"+char+"' character was found "+str(count)+" times")
    print("--- End report ---")
        
    
filename="./books/frankenstein.txt"
with open(filename) as f:
    file_contents = f.read()
    print(count_text(file_contents))
    print(count_letter(file_contents))
    create_report(file_contents,filename)
    
