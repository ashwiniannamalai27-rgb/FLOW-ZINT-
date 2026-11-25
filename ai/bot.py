def chatbot_response(message):

    message = message.lower()

    if "save" in message:
        return "Saving at least 20% of your monthly income is a good financial habit."

    elif "budget" in message:
        return "Create a monthly budget and track your expenses regularly."

    elif "investment" in message:
        return "Consider SIPs, mutual funds, or fixed deposits based on your risk profile."

    elif "credit" in message:
        return "Pay EMIs on time and keep your credit utilization below 30%."

    elif "insurance" in message:
        return "Health insurance is essential. Consider life insurance based on your responsibilities."

    elif "fraud" in message:
        return "Never share OTPs, PINs, or banking passwords. Verify suspicious transactions immediately."

    elif "tax" in message:
        return "Explore eligible deductions and tax-saving investment options before filing taxes."

    else:
        return (
            "I'm your AI Financial Wellness Assistant. "
            "Ask me about budgeting, savings, investments, insurance, credit score, or fraud prevention."
        )