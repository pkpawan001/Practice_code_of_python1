class Conveter:
    @staticmethod
    def celsius_to_fahrenhiet(cel):
        return (cel*9/5)+32
    @staticmethod
    def fahrenhiet_to_celsius(fer):
        return (fer-32)*5/9
    


if __name__=="__main__":
    print(Conveter.celsius_to_fahrenhiet(100))
    print(Conveter.fahrenhiet_to_celsius(100))