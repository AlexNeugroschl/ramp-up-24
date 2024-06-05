def profit(info):
    return round((info.get("sell_price") - info.get("cost_price")) * info.get("inventory"), 2)

print(profit({
  "cost_price": 32.67,
  "sell_price": 45.00,
  "inventory": 1200
}))