from os import name as os_name
from os import system as os_system
from time import sleep as time_sleep
from subprocess import run as subprocess_run

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
    if the bar height is
    """
    if type(bar_height) != int:
        exit("The bar height should be an int.")
    elif bar_height < 10:
        exit("The bar height is too low. it should at least be 10")
    bar_box_number_list = [bar_number+1 for bar_number in range(bar_height)]
    g = y = r = int(bar_height*30/100)

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

def bar_maker(resource_usage:int, bar_height_and_color:dict, bar_width:int):
    return [
        bar_height_and_color[resource_value]*bar_width if resource_value <= resource_usage
        else
            "."*bar_width if resource_value == 1
            else " "*bar_width
        for resource_value in bar_height_and_color]

def chart_maker(
        last_bar:list,              last_chart:list,    chart_width:int=30,
        chart_name:str=None,        left_gap:int=0,     right_gap:int=0,
        resource_usage:str=None,    left_side:str="|",  right_side:str="|",
        roof:str="_",               floor:str="‾",
        ):

    last_chart.pop(0)
    last_chart.append(last_bar)

    full_width = chart_width+len(left_side)+len(right_side)+left_gap+right_gap
    proper_chart = [roof*full_width]

    if chart_name != None:
        proper_chart.append(f"{left_side}{chart_name:^{chart_width+left_gap+right_gap}}{right_side}")
        proper_chart.append(left_side+"="*(chart_width+left_gap+right_gap)+right_side)

    for shit in [list(row) for row in zip(*last_chart)][::-1]:
        y = left_side
        y += " "*left_gap
        for stuff in shit:
            y += stuff
        y += " "*right_gap
        y += right_side
        proper_chart.append(y)

    if resource_usage != None:
        proper_chart.append(left_side+"="*(chart_width+left_gap+right_gap)+right_side)
        resource_usage = resource_usage+"%"
        proper_chart.append(f"{left_side}{resource_usage:^{chart_width+left_gap+right_gap}}{right_side}")

    proper_chart.append(floor*full_width)

    return proper_chart

def main():
    cpu_bar_height:int = 10
    cpu_bar_width:int = 1
    cpu_chart_width:int = 30
    cpu_left_gap:int = 0
    cpu_right_gap:int = 0
    cpu_starting_chart:list = [["."*cpu_bar_width if box == 0 else " "*cpu_bar_width for box in range(cpu_bar_height)]for _ in range(cpu_chart_width)]
    cpu_bar:dict = bar_maker_ini(cpu_bar_height)
    cpu_heading:str = "CPU Usage:"
    cpu_start:bool = True
    cpu_left_side:str = "|"
    cpu_right_side:str = "|"
    cpu_roof:str = "_"
    cpu_floor:str = "‾"
    cpu_box:str = "██"


    if cpu_chart_width < len(cpu_heading):
        exit("cpu chart width is less than cpu heading.")

    while True:
        cpu_usage = psutil_cpu_percent()
        common = {
                "last_bar":bar_maker(
                    resource_usage=int(cpu_usage/100*cpu_bar_height),
                    bar_height_and_color=cpu_bar,
                    bar_width=cpu_bar_width
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
        }
        last_cpu_starting_chart = chart_maker(
            **common, last_chart=cpu_starting_chart if cpu_start==True
                                    else last_cpu_starting_chart)
        time_sleep(1)
        clear()
        for rows in last_cpu_starting_chart:
            print(rows)

if __name__ == "__main__":
    main()
