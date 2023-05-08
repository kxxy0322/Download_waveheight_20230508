import calendar
from ecmwfapi import ECMWFDataServer

server = ECMWFDataServer()

# 定义参数列表
args_list = []
for year in range(2012, 2013):
    for month in range(4, 13):
        # 获取当月的天数
        days_in_month = calendar.monthrange(year, month)[1]
        args_list.append({
            "class": "ei",
            "dataset": "interim",
            "date": f"{year}-{month:02d}-01/to/{year}-{month:02d}-{days_in_month:02d}",
            "expver": "1",
            "grid": "0.125/0.125",
            "levtype": "sfc",
            "param": "229.140",
            "step": "0",
            "stream": "wave",
            "area": "38.5/119/35.5/123.5",
            "time": "00:00:00/06:00:00/12:00:00/18:00:00",
            "type": "an",
            "format": "netcdf",
            "target": f"C:/Users/22769/Desktop/GC/GOCI_data_analyse/waveheight/wave_{year}_{month:02d}.nc"
        })

# 循环下载数据
for args in args_list:
    server.retrieve(args)
