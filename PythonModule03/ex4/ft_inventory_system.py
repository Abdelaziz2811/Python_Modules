def display_inventory(inventory: dict) -> None:
    """Display player inventory contents with value calculations."""
    username = inventory["username"]
    print(f"=== {username}'s Inventory ===")

    inventory_value = 0
    item_count = 0
    categories_count = {}

    for item, data in inventory.items():
        if item == "username":
            continue

        category = data["category"]
        rarity = data["rarity"]
        quantity = data["quantity"]
        price = data["price"]

        inventory_value += price * quantity
        item_count += quantity

        if category in categories_count:
            categories_count[category] += quantity
        else:
            categories_count[category] = quantity

        print(f"{item} ({category}, {rarity}): {quantity}x @ "
              f"{price} gold each = {quantity * price} gold")

    print(f"\nInventory value: {inventory_value} gold")
    print(f"Item count: {item_count} items")
    print("Categories: ", end="")
    counter = 1
    for category, count in categories_count.items():
        if counter < len(categories_count):
            print(f"{category}({count}), ", end="")
        else:
            print(f"{category}({count})")
        counter += 1


def trade_items(
        trader_inv: dict, owner_inv: dict, item: str, amount: int
        ) -> None:
    """Transfer items between two players inventories."""
    if item not in trader_inv:
        print("item cannot be found!")
        return

    trader = trader_inv["username"]
    owner = owner_inv["username"]

    print(f"\n=== Transaction: {trader} gives {owner} {amount} {item}s ===")
    if trader_inv[item]["quantity"] >= amount:
        trader_inv[item]["quantity"] -= amount
        if item not in owner_inv:
            owner_inv[item] = trader_inv[item].copy()
            owner_inv[item]["quantity"] = 0
        owner_inv[item]["quantity"] += amount
        print("Transaction successful!")

        print("\n=== Updated Inventories ===")
        trader_item_count = trader_inv[item]["quantity"]
        owner_item_count = owner_inv[item]["quantity"]
        print(f"{trader} {item}s: {trader_item_count}")
        print(f"{owner} {item}s: {owner_item_count}")

        if trader_inv[item]["quantity"] == 0:
            del trader_inv[item]
    else:
        print("Not enough amount on trader's inventory!")


def inventory_analytics(inventories: list) -> None:
    """Analyze multiple inventories and find most valuable player"""
    print("\n=== Inventory Analytics ===")

    players_gold = {}
    players_items = {}
    rare_items = []

    for inv in inventories:
        player = inv["username"]
        players_gold[player] = 0
        players_items[player] = 0

        for item, data in inv.items():
            if item == "username":
                continue

            players_gold[player] += data["price"] * data["quantity"]
            players_items[player] += data["quantity"]
            if data["rarity"] == "rare":
                rare_items.append(item)

    gold_count = 0
    item_count = 0

    for player in players_gold:
        if players_gold[player] > gold_count:
            gold_count = players_gold[player]
            most_valuable_player = player

    for player in players_items:
        if players_items[player] > item_count:
            item_count = players_items[player]
            player_with_most_items = player

    print(f"Most valuable player: {most_valuable_player} ({gold_count} gold)")
    print(f"Most items: {player_with_most_items} ({item_count} items)")
    rarest_items = ", ".join(rare_items)
    print(f"Rarest items: {rarest_items}")


def inventory_system() -> None:
    """Main function to demonstrate dict operations"""
    print("=== Player Inventory System ===\n")
    alice_inventory = {
        "username": "Alice",
        "sword": {
            "category": "weapon",
            "rarity": "rare",
            "quantity": 1,
            "price": 500
        },
        "potion": {
            "category": "consumable",
            "rarity": "common",
            "quantity": 5,
            "price": 50
        },
        "shield": {
            "category": "armor",
            "rarity": "uncommon",
            "quantity": 1,
            "price": 200
        }
    }
    bob_inventory = {
        "username": "Bob",
        "magic_ring": {
            "category": "accessory",
            "rarity": "rare",
            "quantity": 1,
            "price": 500
        }
    }

    display_inventory(alice_inventory)
    trade_items(alice_inventory, bob_inventory, "potion", 2)
    inventory_analytics([alice_inventory, bob_inventory])


if __name__ == "__main__":
    inventory_system()
