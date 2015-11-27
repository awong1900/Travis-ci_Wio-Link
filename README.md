# Travis-ci_Wio_Link [![Build Status](https://travis-ci.org/awong1900/Travis-ci_Wio-Link.svg?branch=master)](https://travis-ci.org/awong1900/Travis-ci_Wio-Link)
## 项目介绍
这个项目展示了如何用Wio Link与Travis-ci结合，通过巨大的LED信号灯来展示项目的编译的状态。  
把这个放在办公室显眼位置，让那些码农崩溃吧。:smirk:

## 操作步骤
* 配置Wio Link， 添加3个Grove Relay，每个Relay控制一个信号灯. [开始配置Wio Link](https://iot.seeed.cc/getting_started/)  
* 升级Wio Link固件，然后拿到三个Relay的Rest API
* 把pion_one_execute.py放置在根目录，并且修改API常量为你的API
```
    red_led_on_api = "https://cn.iot.seeed.cc/v1/node/GroveRelayDigital0/onoff/1?access_token=774bdd528b05a2adf734301bfbdf10b0"
    red_led_off_api = "https://cn.iot.seeed.cc/v1/node/GroveRelayDigital0/onoff/0?access_token=774bdd528b05a2adf734301bfbdf10b0"
    green_led_on_api = "https://cn.iot.seeed.cc/v1/node/GroveRelayDigital2/onoff/1?access_token=774bdd528b05a2adf734301bfbdf10b0"
    green_led_off_api = "https://cn.iot.seeed.cc/v1/node/GroveRelayDigital2/onoff/0?access_token=774bdd528b05a2adf734301bfbdf10b0"
    orange_led_on_api = "https://cn.iot.seeed.cc/v1/node/GroveRelayDigital1/onoff/1?access_token=774bdd528b05a2adf734301bfbdf10b0"
    orange_led_off_api = "https://cn.iot.seeed.cc/v1/node/GroveRelayDigital1/onoff/0?access_token=774bdd528b05a2adf734301bfbdf10b0"
```
* 本地测试：  
    * 编译成功 `$python wio_link_execute.py success`
    * 编译失败 `$python wio_link_execute.py failure`
    * 编译进行中 `$python wio_link_execute.py building`
* 修改.travis-ci, 把上述命令嵌入进去 [开始使用travis-ci](http://docs.travis-ci.com/user/for-beginners/)
```yml
    language: python
    python:
      - "2.7"   
    before_install:   
      - pip install requests   
      - python pion_one_execute.py building   
    install:   
    script:   
      - python helloworld.py      
    after_success:    
      - python pion_one_execute.py success   
    after_failure:   
      - python pion_one_execute.py failure   
```
* 假设helloworld.py是你的项目。修改它故意设置一个错误，然后提交。一起见证奇迹吧！

## 动态效果
![gif](/images/logo.png)
