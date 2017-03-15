from lib import *


class KernelExceptions(object):
    def __init__(self):
        self.servers = Servers()
        self.options = Options()
        self.sc = ServersController()
        self.ec = ExceptionsController()
        self.vc = VersionComparator()

    def report(self, srv, extra_kernels, running_kernel):
        print 'server %s %s is running kernel version %s' % (srv['id'], srv['server_label'], running_kernel)
        for kernel in extra_kernels:
            msg = "server %s %s has extra %s %s" % (srv['id'], srv['server_label'], kernel['package_name'], kernel['package_version'])
            print msg
            if kernel['status'] == 'bad':
                print '%s %s is vulnerable' % (kernel['package_name'], kernel['package_version'])

    def guard(self):
        if not self.options['report'] and not self.options['execute']:
            print 'Please specify --report or --execute'
            exit(0)
        if self.options['execute'] and not self.options['expires_in']:
            print 'Please specify --expires_in=<number of days> if using --execute'
            exit(0)

    def main(self):
        self.guard()
        total = []
        for srv in self.servers.list_all():
            srv_v2 = self.sc.server_show(srv['id'])['server']
            installed_kernels = self.sc.installed_kernels(srv['id'])
            extra_kernels = self.sc.extra_kernels(installed_kernels, srv_v2)
            if extra_kernels:
                total.append(extra_kernels)
                if self.options['execute'] and extra_kernels:
                    self.report(srv, extra_kernels, srv_v2['kernel_release'])
                    warn = self.sc.version_compare(installed_kernels, srv_v2['kernel_release'])
                    if not warn:
                        self.ec.add_exceptions(srv, extra_kernels)
                        print 'Exceptions for non-running vulnerable kernel packages are added.'
                else:
                    self.report(srv, extra_kernels, srv_v2['kernel_release'])
        if not total:
            print 'No servers with more than one Kernel package has been found'

if __name__ == "__main__":
    KernelExceptions().main()
