#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File:test_list.py
# @Author: Feng
# @Date:2019/8/14
# @Desc:

eth = [(1, 20, 10.0), (2, 20, 20.0), (3, 20, 300), (4, 20, 400), (5, 20, 500), (6, 20, 600), (7, 20, 700), (8, 20, 800),
       (9, 20, 900), (10, 20, 1000), (11, 20, 1100), (12, 20, 1200)]

period_items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
amount_items = [100, 200, 30, 400, 50, 600, 70, 80, 9, 100, 101, 1200]

count = 18
i = 0

for items in eth:
    period = items[0]
    total = items[1]
    limit_price = items[2]
    print(limit_price, type(limit_price))
    if limit_price == float(10.0):
        print("==")

    if period != period_items[i]:
        i += 1
        continue

    if total - count < 0:
        i += 1
        continue

    if limit_price != amount_items[i]:
        i += 1
        continue

    # , type(period), type(total), type(limit_price))
    print(period, total, limit_price)
    i += 1

# import json
# with open("ulordone_node_exchange_info.json",'r') as f:
#     load_dict = json.load(f)
#     print(load_dict)
