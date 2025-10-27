"""Inventory Management System - Clean and Pylint Compliant Version."""

import json
import logging
from datetime import datetime
from typing import Dict, List

# Configure logging once
logging.basicConfig(
    filename="inventory.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Global inventory dictionary
stock_data: Dict[str, int] = {}


def add_item(item: str, qty: int, logs: List[str] | None = None) -> None:
    """Add an item and its quantity to the inventory."""
    if logs is None:
        logs = []
    if not isinstance(item, str) or not isinstance(qty, int):
        logging.warning("Invalid types for add_item: %s, %s", type(item), type(qty))
        return
    if qty <= 0:
        logging.warning("Quantity must be positive for add_item: %s = %d", item, qty)
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    message = f"Added {qty} of {item}"
    logs.append(f"{datetime.now()}: {message}")
    logging.info(message)


def remove_item(item: str, qty: int) -> None:
    """Remove a specific quantity of an item from the inventory."""
    if not isinstance(item, str) or not isinstance(qty, int):
        logging.warning("Invalid types for remove_item: %s, %s", type(item), type(qty))
        return
    if qty <= 0:
        logging.warning("Quantity must be positive for remove_item: %s = %d", item, qty)
        return
    if item not in stock_data:
        logging.warning("Attempted to remove non-existing item: %s", item)
        return

    stock_data[item] -= qty
    if stock_data[item] <= 0:
        del stock_data[item]
        logging.info("Removed all of %s from inventory", item)
    else:
        logging.info("Removed %d of %s", qty, item)


def get_qty(item: str) -> int:
    """Return the quantity of a specific item."""
    return stock_data.get(item, 0)


def load_data(filename: str = "inventory.json") -> None:
    """Load inventory data from a JSON file."""
    global stock_data
    try:
        with open(filename, "r", encoding="utf-8") as file:
            stock_data = json.load(file)
        logging.info("Inventory data loaded successfully.")
    except FileNotFoundError:
        logging.warning("No inventory file found. Starting with empty inventory.")
        stock_data = {}
    except json.JSONDecodeError:
        logging.error("Error decoding JSON file. Starting with empty inventory.")
        stock_data = {}


def save_data(filename: str = "inventory.json") -> None:
    """Save inventory data to a JSON file."""
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(stock_data, file, indent=4)
        logging.info("Inventory data saved successfully.")
    except OSError as error:
        logging.error("Failed to save data: %s", error)


def print_data() -> None:
    """Print all inventory items."""
    print("Items Report:")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold: int = 5) -> List[str]:
    """Return items that are below a given stock threshold."""
    return [item for item, qty in stock_data.items() if qty < threshold]


def main() -> None:
    """Main program execution."""
    load_data()
    add_item("apple", 10)
    add_item("banana", 2)
    add_item("orange", 1)
    remove_item("apple", 3)
    remove_item("grapes", 2)
    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")
    save_data()
    print_data()


if __name__ == "__main__":
    main()
