products = [("phone", 5, 300), ("laptop", 0, 1000), ("tablet", 3, 200), ("headphones", 10, 50)]
res = []
for name, count, price in products:
    if count > 0:
        final_ops = count * price
        res.append((name, final_ops))
print(res)