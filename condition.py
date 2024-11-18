def calculate_discount(price, discount_percent):
    
    if(discount_percent >= 20):
        discount = (price * discount_percent) / 100
        final_price = price - discount
        print(f'The final price after a discount of {discount_percentage}% is {final_price}')
        return final_price
    else:
        print(f"No discount was applied. Final price is ")
        return price

initial_price = float(input('Enter your initial price: '))
discount_percentage = float(input('Enter a discount percent: '))

finalPrice = calculate_discount(initial_price, discount_percentage)

