def chatbot_response(user_input):
    user_input = user_input.lower()

    # Greetings
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"

    # Product related
    elif "product" in user_input:
        return "Sure! Can you tell me which product you want help with?"

    # Order status
    elif "order" in user_input or "status" in user_input:
        return "Please provide your order ID so I can check the status."

    # Refund
    elif "refund" in user_input:
        return "I can help with refunds. When did you place your order?"

    # Shipping
    elif "shipping" in user_input or "delivery" in user_input:
        return "Our standard shipping time is 3–5 business days."

    # Payment
    elif "payment" in user_input:
        return "We accept UPI, Credit/Debit cards, and Net Banking."

    # Thanks
    elif "thank" in user_input:
        return "You're welcome! Happy to help 😊"

    # Default response
    else:
        return "I'm sorry, I didn't understand that. Can you rephrase?"


# Chat loop
print("Customer Service Chatbot is now running...")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chatbot: Thank you for chatting with us!")
        break

    response = chatbot_response(user_input)
    print("Chatbot:", response)
