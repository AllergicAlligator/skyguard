# Ocean Challenge 2024

## Presentation Slides
* https://ppt.cc/fA5G0x

## Teamwork Allocation
|Name|Role|Job Description|
|:--|:--|:--|
|Tiffany Gau|Captain|Software Development, Project Management, Budget Planning, Public Relationship|
|Daniel Gau|Member|Software Development (Auto Patrol)|
|Oliver Chen|Member|Software Development (Auto Patrol) |
|Hong Lai|Member|Software Development (Deep Learning)|
|Marvin Cheng|Member|Software Development (Real-Time Notification)|

## Work Schedule
|Task|1|2|3|4|5|6|
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
|Drone Assembly and Testing|X|X|X|X|||
|Software Development and Testing|X|X|X|X|X|X|
|System Integration||||X|X|X|
|Integration Testing|||||X|X|
|Seeking Collaboration with external resources||X|X|X|X|X|
|% of completion|10%|25%|40%|60%|80%|100%|

## Budget Planning

Budget for thie proposal is mainly allocated for drone (parts, assembly, and testing) and flight coaches.  For details, please check the proposal sent to Ocean Challenge 2024 Committee.

## Relevant Resources

### Ground Station Software
* [Choosing a Ground Station](https://ardupilot.org/copter/docs/common-choosing-a-ground-station.html) 
* [Mission Planner](https://github.com/ArduPilot/MissionPlanner)
* [QGroundControl, QGC](http://qgroundcontrol.com/)

### SITL
* [SITL Simulator (Software in the loop)](https://ardupilot.org/dev/docs/sitl-simulator-software-in-the-loop.html)

  If you are using Mission Planner，you can download SITL from simulation section of it.  If you are using QGC, you will need to install SITL manually.

  Mission Planner is written in C#, so it would be a little bit tricky to use it on a macbook.  Similarly, it is also tricky to use SITL on a macbook.

### pymavlink tutorial
* [pymavlink turtorial](https://www.youtube.com/watch?v=kecnaxlUiTY&list=PLy9nLDKxDN68cwdt5EznyAul6R8mUSNou)
* [How To Start a Mission Using Pymavlink](https://www.youtube.com/watch?v=pAAN055XCxA)

### Teachable Machine
* [Teachable Machine](https://teachablemachine.withgoogle.com/)

### Line Notify
* [Line Notify Help](https://help2.line.me/line_notify/web/pc?lang=zh-Hant)
* [Generate Line Notify Token](https://notify-bot.line.me/en/)
* [Line Notify API Document](https://notify-bot.line.me/doc/en/)
* [Introduction to Line Notify](https://github.com/vcdemy/linenotify)

### Download Line Notify Module in Colab
```bash
!curl -o linenotify.py https://raw.githubusercontent.com/AllergicAlligator/skyguard/main/linenotify.py
```
