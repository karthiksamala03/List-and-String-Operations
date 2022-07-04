
from String import String_Operations
from list import List_Operations
import logging
import log.log_file

def print_hi(name):
    print(f'Hi, {name}')

if __name__ == '__main__':
    print_hi('Karthik')
    logging.info("creating a new string")
    name = String_Operations("usha Mullapudi Cardiac Centre")

###############  String_Operations  ######################

    logging.info("String operations")
    new_name = name.replace('e', 'a')
    print("\n\nReplaced name")
    print(new_name)
    print("\n\nComponents in name ")
    print(name.split_up())
    print("\n\nCapitalizing the name")
    print(name.caps())
    print("\n\nreversing the name")
    print(name.reverse())
    print("\n\nslicing the name")
    print(name.slice(2, 5, 1))
    print("\n\nconvert to lower case")
    print(name.lower())

###############  List_Operations  ######################

    l = List_Operations([3, 4, 5, 6, 7, [23, 456, 67, 8, 78, 78], [345, 56, 87, 8, 98, 9], (234, 6657, 6),
                              {"key1": "sudh", 234: [23, 45, 656]}])
    logging.info(f"created a list l {l}")
    logging.info("data operations")
    print("\nExtract List")
    print(l.extract_list())
    print("\nExtract Numeric")
    print(l.extract_numeric())
    print("\nExtract values from dict")
    print(l.extract_values())
    # print("\nExtract string")
    # print(l.extract_string("ineuron"))
    print("\nExtract Dict")
    print(l.extract_dict())
    print("\nExtract keys from dict")
    print(l.extract_keys())
    # print("\nExtract odd numbers from list")
    # print(l.extract_list_odd())
    print("\nExtract tuples")
    print(l.extract_tuple())
    # print("\nExtract occurrences of all items")
    # print(l.occurrences_all())
    print("\nReverse list")
    print(l.reverse_list())
    print("\nSum of Numeric")
    print(l.sum_numeric())