#Simple Signup code using python 
#code by @princeimmanue

class signup:
    def reg(self):
        mail = input("Mail :")
        pwd  = input("password:")
        c_pwd =input("Confirm password :")
        if(pwd == c_pwd):
            print("Signup successfully !")
        else: 
            print("password or entries are invalid !")
access = signup()
access.reg()
        
        
        
            
        