# conv_neg_pos_nocomp.py
a_list = [7, 5, -4, 6]
def check_negative(z):
  result = []
  for item in z:
    if item < 0:
      result.append(item * -1)
      return result
print(check_negative(a_list))
a_list = [7, 5, -4, 6]
print([-x for x in a_list if x < 0][:1])