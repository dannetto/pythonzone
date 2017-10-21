segundos_str=input("Por gentileza, favor entrar com o número de segundos que necessita converter: ")
total_segs=int(segundos_str)

meses=(total_segs //3600)//24//30
dias=(total_segs //3600)//24
horas=total_segs //3600
segs_restantes=total_segs%3600
minutos=segs_restantes//60
segs_restantes_final=segs_restantes%60

print("é o equivalente a: ",mese(s), "meses,",dias, "dia(s),",horas, "hora(s),", minutos, "minuto(s) e", segs_restantes_final, "segundo(s).")