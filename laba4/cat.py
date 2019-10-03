class Cat():
    def __init__(self):
        pass
	
    def sleep(self):
        print("Zzzzz...")
		
    def cry(self):
        print("Aaaaaa!!!")
        
    def set_name(self, s):
        self.name = s
        
    def get_name(self):
        return self.name
    
    def meow(self):
        print("Мяяяяяуууу!")

    def __str__(self):
        return self.name
    
    def __add__(self, name):
        cat3 = Cat()
        cat3.set_name(self.get_name() + " " + name.get_name())
        return cat3

cat1 = Cat()
cat1.set_name("Василий")
cat2 = Cat()
cat2.set_name("Иваныч")
cat3 = cat1 + cat2
print(cat3)
