import re


class VersionComparator(object):
    @staticmethod
    def remove_arch(s):
        return s.replace('.x86_64', '')

    @staticmethod
    def evr(s):
        return re.search('el\d+', s).group(0)

    @staticmethod
    def normalize(version):
        nums = []
        for v in version:
            try:
                nums.append(int(v))
            except:
                pass

        merged = map(str, nums)
        return ''.join(merged)

    def cut(self, s):
        s = self.remove_arch(s)
        return re.split('\.|-', s)

    def compare(self, a, b):
        evr_a = self.evr(a)
        evr_b = self.evr(b)
        if evr_a == evr_b:
            a = self.normalize(self.cut(a))
            b = self.normalize(self.cut(b))
            if a > b:
                return True
            else:
                return False
        elif evr_a > evr_b:
            return True
        else:
            return False
