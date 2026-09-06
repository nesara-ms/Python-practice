'''program to convert USD to INR '''
def converter(usd_value):
    inr_value = usd_value * 82.74
    return inr_value
print("Enter the amount in USD:")
usd_amount = float(input())
inr_amount = converter(usd_amount)
print(f"The amount in INR is: {inr_amount}")