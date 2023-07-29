import json
from pandas import DataFrame, ExcelWriter


def exportExcel():
    e = ExcelWriter("all.xlsx")

    gz = []
    with open("光锥.json", "r") as f:
        content = f.read()
        gz = json.loads(content)

    df1 = DataFrame(gz)

    gz = []
    with open("活动.json", "r") as f:
        content = f.read()
        gz = json.loads(content)

    df2 = DataFrame(gz)

    gz = []
    with open("常驻.json", "r") as f:
        content = f.read()
        gz = json.loads(content)

    df3 = DataFrame(gz)

    df2.to_excel(e, sheet_name="限定池", index=False, header=True)
    df3.to_excel(e, sheet_name="常驻池", index=False, header=True)
    df1.to_excel(e, sheet_name="光锥池", index=False, header=True)

    e.close()
