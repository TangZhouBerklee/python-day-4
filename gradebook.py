gradebook = {
    "Jacob" : "A",
    "Adele" : "B",
    "Emma" : "C",
}
prompt = input("What is the student's name")
if gradebook.get(prompt):
        print(gradebook[prompt])
else:
        print("Student not found.")