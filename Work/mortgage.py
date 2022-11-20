# mortgage.py
#
# Exercise 1.7

# Parameters
fPrincipal = 500000.0              # Principal to pay back
fRate = 0.05                       # Borrowing annual rate
fMensualRate = (fRate / 12.0)      # Borrowing rate mensualized
fBaselinePayment = 2684.11         # Mensual baseline payment
fExtraPayment = 1000.0             # Additionnal payment for the x first months
iExtraPaymentFirstMonth = 61       # First month of extra payment
iExtraPaymentLastMonth = 108       # Last month of extra payment
fTotalPaid = 0.0                   # Total currently paid

# Declarations and Initialisation
iMonth = 1                         # Current number of months
fPayment = 0                       # Current payment


while fPrincipal > 0.0:
    
    if ((iMonth >= iExtraPaymentFirstMonth) and (iMonth <= iExtraPaymentLastMonth)) :
        fPayment = (fBaselinePayment + fExtraPayment)
    else :
        fPayment = fBaselinePayment

    fPrincipal = ((fPrincipal * (1 + fMensualRate)) - fPayment)

    fTotalPaid += (fPayment)
    iMonth += 1

print('Total payed :', round(fTotalPaid, 2), 'in', iMonth, 'months !')