from ledger import Ledger, Transaction

def test_ledger_balance_loan():
    memberA = "memberA"
    loanA = "loanA"

    ledger = Ledger([
        Transaction(
            from_account=loanA,
            to_account=memberA,
            amount=100,
            transaction_type="CREATE_LOAN"
        ),
        Transaction(
            from_account=memberA,
            to_account=loanA,
            amount=10,
            transaction_type="LOAN_PAYMENT"
        ),
        Transaction(
            from_account=memberA,
            to_account=loanA,
            amount=90,
            transaction_type="LOAN_PAYMENT"
        )
    ])
    ledger.execute_transactions()
    assert ledger.get_loan_receivable(loanA) == 0


def test_total_debt():
    memberA = "memberA"
    loanA = "loanA"
    loanB = "loanB"
    loanC = "loanC"
    ledger = Ledger([
        Transaction(
            from_account=loanA,
            to_account=memberA,
            amount=100,
            transaction_type="CREATE_LOAN"
        ),
        Transaction(
            from_account=loanB,
            to_account=memberA,
            amount=300,
            transaction_type="CREATE_LOAN"
        ),
        Transaction(
            from_account=loanC,
            to_account=memberA,
            amount=400,
            transaction_type="CREATE_LOAN"
        ),
    ])
    ledger.execute_transactions()
    assert ledger.get_loans_receivable_balance() == 800


if __name__=="__main__":
    test_ledger_balance_loan()
    test_total_debt()