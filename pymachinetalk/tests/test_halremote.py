import pytest

@pytest.fixture
def halremote():
    from pymachinetalk import halremote
    return halremote

@pytest.fixture
def dns_sd():
    from pymachinetalk import dns_sd
    return dns_sd

def test_halremote_integration(halremote, dns_sd):
    rcomp = halremote.RemoteComponent('test')
    rcomp.newpin('foo', halremote.HAL_BIT, halremote.HAL_OUT)
    rcomp.newpin('bar', halremote.HAL_FLOAT, halremote.HAL_IN)

    sd = dns_sd.ServiceDiscovery()
    sd.register(rcomp)
