from . import mappings
from .map_url import map_url
from .sweref99_coordinates import sweref99_coordinates


def convert(item: dict, export: dict):
    sweref99 = sweref99_coordinates(
        latitude=item["position_geographical"]["coordinates"][0],
        longitude=item["position_geographical"]["coordinates"][1],
    )

    return {
        "id": item["id"],
        "mätning": item["measurement"],
        "optrambandel": item["position_geographical"]["track_section"],
        "unespår": item["position_geographical"]["une_track"],
        "start_kilometer": item["position_geographical"]["kilometer"],
        "slut_kilometer": item["position_geographical"]["kilometer"],
        "start_meter": item["position_geographical"]["meter"],
        "slut_meter": item["position_geographical"]["meter"],
        "northing": sweref99["northing"],
        "easting": sweref99["easting"],
        "sida": mappings.RAIL_SIDE[item.pop("rail_side")],
        "in_utsida": mappings.RAIL_SIDE_LOCATION[item.pop("rail_side_location")],
        "feltyp": mappings.INTEGRITY[item.pop("fastening_integrity")],
        "mätvagn": "2011T",
        "mätdatum": export["measured"],
        "leverantör": "InfraNord",
        "länk_deepinspection": item["inspection_url"],
        "kartlänk": map_url(item, sweref99, description=mappings.TYPE["fastening"]),
    }
