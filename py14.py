# QUESTION 6

class Product:
    count = 0

    def __init__(self, name, material, costPrice):
        self.name = name
        self.material = material
        self.costPrice = costPrice
        Product.count += 1
        print(f"Count of products - {Product.count}")
        if self.material == "Metal":
            self.discount = 0.20 * self.costPrice
        elif self.material == "Plastic":
            self.discount = 0.10 * self.costPrice

    def sellingPrice(self):
        print(
            f"Selling Price of {self.name} is :- {self.costPrice-self.discount}")

    def display(self):
        print(
            f"Name of the product - {self.name}\nMaterial of Product - {self.material}\nPrice - {self.costPrice-self.discount}")


Product1 = Product('Plate', 'Metal', 170)
Product2 = Product('Spoon', 'Plastic', 26)

print("\n")

Product1.sellingPrice()
print("\n")
Product2.sellingPrice()
print("\n")
Product1.display()
Product2.display()

print(f"Count - {Product.count}")
