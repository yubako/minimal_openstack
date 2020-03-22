
import re

def test_memcached(host):
    assert host.package('memcached').is_installed
    assert host.service('memcached').is_running
    assert host.service('memcached').is_enabled

    content = host.file("/etc/sysconfig/memcached").content
    assert re.match(r'^OPTIONS=.*controller"')


