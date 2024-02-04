from . import client


def test_download_export():
    exports = client.track().exports.fastenings.list()
    export_id = exports[0]["id"]

    export = client.track().exports.fastenings.get(export_id)
    assert export["id"] == export_id
