shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    menu_count=len(menus)
    menu_order=menus+orders
    # print(menu_order)
    menu_order_set=set(menus+orders)
    menu_order_set_count=len(menu_order_set)
    # print(menu_order_set)
    if menu_count==menu_order_set_count:
        return True
    else:
        return False






result = is_available_to_order(shop_menus, shop_orders)
print(result)