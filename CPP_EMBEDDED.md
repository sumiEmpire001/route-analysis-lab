# Embedded C++ companion

Fixed-capacity directed Dijkstra engine for offline robot route planning. Node IDs are integers; unlike Python, no JSON parsing or string node names. No traffic, obstacle sensing, motor control or real navigation. Invalid edges latch a fault until reset.

Run: `cmake -S . -B build && cmake --build build && ctest --test-dir build --output-on-failure`.

The original Python implementation and its tests are unchanged. C++ uses fixed-capacity storage and rejects invalid inputs. Capacity overflow latches a fault; call reset only after handling the fault. Host tests are not hardware verification. No physical Arduino/ESP32 wiring, sensor calibration, watchdog, power-loss recovery, or actuator safety is supplied. Keep this logic isolated from live actuators until validated on the target board.
