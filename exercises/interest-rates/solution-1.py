def cost_after_one_month(loan, month_rate, month_fee):
  month_cost = loan*month_rate/100
  return month_cost + month_fee

# Test cases:
#print(cost_after_one_month(1000, 11, 0))
#print(cost_after_one_month(1000, 0, 42))
#print(cost_after_one_month(1000, 11, 42))

print(f"1000 kr lån i 1 månad hos Buffel&Båg kostar: {cost_after_one_month(1000, 29, 149)} kronor.")

print(f"1000 kr lån i 1 månad hos Lurendrejarna kostar: {cost_after_one_month(1000, 39, 0)} kronor.")
