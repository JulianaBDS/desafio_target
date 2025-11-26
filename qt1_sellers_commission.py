from collections import defaultdict
import json

with open("sales.json", "r", encoding="utf-8") as f:
    data= json.load(f)

commission = lambda v: 0 if v<100 else 0.01*v if v< 500 else 0.05* v
allSales= defaultdict(float)
for sale in data["vendas"]:
    allSales[sale["vendedor"]]+= commission(sale["valor"])

for seller, allSales in allSales.items():
    print(f"{seller}: R${allSales:.2f}")
