inv = {}


class Product:
    def __init__(self, category, name, price, ):
        self.category = category
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.category} {self.name}"


class Store():
    def __init__(self, inv='', income=0):
        self.inv = inv
        self.income = income
        self.set_inventory_info()

    def get_income(self):
        print(f'Total budget: {self.income}')

    def set_item_description(self, item):
        item.description = f'''\
{'_' * 30}
Category:   {item.category}
Name:       {item.name}
Price:      ${item.price}
Q-ty:       {item.qty} pcs
TTL Cost:   ${item.price * item.qty}'''
        return item.description

    def get_product_info(self, product_name):
        print(product_name.description)

    def get_all_products(self):
        for item in self.inv:
            if item.qty > 0:
                print(item.description)

    def add_item(self, new_product='', quantity=0, price_premium=30):
        if not new_product and not quantity:
            print('What item do you want to add?')
            category = input('Enter category: ')
            name = input('Enter name: ')
            price = float(input('Enter price: ')) * (
                        (100 - price_premium) / 100)
            quantity = int(input('Enter q-ty: '))
            new_product = Product(category, name, price)
        elif not quantity:
            print(f'How many "{new_product}" have we received? ')
            quantity = int(input('Enter q-ty: '))

        deal_cost = new_product.price * quantity
        if self.income >= deal_cost:
            self.income -= deal_cost
            try:
                new_product.qty = quantity + inv[new_product]
            except KeyError:
                new_product.qty = quantity
            inv[new_product] = new_product.qty
            self.set_inventory_info()
            print(f'''\n\
{quantity} pieces of "{new_product.name}" was bought for total ${deal_cost},
with discount of {price_premium}%.
Product "{new_product}" was successfully added / amended in the category "{new_product.category}". 
Total there is {new_product.qty} pcs of "{new_product.name}" now.''')
            return new_product
        elif self.income < deal_cost:
            print(f"Sorry, you don't have sufficient money to close the deal "
                  f"of buying {quantity} of '{new_product}''!")

    def item_search(self, identifier='', identifier_type='name'):
        i = 0
        result = []
        if not identifier:
            identifier_type = input(
                "Enter what you will be looking for (Enter 'c' for Category, "
                "'t' for Type or 'n' for Name): ").lower()
            identifier = input('Enter what you wish to find: ').lower()
        if identifier_type == 'n':
            for item in self.inv:
                if item.name.lower() == identifier:
                    result.append(item)
                    i += 1
                    print(
                        f'Found "{item.name}" in category "{item.category}".')
        elif identifier_type == 't':
            for item in self.inv:
                if item.type.lower() == identifier:
                    result.append(item)
                    i += 1
                    print(f'Found "{item.name}" in category "{item.type}".')
        elif identifier_type == 'c':
            for item in self.inv:
                if item.category.lower() == identifier:
                    result.append(item)
                    i += 1
                    print(
                        f'Found "{item.name}" in category "{item.category}".')
        if i < 1:
            print(
                f'Sorry, "{identifier}" was not found in "{identifier_type}". Try again. ')
        return result

    def sell_product(self, sold_product='', quantity=1):
        products = []
        print('We are going to sell...')
        if sold_product:
            products.append(sold_product)
        if not sold_product:
            products = self.item_search()
        for item in products:
            if quantity <= 1:
                quantity = int(
                    input(f'\nHow many "{item.name}" have you sold? '))
            if item.qty >= quantity:
                inv[item] -= quantity
                item.qty -= quantity
                self.set_inventory_info()
                print(
                    f'\nProduct was sold and now there is {inv[item]} of "{item.name}" in stock.')
                self.income = self.income + item.price * quantity
            elif item.qty < quantity:
                print(
                    f'\nSorry, seems like you don\'t have enough "{item}" to '
                    f'sell.')
                decision = input('Do you wish to sell it all? [Y/N]: ').lower()
                if decision == 'y':
                    quantity = item.qty
                    self.income = self.income + item.price * item.qty
                    item.qty = 0
                    inv[item] = 0
                    self.set_inventory_info()
                    print(
                        f'\nEverything was sold and now there is {inv[item]} "{item.name}" in stock.')
                if decision == 'n':
                    continue
            quantity = 0

    def remove_spoiled_product(self, spoiled_product='', quantity=1):
        products = []
        print('Now we are going to throw...')
        if spoiled_product:
            products.append(spoiled_product)
        if not spoiled_product:
            products = self.item_search()
        for item in products:
            if quantity <= 1:
                quantity = int(input(
                    f'How many "{item.name}" have you spoiled and have to be '
                    f'thrown away? '))
            if item.qty >= quantity:
                inv[item] -= quantity
                item.qty -= quantity
                self.set_inventory_info()
                print(
                    f'Product was spoiled and removed. Now there is {inv[item]} of "{item.name}" in stock.')
            elif item.qty < quantity:
                print(
                    f'Sorry, seems like you don\'t have enough "{item}" to '
                    f'throw away.')
                decision = input(
                    'Do you wish to throw it all away? [Y/N]: ').lower()
                if decision == 'y':
                    quantity = item.qty
                    item.qty = 0
                    inv[item] = 0
                    self.set_inventory_info()
                    print(
                        f'Everything was thrown away and now there is {inv[item]} "{item.name}" in stock.')
                if decision == 'n':
                    continue
            quantity = 0

    def set_discount(self, discount_product='', percent=0):
        products = []
        print('We are going to apply discount on something...')
        if discount_product:
            products.append(discount_product)
        if not discount_product:
            products = self.item_search()
        for item in products:
            if not percent:
                percent = int(
                    input(f'Enter the % of discount on "{item}": '))
            if percent > 100:
                print('It is impossible to have a discount over 100%!')
                continue
            item.price = item.price * ((100 - percent) / 100)
            self.set_inventory_info()
            print(
                f'Price of "{item}" was discounted by {percent}% and set to ${item.price}')
            percent = 0
