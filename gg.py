def calculate_total_price(price, quantity, discount=0):
	subtotal = price * quantity
	total = subtotal - discount  # 🔴 Set breakpoint here
	return total


def is_eligible_for_free_shipping(total):
	return total > 50


def generate_receipt(item_name, price, quantity, discount=0):
	print("Generating receipt...")
	total = calculate_total_price(price, quantity, discount)
	shipping = "Free" if is_eligible_for_free_shipping(total) else "$5.00"

	receipt = f"""
    Item: {item_name}
    Quantity: {quantity}
    Unit Price: ${price:.2f}
    Discount: ${discount:.2f}
    Total: ${total:.2f}
    Shipping: {shipping}
    """
	return receipt


def main():
	item = "Bluetooth Speaker"
	price = 25.0
	quantity = 2
	discount = 560

	receipt = generate_receipt(item, price, quantity, discount)
	print(receipt)


main()
