import logging


class Lists:
    try:

        logging.basicConfig (filename="My_Packages.log", level=logging.DEBUG, format='%(asctime)s %(levelname)s:'
                                                                                     '%(message)s')

        def __init__(self, l1):
            self.l1 = l1

        def l_count(self):
            length = 0
            for i in range (len (self.l1)):
                length += 1
            return length

        def l_clear(self):
            li = self.l1 = []
            return li

        def l_copy(self):
            l2 = input ("Enter the list name to be copied to: ")
            l2 = self.l1
            return l2

        def l_extend(self, l3):
            value_list = list (l3)
            self.l1 += value_list
            return self.l1

        def l_insert(self):
            ind = int (input ("Enter the index: "))
            value = eval (input ("Enter the value: "))
            self.l1[ind] = value
            return self.l1

        def l_index(self):
            value = eval (input ("Enter the item: "))
            for i in range (len (self.l1)):
                if value not in self.l1:
                    return "Please enter a valid item"
                    break
                elif self.l1[i] == value:
                    print (i)

        def l_reverse(self):
            value_list = self.l1[::-1]
            return value_list

        def l_append(self):
            value = eval (input ("Enter the item: "))
            # value_list = list(value)
            self.l1[len (self.l1)] = value
            return self.l1

        def l_remove(self):
            value = eval (input ("Enter the item: "))
            for i in range (len (self.l1)):
                if value not in self.l1:
                    return "Please enter a valid item"
                    break
                elif self.l1[i] == value:
                    self.l1[i] = ''
        logging.info (f"Lists function has  Executed successfully!")

    except Exception as e:
        logging.error ("Didn't execute successfully")
        logging.debug ("Please check the entered value")
        logging.exception ("Exception has occurred: " + str (e))
