cli-cpu

this is a real time cli text based renderer that renders your cpu usage as a chart.

well, anyone can make a chart. but the thing is it's fully customizable to your liking.

you can customize it in the resource_monitor.cfg file. this will be in the same directory as the python file.
and you can't still find it, you probably need to run the script first.

here's the default config file and i'll show you how to change it.

[CPU]
cpu_value_seperator = "="
cpu_name_seperator = "="
cpu_zero_fill = "."
cpu_fill = " "
cpu_floor = "‾"
cpu_roof = "_"
cpu_right_side = "|"
cpu_left_side = "|"
cpu_box = "█"
cpu_heading = "CPU Usage:"
cpu_right_gap = 0
cpu_left_gap = 0
cpu_chart_width = 30
cpu_bar_height = 10


this will generate something like this:
________________________________
|          CPU Usage:          |
|==============================|
|                              |
|                              |
|                              |
|  █                        █  |
|  ██                      ██  |
| ████    █                ██  |
| █████ █ ██               ██  |
| ██████████               ██  |
| ███████████    ███     █ ██  |
|.██████████████████.█..███████|
|==============================|
|            16.5%             |
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
the config file is pretty straightforward.
