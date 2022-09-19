class Mathematician:
    def __init__(self, nums):
        self.nums = nums

    def square_nums(self):
        squared = []
        for i in self.nums:
            squared.append(i ** 2)
        return squared

    def remove_positives(self):
        removed = []
        for i in self.nums:
            if i < 0:
                removed.append(i)
        return removed

    def filter_leaps(self):
        filtered = []
        for i in self.nums:
            if i % 4 == 0:
                if i % 100 == 0:
                    if i % 400 == 0:
                        filtered.append(i)
                    continue
                filtered.append(i)
            continue
        return filtered

# m = Mathematician([7, 11, 5, 4])
# print(m.square_nums())
# m = Mathematician([26, -11, -8, 13, -90])
# print(m.remove_positives())
# m = Mathematician([2001, 1884, 1995, 2003, 2020])
# print(m.filter_leaps())

# assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
#
# assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
#
# assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
