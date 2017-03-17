from ..classes.api import Api
from version_comparator import VersionComparator
import re


class ServersController(object):
    def __init__(self):
        self.api = Api()
        self.vc = VersionComparator()

    def server_show(self, server_id):
        return self.api.get("/v2/servers/%s" % server_id)

    def installed_kernels(self, server_id):
        found = []
        vulns = self.api.get("/v1/servers/%s/svm" % server_id)
        for vuln in vulns['scan']['findings']:
            match = re.search('^[kK]ernel(\.|$)', vuln['package_name'])
            if match:
                found.append(vuln)
        return found

    def version_compare(self, kernels, running_kernel):
        msg = ""
        for kernel in kernels:
            if self.vc.compare(kernel['package_version'], running_kernel):
                msg = 'warning: newer kernel %s is installed but not running' % kernel['package_version']
                print msg
        return msg

    @staticmethod
    def extra_kernels(installed_kernels, server):
        for kernel in installed_kernels:
            if kernel['package_version'] in server['kernel_release']:
                installed_kernels.remove(kernel)
        return installed_kernels

