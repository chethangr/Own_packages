import logging


class Dicts:
    try:

        logging.basicConfig (filename="My_Packages.log", level=logging.DEBUG, format='%(asctime)s %(levelname)s:'
                                                                                     '%(message)s')

        def __init__(self, d1):
            self.d1 = d1

        def my_keys(self):
            for i in self.d1:
                print (i)

        def my_values(self):
            for i in self.d1:
                print (self.d1[i])

        def my_clear(self):
            self.d1 = {}
            print(self.d1)

        logging.info (f"Dicts function has  Executed successfully!")

    except Exception as e:
        logging.error ("Didn't execute successfully")
        logging.debug ("Please check the entered value")
        logging.exception ("Exception has occurred: " + str (e))
