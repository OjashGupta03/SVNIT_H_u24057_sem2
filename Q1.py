class Password_manager:
    
    def __init__(self,old_password=[]):
        self.old_password=old_password
    
    def get_password(self):
        return self.old_password[-1]
    
    def set_password(self,new_password):
        if new_password not in self.old_password:
            self.old_password.append(new_password)
        else: 
            print("cannot use previously used password")
            print("try other:",end="")
            self.set_password(input())
    
    def is_correct(self,string):
        return  "correct password" if self.old_password[len(self.old_password)-1]==string else "incorrect passwword"

my_password=Password_manager(["raze main","10102"])
print("current password:",end="")
print(my_password.get_password())
my_password.set_password(input("Enter new password:"))
print("current password:",end="")
print(my_password.get_password())
print(my_password.is_correct(input("Check Password:")))
print(my_password.is_correct(input("Check Password:")))



