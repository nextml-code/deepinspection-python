import deepinspection_optram

import deepinspection

from . import client


def test_download_export():
    exports = client.track().exports.fastenings.list()
    export = exports[0]

    for item in client.track().exports.fastenings.get_data(export["id"]):
        deepinspection_optram.convert(item, export)
