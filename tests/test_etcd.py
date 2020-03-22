
def test_etcd(host):
    assert host.package('etcd').is_installed
    sv = host.service('etcd')
    assert sv.is_running
    assert sv.is_enabled

    var = host.ansible.get_variables()
    assert 'minimal_openstack_controller_management_ip' in var
    mng_ip = var.get('minimal_openstack_controller_management_ip')

    lines= [
        'ETCD_LISTEN_PEER_URLS="http://{mng_ip}:2380"',
        'ETCD_LISTEN_CLIENT_URLS="http://{mng_ip}:2379"',
        'ETCD_INITIAL_ADVERTISE_PEER_URLS="http://{mng_ip}:2380"',
        'ETCD_ADVERTISE_CLIENT_URLS="http://{mng_ip}:2379"',
        'ETCD_INITIAL_CLUSTER="controller=http://{mng_ip}:2380"'
    ]

    content = host.file("/etc/etcd/etcd.conf").content
    for line in lines:
        assert line in content

