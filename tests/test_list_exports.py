from . import client


def test_list_exports():
    client.track().exports.fastenings.list()
