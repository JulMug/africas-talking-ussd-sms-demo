import os
import africastalking
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("AT_USERNAME")
api_key = os.getenv("AT_API_KEY")

africastalking.initialize(username, api_key)

sms = africastalking.SMS


from flask import Flask, request

app = Flask(__name__)

market_prices = {
    "maize": "USD 0.45 per kg",
    "beans": "USD 0.80 per kg",
    "rice": "USD 0.70 per kg"
}


@app.route("/")
def home():
    return "AgriConnect Demo is running!"


@app.route("/ussd", methods=["POST"])
def ussd():
    text = request.values.get("text", "")

    # Main menu
    if text == "":
        response = (
            "CON Welcome to AgriConnect\n"
            "1. Market Prices\n"
            "2. Find Buyers\n"
            "3. Help"
        )

    # Market Prices submenu
    elif text == "1":
        response = (
            "CON Market Prices\n"
            "1. Maize\n"
            "2. Beans\n"
            "3. Rice"
        )

    # Maize price
    elif text == "1*1":
        response = f"END Current maize price: {market_prices['maize']}"

    elif text == "1*2":
        response = f"END Current beans price: {market_prices['beans']}"

    elif text == "1*3":
        response = f"END Current rice price: {market_prices['rice']}"

    # Find Buyers
    elif text == "2":
        response = "END Available buyers: Goma Market, North Kivu Agro"

    # Help
    elif text == "3":
        response = "END For support, contact AgriConnect."

    else:
        response = "END Invalid option."

    return response



# SMS

@app.route("/send-sms", methods=["POST"])
def send_sms():
    phone_number = request.values.get("phone")

    if not phone_number:
        return "Phone number is required", 400

    message = (
        "AgriConnect: Your registration was successful. "
        "Thank you for using our service."
    )

    return {
        "status": "success",
        "phone": phone_number,
        "message": message
    }

if __name__ == "__main__":
    app.run(debug=True)