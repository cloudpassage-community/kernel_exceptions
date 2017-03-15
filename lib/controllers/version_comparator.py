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
        if self.evr(a) == self.evr(b):
            a = self.normalize(self.cut(a))
            b = self.normalize(self.cut(b))
            if a > b:
                return True
            else:
                return False
