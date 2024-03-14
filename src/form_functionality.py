class Form:
    def enter_name(self, name: str):
        if len(name) >20:
            return 'name has more than 20 chars'
        else:
            if len(name) < 3:
                return 'Invalid value'
        return "Your name is " + name

    def enter_age(self, age: str):
        if len(age) < 3:
            return 'Invalid value for field age'
