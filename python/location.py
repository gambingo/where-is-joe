import os
import sys
import time
import json
import click

from pyicloud import PyiCloudService


def get_my_location():
    """Ping the iCloud server and access my location through Find my Iphone"""
    username = os.environ["icloud_username"]
    password = os.environ["icloud_password"]

    api = PyiCloudService(username, password)
    two_factor_authentication(api)

    while True:
        loc = api.iphone.location()
        write_location_to_json(loc)
        time.sleep(60)


def write_location_to_json(loc):
    data = {
    'lat':  loc['latitude'],
    'lng':  loc['longitude'],
    'ts':   loc['timeStamp'],
    }
    with open('../json/location.json', 'w') as outfile:
        json.dump(data, outfile)


def two_factor_authentication(api):
    if api.requires_2fa:
        print("Two-factor authentication required. Your trusted devices are:")

    devices = api.trusted_devices
    for i, device in enumerate(devices):
        print("  %s: %s" % (i, device.get('deviceName',
            "SMS to %s" % device.get('phoneNumber'))))

    device = click.prompt('Which device would you like to use?', default=0)
    device = devices[device]
    if not api.send_verification_code(device):
        print("Failed to send verification code")
        sys.exit(1)

    code = click.prompt('Please enter validation code')
    if not api.validate_verification_code(device, code):
        print("Failed to verify verification code")
        sys.exit(1)


if __name__ == "__main__":
    get_my_location()
