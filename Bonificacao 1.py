#bonificacao

HorasExtras = float(input("Numero de Horas Extras: "))
HorasFaltas = float(input("Numero de Horas Faltantes: "))
TotalDeMinutos = (HorasExtras - (2/3*HorasFaltas)) * 60 


if TotalDeMinutos >= 2401: 
    print("Minutos Totais", TotalDeMinutos, "com gratificação de R$ 500,00")
elif TotalDeMinutos >= 1801 and TotalDeMinutos < 2401:
    print("Minutos Totais", TotalDeMinutos, "com gratificação de R$ 400,00")
elif TotalDeMinutos >= 1201 and TotalDeMinutos < 1800:
    print("Minutos Totais", TotalDeMinutos, "com gratificação de R$ 300,00")
elif TotalDeMinutos >= 600 and TotalDeMinutos < 1200:
    print("Minutos Totais", TotalDeMinutos, "com gratificação de R$ 200,00")
elif TotalDeMinutos < 600:
    print("Minutos Totais", TotalDeMinutos, "com gratificação de R$ 100,00")