from lib import *


class KernelExceptions(object):
    def __init__(self):
        self.servers = Servers()
        self.options = Options()
        self.sc = ServersController()
        self.ec = ExceptionsController()
        self.vc = VersionComparator()

    def guard(self):
        if not self.options['report'] and not self.options['execute']:
            print 'Please specify --report or --execute'
            exit(0)
        if self.options['execute'] and not self.options['expires_in']:
            print 'Please specify --expires_in=<number of days> if using --execute'
            exit(0)

    def run(self):
        self.guard()
        total = []
        for srv in self.servers.list_all():
            srv_v2 = self.sc.server_show(srv['id'])['server']
            installed_kernels = self.sc.installed_kernels(srv['id'])
            extra_kernels = self.sc.extra_kernels(installed_kernels, srv_v2)
            if extra_kernels:
                total.append(extra_kernels)
                if self.options['execute']:
                    Reporter.report(srv, extra_kernels, srv_v2['kernel_release'])
                    if not self.sc.version_compare(installed_kernels, srv_v2['kernel_release']):
                        self.ec.add_exceptions(srv, extra_kernels)
                        print 'Exceptions for non-running vulnerable kernel packages are added.'
                else:
                    Reporter.report(srv, extra_kernels, srv_v2['kernel_release'])
        if not total:
            print 'No servers with more than one Kernel package has been found'

def main():
    kernel_exception = KernelExceptions()
    kernel_exception.run()


if __name__ == "__main__":
    main()