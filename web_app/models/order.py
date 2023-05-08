

class Order:
    def __init__(self, attrs):
        self.id = attrs.get("id")
        self.user_email = attrs.get("user_email")
        self.product_id = attrs.get("product_id")
        self.product_name = attrs.get("product_name")
        self.product_price = attrs.get("product_price")
        self.created_at = attrs.get("created_at")
        self.appointment_datetime = attrs.get("appointment_datetime")

    @property
    def to_row(self):
        return [self.id, self.user_email, self.product_id, self.product_name, self.product_price, self.appointment_datetime, str(self.created_at)]
