clients = {'c1': [600, 300], 'c2': [200, 100], 'c3': [1000,500], 'c4': [400, 200]}
categories = {'высокий': [] ,'средний': [], 'низкий': []}
sort_sum = []
for client_id, score in clients.items():
    total = sum(score)
    sort_sum.append((client_id, total))

sort_sum.sort(key=lambda x: x[1], reverse=True)

if sort_sum:
    max_total = sort_sum[0][1]
    min_total = sort_sum[-1][1]
    vish = max_total * 0.7
    min = max_total * 0.5

    for client_id, total in sort_sum:
        if total >= vish:
            categories['высокий'].append(client_id)
        elif total >= min:
            categories['средний'].append(client_id)
        else:
            categories['низкий'].append(client_id)

print(categories)