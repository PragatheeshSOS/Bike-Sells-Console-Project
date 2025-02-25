class Payment:
    payments = []

    def __init__(self, payment_id, order_id, amount_due, payment_method, status="Pending"):
        self.payment_id = payment_id
        self.order_id = order_id
        self.amount_due = amount_due
        self.payment_method = payment_method
        self.status = status
        Payment.payments.append(self)

    def process_payment(self, amount_paid):
        if amount_paid == 0:
            self.status = "Incomplete"
            return f"Payment for Order {self.order_id} is INCOMPLETE. No payment was made."

        if amount_paid < self.amount_due:
            self.status = "Refunded"
            return f"Payment for Order {self.order_id} is INCORRECT. Paid: ${amount_paid}, Expected: ${self.amount_due}. Refund issued."

        if amount_paid > self.amount_due:
            excess = amount_paid - self.amount_due
            return f"Overpaid! Expected: ${self.amount_due}, Received: ${amount_paid}. Refund issued for excess: ${excess}."

        self.status = "Successful"
        return f"Payment for Order {self.order_id} is SUCCESSFUL! Amount Paid: ${amount_paid}."

    def get_payment_status(self):
        return f"Payment ID: {self.payment_id}, Order ID: {self.order_id}, Status: {self.status}, Amount Due: ${self.amount_due}"
