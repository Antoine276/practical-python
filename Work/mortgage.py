# mortgage.py
#
# Exercise 1.7

fPrincipal = 500000.0              # Principal to pay back
fRate = 0.05                       # Borrowing annual rate
fMensualRate = (fRate / 12.0)      # Borrowing rate mensualized
fBaselinePayment = 2684.11         # Mensual baseline payment
fExtraPayment = 1000.0             # Additionnal payment for the x first months
iExtraPaymentDuration = 12         # Duration in months of the additionnal payment
fTotalPaid = 0.0                   # Total currently paid
iMonth = 1                         # Current number of months
fPayment = 0                       # Current payment


while fPrincipal > 0.0:

    # print('Month :', iMonth)
    # print('Principal :', fPrincipal)
    # print('MensualRate :', fMensualRate)
    # print('Payment :', fPayment)

    if iMonth <= iExtraPaymentDuration :
        fPayment = (fBaselinePayment + fExtraPayment)
    else :
        fPayment = fBaselinePayment

    fPrincipal = ((fPrincipal * (1 + fMensualRate)) - fPayment)

    fTotalPaid += (fPayment)
    iMonth += 1

    # print('----------------------------------------')

print('Total payed :', round(fTotalPaid, 2), 'in', iMonth, 'months !')