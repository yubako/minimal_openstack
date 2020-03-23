
def test_mariadb(host):
    assert host.package('mariadb').is_installed

    sv_mariadb = host.service('mariadb')
    assert sv_mariadb.is_running
    assert sv_mariadb.is_enabled



