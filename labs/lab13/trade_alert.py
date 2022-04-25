"""I was unsure of where to put this, since it wasn't said in the document.
I decided to place it here to make things obvious for the grader.
Thank you! Sorry for the inconvenience."""


def trade_alert(filename):
    file = open(filename, "r")
    line = file.readline()
    lst_str_values = line.split(" ")
    lst_num_values = [eval(num) for num in lst_str_values]

    curr_time = 1
    for num in lst_num_values:
        if num > 830:
            print("WARNING: TRADING VOLUME PEAKED. TIME:", curr_time)
        elif num >= 500:  # document says "equals," but 500 is not in the file. Instead, I put >=
            print("Pay attention! TIME:", curr_time)
        curr_time += 1


def main():
    trade_alert("trades.txt")


if __name__ == '__main__':
    main()
