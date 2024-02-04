# deepinspection python

Python client library for deepinspection. Designed to simplify and exemplify interaction with the External API.

## Usage

```python
import deepinspection


client = deepinspection.track.client(
    customer_id="customer-id",
    client_id="XYZ",
    client_secret="XYZ",
)

# list exports
exports = client.exports.fastenings.list()

# get export data
for line in client.exports.fastenings.get_data(exports[0]["id"]):
    pass
```

_The customer id should match with the website url `https://customer-id.track.deepinspection.io/`._

exports

```json
[
  {
    "updated": "2024-02-01T23:20:20.605136+00:00",
    "id": "461731a1-96c8-4ed6-99e4-9fe424eb9c40",
    "measurement_name": "20231001_124327_2011T",
    "type": "fastenings",
    "downloaded": null,
    "created": "2024-02-01T23:20:20.605136+00:00",
    "user_id": "a338595f-6eba-481b-9f0f-112290a1078b"
  },
...
```

export_data

```json
{"export_datetime": "2024-02-04T21:21:12.866787", "measurement": "20231001_124327_2011T"}
{"id": "56fb582a-0280-43fa-81f3-2a444e7e4273", "position_geographical": {"track_section": "111",
...
```

## Installation

Use your preferred package manager:

```bash
poetry add deepinspection
```

or

```bash
pip install deepinspection
```
