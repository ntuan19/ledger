from collections import defaultdict
class Transaction():
    def __init__(self,from_account,to_account,amount,transaction_type) -> None:
        self.from_account = from_account
        self.to_account = to_account
        self.amount = amount
        self.transaction_type = transaction_type


class Ledger(object):
    def __init__(self,transactions):
        self.accounts_names = defaultdict(int)
        self.transactions = transactions

    def execute_transactions(self):
        for transaction in self.transactions:

            payer = transaction.from_account
            receiver = transaction.to_account
            total_amount  = transaction.amount
            type_transaction = transaction.transaction_type

            # if from_account not in self.accounts_names:
            #     self.accounts_names[from_account]
            # if to_account not in self.accounts_names:
            #     self.accounts_names[to_account]
            
            if type_transaction == "LOAN_PAYMENT":
                self.accounts_names[payer] -= total_amount
                self.accounts_names[receiver] += total_amount
            elif type_transaction == "CREATE_LOAN":
                self.accounts_names[payer] -= total_amount
                self.accounts_names[receiver] += total_amount
    
    def get_loan_receivable(self,account):
        if account not in self.accounts_names:
             return "Not found"
        return self.accounts_names[account]
    
    def get_loans_receivable_balance(self):
        total_loan = 0
        for value in self.accounts_names.values():
            if value <0:
                total_loan -=value
        return total_loan


    
            
            

  
    




        
