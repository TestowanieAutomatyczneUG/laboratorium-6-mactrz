class FizzBuzz:
    def game(self, x):
        """A game of FizzBuzz
        >>> c.game(10)
        'Buzz'
        >>> c.game(15)
        'FizzBuzz'
        >>> c.game(3)
        'Fizz'
        >>> c.game(7)
        '7'
        >>> c.game("test")
        Traceback (most recent call last):
            File "C:/Users/Maciek/Desktop/stepiglab6/zad1/src/fizz.py", line 28, in <module>
                print(maciek.game("kek"))
            File "C:/Users/Maciek/Desktop/stepiglab6/zad1/src/fizz.py", line 15, in game
                raise TypeError("Must be an integer")
        TypeError: Must be an integer
        """
        if type(x) != int:
            raise TypeError("Must be an integer")
        if x % 15 == 0:
            return "FizzBuzz"
        elif x % 3 == 0:
            return "Fizz"
        elif x % 5 == 0:
            return "Buzz"
        elif type(x) == int:
            return str(x)
        else:
            raise Exception("Error in FizzBuzz")



if __name__ == "__main__":
    import doctest
    doctest.testmod(extraglobs={'c': FizzBuzz()})


