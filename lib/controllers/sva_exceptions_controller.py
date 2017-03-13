from ..classes.api import Api
from ..options import Options


class ExceptionsController(object):
    def __init__(self):
        self.api = Api()
        self.options = Options()

    def form(self, **kwargs):
        body = {
            'cve_exception': {
                'package_name': kwargs['package_name'],
                'package_version': kwargs['package_version'],
                'length': self.options['expires_in'],
                'scope': 'server',
                'server_id': kwargs['server_id'],
                'cve_entries': kwargs['cve_entries']
            }
        }
        return body

    def create_exception(self, body):
        return self.api.post('/v1/cve_exceptions', body)

    def cve_entries(self, kernel):
        cves = []
        for cve_entry in kernel['cve_entries']:
            cves.append(cve_entry['cve_entry'])
        return cves

    def add_exceptions(self, srv, kernels):
        for kernel in kernels:
            body = self.form(package_name=kernel['package_name'],
                             package_version=kernel['package_version'],
                             server_id=srv['id'],
                             cve_entries=self.cve_entries(kernel))
            self.create_exception(body)
