# Geo Kong Flask API

This is a Flask API that provides endpoints for updating GEO settings, specifically for a GEO Kong plugin. The API allows you to modify the GEO whitelist and blacklist settings, influencing the behavior of the Kong plugin.

## Setup

> You may want to enter a virtualenv before proceeding with the next steps.

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```
2. Run the Flask application:
```bash
python run.py
```

## Endpoints

### Update GEO Settings
- **Endpoint**: `/update_geo`
- **Method**: `POST`
- **Payload**:
    - mode: The mode of operation (whitelist or blacklist).
    - selectedCountries: An array of selected country codes.

**Example**

```json
{
  "mode": "whitelist",
  "selectedCountries": ["US", "CA", "GB"]
}
```

- **Response**: Returns a JSON object confirming the update.

### Get Country List
- **Endpoint**: /get_country_list
- **Method**: GET
- **Response**: Returns a JSON object containing a list of all available countries.

### Get Allowed Country List
- **Endpoint**: /get_allowed_country_list
- **Method**: GET
- **Response**: Returns a JSON object containing a list of countries allowed by the GEO settings.

## Future Scope

It's important to note that the current state of the project reflects its nature as a non-production project. In order to enhance the functionality and robustness of this Flask API, following areas need to be addressed:

- **Persistent Storage**: This API operates without persistent storage. All changes to the GEO settings are transient and will be lost upon restarting the server.
- **Input Validation**: The API currently lacks extensive validation checks on user-provided country codes. It assumes that the provided codes are valid.
- **Logging**: The API does not incorporate logging mechanisms to track API usage and potential errors.
- **Authentication and Authorization**: The API does not include robust authentication and authorization mechanisms to control access to specific API endpoints.