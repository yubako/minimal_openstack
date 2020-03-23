
def test_rabbitmq(host):
    assert host.package('rabbitmq-server').is_installed

    sv_rabbimq = host.service('rabbitmq')
    assert sv_rabbitmq.is_running
    assert sv_rabbitmq.is_enabled

    assert "openstack" in host.check_output("rabbitmqctl list_users")



