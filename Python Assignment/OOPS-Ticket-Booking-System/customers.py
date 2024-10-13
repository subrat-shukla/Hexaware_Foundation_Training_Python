class customer:
    def __init__(self,firstname,lastname, email,phone_number,address):
        self.firstname=firstname
        self.lastname = lastname
        self.email=email
        self.phone_number=phone_number
        self.address=address

    #getters
    @property
    def getfirstname(self):
        return self.customer_name

    @property
    def getlastname(self):
        return self.lastname

    @property
    def getemail(self):
        return self.email

    @property
    def getphone_number(self):
        return self.phone_number

    @property
    def getaddress(self):
        return self.address

    #setters
    @getfirstname.setter
    def set_customer_name(self,firstname):
        self.firstname=firstname

    @getlastname.setter
    def setlastname(self, lastname):
        self.lastname = lastname
    @getemail.setter
    def set_email(self,email):
        self.email=email
    @getphone_number.setter
    def set_phone_number(self,phone_number):
        self.phone_number=phone_number

    @getaddress.setter
    def setaddress(self, address):
        self.address = address

