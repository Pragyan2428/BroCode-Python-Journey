# A dictionary is a collection of key-value pairs.

# Keys:
# A key is a unique identifier used to access its corresponding value.looks like a list.

# Values:
# A value is the data associated with a key.looks like a list

# Item:
# An item is a key-value pair represented as a tuple, e.g. ("Name", "Pragyan").

# Dictionary Methods:
# dictionary.get(key)       -> Returns the value for the key, or None if the key doesn't exist.
# dictionary.pop(key)       -> Removes the specified key and returns its value.
# dictionary.update({...})  -> Adds new key-value pairs or updates existing ones.
# dictionary.popitem()      -> Removes and returns the last inserted key-value pair.
# dictionary.clear()        -> Removes all items from the dictionary.

def main():
    me = {
        "Name": "Pragyan",
        "Roll": "2430048"
    }

    # print(me.get("Name"))
    # print(me.keys())
    # print(me.values())

    # me.update({"Phone Number": "8353958170"})
    # print(me.pop("Name"))
    # print(me.popitem())
    # print(me.items())
    # print(me)
    for key in me.keys():
        print(key)
    print("---------")
    for value in me.values():
        print(value)
    print("---------")
    for items in me.items():
        print(items)
    print("---------")
    for keys,values in me.items():
        print(f"{keys}:{values}")
main()