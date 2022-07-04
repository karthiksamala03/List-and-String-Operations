"""#Questions
l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]
1 . Try to reverse a list
2.  Try to access 234 out of this list
3 . Try to access 456
4 . Try to extract only a list collection form list l
5 . Try to extract "sudh"
6 . Try to list all the key in dict element avaible in list
7 . Try to extract all the value element form dict available in list
"""
import logging
import log.log_file

class List_Operations():
    """Different list Operations"""
    def __init__(self, list_var):
        self.list_var = list_var

    def reverse_list(self):
        """Reversing the list"""
        try:
            logging.info("Reversing the list ")
            return self.list_var[::-1]
        except Exception as e:
            logging.exception(e)

    def extract_dict(self):
        """Extracting dictionary from the list"""
        try:
            logging.info("Extracting dict from the list")
            dict_items = []
            for i in self.list_var:
                if type(i) == dict:
                    logging.info(f"dict --> {i}")
                    dict_items.append(i)
            return dict_items
        except Exception as e:
            logging.exception(e)

    def extract_keys(self):
        """Extracting dictionary keys from the list"""
        try:
            logging.info("Extracting dict keys from the list")
            dict_keys = []
            for i in self.list_var:
                if type(i) == dict:
                    logging.info(f"dict --> {i}")
                    dict_keys.append(i.keys())
            return dict_keys
        except Exception as e:
            logging.exception(e)

    def extract_values(self):
        """Extracting dictionary values from the list"""
        try:
            logging.info("Extracting dictionary values from the list")
            dict_values = []
            for i in self.list_var:
                if type(i) == dict:
                    logging.info(f"dict --> {i}")
                    dict_values.append(i.values())
            return dict_values
        except Exception as e:
            logging.exception(e)

    def extract_list(self):
        """Extracting lists from the list"""
        try:
            logging.info("Extracting lists from the list")
            list1= []
            for i in self.list_var:
                if type(i) == list:
                    logging.info(f"list --> {i}")
                    list1.append(i)
            return list1
        except Exception as e:
            logging.exception(e)

    def extract_tuple(self):
        """Extracting tuple from the list"""
        try:
            logging.info("Extracting tuple from the list")
            tuplee= []
            for i in self.list_var:
                if type(i) == tuple:
                    logging.info(f"tuple --> {i}")
                    tuplee.append(i)
            return tuplee
        except Exception as e:
            logging.exception(e)

    def extract_numeric(self):
        """extract all numeric data"""
        try :
            logging.info("extract all numeric data")
            q6 = []
            for i in self.list_var:
                if type(i) == int:
                    q6.append(i)
                if type(i) == tuple or type(i) == list or type(i) == set:
                    for j in i:
                        if type(j) == int or type(j) == float:
                            q6.append(j)
                if type(i) == dict:
                    for k, v in i.items():
                        if type(k) == int or type(k) == float:
                            q6.append(k)
                        if type(v) == int or type(v) == float:
                            q6.append(v)
            logging.info(f"Numeric values --> {q6}")
            return q6
        except Exception as e:
            logging.exception(e)

    def sum_numeric(self):
        """SUm of numeric data"""
        try:
            logging.info("Summing up numerical data")
            numerics = self.extract_numeric()
            total = sum(numerics)
            logging.info(f" Sum of numeric values = {total}")
            return total
        except Exception as e:
            logging.exception(e)

    def extract_string(self):
        """Extracting string from the list"""
        try:
            logging.info("Extracting string from the list")
            stringg = []
            for i in self.list_var:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        logging.info(f"string --> {j}")
                        if j == str:
                            logging.info(f"string --> {j}")
                            stringg.append(j)
                elif type(i) == dict:
                    for k, v in i.items():
                        if k == str:
                            logging.info(f"string --> {k}")
                            stringg.append(k)
                        if v == str:
                            logging.info(f"string --> {v}")
                            stringg.append(v)
                elif type(i) == str:
                    logging.info(f"string --> {i}")
                    stringg.append(i)
            return stringg
        except Exception as e:
            logging.exception(e)
