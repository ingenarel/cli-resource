"""
if you want to customize this you shouldn't touch this file.
you should edit the resource_monitor function.
don't worry it's hard to make that crash. i think...

but if you know what you're doing, please go on
"""

from os import name as os_name
from os import system as os_system
from time import sleep as time_sleep
from subprocess import run as subprocess_run
import configparser, re

try:
    from psutil import cpu_percent as psutil_cpu_percent
except ModuleNotFoundError:
    print(f"You're missing the psutil module.")
    print("Trying to install it using pip")
    subprocess_run(["pip", "install", "psutil"])

try:
    from colorama import Fore, init
    init(autoreset=True)
except ModuleNotFoundError:
    print(f"You're missing the colorama module.")
    print("Trying to install it using pip")
    subprocess_run(["pip", "install", "colorama"])

osname = os_name

if osname == "nt":
    def clear():
        os_system("cls")

elif osname == "posix":
    def clear():
        os_system("clear")

def bar_maker_ini(bar_height:int=10, box:str="█"):
    """
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
    """
    if type(bar_height) != int:
        exit("The bar height should be an int.")
    elif bar_height < 3:
        exit("The bar height is too low. it should at least be 3")
    bar_box_number_list = [bar_number+1 for bar_number in range(bar_height)]
    g = int(bar_height*0.429)
    y = int(bar_height*0.286)
    r = int(bar_height*0.143)

    if g+y+r < bar_height:
        g += 1
        if g+y+r < bar_height:
            y += 1
            if g+y+r < bar_height:
                r += 1

    first_items_that_are_green = bar_box_number_list[:g]
    first_items_that_are_yellow = bar_box_number_list[g:g+y]
    first_items_that_are_red = bar_box_number_list[g+y:g+y+r]
    bar_height_and_color = {green_boxes:Fore.GREEN+box for green_boxes in first_items_that_are_green}
    bar_height_and_color.update({yellow_boxes:Fore.YELLOW+box for yellow_boxes in first_items_that_are_yellow})
    bar_height_and_color.update({red_boxes:Fore.RED+box for red_boxes in first_items_that_are_red})

    return bar_height_and_color

def bar_maker(resource_usage:int, bar_height_and_color:dict, bar_width:int, fill:str=".", zero_fill:str="."):
    """
    this is the bar maker function. it takes these values:

    resource_usage: which should be an int. this is the resource currently being used.
        that means the ammount of boxes that the bar will show.

    bar_height_and_color: which should be a dict object. this is actually a value and color map.
    the bar_maker_ini() provides this. i didn't combine these two because this doesn't need to be calculated every time a new bar is calculated.
    so i just made that a new function.

    bar_width: this should be an int. it should be the width of the bar.

    fill: this should be a string. this will fill the empty values in the bar.

    zero_fill: this should be a string. this will make the represent the value of zero if the bar is totally empty.

    it returns a list. if you print each item from that list you should see a vertical bar.

    """
    return [
        bar_height_and_color[resource_value] if resource_value <= resource_usage
        else
            zero_fill*bar_width if resource_value == 1
            else fill*bar_width
        for resource_value in bar_height_and_color]

def chart_updater(
        last_bar:list,
        last_chart:list,
        ):
    """
    this is the chart updater.
    it takes these values.
    last_bar: it should be a list that should be the last bar that's made with the bar_maker() function.
    last_chart: this should be the last chart that's either made with this function, or the starting chart that the code provides.
        it's a custom 2d array. only provide your custom thing if you know what you're doing.

    it returns the updated 2d array aka the updated chart.
    """
    last_chart.pop(0)
    last_chart.append(last_bar)
    return last_chart

def chart_parser(
    chart:list,
    bar_width:int,
    chart_width:int=30,
    chart_name:str=None,
    left_gap:int=0,
    right_gap:int=0,
    resource_usage:str=None,
    left_side:str="|",
    right_side:str="|",
    roof:str="_",
    floor:str="‾",
    name_seperator:str="=",
    value_seperator:str="="
        ):
    """
    this parses the 2d array returned from chart_updater into a human readeable chart.
    it takes these values:

    chart: this should be the chart returned from the chart_updater function. it should be a 2d array.
    bar_width: this should be an int. this is the bar width.
    chart_width: this should be an int. this is the chart width.
    chart_name: this should be an string. this is the heading of the chart.
    left_gap: this should be an int. this should be the gap on the left side.
    right_gap: this should be an int. this should be the gap on the right side.
    resource_usage: this should be a string. this should be the resource that's currently used.
    left_side: this should be a string. it's the left side bar.
    right_side: this should be a string. it's the bar on the right side.
    roof: this should be a string. it's the roof of the chart.
    floor: this should be a string. it's the the floor of the chart.
    name_seperator: this should be a string. it's the seperator that seperates the actual chart from the heading.
    value_seperator: this should be a string. it's the seperator that seperates the actual chart from the value.

    """
    full_width = chart_width*bar_width+len(left_side)+len(right_side)+left_gap+right_gap
    proper_chart = [roof*int(full_width/len(roof))]
    x = chart_width*bar_width+left_gap+right_gap

    if chart_name != None:
        proper_chart.append(f"{left_side}{chart_name:^{x}}{right_side}")
        proper_chart.append(left_side+name_seperator*int(x/len(name_seperator))+right_side)

    for shit in [list(row) for row in zip(*chart)][::-1]:
        y = left_side
        y += " "*left_gap
        for stuff in shit:
            y += stuff
        y += " "*right_gap
        y += right_side
        proper_chart.append(y)

    if resource_usage != None:
        proper_chart.append(left_side+value_seperator*int(x/len(value_seperator))+right_side)
        resource_usage = resource_usage+"%"
        proper_chart.append(f"{left_side}{resource_usage:^{x}}{right_side}")

    proper_chart.append(floor*int(full_width/len(floor)))

    return proper_chart

def av_cpu_ini():
    """
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
    """
    cpu_bar_height = readwrite("CPU", "cpu_bar_height", 10, int)
    cpu_chart_width = readwrite("CPU", "cpu_chart_width", 30, int)
    cpu_left_gap = readwrite("CPU", "cpu_left_gap", 0, int)
    cpu_right_gap = readwrite("CPU", "cpu_right_gap", 0, int)
    cpu_heading = readwrite("CPU", "cpu_heading", "CPU Usage:")
    cpu_box = readwrite("CPU", "cpu_box", "█")
    cpu_left_side = readwrite("CPU", "cpu_left_side", "|")
    cpu_right_side = readwrite("CPU", "cpu_right_side", "|")
    cpu_roof = readwrite("CPU", "cpu_roof", "_")
    cpu_floor = readwrite("CPU", "cpu_floor", "‾")
    cpu_fill = readwrite("CPU", "cpu_fill", " ")
    cpu_zero_fill = readwrite("CPU", "cpu_zero_fill", ".")
    cpu_name_seperator = readwrite("CPU", "cpu_name_seperator", "=")
    cpu_value_seperator = readwrite("CPU", "cpu_value_seperator", "=")

    cpu_bar_width= len(cpu_box)

    cpu_starting_chart:list = [["."*cpu_bar_width if box == 0 else cpu_fill*cpu_bar_width for box in range(cpu_bar_height)]for _ in range(cpu_chart_width)]
    cpu_bar_height_and_color:dict = bar_maker_ini(bar_height=cpu_bar_height,box=cpu_box)
    return(
        {
            "cpu_bar_height": cpu_bar_height,
            "cpu_chart_width": cpu_chart_width,
            "cpu_left_gap": cpu_left_gap,
            "cpu_right_gap": cpu_right_gap,
            "cpu_heading": cpu_heading,
            "cpu_box": cpu_box,
            "cpu_left_side": cpu_left_side,
            "cpu_right_side": cpu_right_side,
            "cpu_roof": cpu_roof,
            "cpu_floor": cpu_floor,
            "cpu_fill": cpu_fill,
            "cpu_zero_fill": cpu_zero_fill,
            "cpu_name_seperator": cpu_name_seperator,
            "cpu_value_seperator": cpu_value_seperator,
            "cpu_bar_width": cpu_bar_width
        },
        cpu_starting_chart,
        cpu_bar_height_and_color,
    )

def readwrite(section:str, key:str, value, data_type:type=str):
    """
    this is the function that reads and/or writes the data.
    it takes these inputs.
    """
    config = configparser.ConfigParser()
    config_file_name = "resource_monitor.cfg"
    config.read(config_file_name)
    value = str(value)
    while True:
        try:
            x = config[section][key][1:-1] if re.search(r"^\".+\"$", config[section][key]) else config[section][key]
            return data_type(x)
        except KeyError:
            config[section]={
                key: f"\"{value}\"" if data_type==str else value,
            }
            if config.has_section(section):
                config.read(config_file_name)
        except ValueError:
            config.read(config_file_name)
            config[section][key] = f"\"{value}\"" if data_type==str else value
        with open(config_file_name, "w") as configfile:
            config.write(configfile)
        continue

def main():
    av_cpu_values, av_cpu_starting_chart, av_cpu_bar_height_and_color = av_cpu_ini()
    start = True
    while True:
        av_cpu_percent = psutil_cpu_percent()
        av_cpu_last_chart = chart_updater(
            last_bar = bar_maker(
                resource_usage=int(av_cpu_percent/100*av_cpu_values["cpu_bar_height"]),
                bar_height_and_color=av_cpu_bar_height_and_color,
                bar_width=av_cpu_values["cpu_bar_width"],
                fill=av_cpu_values["cpu_fill"],
                zero_fill=av_cpu_values["cpu_zero_fill"]
            ),
            last_chart=av_cpu_starting_chart if start==True else av_cpu_last_chart
        )
        av_cpu_chart_proper = chart_parser(
            chart=av_cpu_last_chart,
            bar_width=av_cpu_values["cpu_bar_width"],
            chart_width=av_cpu_values["cpu_chart_width"],
            chart_name=av_cpu_values["cpu_heading"],
            left_gap=av_cpu_values["cpu_left_gap"],
            right_gap=av_cpu_values["cpu_right_gap"],
            resource_usage=str(av_cpu_percent),
            left_side=av_cpu_values["cpu_left_side"],
            right_side=av_cpu_values["cpu_right_side"],
            roof=av_cpu_values["cpu_roof"],
            floor=av_cpu_values["cpu_floor"],
            name_seperator=av_cpu_values["cpu_name_seperator"],
            value_seperator=av_cpu_values["cpu_value_seperator"],
        )
        clear()
        for rows in av_cpu_chart_proper:
            print(rows)
        start=False
        time_sleep(1)

if __name__ == "__main__":
    main()
