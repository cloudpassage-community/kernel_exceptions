import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../', 'lib/controllers'))
from version_comparator import VersionComparator

class TestVersionComparator:
    def create_version_comp_obj(self):
        vc = VersionComparator()
        return vc

    def test_compare(self):
        vc = self.create_version_comp_obj()
        assert vc.compare('3.100.0-514.el7.x86_64', '3.12.el7')
        assert vc.compare('3.18.0-514.el7.x86_64', '3.10.0-514.el7')
        assert vc.compare('3.18.0-514.el8.x86_64', '3.10.0-514.el7')
        assert vc.compare('3.10.0-514.el7', '3.10.0-514.el7.x86_64') == False
        assert vc.compare('3.12.el7', '3.100.0-514.el7.x86_64') == False
        assert vc.compare('3.10.0-514.el7', '3.18.0-514.el7.x86_64') == False
        assert vc.compare('3.10.0-514.el7', '3.18.0-514.el8.x86_64') == False
