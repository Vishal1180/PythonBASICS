def sort_dict_by_value(d, reverse = False):
  return dict(sorted(d.items(), key = lambda x: x[1], reverse = reverse))
print("Original dictionary elements:")
colors = {'Red': 1, 'Green': 3, 'Black': 5, 'White': 2, 'Pink': 4}
print(colors)
print("\nSort (ascending) the said dictionary elements by value:")
print(sort_dict_by_value(colors))
print("\nSort (descending) the said dictionary elements by value:")
print(sort_dict_by_value(colors, True))
