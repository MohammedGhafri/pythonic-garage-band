from abc import abstractmethod,ABC

class Musician(ABC):
    name=''
    member=''
    count=0
    list={''}
    
    def __init__(self,name,member):
        
        self.name=name
        self.member=member
        self.to_list(name,member)
        # print(Band.band_list)
        self.count+=1
        
    
    def to_list(self,name,member):
        new_band=Band(name,member)

    def __str__(self):
        return f"Here is {self.name} and he is a {self.member}"

    @abstractmethod
    def play_solos(self):
        return f"This in the main Band {self.name} will Play a solo"
   

class Band:
    band_list=[]
    def __init__(self,name,member):
        self.band_name=name
        self.instrument=member
        self.band_list.append({self.band_name,self.instrument})

    def __str__(self):
        # return self.band_list[0]
        print(self.band_list)
        pass

# class Musician(ABC):
#     def __init__(self,name):
#         super().__init__(name)

class Guitarist(Musician):
    def __init__(self,name,member):
        super().__init__(name,member)

    
    def play_solos(self):
        return f"{self.name} will Play a solo"
    
    def get_instrument(self):
        return f"{self.name} use a Guitar "
    
class Bassist(Musician):

    def __init__(self,name,member):

        super().__init__(name,member)


    def play_solos(self):
        return f"{self.name} will Play a solo"

    def get_instrument(self):
        return f"{self.name}  use a Guitar "

class Drummer(Musician):
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
print(noor.get_instrument())

# print(Band.play_solos(Ahmad))
print(Band.band_list)

