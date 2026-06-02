"""Exercise 4: JSON Config Reader

Given a JSON config file like:

{
    "app_name": "PyWeek",
    "version": "1.0",
    "settings": {
        "theme": "dark",
        "language": "en",
        "notifications": true
    }
}

Write a script that:
1. Reads the JSON file
2. Prints a formatted summary
3. Allows querying specific keys: python ex_04_json_config.py config.json version
4. Handles errors (file not found, invalid JSON, key not found)

Usage: python ex_04_json_config.py config.json [key]
"""
