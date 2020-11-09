class Pass():
    def ValidPassword(self, passw):
        """
        Check the given password
        >>> c = Pass()
        >>> c.ValidPassword("hsaT45&*jadsd")
        True
        >>> c.ValidPassword("T3&d")
        False
        >>> c.ValidPassword("HGmnjsd45ad")
        False
        >>> c.ValidPassword("dasmdw%^321")
        False
        >>> c.ValidPassword("Avdsad%dadaw")
        False
        >>> c.ValidPassword("dasd5 6&*WEda")
        Traceback (most recent call last):
            File "C:/Users/Maciek/Desktop/stepiglab6/zad2/src/app.py", line 46, in <module>
                maciek.ValidPassword("23fseIUH I&*5")
            File "C:/Users/Maciek/Desktop/stepiglab6/zad2/src/app.py", line 29, in ValidPassword
                raise ValueError("Password can't contain a blank space")
        ValueError: Password can't contain a blank space
        >>> c.ValidPassword(1)
        Traceback (most recent call last):
            File "C:/Users/Maciek/Desktop/stepiglab6/zad2/src/app.py", line 53, in <module>
                maciek.ValidPassword(1)
            File "C:/Users/Maciek/Desktop/stepiglab6/zad2/src/app.py", line 26, in ValidPassword
                raise TypeError("Must be a string")
        TypeError: Must be a string
        """

        if type(passw) != str:
            raise TypeError("Must be a string")

        letters = False
        special = False
        bigletter = False
        isnumber = False
        number = 0
        for i in passw:
            number += 1
            if i.isspace():
                raise ValueError("Password can't contain a blank space")
            if i.isupper():
                bigletter = True
            if i.isnumeric():
                isnumber = True
            if not i.isalnum():
                special = True
        if number >= 8:
            letters = True

        if letters and special and bigletter and isnumber:
            return True
        else:
            return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
