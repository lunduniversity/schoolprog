def cost_after_one_month(loan, month_rate, month_fee):
  month_cost = loan*month_rate/100
  return month_cost + month_fee

def debt_after_m_months(loan, month_rate, month_fee, m):
  debt = loan # initial debt
  for i in range(m):
    debt += cost_after_one_month(debt, month_rate, month_fee)
  return debt

import matplotlib.pyplot as plt

def intplot(f, m, lbl):
  xs = [i+1 for i in range(m)]
  ys = [f(i+1) for i in range(m)]
  plt.plot(xs, ys, label=lbl)

def bb(m):
  return debt_after_m_months(1000, 29, 149, m)

def lur(m):
  return debt_after_m_months(1000, 39, 0, m)

def example_loan(m):
  return debt_after_m_months(100, 10, 0, m)

#intplot(example_loan, 24, "exempel-firma")
intplot(bb, 12, "Buffel&Båg")
intplot(lur, 12, "Lurendrejarna")
plt.title("sms-lån")
plt.xlabel("månader")
plt.ylabel("kronor")
plt.legend(loc = "upper center")
plt.grid(True)
plt.savefig("plot.png")
