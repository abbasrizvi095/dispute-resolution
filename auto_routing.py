ROUTING_MAP = {
    "Fraud Suspected": "Fraud & Risk",
    "KYC Verification Failed": "Compliance",
    "Transaction Not Authorized": "Transaction Ops",
    "Loan Repayment Issue": "Loan Servicing",
    "Card Not Working": "Card Operations",
    "Account Access Problem": "Customer Support",
    "Fee/Charge Dispute": "Finance",
    "Others": "General Support"
}

def get_routing_team(classification):
    return ROUTING_MAP.get(classification, "General Support")
