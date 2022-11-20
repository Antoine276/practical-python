# bounce.py
#
# Exercise 1.5

# Parameters
iHeight = 100                # Height from which to drop the ball
iMaxBounce = 10              # Maximum number of bounces
iBounceStrenght = (3/5)      # Intensity of bounce
iDecimals = 4                # Decimal for rounding

# Initialisations
iBounce = 1


while iBounce <= iMaxBounce :
    iHeight = (iHeight * iBounceStrenght)
    print('Bounce :', iBounce, 'Height :', round(iHeight, iDecimals))

    iBounce += 1



