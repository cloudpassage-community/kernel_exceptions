import re


class VersionComparator(object):
    @staticmethod
    def remove_arch(s):
        return s.replace('.x86_64', '')

    @staticmethod
    def evr(s):
        found = re.search('el\d+', s)
        if found:
            return found.group(0)

    @staticmethod
    def normalize(version):
        nums = []
        for v in version:
            try:
                nums.append(int(v))
            except:
                pass
        return nums

    @staticmethod
    def insert_zeroes(data, size):
        data.extend([0] * size)
        return data

    def equalize_lengths(self, a, b):
        len_a = len(a)
        len_b = len(b)
        if len_a == len_b:
            return a, b
        elif len_a > len_b:
            b = self.insert_zeroes(b, len_a - len_b)
            return a, b
        else:
            a = self.insert_zeroes(a, len_b - len_a)
            return a, b

    def cut(self, s):
        s = self.remove_arch(s)
        return re.split('\.|-', s)

    def partition_comparison(self, a, b):
        a, b = self.equalize_lengths(a, b)
        for i in a:
            j = b[a.index(i)]
            if i != j:
                return int(i) > int(j)
        return False

    def compare(self, a, b):
        evr_a = self.evr(a)
        evr_b = self.evr(b)
        a = self.normalize(self.cut(a))
        b = self.normalize(self.cut(b))
        if not evr_a or not evr_b:
            return self.partition_comparison(a, b)
        if evr_a == evr_b:
            return self.partition_comparison(a, b)
        return evr_a > evr_b
