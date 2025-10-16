from flask import Flask, request

app = Flask(__name__)

@app.route("/ussd", methods=["POST"])
def ussd():
    text = request.form.get("text", "")
    phone_number = request.form.get("phoneNumber", "")
    response = ""

    # Split user input by "*"
    user_input = text.split("*")

    if text == "":
        # Step 0 — show main menu
        response = "CON Welcome to AmalaVerse!\n1. Submit Spot\n2. View Spots"

    elif text == "1":
        # Step 1 — user chose to submit spot
        response = "CON Enter Spot Name:"

    elif len(user_input) == 2 and user_input[0] == "1":
        # Step 2 — user entered spot name
        response = "CON Enter Spot Location:"

    elif len(user_input) == 3 and user_input[0] == "1":
        # Step 3 — user entered location, now confirm
        spot_name = user_input[1]
        location = user_input[2]
        response = f"END Spot '{spot_name}' at '{location}' submitted successfully by {phone_number}!"

    elif text == "2":
        # Just a sample static list
        response = "END Top Spots:\n1. Amala Skye - Shitta\n2. Amala Heaven - Yaba"

    else:
        response = "END Invalid option."

    return response

if __name__ == "__main__":
    app.run(debug=False, port=5000)

# Steps in using Aggregator:

# Register service with aggregator.
# Get USSD code (e.g. *384*123#).
# Provide your callback URL (e.g. https://yourapp.com/ussd).
# Aggregator routes all user input to your URL.
# Deploy your backend online (it must have HTTPS, e.g., using Render, Railway, or AWS).
# Handle user sessions — your backend should remember users by sessionId.

# Endpoint: https://ussd-service-9qck.onrender.com