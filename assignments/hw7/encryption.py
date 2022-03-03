def encode(msg, key):
    # ordinal list of text input
    lst_txt_ord = []
    for i in msg:
        lst_txt_ord.append(ord(i))

    # unformatted addition of ordinals
    lst_shifted_ord = []
    for i in range(len(lst_txt_ord)):
        lst_shifted_ord.append(lst_txt_ord[i] + key)

    # formats ordinals
    """final_ord_lst = []
    for i in range(len(lst_shifted_ord)):
        conv_ord = lst_shifted_ord[i] % 58
        final_ord_lst.append(conv_ord)"""

    # prepares, returns output
    iter_output = ""
    for i in lst_shifted_ord:
        iter_output += chr(i)
    return iter_output

# whole function ran ONCE
# msg = str input
# key = lst input
def encode_better(msg, key):
        lst_key_ord = []
        # ordinal list of key input
        for i in key:
            lst_key_ord.append(ord(i) - 65)

        lst_txt_ord = []
        # ordinal list of text input
        for i in msg:
            lst_txt_ord.append(ord(i) - 65)

        # unformatted addition of ordinals
        lst_shifted_ord = []
        for i in range(len(lst_txt_ord)):
            lst_shifted_ord.append(lst_txt_ord[i] + lst_key_ord[i])

        # formats ordinals
        final_ord_lst = []
        for i in range(len(lst_shifted_ord)):
            conv_ord = lst_shifted_ord[i] % 58
            final_ord_lst.append(conv_ord)
        # prepares, prints output
        iter_output = ""
        for i in final_ord_lst:
            iter_output += chr(i + 65)
        return iter_output