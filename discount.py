# Constants defining the discount rules
DISCOUNT_THRESHOLD_CENTS = 5000
DISCOUNT_RATE = 0.10


def apply_discount(total):
    # Apply a 10% discount if the total exceeds 50 NOK
    if total > DISCOUNT_THRESHOLD_CENTS:
        total = int(total * (1 - DISCOUNT_RATE))

    return total


def apply_discount_to_cart(cart):
    # Calculate total price of items in the cart
    total = sum(item.price_cents * item.qty for item in cart.items)

    # Apply the shared discount rule
    return apply_discount(total)


def generate_invoice(order):
    # Format invoice header and customer information
    invoice = (
        f"Invoice for order {order.id}\n"
        f"Customer: {order.user_email}\n"
    )
    
    # Calculate total price of items in the order
    total = sum(item.price_cents * item.qty for item in order.items)

    # Apply the shared discount rule
    total = apply_discount(total)

    invoice += f"Total (after discount if applicable): {total} cents"
    return invoice