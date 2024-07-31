# Tracking Stationary Objects

In this guide, you will learn how to track stationary objects using the Navixy platform. This is useful for monitoring assets that do not move frequently, such as containers, generators, or any other stationary equipment. Follow these steps to effectively track stationary objects with the Navixy API.

## Prerequisites

Before you begin, ensure you have the following:

1. An active Navixy account.
2. A valid API key. Refer to the [Obtaining an API Key](../../getting-started/authentication.md) guide for instructions on how to get one.

## Step 1: Register the Stationary Object

To track a stationary object, you first need to register it on the Navixy platform. Use the [`tracker/register`](/backend-api/resources/tracking/tracker/index.md#register) endpoint to register the object.

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

## Step 2: Configure Stationary Object Settings

Once the object is registered, configure its settings to ensure it is monitored correctly as a stationary object. Use the `tracker/update` endpoint to update the settings.

### Request

```sh
curl -X POST 'https://api.navixy.com/v2/tracker/update' \
    -H 'Content-Type: application/json' \
    -d '{
          "hash": "your_api_key_hash",
          "tracker_id": 123,
          "settings": {
            "stationary": true,
            "report_interval": 3600
          }
        }'
```

### Response

A successful response will look like this:

```json
{
  "success": true
}
```

## Step 3: Monitor the Stationary Object

To monitor the stationary object, use the [`tracker/get_state`](/backend-api/resources/tracking/tracker/index.md#get_state) endpoint. This will provide you with the current status and location of the object.

### Request

```sh
curl -X POST 'https://api.navixy.com/v2/tracker/get_state' \
    -H 'Content-Type: application/json' \
    -d '{
          "hash": "your_api_key_hash",
          "tracker_id": 123
        }'
```

### Response

A successful response will include the current state of the object:

```json
{
  "success": true,
  "state": {
    "online": true,
    "location": {
      "lat": 34.052235,
      "lng": -118.243683
    },
    "last_update": "2021-12-01T12:00:00Z"
  }
}
```

## Additional Information

For more details on the endpoints used in this guide, refer to the [Navixy API Resources](/backend-api/resources/index.md).

- [tracker/get_state](/backend-api/resources/tracking/tracker/index.md#get_state)

### Common Issues

1. **Invalid API Key**: Ensure your API key is correct and has the necessary permissions.
2. **Device Not Found**: Verify the device ID to ensure it is correct.
3. **Network Errors**: Ensure your network connection is stable and the Navixy API server is reachable.

## Conclusion

You have now successfully configured and are monitoring a stationary object on the Navixy platform. By following these steps, you can effectively track and manage your stationary assets using the Navixy API. For further assistance, refer to the [Navixy API Resources](/backend-api/resources/index.md).

### Related Guides

- [Activating a Device](activate-device.md)
- [Sending Commands to a Device](send-commands.md)
- [Getting Tracker List](/backend-api/guides/data-retrieval/get-tracker-list.md)