#constant: can be helpful when you are working with data science
#PI: is an example of scientific constants:
#example: print the constant value of PI
from scipy import  constants
print(constants.pi)
print("-----------------------")
#constant units: list all constants
print(dir(constants))
print("-----------------------")
#metric(SI) Prefixes: return specifed unit in meter
print(constants.yotta)      #1e+24
print(constants.zetta)      #1e+21
print(constants.exa)        #1e+18
print(constants.peta)       #1000000000000000.0: 10^15
print(constants.tera)       #1000000000000.0   : 10^12
print(constants.giga)       #1000000000.0      : 10^9
print(constants.mega)       #1000000.0         : 10^6
print(constants.kilo)       #1000.0            : 10^3
print(constants.hecto)      #100.0             : 10^2
print(constants.deka)       #10.0              : 10
print(constants.deci)       #0.1               : 10^-1
print(constants.centi)      #0.01              : 10^-2
print(constants.milli)      #0.001             : 10^-3
print(constants.micro)      #1e-06
print(constants.nano)       #1e-09
print(constants.pico)       #1e-12
print(constants.femto)      #1e-15
print(constants.atto)       #1e-18
print(constants.zepto)      #1e-21
print("-----------------------")
#Mass: return the specified unit in kg (eg gram return 0.001)
print(constants.gram)       #0.001
print(constants.metric_ton) #1000.0
print(constants.grain)      #6.479891e-05
print(constants.lb)         #0.45359236999999997
print(constants.pound)      #0.45359236999999997
print(constants.oz)         #0.028349523124999998
print(constants.ounce)      #0.028349523124999998
print(constants.stone)      #6.3502931799999995
print(constants.long_ton)   #1016.0469088
print(constants.short_ton)  #907.1847399999999
print(constants.troy_ounce) #0.031103476799999998
print(constants.troy_pound) #0.37324172159999996
print(constants.carat)      #0.0002
print(constants.atomic_mass)#1.66053904e-27
print(constants.m_u)        #1.66053904e-27
print(constants.u)          #1.66053904e-27
print("-----------------------")
#angle: return the specified unit in radians( eg: degree: 0.0174...)
print(constants.degree)     #0.017453292519943295
print(constants.arcmin)     #0.0002908882086657216
print(constants.arcminute)  #0.0002908882086657216
print(constants.arcsec)     #4.84813681109536e-06
print(constants.arcsecond)  #4.84813681109536e-06
print("-----------------------")
#time: return the specified unit in seconds (eg: hour return 3600)
print(constants.minute)     #60
print(constants.hour)       #3600
print(constants.day)        #86400
print(constants.week)       #604800
print(constants.year)       #31536000
print(constants.Julian_year)#31536000
print("-----------------------")
#Length: return the specified unit in meter
print(constants.inch)       #0.0254
print(constants.foot)       #0.30479999999999996
print(constants.yard)       #0.9143999999999999
print(constants.mile)       #1609.3439999999998
print(constants.mil)        #2.5399999999999997e-05
print(constants.pt)         #0.00035277777777777776
print(constants.point)      #0.00035277777777777776
print(constants.survey_foot)#0.3048006096012192
print(constants.survey_mile)#1609.3472186944373
print(constants.nautical_mile)  #1852.0
print(constants.fermi)          #1e-15
print(constants.angstrom)       #1e-10
print(constants.micron)         #1e-06
print(constants.au)             #149597870691.0
print(constants.astronomical_unit) #149597870691.0
print(constants.light_year)        #9460730472580800.0
print(constants.parsec)            #3.0856775813057292e+16
print("-----------------------")
#pressure: return the specified unit in pascals
print(constants.atm)        #101325.0
print(constants.atmosphere) #101325.0
print(constants.bar)        #100000.0
print(constants.torr)       #133.32236842105263
print(constants.mmHg)       #133.32236842105263
print(constants.psi)        #6894.757293168361
print("-----------------------")
#Area: return the specified unit in square meters
print(constants.hectare)    #10000.0
print(constants.acre)       #4046.8564223999992
print("-----------------------")
#Volume: return the specified unit in cubic meters
print(constants.liter)      #0.001
print(constants.litre)      #0.001
print(constants.gallon)     #0.0037854117839999997
print(constants.gallon_US)  #0.0037854117839999997
print(constants.gallon_imp) #0.00454609
print(constants.fluid_ounce)#2.9573529562499998e-05
print(constants.fluid_ounce_US)#2.9573529562499998e-05
print(constants.fluid_ounce_imp)#2.84130625e-05
print(constants.barrel)         #0.15898729492799998
print(constants.bbl)            #0.15898729492799998
print("-----------------------")
#speed : return the specified unit in meters per second
print(constants.kmh)        #0.2777777777777778
print(constants.mph)        #0.44703999999999994
print(constants.mach)       #340.5
print(constants.speed_of_sound)#340.5
print(constants.knot)          #0.5144444444444445
print("-----------------------")
#temperature: return the specified unit in Kevin
print(constants.zero_Celsius)       #273.15
print(constants.degree_Fahrenheit)  #0.5555555555555556
print("-----------------------")
#Energy: return the specified unit in joules
print(constants.eV)             #1.6021766208e-19
print(constants.electron_volt)  #1.6021766208e-19
print(constants.calorie)        #4.184
print(constants.calorie_th)     #4.184
print(constants.calorie_IT)     #4.1868
print(constants.erg)            #1e-07
print(constants.Btu)            #1055.05585262
print(constants.Btu_IT)         #1055.05585262
print(constants.Btu_th)         #1054.3502644888888
print(constants.ton_TNT)        #4184000000.0
print("-----------------------")
#Power: return the specified unit in watts
print(constants.hp)             #745.6998715822701
print(constants.horsepower)     #745.6998715822701
print("-----------------------")
#Force: return the specified unit in newton
print(constants.dyn)            #1e-05
print(constants.dyne)           #1e-05
print(constants.lbf)            #4.4482216152605
print(constants.pound_force)    #4.4482216152605
print(constants.kgf)            #9.80665
print(constants.kilogram_force) #9.80665
