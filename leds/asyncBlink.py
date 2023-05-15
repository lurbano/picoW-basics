# SPDX-FileCopyrightText: 2022 Dan Halbert for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# Requires asyncio/ and adafruit_ticks.mpy

import asyncio
import board
import neopixel

pixels = neopixel.NeoPixel(board.GP0, 20)
pixels[0] = (20,0,0)
    
async def blink(n, interval, count):
    for i in range(count):
        pixels[n] = (0,100,0)
        await asyncio.sleep(interval)
        pixels[n] = (0,0,100)
        await asyncio.sleep(interval)


async def main():
    
    led1_task = asyncio.create_task(blink(2, 1.0, 10))
    led2_task = asyncio.create_task(blink(3, 0.25, 20))

    await asyncio.gather(led1_task, led2_task)  # Don't forget "await"!
    print("done")


asyncio.run(main())

