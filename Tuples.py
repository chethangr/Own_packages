import logging


class Tuples:

    try:
        logging.basicConfig (filename="Newlogfile3.log", level=logging.DEBUG, format='%(asctime)s %(levelname)s:'
                                                                                     '%(message)s')

        def __init__(self, t1, v):
            self.t1 = t1
            self.v = v

        def my_count(self, v):
            count = 0
            t = list (self.t1)
            for i in range (len (t)):
                if v == t[i]:
                    count += 1
            return count

        def my_index(self, v):
            t = list (self.t1)
            for i in range (len (t)):
                if v == t[i]:
                    print (i)
                    break
        logging.info ("Tuples function Executed successfully!")

    except Exception as e:
        logging.error ("Didn't execute successfully")
        logging.debug ("Please check the entered value")
        logging.exception ("Exception has occurred: " + str (e))
