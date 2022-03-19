class Account:
    def __init__(self):
        self.bank = ""
        self.account_number=0
        self.deposit=0

    def get_bank_name():
        pass
    def set_bank_name():
        pass
    
    def get_account_number():
        pass
    def set_account_number():
        pass

    def get_deposit():
        pass
    def set_deposit():
        pass
        
class User_Info(Account):
    def __init__(self):
        self.user_id=""
        self.user_pw=""
        self.user_account_list=[]
        self.user_deposit=0

    def set_user_id(user_id):
        self.user_id = user_id
    def get_user_id():
        return self.user_id

    def set_user_pw(user_pw):
        self.user_pw = user_pw
        
    def get_user_pw():
        return self.user_pw

    
class Bank_Server:
    def __init__(self):
        self.server_url=""
        self.server_certificates=None

    def connect(user_pw):
        pass

    def is_connect():
        pass

    def disconnect():
        pass


    
class ATM(Bank_Server,User_Info):
    def __init__(self):
        self.super()
        self.ATM_deposit=0
        self.server=None
        self.user_pw=""

    def check_card_inserted():
        pass

    def check_user_pw():
        pass

    # check pin number
    def validate_user(user_id, user_pw):
        if(server==None):
            print("Errror")

    def update_user_info(server, user_pw):
        pass

    def user_input(account_to_select):
        pass
    
    
    def check_enough_cash_in_ATM(withdraw_money):
        if withdraw_money < ATM_deposit:
            return True
        else:
            return False

    def User_input(order):
        if order == withdraw:
            pass
        elif order == save_deposit:
            pass
        elif order == show_balance:
            pass
        


if __name__ == "__main__":
    print("Helloworld")
    
