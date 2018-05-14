def cost_after_one_month(loan, month_rate, month_fee):
  month_cost = loan*month_rate/100
  return month_cost + month_fee

def debt_after_m_months(loan, month_rate, month_fee, m):
  debt = loan # initial debt
  for i in range(m):
    debt += cost_after_one_month(debt, month_rate, month_fee)
  return debt

def effective_rate(loan, month_rate, month_fee):
  debt = debt_after_m_months(loan, month_rate, month_fee, 12)
  cost = debt - loan
  return (cost/loan) * 100

print(f"Effektiv ränta för Buffel&Båg: {effective_rate(1000, 29, 149)} kronor.")

print(f"Effektiv ränta för Lurendrejarna: {effective_rate(1000, 39, 0)} kronor.")
