
# Foor Loop Add Diff
# a = 1000000000
#
# for i in range(1000000):
#     a += 1e-6
#
# print(a - 1000000000)


# Numpy Math

import numpy as np

values = [1,2,3,4,5]
values = np.array(values) + 5

a = np.array([[1,3],[5,7]])
a
# displays the following result:
# array([[1, 3],
#        [5, 7]])
c = np.array([[2,3,6],[4,5,9],[1,8,7]])
c
# displays the following result:
# array([[2, 3, 6],
#        [4, 5, 9],
#        [1, 8, 7]])

a.shape
# displays the following result:
#  (2, 2)

c.shape
# displays the following result:
#  (3, 3)

a + c
# displays the following error:
# ValueError: operands could not be broadcast together with shapes (2,2) (3,3)
