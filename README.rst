#############
umqtt-example
#############


About
=====

Concise example to test the behavior of MicroPython's ``umqtt.simple`` against
Mosquitto 2.0.11 / 2.0.12.

The reason is to investigate a potential regression with Mosquitto 2.0.12,
being more strict wrt. protocol compliance, which apparently breaks
``umqtt.simple``.

See also:

- https://github.com/micropython/micropython-lib/issues/445
- https://github.com/hiveeyes/terkin-datalogger/pull/97


Notes
=====

There is a module ``umqtt.universal``, which is derived from ``umqtt.simple``.
It is compatible with both MicroPython and CPython.


Setup
=====

Install MicroPython::

    brew install micropython

Acquire sources::

    git clone https://github.com/daq-tools/umqtt-example
    cd umqtt-example


Usage
=====

Run Mosquitto::

    # Version 2.0.11
    docker run -it --rm --publish=1883:1883 eclipse-mosquitto:2.0.11 mosquitto -c /mosquitto-no-auth.conf

    # Version 2.0.12
    docker run -it --rm --publish=1883:1883 eclipse-mosquitto:2.0.12 mosquitto -c /mosquitto-no-auth.conf

Invoke tests, on both CPython and MicroPython::

    make test

In order to individually invoke the tests, run::

    # CPython
    make test-cpython

    # MicroPython
    make test-micropython
