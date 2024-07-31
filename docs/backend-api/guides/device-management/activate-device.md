# Activating a Device

In this guide, you will learn how to activate a device on the Navixy platform. This process is essential for tracking and monitoring your devices. Follow these steps to successfully activate your device using the Navixy API.

## Prerequisites

Before you begin, ensure you have the following:

1. An active Navixy account.
2. A valid API key. Refer to the [Obtaining an API Key](/backend-api/getting-started/authentication.md) guide for instructions on how to get one.

## Step 1: Prepare the Device Data

To activate a device, you need to prepare the device data. This includes the device ID, model, and other relevant information.

### Example

```json
{
  "device_id": "1234567890",
  "model": "XYZ-1000",
  "phone": "+1234567890"
}
```

## Step 2: Make the API Call

Use the `tracker/register` endpoint to activate the device. This endpoint requires the prepared device data.

### Request

```sh
curl -X POST 'https://api.navixy.com/v2/tracker/register' \
    -H 'Content-Type: application/json' \
    -d '{
          "hash": "your_api_key_hash",
          "device_id": "1234567890",
          "model": "XYZ-1000",
          "phone": "+1234567890"
        }'
```

### Response

A successful response will look like this:

```json
{
  "success": true,
  "id": 123
}
```

If there is an error, the response will include an error code and description:

```json
{
  "success": false,
  "status": {
    "code": 4,
    "description": "Device already exists"
  }
}
```

## Step 3: Verify the Activation

After activating the device, verify that it is correctly activated by using the `tracker/list` endpoint. This will return a list of all activated devices.

### Request

```sh
curl -X POST 'https://api.navixy.com/v2/tracker/list' \
    -H 'Content-Type: application/json' \
    -d '{
          "hash": "your_api_key_hash"
        }'
```

### Response

A successful response will include the list of devices:

```json
{
  "success": true,
  "list": [
    {
      "id": 123,
      "device_id": "1234567890",
      "model": "XYZ-1000",
      "phone": "+1234567890"
    }
  ]
}
```

## Additional Information

For more details on the `tracker/register` and `tracker/list` endpoints, refer to the [Navixy API Resources](/backend-api/resources/index.md).

### Common Issues

1. **Invalid API Key**: Ensure your API key is correct and has the necessary permissions.
2. **Device Already Exists**: Verify the device ID and model to avoid duplicate activations.

### Related Guides

- [Sending Commands to a Device](send-commands.md)
- [Getting Tracker List](/backend-api/guides/data-retrieval/get-tracker-list.md)
- [Retrieving Track Points](/backend-api/guides/data-retrieval/get-track-points.md)