custo1 = {"arrendamento": 800.0, "mão de obra": 900.0, "sementes": 2000.0, "energia": 500.0, "insumos": 2000.0}
venda1 = {"valor/T": 170.0, "tonelada/ha": 75.0}
calculo_custo1 = custo1["arrendamento"] + custo1["mão de obra"] + custo1["energia"] + custo1["insumos"]
lucro_bruto1 = venda1["valor/T"] * venda1["tonelada/ha"]
lucro_liquido1 = lucro_bruto1 - calculo_custo1

custo2 = {"arrendamento": 800.0, "mão de obra": 1000.0, "sementes": 55000, "energia": 500.0, "insumos": 15000.0}
venda2 = {"valor/uni": 3.0, "unidade/ha": 55000}
calculo_custo2 = custo2["arrendamento"] + custo2["mão de obra"] + custo2["energia"] + custo2["insumos"]
lucro_bruto2 = venda2["valor/uni"] * venda2["unidade/ha"]
lucro_liquido2 = lucro_bruto2 - calculo_custo2 

custo3 = {"arrendamento": 800.0, "mão de obra": 5000.0, "sementes": 15000, "energia": 500.0, "insumos": 5000.0}
venda3 = {"valor/T":900.0, "toneladas/ha": 30}
calculo_custo3 = custo3["arrendamento"] + custo3["mão de obra"] + custo3["energia"] + custo3["insumos"]
lucro_bruto3 = venda3 ["valor/T"] * venda3["toneladas/ha"] 
lucro_liquido3 = lucro_bruto3 = lucro_bruto3

custo4 = {"arrendamento": 800.0, "mão de obra": 5000.0, "sementes": 28000.0, "energia": 500.0, "insumos": 10000.0}
venda4 = {"valor/saco":150.0, "sacos/ha": 75}
calculo_custo4 = custo4["arrendamento"] + custo4["mão de obra"] + custo4["energia"] + custo4["insumos"]
lucro_bruto4 = venda4 ["valor/saco"] * venda4["sacos/ha"] 
lucro_liquido4 = lucro_bruto4 - lucro_bruto4

custo5 = {"arrendamento": 800.0, "mão de obra": 5000.0, "sementes": 2100.0, "energia": 500.0, "insumos": 20000.0}
venda5 = {"valor/caixa":52.0, "caixa/ha": 2500}
lucro_bruto5 = venda5 ["valor/caixa"] * venda5 ["caixa/ha"]
calculo_custo5 = custo5["arrendamento"] + custo5["mão de obra"] + custo5["energia"] + custo5["insumos"]
lucro_liquido5 = lucro_bruto5 - lucro_bruto5


cultura1 = "cana"
cultura2 = "abacaxi"
cultura3 = "macaxeira"
cultura4 = "feijão"
cultura5 = "maracujá"

menu = f"BEM VINDO! Ao agroCalc. O sistema que prever sua produção agricula! \n" \
                    f"Digite o número correspondente a cultura que você deseja prever \n" \
                    f"1. {cultura1}\n" \
                    f"2. {cultura2}\n" \
                    f"3. {cultura3}\n" \
                    f"4. {cultura4}\n" \
                    f"5. {cultura5}\n" \
                    
print (menu)
cultura_usuario = input("Escolha a cultura que você quer prever!: ")
hectares = int (input(f"Digite a quantidade de hectareas que você quer plantar: "))


if cultura_usuario == "1":
    calculo1A = calculo_custo1 * hectares
    calculo2A = lucro_bruto1 * hectares
    calculo3A = lucro_liquido1 * hectares
    print(f"Na cultura de {cultura1} o custo geral estimado é: {calculo1A} \n" 
          f"O lucro bruto estimado é: {calculo2A} \n"
          f"o lucro líquido estimado é: {calculo3A}")

elif cultura_usuario == "2":
    calculo1B = calculo_custo2 * hectares
    calculo2B = lucro_bruto2 * hectares
    calculo3B = lucro_liquido2 * hectares
    print (f"Na cultura de {cultura2} o custo geral estiamdo é: {calculo1B} \n"
           f"O lucro bruto estimado é: {calculo2B} \n"
           f"O lucro líquido estimado é: {calculo2B}")

elif cultura_usuario == "3":
    calculo1C = calculo_custo3 * hectares
    calculo2C = lucro_bruto3 * hectares
    calculo3C = lucro_liquido3 * hectares
    print (f"Na cultura de {cultura3} o custo geral estimado é: {calculo1C} \n"
           f"O lucro bruto estimado é: {calculo2C} \n"
           f"O lucro líquido estimado é: {calculo2C}")


elif cultura_usuario == "4":
    calculo1D = calculo_custo4 * hectares
    calculo2D = lucro_bruto4 * hectares
    calculo3D = lucro_liquido4 * hectares
    print (f"Na cultura de {cultura4} o custo feral estimado é: {calculo1D} \n"
           f"O lucro bruto estimado é: {calculo2D} \n"
           f"O lucro líquido estimado é: {calculo2D}")


elif cultura_usuario == "5":
    calculo1E = calculo_custo5 * hectares
    calculo2E = lucro_bruto5 * hectares
    calculo3E = lucro_liquido5 * hectares
    print (f"Na cultura de {cultura5} o custo geral estimado é: {calculo1E} \n"
           f"O lucro bruto estimado é: {calculo2E} \n"
           f"O lucro líquido estimado é: {calculo2E}")
else: 
    print("ERRO!!! Reveja a sua escilha de cultura:)")