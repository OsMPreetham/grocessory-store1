class GroceryStoreInventory:
    def __init__(self):
        self.inventory = {}

    def add_product(self, name, quantity, price):
        if name in self.inventory:
            self.inventory[name]['quantity'] += quantity
            self.inventory[name]['price'] = price
        else:
            self.inventory[name] = {
                'quantity': quantity,
                'price': price
            }

    def remove_product(self, name, quantity):
        if name in self.inventory and self.inventory[name]['quantity'] >= quantity:
            self.inventory[name]['quantity'] -= quantity
            if self.inventory[name]['quantity'] <= 0:
                del self.inventory[name]
            return True
        return False

    def update_price(self, name, price):
        if name in self.inventory:
            self.inventory[name]['price'] = price
            return True
        return False

    def get_product_info(self, name):
        return self.inventory.get(name)

    def list_inventory(self):
        for name, details in self.inventory.items():
            print(f"{name}: {details['quantity']} units at ${details['price']} each")

def main():
    store = GroceryStoreInventory()
    store.add_product('Apples', 100, 0.99)
    store.add_product('Bananas', 150, 0.39)
    store.add_product('Oranges', 80, 1.29)

    store.list_inventory()

    print("\nRemoving 30 Bananas...")
    store.remove_product('Bananas', 30)
    store.list_inventory()

    print("\nUpdating Apples price to $1.09...")
    store.update_price('Apples', 1.09)
    store.list_inventory()

    print("\nGetting information for Oranges...")
    oranges_info = store.get_product_info('Oranges')
    print(oranges_info)

if __name__ == '__main__':
    main()
