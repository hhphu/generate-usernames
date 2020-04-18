#!/bin/python3

import sys

def generate_username(fullname):
    name = fullname.lower().split(' ')
    username_list = [name[0]]                                                       # username= Firstname                   (james)
    username_list.append(name[1])                                                   # username= Lastname                    (bond)
    username_list.append(first_dot_last(name))                                      # username= Firstname.Lastname          (james.bond)
    username_list.append(first_last(name))                                          # username= FirstnameLastname           (jamesbond)
    username_list.append(f_last(name))                                              # username= FLastname                   (jbond)
    username_list.append(f_dot_last(name))                                          # username= F.Lastname                  (j.bond)
    username_list.append(first_l(name))                                             # username= FirstL                      (jamesb)
    username_list.append(first_dot_l(name))                                        # username= Firstname.L                 (james.b)

    #print (first_name + " " + last_name)
    #username_list = [first_name.join(last_name)]
    #username_list.append((first_name.join(".")).join(last_name))
    return username_list

def first_dot_last (sublist):
    first_name=sublist[0]
    last_name=sublist[1]
    return ''.join([first_name,'.',last_name])

def first_last (sublist):
    first_name=sublist[0]
    last_name=sublist[1]
    return ''.join([first_name,last_name])

def f_last (sublist):
    first_name=sublist[0]
    last_name=sublist[1]
    return ''.join([first_name[0],last_name])   

def f_dot_last (sublist):
    first_name=sublist[0]
    last_name=sublist[1]
    return ''.join([first_name[0],'.',last_name])

def first_l (sublist):
    first_name=sublist[0]
    last_name=sublist[1]
    return ''.join([first_name,last_name[0]])

def first_dot_l (sublist):
    first_name=sublist[0]
    last_name=sublist[1]
    return ''.join([first_name,'.',last_name[0]])

if __name__ == "__main__":
    
    # Read the file from the
    name_list= open(str(sys.argv[1]),"r")
    name_list_text=name_list.read()

    f = open("users.txt","w+")

    # put the names into a list
    individual_name_list = name_list_text.split('\n')                    # put the names into a list
    individual_name_list.pop()                                           # remove the last index of the list, which is ''

    for fn in individual_name_list:                                      #fn is short for fullname
        temp_list = generate_username(fn)
        for username in temp_list:
            f.write(username + '\n')
        
    # close files
    name_list.close()
    f.close()


