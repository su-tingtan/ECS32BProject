class Package:
    def __init__(self, id):
        self.id = id
        self.address = ""
        self.office = ""
        self.ownerName = ""
        self.collected = False
        self.delivered = False

    ##### Accessors #####
    def get_id(self):
        return self.id
    
    def get_address(self):
        return self.address

    def get_office(self):
        return self.office
    
    def get_ownerName(self):
        return self.ownerName

    def get_collected(self):
        return self.collected
    
    def get_delivered(self):
        return self.delivered
    #####################


    ##### Mutaters #####
    def set_address(self, address):
        self.address = address

    def set_office(self, office):
        self.office = office 

    def set_ownerName(self, ownerName):
        self.ownerName = ownerName

    def set_collected(self, boolean):
        self.collected = boolean

    def set_delivered(self, boolean):
        self.delivered = boolean 
    ####################



class Truck:
    def __init__(self, id, n, loc):
        self.id = id
        self.size = n
        self.location = loc
        self.packages = []
        self.space = n 


    def collectPackage(self, pk):
        if self.space > 0:
            if self.location == pk.get_office() and pk.get_collected() == False:
                self.packages.append(pk)
                pk.set_collected(True)
                self.space -= 1


    def deliverOnePackage(self, pk):
        if self.location == pk.get_address() and pk in self.packages:
            self.packages.remove(pk)
            pk.set_delivered(True)
            self.space += 1


    def deliverPackages(self):
        new_self_packages = []
        for pk in self.packages:
            if self.location == pk.get_address() and pk in self.packages:
                pk.set_delivered(True)
                self.space += 1
            else:
                new_self_packages.append(pk)
        self.packages = new_self_packages


    def removePackage(self, pk):
        if self.location[:3] == 'ups' and pk in self.packages:
            self.packages.remove(pk)
            pk.set_office(self.location)
            pk.set_collected(False)
            self.space += 1


    def driveTo(self, loc):
        self.location = loc


    def getPackagesIds(self):
        id_lst = []
        for pk in self.packages:
            id_lst.append(pk.get_id())
        return id_lst