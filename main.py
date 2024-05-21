def main():
    frankenstein_path = 'books/frankenstein.txt'
    text = get_text(frankenstein_path)
    num_words = word_count(text)
    letter_dict = letter_occur(text)
    list_of_dict = dict_to_list_of_dicts(letter_dict)
    list_of_dict.sort(reverse=True, key=sort_on)
    report_print(frankenstein_path, num_words, list_of_dict)
    
def get_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    word_list = text.split()
    return len(word_list)

def letter_occur(text):
    lowered_text = text.lower()
    occur_dict = {}
    for i in lowered_text:
        if i.isalpha():
            if i in occur_dict:
                occur_dict[i] += 1
            else:
                occur_dict[i] = 1
    return occur_dict

def dict_to_list_of_dicts(dict):
    return [{'letter': k, 'count': v} for k, v in dict.items()]

def sort_on(dict):
    return dict['count']

def report_print(path, num_words, list_of_dict):
    print(f'--- Begin report of {path} ---')
    print(f'{num_words} words found in the document')
    for item in list_of_dict:
        print(f'The "{item["letter"]}" character was found {item["count"]} times')
    print('--- End Report ---')

main()
