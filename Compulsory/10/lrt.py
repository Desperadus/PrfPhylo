from scipy.stats import chi2

lnL0 = -17652.4
lnL1 = -17646.5

delta = 2 * (lnL1 - lnL0)

dof = 6

p_value = 1 - chi2.cdf(delta, df=dof)

print(f"LRT Statistic: {delta}")
print(f"Degrees of Freedom: {dof}")
print(f"P-value: {p_value}")
