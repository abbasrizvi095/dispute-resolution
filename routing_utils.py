# routing_utils.py

def get_routing_team(classification: str) -> str:
    routing_map = {
        "Payment Delay": "Payments Operations Team",
        "Transaction Not Authorized": "Fraud Investigation Unit",
        "KYC Verification Failed": "Compliance Team",
        "Loan Repayment Issue": "Lending Support",
        "Account Access Problem": "Digital Support",
        "Card Not Working": "Card Services",
        "Fraud Suspected": "Fraud Investigation Unit",
        "Fee/Charge Dispute": "Billing Support",
        "UPI/NEFT/IMPS Failure": "Payments Operations Team",
        "Others": "General Support"
    }
    return routing_map.get(classification, "General Support")
