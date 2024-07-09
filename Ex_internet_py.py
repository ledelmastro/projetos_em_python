def recomendar_plano(consumo):
  while True:
    if consumo <= 10:
      return "Plano Essencial Fibra - 50Mbps"
    if consumo > 10 and consumo <= 20:
      return "Plano Prata Fibra - 100Mbps"
    if consumo > 20 and consumo <= 21:  
      return "Plano Premium Fibra - 300Mbps"
    else:
      print("Valor inválido.")
      break 
    
consumo = float(input())
print(recomendar_plano(consumo))
