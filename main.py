# 1-masala
def filter(filter_list):
    lst = [list for list in filter_list if type(list) == int]
    print(lst)


filter_list = [1, 2, 3, "a", "b", 4]
filter(filter_list)
# 2-masala
# 3-masala
def task_3(list, list2):
    for x in list:
        if 6 < x:
           list2.append(x)
    return list2
print(task_3([7, 4, 17, 14, 12, 3], []))
# 4-masala
def line(next_in_line):
    if not next_in_line:
        print("No list has been selected")
    else:
        next_in_line.pop(0)
        next_in_line.append(xoxlagan_son)
        print(next_in_line)


xoxlagan_son = 1
next_in_line = [5, 6, 7, 8, 9]
line(next_in_line)
# 5-masala
# 6-masala
def clon(klone):
    lst = list(klone)
    lst.append(klone)
    print(lst)


klone = ([1, 1])
clon(klone)
# 7-masala
def integer(return_only_integer):
    lst2 = [list2 for list2 in return_only_integer if type(list2) == int]
    print(lst2)


return_only_integer = [9, 2, "space", "car", "lion", 16]
integer(return_only_integer)
# 8-masala
def chatroom(chatroom_status):
    if not chatroom_status:
        print("no one online")

    elif len(chatroom_status)<2:
        natija3 = " ".join(chatroom_status)
        print(natija3, "online")

    elif len(chatroom_status)<3:
        y = chatroom_status[:1]
        i = chatroom_status[1:]
        natija = ' '.join(i)
        natija2 = ' '.join(y)
        print(f"{natija2} and {natija} online")
        return chatroom_status

    elif len(chatroom_status)>2:
        x1 = chatroom_status[:-5]
        x2 = chatroom_status[1:-4]
        n1 = " ".join(x1)
        n2 = " ".join(x2)
        natija3 = len(chatroom_status)-2
        print(f"{n1}, {n2} and {natija3} more online")


chatroom_status = (["paRIE_to"])
chatroom(chatroom_status)
# 9-masala
# 10-masala