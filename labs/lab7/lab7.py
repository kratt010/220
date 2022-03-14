# input: firstName lastName: w1 g1 w2 g2
# Billy Bother: 20 89 30 94 50 82
def weighted_average(in_file_name, out_file_name):
    # opens files, reads line, global variables
    file_in = open(in_file_name, "r")
    file_out = open(out_file_name, "w")
    lst_of_lst = file_in.readlines()
    final_output_lst = []
    class_avg_lst = []

    # loops over each line from file_in
    for i in lst_of_lst:
        output_str = ""
        lst_build = i.strip("\n") # strips newline characters
        lst_build = lst_build.split(": ") # splits list in half, name and then numbers
        output_str += (lst_build[0] + "'s average:")  # prepares output: First Last's average
        lst_grades_weight = lst_build[1].split(" ")  # isolate grades and weight into separate list

        lst_weight = []
        lst_grade = []
        count = 1  # since iterating over list objects, count variable necessary
        for i in lst_grades_weight:
            if count % 2 == 0:
                lst_grade.append(int(i))  # isolates list of grades
            elif count % 2 == 1:
                lst_weight.append(int(i))  # isolates list of weight
            count += 1

        if sum(lst_weight) > 100:
            student_value_term = "Error: The weights are more than 100."
        elif sum(lst_weight) < 100:
            student_value_term = "Error: The weights are less than 100."
        else:
            iter_sum = 0 # baseline sum value
            for g in range(len(lst_weight)):
                iter_mult = lst_weight[g] * lst_grade[g]  # grade * test
                iter_sum += iter_mult
            student_avg = iter_sum / 100
            student_value_term = student_avg
            class_avg_lst.append(student_avg)

        output_str += " " + str(student_value_term)  # adds space, score after firstName lastNAme
        final_output_lst.append(output_str)

    class_avg = sum(class_avg_lst) / len(class_avg_lst)
    final_output_lst.append("Class average: " + str(class_avg))
    for i in final_output_lst:
        print(i, file=file_out)


weighted_average("grades.txt", "avg.txt")


if __name__ == '__main__':
    pass
