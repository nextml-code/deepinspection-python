# Optram example

This is an example of how to use the `deepinspection` package and converting fastening data to an Optram compatible format.

## Install

```bash
poetry install
```

## Usage

```python
import deepinspection
import deepinspection_optram


client = deepinspection.track.client(
    customer_id="customer-id",
    client_id="XYZ",
    client_secret="XYZ",
)

# list exports
exports = client.exports.fastenings.list()

# get export data
export = exports[0]

for fastening in client.exports.fastenings.get_data(export["id"]):
    optram_fastening = deepinspection_optram.convert(fastening, export)
```

export_data

```json
{
  "id": "71ef13c2-cc4e-4fc2-a2c8-58d2ab6d29b3",
  "mätning": "20231010_205621_2011T",
  "optrambandel": "400A",
  "unespår": "U3",
  "start_kilometer": 100,
  "slut_kilometer": 100,
  "start_meter": 210,
  "slut_meter": 210,
  "northing": 6580942.200002984,
  "easting": 673788.4999998582,
  "sida": "Höger",
  "in_utsida": "Insida",
  "feltyp": "Saknad",
  "mätvagn": "2011T",
  "mätdatum": "2023-10-10T21:56:21Z",
  "leverantör": "InfraNord",
  "länk_deepinspection": "https://xyz.track.deepinspection.io/inspection/20230920_215621_2011T/80536",
  "kartlänk": "https://portal.gis.trafikverket.local/portal/apps/webappviewer/index.html?id=1b6b638eba0d4e689a3c45ba1d082839&marker=673788.4999998582%3b6580942.200002984%3b3006%3b20230920_215621_2011T%3b%3bBefästning&level=15"
}
{
  "id": "71ef13c2-cc4e-4fc2-a2c8-58d2ab6d29b3",
  "mätning": "20231010_205621_2011T",
  ...
}
...
```
