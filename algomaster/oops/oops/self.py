class Product:
    def describe(self):
        print(f"{self.name} costs ${self.price}")

product_a = Product()
product_a.name = "Wireless Mouse"
product_a.price = 29.99

product_b = Product()
product_b.name = " Mouse"
product_b.price = 20.99

Product.describe(product_a)
Product.describe(product_b)