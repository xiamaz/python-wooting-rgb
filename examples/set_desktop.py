#!/usr/bin/env python3
"""Show the currently active desktop with a red key on the number row.
"""
import sys
from wooting_rgb import wooting_rgb_wrapper

active_color = (255, 0, 0)

active_desktop = int(sys.argv[1])
last_active_desktop = int(sys.argv[2])

with open("/tmp/log.txt", "a") as f:
    f.write(f"{active_desktop} {sys.argv}\n")

wooting_rgb_wrapper.wooting_rgb_kbd_connected()
wooting_rgb_wrapper.wooting_rgb_direct_reset_key(1, last_active_desktop-2)
wooting_rgb_wrapper.wooting_rgb_direct_set_key(1, active_desktop-2, *active_color)
