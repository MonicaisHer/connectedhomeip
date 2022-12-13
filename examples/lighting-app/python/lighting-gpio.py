from chip.server import (
    GetLibraryHandle,
    NativeLibraryHandleMethodArguments,
    PostAttributeChangeCallback,
)

from chip.exceptions import ChipStackError

import sys
import os

from gpiozero import LED

led = LED(17)


@PostAttributeChangeCallback
def attributeChangeCallback(
    endpoint: int,
    clusterId: int,
    attributeId: int,
    xx_type: int,
    size: int,
    value: bytes,
):
    if endpoint == 1:
        if clusterId == 6 and attributeId == 0:
            if len(value) >= 1 and value[0] == 1:
                print("[PY] light on")
                led.on()
            else:
                print("[PY] light off")
                led.off()


chipLib = GetLibraryHandle(attributeChangeCallback)

input('Press enter to quit')

sys.exit(0)
