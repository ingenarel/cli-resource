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
    It takes a bar_height which is the bar height which should be an int.
    if the bar height is less than 3, it doesn't allow it.
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
    return [
        bar_height_and_color[resource_value] if resource_value <= resource_usage
        else
            zero_fill*bar_width if resource_value == 1
            else fill*bar_width
        for resource_value in bar_height_and_color]

def chart_maker(
        last_bar:list,
        last_chart:list,
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

    last_chart.pop(0)
    last_chart.append(last_bar)

    full_width = chart_width*bar_width+len(left_side)+len(right_side)+left_gap+right_gap
    proper_chart = [roof*int(full_width/len(roof))]
    x = chart_width*bar_width+left_gap+right_gap

    if chart_name != None:
        proper_chart.append(f"{left_side}{chart_name:^{x}}{right_side}")
        proper_chart.append(left_side+name_seperator*int(x/len(name_seperator))+right_side)

    for shit in [list(row) for row in zip(*last_chart)][::-1]:
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

def av_cpu_ini(
    cpu_bar_height:int = 30,
    cpu_chart_width:int = 140,
    cpu_left_gap:int = 0,
    cpu_right_gap:int = 0,
    cpu_heading:str = "CPU Usage:",
    cpu_box:str = "█",
    cpu_left_side:str = "|",
    cpu_right_side:str = "|",
    cpu_roof:str = "_",
    cpu_floor:str = "‾",
    cpu_fill:str = " ",
    cpu_zero_fill:str = ".",
    cpu_name_seperator:str = "=",
    cpu_value_seperator:str = "=",
    ):
    cpu_bar:dict = bar_maker_ini(
        bar_height=cpu_bar_height,
        box=cpu_box
        )
    cpu_bar_width= len(cpu_box)
    cpu_starting_chart:list = [["."*cpu_bar_width if box == 0 else cpu_fill*cpu_bar_width for box in range(cpu_bar_height)]for _ in range(cpu_chart_width)]

    if cpu_chart_width < len(cpu_heading):
        exit("cpu chart width is less than cpu heading.")
    cpu_usage = psutil_cpu_percent()
    common = {
            "last_bar":bar_maker(
                resource_usage=int(cpu_usage/100*cpu_bar_height),
                bar_height_and_color=cpu_bar,
                bar_width=cpu_bar_width,
                fill=cpu_fill,
                zero_fill=cpu_zero_fill
                ),
            "chart_width": cpu_chart_width,
            "chart_name": cpu_heading,
            "left_gap": cpu_left_gap,
            "right_gap": cpu_right_gap,
            "resource_usage": str(cpu_usage),
            "left_side": cpu_left_side,
            "right_side": cpu_right_side,
            "roof": cpu_roof,
            "floor": cpu_floor,
            "bar_width": cpu_bar_width,
            "name_seperator": cpu_name_seperator,
            "value_seperator": cpu_value_seperator,
    }
    # if cpu_start == True:
    #     last_cpu_starting_chart = chart_maker(**common, last_chart=cpu_starting_chart)
    #     cpu_start = False
    # else:
    #     last_cpu_starting_chart = chart_maker(**common, last_chart=last_cpu_starting_chart)

    # for rows in last_cpu_starting_chart:
    #     yield rows

    return(cpu_starting_chart, common)

def readwrite(section:str, key:str, value, data_type:type=str):
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

def av_cpu_startup():
    return{
        "cpu_bar_height": readwrite("CPU", "cpu_bar_height", 10, int),
        "cpu_chart_width": readwrite("CPU", "cpu_chart_width", 30, int),
        "cpu_left_gap": readwrite("CPU", "cpu_left_gap", 0, int),
        "cpu_right_gap": readwrite("CPU", "cpu_right_gap", 0, int),
        "cpu_heading": readwrite("CPU", "cpu_heading", "CPU Usage:"),
        "cpu_box": readwrite("CPU", "cpu_box", "█"),
        "cpu_left_side": readwrite("CPU", "cpu_left_side", "|"),
        "cpu_right_side": readwrite("CPU", "cpu_right_side", "|"),
        "cpu_roof": readwrite("CPU", "cpu_roof", "_"),
        "cpu_floor": readwrite("CPU", "cpu_floor", "‾"),
        "cpu_fill": readwrite("CPU", "cpu_fill", " "),
        "cpu_zero_fill": readwrite("CPU", "cpu_zero_fill", "."),
        "cpu_name_seperator": readwrite("CPU", "cpu_name_seperator", "="),
        "cpu_value_seperator": readwrite("CPU", "cpu_value_seperator", "="),
        }

def main():
    cpu_start = True
    cpu_starting_chart, common = av_cpu_ini(av_cpu_startup)
    if cpu_start == True:
        last_cpu_starting_chart = chart_maker(**common, last_chart=cpu_starting_chart)
        cpu_start = False
    else:
        last_cpu_starting_chart = chart_maker(**common, last_chart=last_cpu_starting_chart)

    clear()
    for rows in last_cpu_starting_chart:
        print(rows)
    time_sleep(1)

if __name__ == "__main__":
    main()
