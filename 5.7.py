import json

with open('5.7.txt') as read_file:
    text = read_file.readlines()
all_revenue = 0
end_result = list()
results = dict()
profitable_company_count = 0
for info in text:
    company,company_type, revenue, costs = info.split(' ')
    results[company] = int(revenue) - int(costs)
    if results[company] > 0:
        all_revenue += results[company]
        profitable_company_count +=1
end_result.append(results)
end_result.append({'average_profit':all_revenue/profitable_company_count})

with open('5.7.json',mode='w') as f:
    json.dump(end_result, f)






