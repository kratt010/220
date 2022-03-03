"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""
from encryption import encode, encode_better

def number_words(in_file_name, out_file_name):
    in_file = open(in_file_name, "r")
    out_file = open(out_file_name, "w")
    lst_wrds = []
    for i in in_file.readlines():
        lst_wrds.extend(i.split())
    count = 1
    build = ""
    for i in lst_wrds:
        build += str(count) + " " + i
        print(build, file=out_file)
        count += 1
        build = ""


def hourly_wages(in_file_name, out_file_name):
    in_file = open(in_file_name, "r")
    out_file = open(out_file_name, "w")
    lst_inpt = []
    lst_out = []
    for i in in_file.readlines():
        lst_inpt.extend(i.split())
        for g in range(2):  # conv. violation, but what else should we use in nested for loops?
            lst_out.append(lst_inpt[g])
        lst_out.append("{:.2f}".format((float(lst_inpt[2]) + 1.65) * int(lst_inpt[3])))
        print(" ".join(lst_out), file=out_file)
        lst_inpt = []
        lst_out = []


def calc_check_sum(isbn):
    isbn_lst = isbn.split("-")  # splits str into list of strs but without hyphen chr
    isbn_lst = list("".join(isbn_lst))  # joins items back together, now without hyphen chr
    sum_var = 0
    for i in range(0, 11):
        sum_var += int(isbn_lst[-i]) * (i)
    return sum_var


def send_message(file_name, friend_name):
    in_file = open(file_name, "r")
    appnd_txt_name = friend_name + ".txt"
    out_file = open(appnd_txt_name, "w")
    lst_lines = in_file.readlines()
    for i in lst_lines:
        print(i, file=out_file, end="")  # \n chr already included from .readlines()


def send_safe_message(file_name, friend_name, key):
    in_file = open(file_name, "r")
    friend_txt = friend_name + ".txt"
    out_file = open(friend_txt, "w")
    lst_lines_f = in_file.readlines()
    for i in lst_lines_f:
        secure_line = encode(i, key)
        secure_line = secure_line[:-1] # BACKDOOR SOLUTION BECAUSE OF \N CHRS, STRIP LATER
        print(secure_line, file=out_file)


def send_uncrackable_message(file_name, friend_name, pad_file_name):

    in_file = open(file_name, "r")
    str_chrs = "".join(in_file.readlines())

    pad_file = open(pad_file_name, "r")
    key_lst = list(pad_file.readline())

    output = encode_better(str_chrs, key_lst)
    out_file = open(friend_name + ".txt", "w")
    print(output, file=out_file)




if __name__ == '__main__':
    pass
