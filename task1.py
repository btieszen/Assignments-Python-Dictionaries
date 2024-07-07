#1. Real-World Python Dictionary Applications
#Task 1: Restaurant Menu Update You are given an initial structure of a restaurant menu stored in a nested dictionary. Your task is to update this menu based on given instructions
#- Add a new category called "Beverages" with at least two items.

#- Update the price of "Steak" to 17.99.

#- Remove "Bruschetta" from "Starters". 

print(f" The Original menu was:")
print(f" Starters: Soup: 5.99, Bruschetta: 6.50")
print(f"Main Course: Steak: 15.99, Salmon: 13.99")
print(f"Desserts: Cake: 4.99, Ice Cream: 3.99")
print(f"The updated menu is :")

def add_catagory(menu, catagory):
    if catagory not in menu:
        menu [catagory] =[]
        print(f"Catagory '{catagory}', added to the menu")
    else:
        print(f"Catagory '{catagory}' already exist")
def add_items(menu,catagory,item,):
    if catagory in menu:
        if item not in menu[catagory]:
            menu[catagory].append(item)
def display_menu(menu):
    for catagory, items in menu.items():
        print(f"{catagory}:{items}.")
        
    

            
        
restaurant_menu = {"Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}}

add_catagory(restaurant_menu,"Beverages")        
add_items(restaurant_menu,"Beverages","Tea: 1.79")
add_items(restaurant_menu,"Beverages","Soda: 1.99")
del restaurant_menu["Starters"]["Bruschetta"]
restaurant_menu["Main Course"]["Steak"] = 17.99


display_menu(restaurant_menu)
             


            
        
         
    












