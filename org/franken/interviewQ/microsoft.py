# 1.Given an integer, what's the maximum integer you can get by at most 1 swapping of 2 digits?
def max_num(num, is_positive=True):
    num_str = str(num)
    num_list = list(num_str)
    num_length = len(num_list)
    temp = [num, 0]
    if num_length > 1:
        for i in range(1, num_length):
            num_list[0], num_list[i] = num_list[i], num_list[0]
            temp_str = "".join(num_list)
            temp_num = int(temp_str)
            if (is_positive and temp_num > temp[0]) or (not is_positive and temp_num < temp[0]):
                temp[0] = temp_num
                temp[1] = i
            num_list[0], num_list[i] = num_list[i], num_list[0]
        if temp[1] == 0:
            temp_h = (int(num_list[0])) * 10**(num_length-1)
            return temp_h + max_num(num - temp_h, is_positive)
    return temp[0]


def get_max_num(num):
    if num >= 0:
        return max_num(num, True)
    else:
        num_str = str(num)
        num_str = num_str[1:]
        return max_num(int(num_str), False) * -1


def test_get_max_num():
    print("Question: 1.Given an integer, what's the maximum integer you can get by at most 1 swapping of 2 digits?")
    print(str(get_max_num(9219)))
    print(str(get_max_num(2345)))
    print(str(get_max_num(0)))
    print(str(get_max_num(12)))
    print(str(get_max_num(1299)))
    print(str(get_max_num(-1299)))
    print(str(get_max_num(-9219)))
