class Account:
    def __init__(self,name,age,password,acc_no):
        self.name = name
        self.age = age
        self.__password = password
        self.__balance = 0
        self.acc_no = acc_no
    
    def update_password(self,acc_no,new_password):
        if self.acc_no ==acc_no:
            self.__password = new_password
        
    def show_password(self,acc_no):
        if self.acc_no ==acc_no:
            print(self.__password)




gaurav = Account("Gaurav",10,12345,12345678)
print("password before updating",end=" ")
gaurav.show_password(12345678)
gaurav.update_password(12345678,55555)
print("password after updating",end=" ")
gaurav.show_password(12345678)