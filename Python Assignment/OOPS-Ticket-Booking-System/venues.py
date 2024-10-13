class venue:
    def __init__(self,venue_name,address):
        self.venue_name=venue_name
        self.address=address

    def print_venue_details(self):
        print("venue name: ",self.venue_name)
        print("address: ",self.address)

    # getters
    @property
    def get_venue_name(self):
        return self.venue_name
    @property
    def get_address(self):
        return self.address

    # setters
    @get_venue_name.setter
    def set_venue_name(self, venue_name):
        self.venue_name = venue_name
    @get_address.setter
    def set_address(self, address):
        self.address = address
