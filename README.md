# Application Exerciser Monkey for iOS

This repository provides a basic automated instrumentation tool for iOS. It is inspired by the existing [Application Exerciser Monkey for Android](https://developer.android.com/studio/test/other-testing-tools/monkey).

Unfortunately, there currently exist no other tools for the automated instrumentation of *arbitrary* iOS apps, including those that you don't develop yourself.

## Getting started

Install and run this project with the Arduino IDE on an ESP32 microcontroller. You need to also install the [ESP32-BLE-Keyboard library](https://github.com/T-vK/ESP32-BLE-Keyboard) and the [Bluetooth Nimble Library](https://github.com/T-vK/ESP32-BLE-Keyboard#how-to-activate-nimble-mode).

Connect the ESP32 then to a *jailbroken* iPhone. Make sure you enable Full Keyboard Access. The iPhone must run [Frida](https://frida.re), [`open` for iOS 11+](http://cydia.saurik.com/package/com.clarkecdc.open/), and be set up for SSH access on port 2222 (e.g. with [`iproxy`](https://iphonedev.wiki/index.php/SSH_Over_USB)).

Once that's done, you can start the testing by running `python monitor.py [bundleId of iOS app] [serial ESP32 controller]`.

*Tested only with iOS 14.2 and the [checkra1n](https://checkra.in) jailbreak.*

## Credits
- ESP32-BLE-Keyboard: <https://github.com/T-vK/ESP32-BLE-Keyboard>
- Open for iOS 11+: <http://cydia.saurik.com/package/com.clarkecdc.open/>
- Frida: <https://frida.re>