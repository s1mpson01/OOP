# import json


class Product:
    """Класс продукт"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс категории"""

    name: str
    description: str
    product: list
    product_count = 0
    category_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.product_count += 1
        Category.category_count = len(products)


# pr_1 = Product("a12", "With two cams", 2000.5, 30)
# cat_1 = Category("Mobile phone", "Samsung brand", ["a12", "a22", "a51"])
# print(Category.category_count)
# cat_2 = Category("Mobile phone", "iPhone brand", product="pr_1")
# print(Category.category_count)
# print(Category.__dict__)
# print(cat_2.__dict__)
# print(dir(pr_1))

# def get_obj_from_json():
#     try:
#         with open("../data/products.json") as file:
#             json_data = json.load(file)
#     except json.JSONDecodeError:
#         raise Exception("Файл не Json")
#     except FileNotFoundError:
#         raise Exception("Файл не найден")
#
#     else:
#         categories = []
#         product = []
#
#         for category_data in json_data:
#             for product_data in category_data["products"]:
#                 product.append(Product(**product_data))
#             categories.append(Category(**category_data))
#
#         return categories, product
# ww = get_obj_from_json()
# print(ww[0])
# print(ww[1])
