students = {
    "ANU": 340,
    "TEENA": 458,
    "John": 300
}
asc_by_name = dict(sorted (students.items()))
print("sorted_by_Name (Ascending):")
print(asc_by_name)
desc_by_name = dict(sorted (students.items(), reverse=True))
print("sorted_by_Name (Descending):")
print(desc_by_name)
