types = ['(л)','(пр)','(лаб)']
file = open('5.6.txt',encoding='utf-8')
text = file.readlines()
file.close()
result = dict()
for i in text:
    subject,activity_types = i.split(':')
    result[subject] = 0
    clear = activity_types.strip().replace('.','')
    activity_types_list = clear.split(' ')

    for activity_type in activity_types_list:
        need_add = False
        for work_type in types:
            if work_type in activity_type:
                clear_hour =activity_type.replace(work_type,'')
                need_add = True
                break
        if need_add:
            result[subject] += int(clear_hour)

print(result)






