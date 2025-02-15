from datetime import datetime
# python discount.py
#Please enter the subtotal: 42.75
#Sales tax amount: 2.56
#Total: 45.31

subtotal= float(input("Please enter the subtotal:"))
current_date_and_time = datetime.now()
weekday = current_date_and_time.weekday()

discount= (subtotal * 0.10)
if subtotal >= 50 and weekday ==1 and weekday ==2:
    print(f"Discount amount: {discount:.2f}")
    subtotal -= discount

sales_tax= (subtotal * 0.06)
print(f"Salex tax amount:{sales_tax:.2f}")

print(f"Total: {subtotal + sales_tax:.2f}")

    