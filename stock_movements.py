import json

with open("stock.json","r", encoding="utf-8") as f:
    data = json.load(f)

products = {item["codigoProduto"]: item for item in data["estoque"]}
movement_id= 1

def register_movement(product_code, qtd, desc):
    global movement_id
    if product_code not in products:
        raise ValueError("Produto nao encontrado")

    product = products[product_code]
    new_stock= product["estoque"]+ qtd
    if new_stock<0:
        raise ValueError("Nao ah quantidade suficiente do produto para a movimentacao.")

    product["estoque"] = new_stock
    movement= {
        "id": movement_id,
        "Codigo do produto": product_code,
        "Descricao do produto":product["descricaoProduto"],
        "Descricao da movimentaca":desc,
        "Quantidade movimentada":qtd,
        "Em estoque": new_stock
    }
    movement_id+= 1
    return movement

if __name__ == "__main__":
    try:
        movement1= register_movement(101,-20, "Saida")
        print(movement1)

        movement2= register_movement(104,50, "Entrada")
        print(movement2)

    except ValueError as e:
        print("Error:", e)
