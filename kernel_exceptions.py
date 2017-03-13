from lib import *


class KernelExceptions(object):
    def __init__(self):
        self.servers = Servers()
        self.options = Options()
        self.sc = ServersController()
        self.ec = ExceptionsController()

    def report(self, srv, kernels):
        for kernel in kernels:
            msg = "server %s has the following extra kernels %s%s" % (srv['id'],
                                                                      kernel['package_name'],
                                                                      kernel['package_version'])
            print msg

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
            kernels = self.sc.extra_kernels(srv['id'])
            if kernels:
                total.append(kernels)
                if self.options['execute'] and kernels:
                    self.report(srv, kernels)
                    self.ec.add_exceptions(srv, kernels)
                    print 'Exceptions for non-running vulnerable kernel packages are added.'
                else:
                    self.report(srv, kernels)
        if not total:
            print 'No servers with more than one Kernel package has been found'

if __name__ == "__main__":
    KernelExceptions().main()
