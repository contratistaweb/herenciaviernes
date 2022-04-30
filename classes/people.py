class ClassName:
    
    def __init__(self, *args):
        self.__name = args.name;
        self.__old = args.old;
        self.__phone = args.phone;
        self.__street = args.street;
        self.__email = args.email;
    
    # Getters
    @property
    def name(self):
        return self.__name

    @property
    def old(self):
        return self.__old

    @property
    def phone(self):
        return self.__phone

    @property
    def street(self):
        return self.__street

    @property
    def email(self):
        return self.__email

    # Setters
    @name.setter
    def name(self, name):
        self.__name = name

    @old.setter
    def old(self, old):
        self.__old = old

    @phone.setter
    def phone(self, phone):
        self.__phone = phone

    @street.setter
    def street(self, street):
        self.__street = street

    @email.setter
    def email(self, email):
        self.__email = email

    def hello(self):
        print(f'Hi {self.name}')