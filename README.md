# LearnPython
Descrição
Atividade 1:
Uma empresa decidiu dar uma gratificação de Natal a seus funcionários, baseada no número de horas extras e no número de horas que o funcionário faltou ao trabalho. O valor do prêmio é obtido pela consulta à tabela que se segue, na qual:

H = número de horas extras – (2/3 * ( número de horas falta ))

![image](https://github.com/Rosajoaohttps/LearnPython/assets/105798242/2b383820-d507-4032-b2c7-f80d9e9e6244)



Pseudocódigo Atividade 1: 

Var 
HorasExtras, HorasFalta, TotalMinutos Real 

escreva ("Numero de horas extras: ")
leia(HorasExtras)

escreva ("Numero de horas Faltantes: ")
leia(HorasFalta)

TotalMinutos = (HoraExtras = (2/3*HorasFaltas)) * 60 

se (TotalMinutos >= 2401 ) entao 

 escreva ("A gratificação sera de 500,00 reais")
 
  se (TotalMinutos >= 1801 e TotalMinutos <= 2400) entao 
  
   escreva ("Sua Bonificação e 400,00 reais")
   
 se (TotalMinutos >= 1201 e TotalMinutos <= 1800) entao 
 
   escreva ("Sua Bonificação e 300,00 reais")
   
 se (TotalMinutos >= 600 e TotalMinutos <= 1200) entao 
 
   escreva ("Sua Bonificação e 200,00 reais")
   
 se (TotalMinutos < 600) entao 
 
   escreva ("Sua Bonificação e 100,00 reais")
fimse  

fimse

fimse

fimse

fimse

fim







Descrição Atividade 2: 
Faça um programa que receba a idade e o peso de uma pessoa. De acordo com a tabela a seguir, verifique e mostre em qual grupo de risco essa pessoa se encaixa.

![image](https://github.com/Rosajoaohttps/LearnPython/assets/105798242/972bcd9c-aa47-479c-b6e8-f4a4896a5a0e)


Pseudocódigo Atividade 2: 

var 

peso, idade int

escreva: ("Digite sua idade")

leia (idade) 


escreva: ("Digite sua peso")

leia (peso)


se (idade < 20 e  peso <= 60 ) entao 

 escreva (" Grasu de risco  9 ")
 
se (idade < 20 e  peso > 60  <= 90 ) entao 

 escreva (" Grasu de risco  8 ")
 
se (idade < 20 e  peso >91) entao 

 escreva (" Grasu de risco  7 ")
 

se (idade >= 20 e idade <= 50  peso <=60) entao 

 escreva (" Grasu de risco  6 ")
 
se (idade >= 20 e idade <= 50  peso >60 e peso <= 90) entao 

 escreva (" Grasu de risco  5 ")
 
se (idade >= 20 e idade <= 50  > 90) entao 

 escreva (" Grasu de risco  4 ")
 

se (idade > 50  e peso <= 60) entao 

 escreva (" Grasu de risco  3")
 
se (idade > 50  e peso >  60 e peso <= 90) entao 

 escreva (" Grasu de risco  2")
 
se (idade > 50  e peso <90) entao 

 escreva (" Grasu de risco  1")
 



