
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Use the JSON key file to authenticate
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('finanal-7bbc65b6c0b4.json', scope)
client = gspread.authorize(creds)

# Open the Google Sheet by title
# sheet = client.open("Calcul").sheet1
spreadsheet = client.open_by_key('https://docs.google.com/spreadsheets/d/1yxiZqdhvMKctMU5MvgC_-UJjfv6IXV_sNSFMjanJLz0/edit')
print(gc.auth.service_account_email)

try:
    sheet = client.open("FINANCIALS").Ledger
    data = sheet.get_all_records()
    print(data)
except Exception as e:
    print(f"An error occurred: {e}")


# Read data
data = sheet.get_all_records()
print(data)

#df.groupby("symbol")
date
symbol
action
qty
price
fees

append()    # add buy
popleft()   # remove oldest buy

from collections import deque

ledger = [
    {"action": "buy", "qty": 10, "price": 100},
    {"action": "buy", "qty": 5, "price": 120},
    {"action": "sell", "qty": 8, "price": 130},
]

inventory = deque()
realized_pnl = 0

for trade in ledger:

    if trade["action"] == "buy":
        inventory.append({
            "qty": trade["qty"],
            "price": trade["price"]
        })

    elif trade["action"] == "sell":

        qty_to_sell = trade["qty"]
        sell_price = trade["price"]

        while qty_to_sell > 0:

            lot = inventory[0]

            if lot["qty"] <= qty_to_sell:

                cost = lot["qty"] * lot["price"]
                revenue = lot["qty"] * sell_price

                realized_pnl += revenue - cost

                qty_to_sell -= lot["qty"]
                inventory.popleft()

            else:

                cost = qty_to_sell * lot["price"]
                revenue = qty_to_sell * sell_price

                realized_pnl += revenue - cost

                lot["qty"] -= qty_to_sell
                qty_to_sell = 0

print("Realized PnL:", realized_pnl)
print("Remaining Inventory:", list(inventory))
