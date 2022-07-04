"""
String class to implement following string operations:
    replacing some character with another
    capitalize the string
    convert the string to lower case
    Split the string after converting to uppercase
    Slice the string
    reverse the string
"""
import logging
import log.log_file

class String_Operations():
    """Different String Operations"""
    def __init__(self, str_var):
        self.str_var = str_var

    def replace(self, old, new):
        """Replacing old data with new data"""
        try:
            logging.info(f'replacing the cahracter {old} with {new}')
            return self.str_var.replace(old,new)
        except Exception as e:
            logging.exception(e)

    def caps(self):
        """Capitalizing the string"""
        try:
            logging.info("Capitalizing the String")
            return self.str_var.capitalize()
        except Exception as e:
            logging.exception(e)

    def lower(self):
        """converting string to lowerr case"""
        try:
            logging.info(f"Converting {self.str_var} to lower case")
            return self.str_var.lower()
        except Exception as e:
            logging.exception(e)

    def split_up(self, ch=' '):
        """Spliting the string after converting into lower case"""
        try:
            logging.info(f"Spliting the string {self.str_var} after converting into upper case")
            return self.str_var.upper().split(ch)
        except Exception as e:
            logging.exception(e)

    def slice(self,start, end, step):
        """Slicing the string"""
        try:
            logging.info("slicing the string")
            return self.str_var[start:end:step]
        except Exception as e:
            logging.exception(e)

    def reverse(self):
        """Reversing the string"""
        try:
            logging.info("reversing the string")
            return self.str_var[::-1]
        except Exception as e:
            logging.exception(e)
