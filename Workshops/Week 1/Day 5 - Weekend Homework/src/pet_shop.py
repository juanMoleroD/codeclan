# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop['admin']["total_cash"]

def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount

def get_pets_sold(pet_store):
    return pet_store["admin"]["pets_sold"]

def increase_pets_sold(pet_store, amount):
    pet_store["admin"]["pets_sold"] =+ amount

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, search_breed):
    pets_by_breed = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == search_breed:
            pets_by_breed.append(pet)
    return pets_by_breed

def find_pet_by_name(pet_shop, search_name):
    pets_by_name = []
    for pet in pet_shop["pets"]:
        if pet["name"] == search_name:
            return pet

def remove_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            pet_shop["pets"].remove(pet)

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, amount):
    customer["cash"] -= amount

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

def customer_can_afford_pet(customer, pet):
    return customer["cash"] >= pet["price"]

def sell_pet_to_customer(pet_shop, pet, customer):
    remove_customer_cash(customer, pet["price"])
    add_or_remove_cash(pet_shop, pet["price"])
    increase_pets_sold(pet_shop, 1)
    add_pet_to_customer(customer, pet)
    remove_pet_by_name(pet_shop, pet["name"])