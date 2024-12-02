import time
from contextlib import contextmanager

from rich.align import Align
from rich.console import Console
from rich.live import Live
from rich.table import Table
from rich.text import Text
from rich.layout import Layout
from rich.panel import Panel


def update_row(table: Table, row_index: int, new_values: list):
    if row_index < len(table.rows):
        for column_index, new_value in enumerate(new_values):
            table.columns[column_index]._cells[row_index] = new_value

   

console = Console()

layout = Layout()

BEAT_TIME = 0.04

table1 = Table(show_footer=False)
table_centered = Align.center(table1)

@contextmanager
def beat(length: int = 1) -> None:
    yield
    time.sleep(length * BEAT_TIME)
    
console.clear()

table1 = Table(title="FCFS", show_header=True, show_footer=False, header_style="bold magenta")

table2 = Table(title="PB", show_header=True, show_footer=False,header_style="bold magenta")

table3 = Table(title="RR", show_header=True, show_footer=False,header_style="bold magenta")

table4 = Table(title="MLFQ", show_header=True, show_footer=False,header_style="bold magenta")

table1_centered = Align.center(table1)
table2_centered = Align.center(table2)
table3_centered = Align.center(table3)
table4_centered = Align.center(table4)
layout.split_column(
    Layout(Panel(table1_centered,expand=True)),
    Layout(Panel(table2_centered,expand=True)),
    Layout(Panel(table3_centered,expand=True)),
    Layout(Panel(table4_centered,expand=True))
)

with Live(layout, console=console, screen = False, refresh_per_second=20) as live:
    with beat(1):
        table1.add_column("New Queue", justify="center", style="cyan", no_wrap=True)
    with beat(1):
        table1.add_column("Ready Queue", justify="center", style="cyan", no_wrap=True)
    with beat(1):
        table1.add_column("Running", justify="center", style="cyan", no_wrap=True)
    with beat(1):
        table1.add_column("Waiting Queue", justify="center", style="cyan", no_wrap=True)
    with beat(1):
        table1.add_column("IO Queue", justify="center", style="cyan", no_wrap=True)
    with beat(1):
        table1.add_column("Finished Queue", justify="center", style="cyan", no_wrap=True)
   
    with beat(1):
        table2.add_column("New Queue", justify="center", style="cyan", no_wrap=True)
    with beat(1):
        table2.add_column("Ready Queue", justify="center", style="cyan", no_wrap=True)
    with beat(1):
        table2.add_column("Running", justify="center", style="cyan", no_wrap=True)
    with beat(1):
        table2.add_column("Waiting Queue", justify="center", style="cyan", no_wrap=True)
    with beat(1):
        table2.add_column("IO Queue", justify="center", style="cyan", no_wrap=True)
    with beat(1):
        table2.add_column("Finished Queue", justify="center", style="cyan", no_wrap=True)

    with beat(1):
        table3.add_column("New Queue", justify="center", style="cyan", no_wrap=True)
    with beat(1):
        table3.add_column("Ready Queue", justify="center", style="cyan", no_wrap=True)
    with beat(1):
        table3.add_column("Running", justify="center", style="cyan", no_wrap=True)
    with beat(1):
        table3.add_column("Waiting Queue", justify="center", style="cyan", no_wrap=True)
    with beat(1):
        table3.add_column("IO Queue", justify="center", style="cyan", no_wrap=True)
    with beat(1):
        table3.add_column("Finished Queue", justify="center", style="cyan", no_wrap=True)
        
    with beat(1):
        table4.add_column("New Queue", justify="center", style="cyan", no_wrap=True)
    with beat(1):
        table4.add_column("Ready Queue", justify="center", style="cyan", no_wrap=True)
    with beat(1):
        table4.add_column("Running", justify="center", style="cyan", no_wrap=True)
    with beat(1):
        table4.add_column("Waiting Queue", justify="center", style="cyan", no_wrap=True)
    with beat(1):
        table4.add_column("IO Queue", justify="center", style="cyan", no_wrap=True)
    with beat(1):
        table4.add_column("Finished Queue", justify="center", style="cyan", no_wrap=True)   
        
    object = "Object"
    
    Working = True
    pos = 0
    id = 1
    
    with beat(2):
        table1.add_row(str(pos), "", "", "", "", "")
        table2.add_row(object, None, None, None, None, None)
        table3.add_row(object, None, None, None, None, None)
        table4.add_row(object, None, None, None, None, None)
    
    while Working:
        
        with beat(10):
            update_row(table1, id - 1, [str(pos), "", "", "", "", ""])
        with beat(10):
            update_row(table1, id - 1, ["", str(pos), "", "", "", ""])
        with beat(10):
            update_row(table2, id - 1, [str(pos), "", "", "", "", ""])
        with beat(10):
            update_row(table2, id - 1, ["", str(pos), "", "", "", ""])
        with beat(10):
            update_row(table3, id - 1, [str(pos), "", "", "", "", ""])
        with beat(10):
            update_row(table3, id - 1, ["", str(pos), "", "", "", ""])
        with beat(10):
            update_row(table4, id - 1, [str(pos), "", "", "", "", ""])
        with beat(10):
            update_row(table4, id - 1, ["", str(pos), "", "", "", ""])
        pos += 1
        
        if pos == 10:
            Working = False
    
    

  
