#######################################################
#     Spiros Daskalakis                               #
#     last Revision: 13/10/2022                       #
#     Python Version:  3.7                            #
#     Email: daskalakispiros@gmail.com                #
#######################################################

# MAX77504 is a synchronous 3A step-down DC-DC
# converter optimized for portable 2-cell and 3-cell batteryoperated applications.
# The converter operates on an input supply between 2.6V and 14V.
# Output voltage is adjustable between 0.6V and 6V with external feedback resistors.

# Datasheet: https://datasheets.maximintegrated.com/en/ds/MAX77504.pdf

tON_MIN = 100e-9  # ns
Vout = 3.3
Vinmax = 12.6

Fsw_1_max = 0.5e6
Fsw_2_max = 0.75e6
Fsw_3_max = 1.05e6
Fsw_4_max = 1.575e6

VSUP_UVLO = 2.5  # (Typical)

# Selected Frequency
Fsw = Fsw_4_max

# Switching Frequency Selection
tON_REQ = Vout / (Vinmax * Fsw_4_max)
print('tON(REQ) (ns):', tON_REQ / 1e-9)
if tON_REQ > tON_MIN:
    print('Switching frequency is OK')
else:
    print('Switching frequency is NOT OK')

# Gain Selection
# fBW< 0.2*Fsw_4_max

# Inductor Selection
L_1 = 1.5e-6
L_2 = 2.2e-6
L = L_1
ILOAD = 2
ILX_PLIM = 4
Ipp = (Vout * (Vinmax - Vout)) / (Vinmax * Fsw_4_max * L_2)
IPEAK = ILOAD + (Ipp / 2)
print('IPEAK:', IPEAK)
if Ipp > ILX_PLIM:
    print('Increase the inductor value')
else:
    print('Inductor value is OK')

# Setting the Output Voltage
VFB = 0.6
# RTOP = RBOT * ((Vout / VFB) - 1)
RTOP = 49.9e3
RBOT = 11.1e3
Vout = VFB * (RTOP + RBOT) / RBOT
print(' Output Voltage (V):', Vout)
