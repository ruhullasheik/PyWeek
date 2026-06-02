"""Exercise 1: Library Catalog

Design a library catalog system.

Classes:
- Item (base): title, year, is_checked_out
- Book(Item): author, pages
- DVD(Item): director, duration (minutes)
- Magazine(Item): issue_number

All items should have:
- check_out() / return_item() methods
- __str__ representation

Create a Library class that:
- Holds a collection of items
- Can add/remove items
- Can search by title (partial match, case-insensitive)
- Can list all checked-out items

Add a few items and demonstrate the system.
"""
