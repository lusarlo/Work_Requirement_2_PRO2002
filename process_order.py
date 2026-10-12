# Constants defining the discount rules
VIP_DISCOUNT_RATE = 0.20
FREE_SHIPPING_DISCOUNT = 50

class OrderRepository:
    def save(self, order, total):
        # Placeholder for future database operations
        pass

def calculate_total(order):
    # Calculate the total price of all items in the order
    return sum(item.price * item.qty for item in order.items)


def apply_vip_discount(total):
    # Apply a 20% discount for VIP customers
    return total * (1 - VIP_DISCOUNT_RATE)


def apply_free_shipping_discount(total):
    # Subtract the free shipping discount
    return total - FREE_SHIPPING_DISCOUNT


# Map discount codes to their corresponding functions
DISCOUNT_RULES = {
    "VIP": apply_vip_discount,
    "FREESHIP": apply_free_shipping_discount
}


def apply_discount(total, discount_code):
    # Find and apply the discount associated with the code
    discount_function = DISCOUNT_RULES.get(discount_code)

    if discount_function:
        total = discount_function(total)

    return total


def notify_user(user, total, notify):
    # Notify the user if notifications are enabled
    if notify:
        print(f"Email sent to {user.email}: Your order total is {total}")


def process_order(order, user, discount_code, order_repository, notify):
    # Calculate the order total
    total = calculate_total(order)

    # Apply the discount
    total = apply_discount(total, discount_code)

    # Save the order using the repository
    order_repository.save(order, total)

    # Notify the user
    notify_user(user, total, notify)

    return total