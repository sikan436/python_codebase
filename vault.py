class Vault:
    def __init__(self,galleons=0,sickes=0,knuts=0):
        self.galleons=galleons
        self.sickes=sickes
        self.knuts=knuts

    def __str__(self):
        return f"{self.galleons} galleons, {self.sickes} sickes, {self.knuts} knuts"

    def __add__(self,other):
        galleons=self.galleons+other.galleons
        sickes=self.sickes+other.sickes
        knuts=self.knuts+other.knuts
        return Vault(galleons,sickes,knuts)

potter=Vault(100,50,30)
print(potter)

wisley=Vault(30,50,60)
print(wisley)
total=potter+wisley
print(total)



