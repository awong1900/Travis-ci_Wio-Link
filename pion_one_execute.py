import sys
import requests

red_led_on_api = "https://cn.iot.seeed.cc/v1/node/GroveRelay/onoff/1?access_token=14e9888a13b1d9b6c1e7d66ef364d1f6"
red_led_off_api = "https://cn.iot.seeed.cc/v1/node/GroveRelay/onoff/0?access_token=14e9888a13b1d9b6c1e7d66ef364d1f6"
green_led_on_api = "https://cn.iot.seeed.cc/v1/node/GroveRelay_02/onoff/1?access_token=14e9888a13b1d9b6c1e7d66ef364d1f6"
green_led_off_api = "https://cn.iot.seeed.cc/v1/node/GroveRelay_02/onoff/0?access_token=14e9888a13b1d9b6c1e7d66ef364d1f6"
orange_led_on_api = "https://cn.iot.seeed.cc/v1/node/GroveRelay_01/onoff/1?access_token=14e9888a13b1d9b6c1e7d66ef364d1f6"
orange_led_off_api = "https://cn.iot.seeed.cc/v1/node/GroveRelay_01/onoff/0?access_token=14e9888a13b1d9b6c1e7d66ef364d1f6"

def main(argv):
    status = argv
    if status == "success":
        requests.post(red_led_off_api,verify=False)
        requests.post(orange_led_off_api,verify=False)
        requests.post(green_led_on_api,verify=False)
    elif status == "fail":
        requests.post(green_led_off_api,verify=False)
        requests.post(orange_led_off_api,verify=False)
        requests.post(red_led_on_api,verify=False)
    elif status == "building":
        requests.post(green_led_off_api,verify=False)
        requests.post(orange_led_on_api,verify=False)
        requests.post(red_led_off_api,verify=False)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print 'Usage: python success/fail/building'
        exit(1)
    main(sys.argv[1])
