
def test_memcached(host):
    assert host.package('memcached').is_installed
    memcached = host.service('memcached')
    assert memcached.is_running
    assert memcached.is_enabled

    content = host.file("/etc/sysconfig/memcached").content
    assert 'OPTIONS="-l 127.0.0.1,::1,controller"' in content


