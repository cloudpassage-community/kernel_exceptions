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
    def mark_sets(a, b):
        if len(a) > len(b):
            return {'primary': b, 'secondary': a}
        else:
            return {'primary': a, 'secondary': b}

    def cut(self, s):
        s = self.remove_arch(s)
        return re.split('\.|-', s)

    def merge_comparison(self, a, b):
        sets = self.mark_sets(a, b)
        results = []
        for i in sets['primary']:
            j = sets['secondary'][sets['primary'].index(i)]
            if i != j:
                results.append(int(i) > int(j))

        if not results:
            return False
        else:
            return True

    def compare(self, a, b):
        evr_a = self.evr(a)
        evr_b = self.evr(b)
        a = self.normalize(self.cut(a))
        b = self.normalize(self.cut(b))
        if not evr_a or not evr_b:
            return self.merge_comparison(a, b)
        if evr_a == evr_b:
            return self.merge_comparison(a, b)
        return evr_a > evr_b
