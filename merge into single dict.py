contacts1 = {
    "ANU": "9087654321",
    "TEENA":"8977653727"
}
contacts2 = {
    "John": "8907654321",
    "priya": "8977653427"
}
print("contact1:",contacts1)
print("contact2:",contacts2)
merged_contacts = contacts1.copy()
merged_contacts.update(contacts2)
print("merged_contacts:")
print(merged_contacts)