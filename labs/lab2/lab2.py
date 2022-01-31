"""
1.  What will the program do?
    The program will calculate three different kinds of means: rms, harmonic, and geometric.
2. What will be the inputs and outputs?
    The user will input the n number of times to ask for input,
    then will input n number of values after being prompted.
3. Ask for the number of inputs, accept that n number of inputs, run through a loop n number of times,
   redefine each variable according to the iterative portion of the mathematical operation, and then
   finish with the non-iterative portion outside the loop. Finally, print the output.
"""
rms_iter = 0  # Value solely redefined using addition, ergo starting value == 0
harmonic_iter = 0  # Value solely redefined using addition, ergo starting value == 0
geo_iter = 1  # Value solely redefined using multiplication, ergo starting value == 1
num_values = eval(input("enter the values to be entered: "))

for i in range(num_values):
    curr_input = eval(input("enter value: "))
    rms_iter += curr_input ** 2
    harmonic_iter += 1 / curr_input
    geo_iter *= curr_input

# Broken up for readability
rms_average = round((rms_iter / num_values) ** (1/2), 3)  # average == (iterated / n)^2
harmonic_mean = round(num_values / harmonic_iter, 3)  # average == n / iterated
geometric_mean = round(geo_iter ** (1/num_values), 3)  # average == nth root of iterated
print(rms_average)
print(harmonic_mean)
print(geometric_mean)

