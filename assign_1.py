string = input("Enter the string :")
list_string = list(string)
if " " not in list_string:
    new_list = []
    for character in list_string:
        if character not in new_list:
            new_list += character
    for i in new_list:
        print(f"count of {i} is : {list_string.count(i)}")
else:
    new_list=string.split()
    created_list=[]
    for word in new_list:
        if word not in created_list:
            created_list.append(word)
    for i in created_list:
        print(f"count of {i}:{new_list.count(i)}")