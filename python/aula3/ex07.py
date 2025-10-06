matriz =[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

a,b,c = matriz[0]
d,e,f = matriz[1]
g,h,i = matriz[2]

#essa pode ajudar no jogo da velha

det = a * (e * i - f * h) - b * (d * h - e * g) + c * (d * h - e * g)

print(f"O determinante da matriz é: {det}")

#ver uma aula de matriz determinate so pra entender oq foi feito
#ver como funciona o break
