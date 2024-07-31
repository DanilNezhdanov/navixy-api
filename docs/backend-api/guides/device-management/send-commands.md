# Sending Commands to a Device

In this guide, you will learn how to send commands to a device on the Navixy platform. This process is essential for remote control and management of your devices. Follow these steps to successfully send commands using the Navixy API.

## Prerequisites

Before you begin, ensure you have the following:

1. An active Navixy account.
2. A valid API key. Refer to the [Obtaining an API Key](/backend-api/getting-started/authentication.md) guide for instructions on how to get one.

## Step 1: Understand the Available Commands

Navixy supports a variety of commands that you can send to your devices. These commands include actions like requesting location, restarting the device, and more. Refer to the [Navixy API Resources](/backend-api/resources/index.md) for a complete list of available commands and their descriptions.

## Step 2: Prepare the Command Data

To send a command to a device, you need to prepare the command data. This includes the device ID, command name, and any required parameters.

### Example

```json
{
  "device_id": "1234567890",
  "command": "request_location"
}
```

## Step 3: Make the API Call

Use the `tracker/send_command` endpoint to send the command to the device. This endpoint requires the prepared command data.

### Request

```sh
curl -X POST 'https://api.navixy.com/v2/tracker/send_command' \
    -H 'Content-Type: application/json' \
    -d '{
          "hash": "your_api_key_hash",
          "device_id": "1234567890",
          "command": "request_location"
        }'
```

### Response

A successful response will look like this:

```json
{
  "success": true,
  "queued": true
}
```

If there is an error, the response will include an error code and description:

```json
{
  "success": false,
  "status": {
    "code": 4,
    "description": "Device not found"
  }
}
```

## Step 4: Verify the Command Execution

After sending the command, verify that it was executed correctly by checking the device's response or status using the appropriate endpoint.

### Request

```sh
curl -X POST 'https://api.navixy.com/v2/tracker/get_command_status' \
    -H 'Content-Type: application/json' \
    -d '{
          "hash": "your_api_key_hash",
          "device_id": "1234567890"
        }'
```

### Response

A successful response will include the command status:

```json
{
  "success": true,
  "status": "executed"
}
```

## Additional Information

For more details on the `tracker/send_command` and `tracker/get_command_status` endpoints, refer to the [Navixy API Resources](/backend-api/resources/index.md):

 - [tracker/send_command]([Navixy API Resources](/backend-api/resources/tracking/tracker#send_command)
 - [tracker/raw_command/send](/backend-api/resources/tracking/tracker#raw_commandsend)

### Common Issues

1. **Invalid API Key**: Ensure your API key is correct and has the necessary permissions.
2. **Device Not Found**: Verify the device ID to ensure it is correct.
3. **Unsupported Command**: Ensure the command is supported by the device model.

### Related Guides

- [Activating a Device](activate-device.md)
- [Getting Tracker List](/backend-api/getting-started/data-retrieval/get-tracker-list.md)
- [Retrieving Track Points](/backend-apigetting-started/data-retrieval/get-track-points.md)