# gegeben Temperatur in Celsius = c
# gesucht Temperatur in Kelvin = k
# k = c+273,15

def get_temperature():
    while True:
        c = input("gibt die Temperatur in Celsuis an:")
        try:
            c = float(c)
            return c
        except ValueError: 
            print("Das ist keine Gültige Zahl")

def convert_to_kelvin(c):
    k = c + 273.15
    return k

if __name__ == "__main__":                          # wird nur aufgerufen wenn diese Datei hier die main ist (bei import nicht!)
    c = get_temperature()
print("Die Temperatur ist " + str(convert_to_kelvin(c)) + " Kelvin" )