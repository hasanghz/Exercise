class Customer:
    def __init__(self,fname,lname,tel):
          self.fname=fname
          self.lname=lname
          self.tel=tel

    def __del__(self):
        print('object is deleted')

    def __str__(self):
         s=f'Customer name is {self.fname} {self.lname}\n'
         s+=f'Customer phone number is {self.tel}'
         return s
    def __repr__(self):
         return self.__str__()
    



