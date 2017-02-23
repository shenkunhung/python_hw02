def SD(input_list):
    N = len(input_list)
    def mean_of_input(input_list):
        sum_of_input = 0
        for i in input_list:
            sum_of_input += i
        return sum_of_input/N
    
    def sum_of_squared_diff(input_list):
        sum_of_squared_diff = 0
        for i in input_list:
            sum_of_squared_diff += (i-mean_of_input(input_list))**2
        return sum_of_squared_diff
    
    return (sum_of_squared_diff(input_list)/N)**(1/2)

X = [13,23,12,44,55]
print(SD(X))
