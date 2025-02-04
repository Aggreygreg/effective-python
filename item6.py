# pantry = [
#     ('avocados', 1.25),
#     ('bananas', 2.5),
#     ('cherries', 15),
# ]
# for i, (item, count) in enumerate(pantry, start=1):
#     print('#%d: %-10s = %.2f' % (i, item.capitalize(), round(count)))

key = 'my_var'
value = 1.234
old_way = '%-10s = %.2f' % (key, value)
new_way = '%(key)-10s = %(value).2f' % {'key': key, 'value': value}
assert old_way == new_way
print(new_way)
print(old_way)
