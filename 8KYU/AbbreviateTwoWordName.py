def abbrev_name(name):
    new_list = []
    new_string = ''
    for items in name.split():
        new_list.append(items)
    for names in new_list:
        new_string += names[0]
        print_this = new_string[0] + '.' + new_string[1:]
    return print_this.upper()
