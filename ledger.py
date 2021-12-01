class Ledger(object):
    def __init__(self,transactions):
        self.transactions = transactions
        self.balances = {}
        self.receivable_loans= 0

    def execute_transactions(self):
        self.balances = {}
        for transaction in self.transactions:
            amount = transaction.amount
            if transaction.from_account in self.balances:
                if transaction.transaction_type == "CREATE_LOAN":
                    self.balances[transaction.from_account] += amount
                elif transaction.transaction_type == "LOAN_PAYMENT":
                    self.balances[transaction.from_account] -= amount
            else:
                self.balances[transaction.from_account] = 0
    
    def get_loan_receivable(self,loan_name):
        balances = self.balances
        if loan_name in balances:
            return balances[loan_name]
        else:
            return "None"
    
    def get_loans_receivable_balance(self):
        for transaction in self.transactions:
            amount = transaction.amount
            if transaction.transaction_type == "CREATE_LOAN":
                self.receivable_loans+=amount
        return self.receivable_loans
           

        



class Transaction(object):
    def __init__(self,from_account, to_account,amount,transaction_type):
        self.from_account = from_account
        self.to_account = to_account
        self.amount = amount
        self.transaction_type = transaction_type
        
