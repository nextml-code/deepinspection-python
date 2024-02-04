from . import client


def test_download_export():
    exports = client.track().exports.fastenings.list()
    export_id = exports[0]["id"]

    for _ in client.track().exports.fastenings.get_data(export_id):
        pass
