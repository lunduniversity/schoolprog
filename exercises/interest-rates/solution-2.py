def cost_after_one_month(loan, month_rate, month_fee):
  month_cost = loan*month_rate/100
  return month_cost + month_fee



def debt_after_m_months(loan, month_rate, month_fee, m):
  debt = loan # initial debt
  for i in range(m):
    debt += cost_after_one_month(debt, month_rate, month_fee)
  return debt

# Test cases:
#print(debt_after_m_months(1000, 11, 0, 1))
#print(debt_after_m_months(1000, 0, 42, 1))
#print(debt_after_m_months(1000, 11, 42, 1))

#print(debt_after_m_months(1000, 11, 0, 2))
#print(debt_after_m_months(1000, 0, 42, 2))
#print(debt_after_m_months(1000, 11, 42, 2))

print(f"1000 kr lån i 1 månad hos Buffel&Båg ger en skuld på: {debt_after_m_months(1000, 29, 149, 1)} kronor.")

print(f"1000 kr lån i 1 månad hos Lurendrejarna ger en skuld på: {debt_after_m_months(1000, 39, 0, 1)} kronor.")

print(f"1000 kr lån i 1 år hos Buffel&Båg ger en skuld på: {debt_after_m_months(1000, 29, 149, 12)} kronor.")

print(f"1000 kr lån i 1 år hos Lurendrejarna ger en skuld på: {debt_after_m_months(1000, 39, 0, 12)} kronor.")
