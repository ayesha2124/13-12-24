import streamlit as st

st.title("ATM Machine")


class Bank:
    def __init__(self):
        self.acc_bal = 10000
        self.deposit_count = 0
        self.withdrawal_count = 0

    def deposit(self, amount):
        if self.deposit_count >= 3:
            return "Deposit transaction limit reached. You can only perform 3 deposits."
        if amount < 100:
            return "Deposit amount must be at least 100."
        elif amount > 50000:
            return "Deposit amount cannot exceed 50,000."
        elif amount % 100 != 0:
            return "Deposit amount must be a multiple of 100."
        else:
            self.acc_bal += amount
            self.deposit_count += 1
            return f"Successfully deposited {amount}. New balance: {self.acc_bal}"

    def withdraw(self, amount):
        if self.withdrawal_count >= 3:
            return "Withdrawal transaction limit reached. You can only perform 3 withdrawals."
        if amount < 100:
            return "Withdrawal amount must be at least 100."
        elif amount > 20000:
            return "Withdrawal amount cannot exceed 20,000."
        elif amount % 100 != 0:
            return "Withdrawal amount must be a multiple of 100."
        elif amount > (self.acc_bal - 500):
            return "You must maintain a minimum balance of 500."
        elif amount <= self.acc_bal:
            self.acc_bal -= amount
            self.withdrawal_count += 1
            return f"Successfully withdrew {amount}. New balance: {self.acc_bal}"
        else:
            return "Insufficient balance."

    def tot_balance(self):
        return f"Your current balance is: {self.acc_bal}"

    def validate_pin(self, pin):
        if pin == 1234:
            return True
        return False


obj = Bank()


if 'pin_attempts' not in st.session_state:
    st.session_state.pin_attempts = 0


pin = st.text_input("Enter your PIN", type="password")
if pin:
    if st.session_state.pin_attempts < 3:
        if obj.validate_pin(int(pin)):
            st.success("PIN validated successfully!")
            option = st.selectbox("Choose an option", ("Deposit", "Withdraw", "Balance Enquiry"))

            if option == "Deposit":
                deposit_amount = st.number_input("Enter the amount to deposit", min_value=100, max_value=50000,
                                                 step=100)
                if st.button("Deposit"):
                    result = obj.deposit(deposit_amount)
                    st.write(result)

            elif option == "Withdraw":
                withdraw_amount = st.number_input("Enter amount to withdraw", min_value=100, max_value=20000, step=100)
                if st.button("Withdraw"):
                    result = obj.withdraw(withdraw_amount)
                    st.write(result)

            elif option == "Balance Enquiry":
                result = obj.tot_balance()
                st.write(result)

        else:
            st.session_state.pin_attempts += 1
            st.error("Invalid PIN. Attempts left: " + str(3 - st.session_state.pin_attempts))

    else:
        st.error("Too many invalid attempts. You are locked out.")
