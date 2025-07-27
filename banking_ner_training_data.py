# cleaned_banking_ner_training_data.py

TRAIN_DATA = [
    ("₹2500 withdrawn from ATM at HDFC Bank, Connaught Place.", {"entities": [(0, 6, "AMOUNT"), (26, 35, "BANK"), (37, 53, "LOCATION")]}),
    ("The transaction on 5th June failed due to insufficient funds.", {"entities": [(21, 30, "DATE")]}),
    ("Payment of ₹900 via UPI to Swiggy was declined.", {"entities": [(11, 16, "AMOUNT"), (21, 24, "CHANNEL"), (28, 34, "MERCHANT")]}),
    ("Received ₹5000 through NEFT from Axis Bank.", {"entities": [(9, 15, "AMOUNT"), (24, 28, "CHANNEL"), (34, 43, "BANK")]}),
    ("₹1200 was double charged on my credit card ending 2345.", {"entities": [(0, 6, "AMOUNT"), (47, 51, "CARD_NO")]}),
    ("IMPS transaction of ₹3000 to BigBasket on 10th May failed.", {"entities": [(20, 26, "AMOUNT"), (30, 39, "MERCHANT"), (43, 52, "DATE")]}),
    ("Loan EMI of ₹8000 was auto-debited on 1st July.", {"entities": [(12, 18, "AMOUNT"), (41, 49, "DATE")]}),
    ("My debit card ending 1122 was blocked after failed PIN attempts.", {"entities": [(23, 27, "CARD_NO")]}),
    ("Transaction at Amazon was not authorized by me.", {"entities": [(15, 21, "MERCHANT")]}),
    ("₹750 refund from Myntra has not been received.", {"entities": [(0, 5, "AMOUNT"), (19, 25, "MERCHANT")]}),
    ("KYC verification failed for my account last week.", {"entities": [(41, 50, "DATE")]}),
    ("The NEFT sent to LIC Housing did not process.", {"entities": [(4, 8, "CHANNEL"), (17, 28, "MERCHANT")]}),
    ("No OTP received for ₹4500 transaction on my ICICI card.", {"entities": [(20, 26, "AMOUNT"), (45, 50, "BANK")]}),
    ("₹200 was charged as a convenience fee on IRCTC.", {"entities": [(0, 5, "AMOUNT"), (42, 47, "MERCHANT")]}),
    ("PhonePe UPI transfer of ₹9000 to JioMart failed.", {"entities": [(0, 7, "CHANNEL"), (26, 32, "AMOUNT"), (36, 43, "MERCHANT")]}),
]

