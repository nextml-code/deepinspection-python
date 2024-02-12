from sweref99 import projections

tm = projections.make_transverse_mercator("SWEREF_99_TM")


def sweref99_coordinates(latitude, longitude):
    if latitude is None or longitude is None:
        return dict(
            northing=None,
            easting=None,
        )
    else:
        northing, easting = tm.geodetic_to_grid(latitude, longitude)
        return dict(
            northing=northing,
            easting=easting,
        )
