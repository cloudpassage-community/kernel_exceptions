class Reporter(object):
    def report(self, srv, extra_kernels, running_kernel):
        label = self.report_srv_label(srv)
        print 'server %s %s is running kernel version %s' % (srv['id'], label, running_kernel)
        for kernel in extra_kernels:
            msg = "server %s %s has extra %s %s" % (srv['id'], label, kernel['package_name'], kernel['package_version'])
            print msg
            if kernel['status'] == 'bad':
                print '%s %s is vulnerable' % (kernel['package_name'], kernel['package_version'])

    @staticmethod
    def report_srv_label(srv):
        if srv['server_label']:
            return srv['server_label']
        return srv['hostname']