def call_by_val(x):
    x = x * 2
    return x


def call_by_ref(b):
    b.append("D")
    return b


a = ["E"]
num = 6

# Call functions
updated_num = call_by_val(num)
updated_list = call_by_ref(a)

# Print after function calls
print("Updated value after call_by_val:", updated_num)
print("Updated list after call_by_ref:", updated_list)
