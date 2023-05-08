import csv
from math import log10

# Função para imprimir os 20 principais municípios de acordo com o valor e o mínimo de habitantes
def print_top_20(data, reverse_order, min_habitants):
    # Ordena os dados com base no valor (IDHM, IDHM-L, ou IDHM-R) em ordem crescente ou decrescente
    sorted_data = sorted(data.items(), key=lambda x: x[1]["value"], reverse=reverse_order)
    count = 0
    for index, (city, city_data) in enumerate(sorted_data):
        if city_data["habitantes"] >= min_habitants:
            count += 1
            print(f"{count:<7} {city_data['estado']:<10} {city:<30} {city_data['value']:<6.2f} {city_data['habitantes']:>10} habitantes")
            if count == 20:
                break
# Função para calcular o IDHM com base nos subíndices IDHM-E, IDHM-L e IDHM-R                
def calculate_idh(subindices):
    return (subindices['IDHM-E'] + subindices['IDHM-L'] + subindices['IDHM-R']) / 3
    
# Função principal
def main():
    # Dicionário para armazenar informações dos municípios
    municipalities = {}

    with open("idhm.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            city = row["município"]
            espvida = float(row["espvida"])
            rdpc = float(row["rdpc"])
            idhm_l = (espvida - 25) / 60
            idhm_r = log10(rdpc / 3.9) / 2.6
            idhm_e = float(row["idhm_e"])
            idhm = calculate_idh({"IDHM-E": idhm_e, "IDHM-L": idhm_l, "IDHM-R": idhm_r})
            
	    # Armazena informações do município no dicionário
            municipalities[city] = {
                "estado": row["sigla"],
                "habitantes": int(row["pesotot"]),
                "IDHM": idhm,
                "IDHM-L": idhm_l,
                "IDHM-R": idhm_r, }
            

    while True:
        min_habitants = int(input("Informe o mínimo de habitantes que o município deve ter: "))
        print("\n")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print("Top 20 municípios com mais de", min_habitants, "habitantes com maior IDHM")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print_top_20({city: {"estado": data["estado"], "habitantes": data["habitantes"], "value": data["IDHM"]} for city, data in municipalities.items()}, True, min_habitants)
        
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print("Top 20 municípios com mais de", min_habitants, "habitantes com menor IDHM")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print_top_20({city: {"estado": data["estado"], "habitantes": data["habitantes"], "value": data["IDHM"]} for city, data in municipalities.items()}, False, min_habitants)

        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print("Top 20 municípios com mais de", min_habitants, "habitantes com maior IDHM-L")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print_top_20({city: {"estado": data["estado"], "habitantes": data["habitantes"], "value": data["IDHM-L"]} for city, data in municipalities.items()}, True, min_habitants)

        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print("Top 20 municípios com mais de", min_habitants, "habitantes com menor IDHM-R")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print_top_20({city: {"estado": data["estado"], "habitantes": data["habitantes"], "value": data["IDHM-R"]} for city, data in municipalities.items()}, False, min_habitants)

        stop = input("Digite n/N para parar: ")
        if stop.lower() == "n":
            break
            
# Inicia a função principal quando o script é executado
if __name__ == "__main__":
    main()


