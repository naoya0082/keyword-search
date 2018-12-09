data = [["k1", 100],
        ["k2", 200],
        ["k3", 300],
        ]

line_numbers = list(range(2, 2 + len(data)))

for idx, num in enumerate(line_numbers):
    print(f"{num}行目 2列:", data[idx][0])
    print(f"{num}行目 3列:", data[idx][1])

print("-------------------------------------------")

members = ["Bob", "Tom", "Ken"]
for idx, members in enumerate(members):
    print(idx, members)
