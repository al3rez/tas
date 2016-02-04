#!/usr/bin/env python3
from tas import make_schedule
from tabulate import tabulate


if __name__ == '__main__':
    table = make_schedule()
    tabular = tabulate(list(table), tablefmt="plain")
    print(tabular)
