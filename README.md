## Ledger bookkeeping

Most businesses rely on double entry boookeeping to keep track of their financials. A bank is no exception.
In double entry bookkeeping every income and expense must match, they "balance out". In addition, each expense and income is recorded as part of an "account". Accounts are mostly conceptual, and are used for tracking purposes. For example, banks have an account called "loans receivable" to keep track of all loans given.

Your task is to implement a basic double bookkeeeping ledger from the perspective of a bank. The functionality will focus on loans, and your code needs to be able to

1. Record a loan creation
2. Record loan payments
3. Calculate the remaining balance for a loan
4. Calculate the remaining aggregate balance for all loans (total balance of the account Loans Receivable)

For your convience we have added a file test_ledger.py with a hypothetical interface to test the functionality, and a file ledger.py which is mostly empty.

You have 45 minutes to implement the solution and make the tests pass.

## Follow up questions?
1. How can we model interest rate for the loans
2. What other tests would you add
3. Who should have a ledger