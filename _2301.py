

import humanize
x = humanize.naturalsize(1024 * 1024 * 1024)

import humanize as h
x = h.naturalsize(1024 * 1024 * 1024)
print(x)

from humanize import intcomma as comma, intword as w
print(comma(123456), w(124325134))

import datetime as dt
print(dt.datetime(2024,1,23))

import numbertranslator as nt
x = nt.translate_number(12345)
print(x)