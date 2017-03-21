import re


class VersionComparator(object):
    @staticmethod
    def evr(s):
        found_el = re.search('el\d+', s)
        found_fc = re.search('fc\d+', s)
        if found_el:
            return found_el.group(0)
        elif found_fc:
            return found_fc.group(0)

    def cut(self, s):
        return re.split('\.|-', re.split('.[a-z]', s)[0])

    def partition_comparison(self, a, b):
        for i in range(len(a)):
            try:
                if (int(a[i]) - int(b[i])) > 0:
                    return int(a[i]) > int(b[i])
            except IndexError:
                return True
        return False

    def compare(self, a, b):
        evr_a = self.evr(a)
        evr_b = self.evr(b)
        a = self.cut(a)
        b = self.cut(b)
        if not evr_a or not evr_b:
            return self.partition_comparison(a, b)
        if evr_a == evr_b:
            return self.partition_comparison(a, b)
        return evr_a > evr_b
