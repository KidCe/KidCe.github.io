
# Betaflight RX Monitor

Betaflight RX Monitor is a read-only browser tool for diagnosing receiver and USB connection problems on a Betaflight flight controller. It connects directly through Web Serial and provides a focused dashboard with visual status information and configurable audio alerts.

[Open Betaflight RX Monitor](https://kidce.github.io/BetaflightStatusReadout/){ .md-button .md-button--primary }
[View source on GitHub](https://github.com/KidCe/BetaflightStatusReadout){ .md-button }

!!! warning "Bench testing only"
    Remove all propellers before connecting a flight controller. The tool does not prevent arming and is not intended for in-flight telemetry.

## What it mooniitors

- RXLOSS, FAILSAFE, and BOXFAILSAFE status flags.
- RSSI and live RC channel values.
- MSP connection health and stale data.
- USB disconnect and successful reconnect events.

Numeric Link Quality is intentionally not displayed because the normal Betaflight MSP API 1.48 read path does not expose a general live-LQ value. The tool avoids presenting a receiver-specific approximation as a universal metric.

## Audio alerts

- Configurable RXLOSS and RSSI alarm behavior.
- Individual previews for every alarm and recovery sound.
- Separate sounds for USB disconnect and reconnect.
- Automatic reconnection to the previously authorized USB port after a cable interruption.

## How to use it

1. Remove all propellers and secure the aircraft on the bench.
2. Close Betaflight Configurator and any other application using the serial port.
3. Open the hosted tool in a current version of Chrome or Edge.
4. Select **Enable audio** and preview the available sounds.
5. Select **Connect flight controller** and choose the correct USB serial device.
6. Switch the transmitter off and on, or interrupt the USB connection, to test the relevant status and recovery behavior.

The included Demo mode can be used to test alarm behavior without connected hardware.

## Browser and privacy notes

- Web Serial requires a Chromium-based browser and a secure HTTPS context. Chrome and Edge are the supported targets for the current alpha.
- Serial data, RC values, and event-log entries remain in browser memory and are not uploaded by the application.
- Settings and event history are not persisted in the current alpha.
- When several identical flight controllers are connected, verify the selected device because automatic reconnect primarily identifies ports through the browser port object and USB vendor/product identifiers.

## Project links

- Hosted application: https://kidce.github.io/BetaflightStatusReadout/
- Source repository: https://github.com/KidCe/BetaflightStatusReadout
- Testing guide: https://github.com/KidCe/BetaflightStatusReadout/blob/main/docs/TESTING.md
- Alpha release notes: https://github.com/KidCe/BetaflightStatusReadout/blob/main/docs/RELEASE_NOTES_v0.1.0-alpha.1.md
- License: https://github.com/KidCe/BetaflightStatusReadout/blob/main/LICENSE

The project is independent and is not affiliated with or endorsed by the Betaflight project.
