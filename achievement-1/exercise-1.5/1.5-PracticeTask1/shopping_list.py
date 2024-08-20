class ShoppingList(object):
    def __init__(self, list_name): 
        self.list_name = list_name
        self.shopping_list = []

    def add_item(self, item):
        if not item in self.shopping_list:
            self.shopping_list.append(item)

    def remove_item(self, item):
        try:
            self.shopping_list.remove(item)
        except:
            print('Item not found.')

    def view_list(self):
        if not self.shopping_list:
            print("The shopping list is empty.")
        else:
            print(f"{self.list_name}:")
            for index, item in enumerate(self.shopping_list, start=1):
                print(f"{index}. {item}")

    def merge_lists(self, obj):
        # Creating a name for the new, merged shopping list
        merged_lists_name = f"Merged List - {self.list_name} + {obj.list_name}"
        # Creating an empty ShoppingList object
        merged_lists_obj = ShoppingList(merged_lists_name)
        # Adding the first shopping list's items to the new list
        merged_lists_obj.shopping_list = self.shopping_list.copy()

        for item in obj.shopping_list:
            if not item in merged_lists_obj.shopping_list:
              merged_lists_obj.shopping_list.append(item)

        return merged_lists_obj
    
def main():
    pet_store_list = ShoppingList("Pet Store Shopping List")
    pet_store_list.add_item('dog food')
    pet_store_list.add_item('frisbee')
    pet_store_list.add_item('bowl')
    pet_store_list.add_item('collars')
    pet_store_list.add_item('flea collars')

    pet_store_list.remove_item('flea collars')

    pet_store_list.add_item('frisbee')

    pet_store_list.view_list()

    pet_store_list = ShoppingList('Pet Store List')
    grocery_store_list = ShoppingList('Grocery Store List')

    for item in ['dog food', 'frisbee', 'bowl', 'collars', 'flea collars']:
        pet_store_list.add_item(item)

    for item in ['fruits' ,'vegetables', 'bowl', 'ice cream']:
        grocery_store_list.add_item(item)

    merged_list = ShoppingList.merge_lists(pet_store_list, grocery_store_list)
    # or 
    # grocery_store_list.merge_lists(pet_store_list)
    # or
    # pet_store_list.merge_lists(grocery_store_list)
    merged_list.view_list()

if __name__ == "__main__":
    main()