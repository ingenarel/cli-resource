# cli-cpu

this is a real time cli text based renderer that renders your cpu usage as a chart.

well, anyone can make a chart. but the thing is it's fully procedural and
you can customize it to your liking.

you can customize it in the resource_monitor.cfg file. this will be in the
same directory as the python file.
and you can't still find it, you probably need to run the script first.

here's the default config file and i'll show you how to change it.
```
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
```

this will generate something like this:
```
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
```
the config file is pretty straightforward.
before we talk about anything in this file, we should actually talk about how
to change the size of the chart width and height.
to change the height you should change the cpu_bar_height variable.

let's change it to something like 70 and see what happens.

it should generate  a chart like this:
```
________________________________
|          CPU Usage:          |
|==============================|
|                █             |
|               ██             |
|               ██             |
|               ██             |
|               ██             |
|               ███            |
|               ███            |
|               ███            |
|               ███            |
|               ███            |
|               ███            |
|               ███            |
|               ███            |
|               ███            |
|               ███            |
|               ███            |
|               ███            |
|              ████            |
|              ████            |
|              ████            |
|              ████            |
|              ████            |
|              ████            |
|              ████            |
|              ████            |
|              ████            |
|              ████            |
|              ████            |
|              ████            |
|              ████            |
|              ████            |
|              ████            |
|              ████            |
|              ████            |
|             █████            |
|             █████            |
|             █████            |
|             █████            |
|             █████            |
|             ██████          █|
|             ██████          █|
|        █    ██████  █       █|
|█       █    ███████ █    █  █|
|██     ██    █████████    ████|
|██     ██    ██████████   ████|
|██   █ ███  █████████████ ████|
|██ █ █ ███  ██████████████████|
|██████ ███ ███████████████████|
|██████████████████████████████|
|██████████████████████████████|
|██████████████████████████████|
|██████████████████████████████|
|██████████████████████████████|
|██████████████████████████████|
|██████████████████████████████|
|██████████████████████████████|
|██████████████████████████████|
|██████████████████████████████|
|██████████████████████████████|
|██████████████████████████████|
|██████████████████████████████|
|██████████████████████████████|
|██████████████████████████████|
|██████████████████████████████|
|██████████████████████████████|
|██████████████████████████████|
|██████████████████████████████|
|██████████████████████████████|
|██████████████████████████████|
|██████████████████████████████|
|==============================|
|            44.5%             |
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
```

if you want to change the width you should change the cpu_chart_width variable.
let's change it to 400 and see what happens.

```
__________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
|                                                                                                                                                                                                   CPU Usage:                                                                                                                                                                                                   |
|================================================================================================================================================================================================================================================================================================================================================================================================================|
|                                                                                                                                                                                                                                                                                                                    █                                                                                           |
|                                                                                                                                                                                                                                                                                                                    █                                                                                           |
|                                                                                                                                                                                                                                                                                                                    █                                                                                           |
|                                                                                                                                                                                                                                                                                                                    █                                                                                           |
|                                                                                                                                                                                                                                                                                                                    █                                                                                           |
|                                                                                                                                                                                                                                                                                                                    █                                                                                           |
|                                                                                                                                                                                                                                                                                                                    █                                                                                           |
|                                                                                                                                                                                                                                                                                                                    █                                                                                           |
|                                                                                                                                                                                                                                                                                                                    █                                                                                           |
|                                                                                                                                                                                                                                                                                                                    █                                                                                           |
|                                                                                                                                                                                                                                                                                                                    █                                                                                           |
|                                                                                                                                                                                                                                                                                                                    █                                                                                           |
|                                                                                                                                                                                                                                                                                                                    █                                                                                           |
|                                                                                                                                                                                                                                                                                                                    ██                                                                                          |
|                                                                                                                                                                                                                                                                                                                    ██                                                                                          |
|                                                                                                                                                                                                                                                                                                                    ██                                                                                          |
|                                                                                                                                                                                                                                                                                                                    ██                                                                                          |
|                                                                                                                                                                                                                                                                                                                    ██                           █                                                              |
|                                                                                                                                                                                                                                                                                                                    ██                           █                                                              |
|                                                                                                                                                                                                                                                                                                                    ██                           █                                                              |
|                                                                                                                                                                                                                                                                                                                    ██                           █                                                              |
|                                                                                                                                                                                                                                                                                                                    ██                           █                                                              |
|                                                                                                                                                                                                                                                                                                                    ██                           █                                                              |
|                                                                                                                                                                                                                                                                                                                    ██                           █                                                              |
|                                                                                                                                                                                                                                                                                                                    ██                           █                                                              |
|                                                                                                                                                                                                                                                                                                                    ██                           █                                                              |
|                                                                                                                                                                                                                                                                                                                    ██                           █                                                              |
|                                                                                                                                                                                                                                                                                                                    ██                           █                                                              |
|                                                                                                                                                                                                                                                                                                                    ██                           █                                                              |
|                                                                                                                                                                                                                                                                                                                    ██                           █                                                              |
|                                                                                                                                                                                                                                                                                                                    ██ █                         █                                                              |
|                                                                                                                                                                                                                                                                                                                    ██ █                         █                                                              |
|                                                                                                                                                                                                                                                                                                                    ██ █                         █                                                              |
|                                                                                                                                                                                                                                                                                                                    ██ █                         █                                                              |
|                                                                                                                                                                                                                                                                                                                    ██ █             █           █                                                              |
|                                                                                                                                                                                                                                                                                                                    ██ █           █ █           █                                                              |
|                                                                                                                                                                                                                                                                                                                    ██ █           █ █           █                                                              |
|                                                                                                                                                                                                                                                                                                                    ██ █           █ █           █                                                             █|
|                                                                                                                                                                                                                                                                                                                    ██ █           █ █           ██                                                            █|
|                                                                                                                                                                                                                                                                                                                    ██ █           █ █           ██                                                           ██|
|                                                                                                                                                                                                                                                                                                                    ████           █ █           ██                                                           ██|
|                                                                                                                                                                                                                                                                                                                    ████           █ █           ██                                                           ██|
|                                                                                                                                                                                                                                                                                                                    ████           █ █           ██                                                       ██  ██|
|                                                                                                                                                                                                                                                                                                                    █████          █ █ █         ██                                                       ██  ██|
|                                                                                                                                                                                                                                                                                                                    █████          ███ █  █  █  ████  ██        ███ █      █ █ █        █ ██              ██ ███|
|                                                                                                                                                                                                                                                                                                                    ██████         █████  █ ██  ████  ██  █  █  ███ ███    █ ███   ██  ██ ██  ███  █      ██ ███|
|                                                                                                                                                                                                                                                                                                                    ████████ █    █████████████ ████ ████ ██ ██ ███████ █  ██████ ███ ███ ███████ ███ ██████ ███|
|                                                                                                                                                                                                                                                                                                                    ██████████  ███████████████████████████████ ███████ ████████████████████████████████████████|
|                                                                                                                                                                                                                                                                                                                    ███████████ ███████████████████████████████ ████████████████████████████████████████████████|
|                                                                                                                                                                                                                                                                                                                    ████████████████████████████████████████████████████████████████████████████████████████████|
|                                                                                                                                                                                                                                                                                                                    ████████████████████████████████████████████████████████████████████████████████████████████|
|                                                                                                                                                                                                                                                                                                                    ████████████████████████████████████████████████████████████████████████████████████████████|
|                                                                                                                                                                                                                                                                                                                    ████████████████████████████████████████████████████████████████████████████████████████████|
|                                                                                                                                                                                                                                                                                                                    ████████████████████████████████████████████████████████████████████████████████████████████|
|                                                                                                                                                                                                                                                                                                                    ████████████████████████████████████████████████████████████████████████████████████████████|
|                                                                                                                                                                                                                                                                                                                    ████████████████████████████████████████████████████████████████████████████████████████████|
|                                                                                                                                                                                                                                                                                                                    ████████████████████████████████████████████████████████████████████████████████████████████|
|                                                                                                                                                                                                                                                                                                                    ████████████████████████████████████████████████████████████████████████████████████████████|
|                                                                                                                                                                                                                                                                                                                    ████████████████████████████████████████████████████████████████████████████████████████████|
|                                                                                                                                                                                                                                                                                                                    ████████████████████████████████████████████████████████████████████████████████████████████|
|                                                                                                                                                                                                                                                                                                                    ████████████████████████████████████████████████████████████████████████████████████████████|
|                                                                                                                                                                                                                                                                                                                    ████████████████████████████████████████████████████████████████████████████████████████████|
|                                                                                                                                                                                                                                                                                                                    ████████████████████████████████████████████████████████████████████████████████████████████|
|                                                                                                                                                                                                                                                                                                                    ████████████████████████████████████████████████████████████████████████████████████████████|
|                                                                                                                                                                                                                                                                                                                    ████████████████████████████████████████████████████████████████████████████████████████████|
|                                                                                                                                                                                                                                                                                                                    ████████████████████████████████████████████████████████████████████████████████████████████|
|                                                                                                                                                                                                                                                                                                                    ████████████████████████████████████████████████████████████████████████████████████████████|
|                                                                                                                                                                                                                                                                                                                    ████████████████████████████████████████████████████████████████████████████████████████████|
|                                                                                                                                                                                                                                                                                                                    ████████████████████████████████████████████████████████████████████████████████████████████|
|....................................................................................................................................................................................................................................................................................................................████████████████████████████████████████████████████████████████████████████████████████████|
|================================================================================================================================================================================================================================================================================================================================================================================================================|
|                                                                                                                                                                                                     47.5%                                                                                                                                                                                                      |
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
```
yes we got a really big chart now.

but for easy understanding we're gonna use 20 height and 60 width for now.

you can change the cpu_fill to overwrite the empty stuff in the chart.
well let's see it in action. i'm gonna use set it to ".".
```

```

cool right?

cpu_zero_fill is the ..... thing that you see below.

if i set it to z then this happens.
```
______________________________________________________________
|                         CPU Usage:                         |
|============================================================|
|............................................................|
|............................................................|
|.█..........................................................|
|.█..........................................................|
|.█..........................................................|
|.█..........................................................|
|.█..........................................................|
|.█..........................................................|
|.█..........................................................|
|.█..........................................................|
|.█..........................................................|
|.█.........................................................█|
|██.......................................................███|
|████.██.███...██..█.█..█.█████....█.██████...███.██.█...████|
|████████████████████████████████████████████████████████████|
|████████████████████████████████████████████████████████████|
|████████████████████████████████████████████████████████████|
|████████████████████████████████████████████████████████████|
|████████████████████████████████████████████████████████████|
|████████████████████████████████████████████████████████████|
|============================================================|
|                           47.1%                            |
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
```

cpu_box is the boxes that represents the bar values. what do i mean by that?
well let me set it to x and show that to you
```

```

cpu_value_seperator is the "=" you see on top of the percent value. and
cpu_name_seperator is the "=" you see after the heading, aka the "cpu usage:" thing.
lemme change revert the other stuff to default and then change the cpu_value_seperator to "v"
and cpu_name_seperator to "n".
btw you don't have to change the other values to change these two. i just did this so that you can understand the chart more easily.

```

```

you can change the heading, the roof of the chart, the floor of the chart,
the left side, the right side.

let's change these values to these:
cpu_floor = "f"
cpu_roof = "r"
cpu_right_side = "x"
cpu_left_side = "y"

this will generate a chart something like this:
```

```

you can even set a gap to the left and right side.
let's change the values to these:
cpu_right_gap = 4
cpu_left_gap = 10
and see what happens.

```

```

and finally you can change the heading too by changing the cpu_heading value.
cpu_heading = "FULL CUSTOMIZABILITY"

and this happens:

```

```


you don't have to worry about deleting the config or deleting a part of the config.
the code will handle that.

and if you mess up the config so bad that even my error checking can't fix it, just delete it.
it will regenerate.


this is for people who wants to know what's happening under the hood:
here are the main functions and what they do:

### bar_ini():
This is the initialization before the bar_maker() function makes the bars.
It takes these value:

bar_height: which is the bar height which should be an int.
    if the bar height is less than 3, it doesn't allow it.
    the default value is 10.

box: which should be a string, and this will represent each
    so called box that the chart will render.
    the default value is "█".

it returns a dict object. each value within the bar heigh representing a box.

the box are colors are this:
red which is an x ammount of boxes.
yellow which is the value of twice the number of green boxes.
green which is the value of yellow and red combined.

### bar_maker():
this is the bar maker function. it takes these values:

resource_usage: which should be an int. this is the resource currently being used.
    that means the ammount of boxes that the bar will show.

bar_height_and_color: which should be a dict object. this is actually a value and color map.
the bar_maker_ini() provides this. i didn't combine these two because this doesn't need to be calculated every time a new bar is calculated.
so i just made that a new function.

bar_width: this should be an int. it should be the width of the bar.

fill: this should be a string. this will fill the empty values in the bar.
    the defualt value is " ".

zero_fill: this should be a string. this will make the represent the value of zero if the bar is totally empty.
    the default value is ".".

it returns a list. if you print each item from that list you should see a vertical bar.

### chart_updater():
this is the chart updater.
it takes these values.
last_bar: it should be a list that should be the last bar that's made with the bar_maker() function.
last_chart: this should be the last chart that's either made with this function, or the starting chart that the code provides.
    it's a custom 2d array. only provide your custom thing if you know what you're doing.

it returns the updated 2d array aka the updated chart.

### chart_parser():
this parses the 2d array returned from chart_updater into a human readeable chart.
it takes these values:

chart: this should be the chart returned from the chart_updater function. it should be a 2d array.
bar_width: this should be an int. this is the bar width.
chart_width: this should be an int. this is the chart width.
    the default value is 30.
chart_name: this should be an string. this is the heading of the chart.
    the default value is none.
left_gap: this should be an int. this should be the gap on the left side.
    the default value is 0
right_gap: this should be an int. this should be the gap on the right side.
    the default value is 0.
resource_usage: this should be a string. this should be the resource that's currently used.
    the default value is None.
left_side: this should be a string. it's the left side bar.
    the default value is "|"
right_side: this should be a string. it's the bar on the right side.
    the default value is "|"
roof: this should be a string. it's the roof of the chart.
    the default value is "_"
floor: this should be a string. it's the the floor of the chart.
    the default value is "‾"
name_seperator: this should be a string. it's the seperator that seperates the actual chart from the heading.
    the default value is "="
value_seperator: this should be a string. it's the seperator that seperates the actual chart from the value.
    the default value is "="

### av_cpu_ini():
this is the cpu data initiation function.
it takes nothing as input.
it returns a list of data.
the first thing is the cpu datas that it reads from the ini file
or if something is wrong with it, then writes to the ini file and
then reads from it.
that data is a dict object.
the second thing it returns is the cpu starting chart. that's a list of lists.
it's actually a 2d array.
the third thing it returns is the bar height and color map.
it's a dict object.

### readwrite():
this is the function that reads and/or writes the data.
it takes these inputs.
section: which should be an string. this should be the the section name.
key: which should be a string. this should be the the key name.
value: this could be anything idk.... this should be the value the you're assigning the key to.
data_type: this should be a type. this should be the type of the value.
    it returns the value converted to the data type.
    the default is string.
