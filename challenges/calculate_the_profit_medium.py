def profit(info):
    return round((info.get("sell_price") - info.get("cost_price")) * info.get("inventory"), 2)
