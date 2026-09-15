# Africa's Talking USSD & SMS Demo

A small Flask prototype inspired by AgriConnect, demonstrating how USSD and SMS services can be integrated into an application.

## Features

- USSD menu navigation
- Agricultural market price demo
- Buyer information
- SMS confirmation endpoint
- Flask backend
- Africa's Talking SDK integration structure

## Technologies

- Python
- Flask
- Africa's Talking SDK
- python-dotenv

## USSD Flow

1. Welcome to AgriConnect
2. Market Prices
3. Select a crop
4. Display the sample market price

Example:

CON Welcome to AgriConnect
1. Market Prices
2. Find Buyers
3. Help

## SMS

The SMS endpoint currently simulates the response locally.

In a production environment, it would be connected to the Africa's Talking SMS API.

## Important

This project uses sample agricultural prices for demonstration purposes.

API credentials are stored in `.env` and are intentionally excluded from Git using `.gitignore`.

## Run locally

```bash
pip install -r requirements.txt
python app.py

