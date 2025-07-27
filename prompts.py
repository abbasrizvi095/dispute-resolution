# prompts.py

DISPUTE_PROMPT = """
Given the following customer dispute, perform three tasks:

1. Classify the issue based on type.
2. Suggest a resolution path an internal banking team might take.
3. Generate a 2-3 line internal summary for compliance/legal use.

Use the following format:
Classification: <type>
Suggested Resolution: <steps>
Internal Summary: <short summary>

Dispute Text:
"""
{dispute_text}
"""

Common dispute categories you can consider:
- Payment Delay
- Transaction Not Authorized
- KYC Verification Failed
- Loan Repayment Issue
- Account Access Problem
- Card Not Working
- Fraud Suspected
- Fee/Charge Dispute
- UPI/NEFT/IMPS Failure
- Others
