#dictionaries
#key values
customer = {
    "name":"John Smith",
    "age":30,
    "is_verified":True
}
#returns the value associated with the key
print(customer["name"])
#use get to no receive error when it doesnt exist
print(customer.get("birthdate"))

# None = Null
#add new key value
customer["birthdate"]="Jan 1 1990"
print(customer["birthdate"])

# creates a dictionary to replace input numbers for their word name
phone = input("Phone: ")
digit_mapping = {
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four"
}
output = ""
for ch in phone:
    output += digit_mapping.get(ch,"!")+" "
print(output)


#split string into single words
message = input(">")
words = message.split(" ")
print(words)









