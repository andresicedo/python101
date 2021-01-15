file_name = "to_do_list.txt"
with open(file_name, "r") as file_handle:
    contents = file_handle.read()
    print(contents)
