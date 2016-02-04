#!/usr/bin/env python3
from tas import make_schedule
from tabulate import tabulate
import os
import csv


if __name__ == '__main__':
    table = make_schedule()
    tabular = tabulate(list(table), tablefmt="plain")
    print(tabular)

