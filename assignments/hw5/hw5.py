"""
Name: Brendan Kratt
hw5.py

Problem: This program defines a number of functions using various methods, slicing being
         particularly prominent. All deal with both lists and strings.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def name_reverse():
    first_last = input("enter a name (first last): ")
    list_input = first_last.split(" ")
    last_comma_first = list_input[1] + ", " + list_input[0]
    print(last_comma_first)


def company_name():
    company_input = input("enter a domain: ")
    company_list = company_input.split(".")
    print(company_list[1])


def initials():
    num_students = eval(input("how many students are in the class? "))
    for i in range(num_students):
        concat = "what is the name of student " + str(i) + "? "
        input_name = input(concat)
        split_lst = input_name.split(" ")
        initials_str = split_lst[0][:1] + split_lst[1][:1]
        print(initials_str)


def names():
    str_lst = input("enter a list of names: ")
    real_lst = str_lst.split(", ")
    initials_str = ""
    for i in real_lst:
        iter_lst = i.split(" ")
        initials_str += iter_lst[0][:1] + iter_lst[1][:1] + " "
    print(initials_str)


def thirds():
    num_sentences = eval(input("enter the number of sentences: "))
    builder_str = ""
    for i in range(1, num_sentences + 1):
        concat = "enter sentence " + str(i) + ": "
        curr_sentence = input(concat)
        builder_str += curr_sentence[::3]
    print(builder_str)


def word_average():
    sent_input = input("enter a sentence: ")
    lst_words = sent_input.split(" ")
    avg = 0
    for i in lst_words:
        avg += len(i)
    avg /= len(lst_words)
    print(avg)


def pig_latin():
    sent_input = input("enter a sentence to convert to pig latin: ")
    wrd_lst = sent_input.split(" ")
    pig_lst = []
    for i in wrd_lst:
        pig_lst.append(i[1:] + i[0] + "ay")
    output = " ".join(pig_lst).lower()
    print(output)


if __name__ == '__main__':
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    # pig_latin()
    pass
