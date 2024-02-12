def map_url(fastening, sweref99, description):
    measurement = fastening["measurement"]
    northing = sweref99["northing"]
    easting = sweref99["easting"]

    if northing is None or easting is None:
        return None

    # TODO: unclear what this should be
    unknown_id = "1b6b638eba0d4e689a3c45ba1d082839"

    return (
        "https://portal.gis.trafikverket.local/portal/apps/webappviewer/index.html?"
        f"id={unknown_id}&marker={easting}"
        f"%3b{northing}%3b3006%3b"
        f"{measurement}%3b%3b"
        f"{description}&level=15"
    )
