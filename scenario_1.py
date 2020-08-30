

a = {"SK하이닉스": 22000, "셀트리온": 11000}
print(a)

a["현대차동차"] = 7000
print(a)

print(a.keys())
print(a.values())


for k, v in a.items():
    print(k, v)
