def create_building_from_information_from_dict(info):
    return Building(
        name=info.get("name"),
        floors=info.get("floors"),
        address=info.get("address"),
        price=info.get("price")
    )


class Building:
    def __init__(self, name, floors, address, price):
        self.seller_name = name
        self.floors = floors
        self.address = address
        self.price = price


    def get_description(self):
        return f"Seller: {self.seller_name}\nBuilding Details:\n- Floors: {self.floors}\n- Address: {self.address}\n- Price: ${self.price}"

    def update_price(self, new_price):
        self.price = new_price

    def get_price(self):
        return self.price

