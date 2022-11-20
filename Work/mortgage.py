# mortgage.py
#
# Exercise 1.7

# Parameters
fInitialPrincipal = 500000.0       # Principal to pay back
fRate = 0.05                       # Borrowing annual rate
fMensualRate = (fRate / 12.0)      # Borrowing rate mensualized
fBaselinePayment = 2684.11         # Mensual baseline payment
fExtraPayment = 1000.0             # Amount of extra payment
iExtraPaymentFirstMonth = 61       # First month of extra payment
iExtraPaymentLastMonth = 108       # Last month of extra payment

# Declarations and Initialisations
fTotalPaid = 0.0                   # Current total paid
iMonth = 0                         # Current number of months
fPayment = 0                       # Current payment
fPrincipal = fInitialPrincipal     # Current principal remaining


while fPrincipal > 0.0:

    # Incremenation of current month and principal
    iMonth += 1
    fPrincipal *= (1.0 + fMensualRate)
    
    # Calculation of mensual payment
    if not (fPayment > fPrincipal) :
        if ((iMonth >= iExtraPaymentFirstMonth) and (iMonth <= iExtraPaymentLastMonth)) :
            fPayment = (fBaselinePayment + fExtraPayment)
        else :
            fPayment = fBaselinePayment
    else :
        fPayment = fPrincipal

    # Calculation of remaining principal
    fPrincipal = (fPrincipal - fPayment)

    # Update of total currently paid
    fTotalPaid += fPayment

    print('Currently paid :', round(fTotalPaid, 2), 'in', iMonth, 'months.', 'Remaining :', round(fPrincipal, 2))


print('Total paid :', round(fTotalPaid, 2), 'in', iMonth, 'months !')