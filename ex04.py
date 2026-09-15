# Atividade 04 - Estrutura condicional (if / elif / else)

idade = int(input('Digite sua idade: '))
reposta = input('Você possui CNH? (S/N): ').strip().upper()
tem_cnh = reposta == 'S'

if idade >= 18 and tem_cnh:
    print('Você pode dirigir!')
elif idade >= 18 and not tem_cnh:
    print('Você não pode dirigir, pois não possui CNH!')
else:
    print('Você não pode dirigir, pois é menor de idade!')

print(f'Idade informada: {idade} anos')
print(f'CNH informada: {tem_cnh}')
print(f'Você pode dirigir? {idade >= 18 and tem_cnh}')