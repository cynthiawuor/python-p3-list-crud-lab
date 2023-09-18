def create_an_empty_list():
    return []

def create_a_list():
    my_list = [4, 'apple', True, 3.14]
    return my_list

def add_element_to_end_of_list(l, element):
    l.append(element)
    return l  

def add_element_to_start_of_list(l, element):
    l.insert(0, element)  
    return l

def remove_element_from_end_of_list(l):
    if len(l) > 0:
        l.pop() 
    return l

def remove_element_from_start_of_list(l):
   if len(l) > 0:
    del l[0]  
    return l

def retrieve_first_element_from_list(l):
    if len(l) > 0:  
        return l[0] 
    else:
     return None

def retrieve_element_from_index(l, index):
    if 0 <= index < len(l):
        return l[index]  # Return the element at the specified index
    else:
     return None

def retrieve_last_element_from_list(l):
    if len(l) > 0:
        return l[-1]  # Return the last element using index -1
    else:
     return None
