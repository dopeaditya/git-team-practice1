users = ["Mitsuo", "Sumire", "Kiteretsu", "Miyoko", "Perman", "Pako", "Machiko"]

for user in users:
    print(f"--> {user}")

name = input("Enter the name:- ")

print(f"Is {name} present in users => {name in users}")