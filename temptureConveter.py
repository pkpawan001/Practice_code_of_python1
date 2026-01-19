class TemPConveter:
    def __init__(self,s):
        self.s=s
        
    def Celsius_to_fahrenheit(self,cel):
        return (cel* (9/5))+32
    def fahrenheit_to_celsius(self,f):
        return (f-32)*5/9
    def celsius_to_kelvin(self,cel):
        return cel+273.5
    def kelvin_to_celsius(self,kel):
        return kel-273.5
    def fahrenheit_to_kelvin(self,f):
        cel=(f-32)*5/9
        return cel+273.5


t=TemPConveter(1)
print(t.Celcious_to_farenhight(10))
print(t.ferenhight_to_celcious(10))
