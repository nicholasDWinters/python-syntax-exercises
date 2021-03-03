my_list = ['blah', 'word', 'this', 'name', 'elephant', 'Ear']


def print_upper_words(list, must_start_with):
    '''take a list of words, and print the uppercased versions of each word on a new line '''
    for word in list:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())


print_upper_words(my_list, {'b', 'n', 'e'})
