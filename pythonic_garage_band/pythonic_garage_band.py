from abc import abstractmethod,ABC

class Band(ABC):
    name=''
    member=''
    count=0
    list={''}
    
    def __init__(self,name,member):
        self.name=name
        self.member=member
        self.count+=1
        
    
    
    def __str__(self):
        return f"Here is {self.name} and he is a {self.member}"

    @abstractmethod
    def play_solos(self):
        return f"This in the main Band {self.name} will Play a solo"
   


# class Musician(ABC):
#     def __init__(self,name):
#         super().__init__(name)

class Guitarist(Band):
    def __init__(self,name,member):
        super().__init__(name,member)

    
    def play_solos(self):
        return f"{self.name} will Play a solo"
    
    def get_instrument(self):
        return f"{self.name} use a Guitar "
    
class Bassist(Band):

    def __init__(self,name,member):
        super().__init__(name,member)


    def play_solos(self):
        return f"{self.name} will Play a solo"

    def get_instrument(self):
        return f"{self.name}  use a Guitar "

class Drummer(Band):
    def __init__(self,name,member):
        super().__init__(name,member)

    def play_solos(self):
        return f"{self.name} will Play a solo"

    def get_instrument(self):
        return f"{self.name}  use a drum "
    def __str__(self):
        return f"Here is {self.name} and he is a {self.member}"
    


mahmoud=Bassist("mahmoud","Bassist")
Ahmad=Guitarist("ahmad","Guitarist")
noor=Drummer("noor","Drummer")

# print(Ahmad.play_solos())
# print(mahmoud.play_solos())
# print(noor.play_solos())
print(noor)

# print(Band.play_solos(Ahmad))

