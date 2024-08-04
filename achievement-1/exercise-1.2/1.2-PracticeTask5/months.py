months_named = ['January', 'February', 'March', 'April', 'May', 'June',
                'July', 'August', 'September', 'October', 'November', 'December']

months_numbered = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# months_dict = dict(zip(months_named, months_numbered));
months_dict = {k:v for k, v in zip(months_named, months_numbered)}
print(months_dict)

months_lst = list(months_dict.items())
print(months_lst)

months_numbered.clear()
months_named.clear()
print('Numbers', months_numbered)
print('Months', months_named)
print('After clearing months_numbered and months_named:\n', months_dict)

months_extracted = list(months_dict.keys())
print('Extracted Months', months_extracted)