DSTV SUBSCRIPTION MANAGEMENT SYSTEM  
# ======================================================  
# Student Name   : OGUNYEMI KOREDE HABEEB  
# Matric Number  : 25/18843  
# Course         : SEN 201  
# Description    : This program manages DSTV subscription  
#                  details and determines subscription status  
# ======================================================  
  
  
# ------------------------------------------------------  
# Function: get_customer_details  
# Purpose : Collects customer and subscription information  
# ------------------------------------------------------  
def get_customer_details():  
    customer_name = "OGUNYEMI KOREDE HABEEB"  
    matric_number = "25/18843"  
    smart_card_number = "DSTV-90214567"  
  
    print("===== DSTV SUBSCRIPTION INPUT =====")  
    print("Customer Name:", customer_name)  
    print("Matric Number:", matric_number)  
    print("Smart Card Number:", smart_card_number)  
  
    amount_paid = int(input("Enter amount paid for subscription (₦): "))  
    return customer_name, matric_number, smart_card_number, amount_paid  
  
  
# ------------------------------------------------------  
# Function: select_package  
# Purpose : Determines DSTV package based on amount paid  
# ------------------------------------------------------  
def select_package(amount_paid):  
    if amount_paid >= 25000:  
        return "Premium Package"  
    elif amount_paid >= 14000:  
        return "Compact Plus Package"  
    elif amount_paid >= 9000:  
        return "Compact Package"  
    elif amount_paid >= 5000:  
        return "Family Package"  
    else:  
        return "No Valid Package"  
  
  
# ------------------------------------------------------  
# Function: check_subscription_status  
# Purpose : Checks whether subscription is active or inactive  
# ------------------------------------------------------  
def check_subscription_status(amount_paid):  
    if amount_paid >= 5000:  
        return "Active"  
    else:  
        return "Inactive"  
  
  
# ------------------------------------------------------  
# Function: calculate_bonus_days  
# Purpose : Calculates bonus days based on payment  
# ------------------------------------------------------  
def calculate_bonus_days(amount_paid):  
    if amount_paid >= 25000:  
        return 7  
    elif amount_paid >= 14000:  
        return 5  
    elif amount_paid >= 9000:  
        return 3  
    else:  
        return 0  
  
  
# ------------------------------------------------------  
# Function: display_subscription_details  
# Purpose : Displays all DSTV subscription information  
# ------------------------------------------------------  
def display_subscription_details(customer_name, matric_number,  
                                 smart_card_number, amount_paid,  
                                 package, status, bonus_days):  
  
    print("\n========== DSTV SUBSCRIPTION DETAILS ==========")  
    print("Customer Name        :", customer_name)  
    print("Matric Number        :", matric_number)  
    print("Smart Card Number    :", smart_card_number)  
    print("Amount Paid          : ₦", amount_paid)  
    print("DSTV Package         :", package)  
    print("Subscription Status  :", status)  
    print("Bonus Days Awarded   :", bonus_days)  
    print("================================================")  
  
  
# ------------------------------------------------------  
# Function: display_conclusion  
# Purpose : Displays final message to the customer  
# ------------------------------------------------------  
def display_conclusion(status):  
    if status == "Active":  
        print("\nThank you for subscribing to DSTV.")  
        print("Enjoy uninterrupted entertainment!")  
    else:  
        print("\nSubscription inactive.")  
        print("Please recharge to enjoy DSTV services.")  
  
  
# ------------------------------------------------------  
# MAIN PROGRAM EXECUTION  
# ------------------------------------------------------  
def main():  
    customer_name, matric_number, smart_card_number, amount_paid = get_customer_details()  
  
    package = select_package(amount_paid)  
    status = check_subscription_status(amount_paid)  
    bonus_days = calculate_bonus_days(amount_paid)  
  
    display_subscription_details(  
        customer_name,  
        matric_number,  
        smart_card_number,  
        amount_paid,  
        package,  
        status,  
        bonus_days  
    )  
  
    display_conclusion(status)  
  
  
# Run the program  
main()  
