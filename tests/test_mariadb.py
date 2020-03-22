
def test_mariadb(host):
    assert host.package('mariadb').is_installed

    sv_mariadb = host.service('mariadb')
    assert sv_mariadb.is_running
    assert sv_mariadb.is_enabled

def test_rabbitmq(host):
    assert host.package('rabbitmq-server').is_installed

    sv_rabbimq = host.service('rabbitmq')
    assert sv_rabbitmq.is_running
    assert sv_rabbitmq.is_enabled

    assert "openstack" in host.check_output("rabbitmqctl list_users")



