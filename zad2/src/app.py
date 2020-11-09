class Pass():
    def ValidPassword(self, passw):
        """Check the given password
        """
        letters = False
        special = False
        bigletter = False
        isnumber = False
        number = 0
        for i in passw:
            number += 1
            if i.isupper():
                bigletter = True
            if i.isnumeric():
                isnumber = True
            if not i.isalnum():
                special = True
        if number >= 8:
            letters = True

        print(letters,special,bigletter,isnumber)
        if letters and special and bigletter and isnumber:
            return True
        else:
            return False
