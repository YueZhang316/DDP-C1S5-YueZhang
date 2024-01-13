#try to create a chatbot that can reply customers about the size of clothes

def size_recommendation(height, weight):
    if height < 160 and weight < 50:
        return "Based on your height and weight, we recommend choosing size XS."
    elif 160 <= height < 170 and 50 <= weight < 65:
        return "Based on your height and weight, we recommend choosing size S or M."
    elif 170 <= height < 180 and 65 <= weight < 90:
        return "Based on your height and weight, we recommend choosing size L or XL."
    else:
        return "We recommend contacting our customer service for personalized assistance regarding size selection."

# Loop for repeated inquiries
while True:
    # Example customer information
    customer_height = float(input("Please enter your height in centimeters: "))
    customer_weight = float(input("Please enter your weight in kilograms: "))

    # Get the size recommendation
    recommendation = size_recommendation(customer_height, customer_weight)

    # Display the size recommendation
    print("Size Recommendation: " + recommendation)

    # Ask if the user wants to make another inquiry
    another_inquiry = input("Do you have another inquiry? (yes/no): ").lower()

    # Exit the loop if the user doesn't want to make another inquiry
    if another_inquiry != "yes":
        break
