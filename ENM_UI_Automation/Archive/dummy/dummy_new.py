# import re
#
# val = input("Enter String: ")
# ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', val )
#
# print(ip)

data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
new_list = []

while data_list:
    minimum = data_list[0]  # arbitrary number in list

    for x in data_list:
        if x < minimum:

            minimum = x
            # print(minimum)
    new_list.append(minimum)
    data_list.remove(minimum)

print(new_list)
