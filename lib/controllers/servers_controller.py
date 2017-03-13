from ..classes.api import Api
import re


class ServersController(object):
    def __init__(self):
        self.api = Api()

    def server_show(self, server_id):
        return self.api.get("/v2/servers/%s" % server_id)

    def installed_kernels(self, server_id):
        found = []
        vulns = self.api.get("/v1/servers/%s/svm" % server_id)
        for vuln in vulns['scan']['findings']:
            match = re.search('^Kernel$', vuln['package_name'])
            if match:
                found.append(vuln)
        return found

    def extra_kernels(self, server_id):
        server = self.server_show(server_id)['server']
        kernels = self.installed_kernels(server_id)
        for kernel in kernels:
            if kernel['package_version'] in server['kernel_release']:
                kernels.remove(kernel)
        return kernels
