from flask import Flask, request

app = Flask(__name__)

@app.route("/ussd", methods=["POST"])
def ussd():
    text = request.form.get("text", "")
    response = ""

    if text == "":
        response = "CON Welcome to AmalaVerse!\n1. Submit Spot\n2. View Spots"
    elif text == "1":
        response = "CON Enter Spot Name:"
    elif text.startswith("1*"):
        spot_name = text.split("*")[1]
        response = f"END Spot '{spot_name}' submitted successfully!"
    elif text == "2":
        response = "END Top Spots:\n1. Amala Skye\n2. Amala Shitta"
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