import pytest
from calculate_the_profit_medium import profit

def test_calculate1():
    assert profit({
  "cost_price": 32.67,
  "sell_price": 45.00,
  "inventory": 1200
    }) == 14796

def test_calculate2():
    assert profit({
  "cost_price": 225.89,
  "sell_price": 550.00,
  "inventory": 100
    }) == 32411

def test_calculate3():
    assert profit({
  "cost_price": 2.77,
  "sell_price": 7.95,
  "inventory": 8500
   }) == 44030
    
