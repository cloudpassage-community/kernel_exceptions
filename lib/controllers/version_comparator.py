import re


class VersionComparator(object):
    @staticmethod
    def remove_arch(s):
        return s.replace('.x86_64', '')

    @staticmethod
    def evr(s):
        found_el = re.search('el\d+', s)
        found_fc = re.search('fc\d+', s)
        if found_el:
            return found_el.group(0)
        elif found_fc:
            return found_fc.group(0)

    @staticmethod
    def normalize(version):
        nums = []
        for v in version:
            try:
                nums.append(int(v))
            except:
                pass
        return nums

    def cut(self, s):
        s = self.remove_arch(s)
        return re.split('\.|-', s)

    def partition_comparison(self, a, b):
        for i in range(len(a)):
            try:
                if (a[i] - b[i]) > 0:
                    return a[i] > b[i]
            except IndexError:
                return True
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
