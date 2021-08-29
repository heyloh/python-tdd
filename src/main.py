from leilao.dominio import Usuario, Lance, Leilao, Avaliador

loh = Usuario('Loh')
tauri = Usuario('Tauri')

lance_da_tauri = Lance(tauri, 100.0)
lance_da_loh = Lance(loh, 150.0)

leilao = Leilao('Celular')

leilao.lances.append(lance_da_loh)
leilao.lances.append(lance_da_tauri)

for lance in leilao.lances:
    print(f'O usuario {lance.usuario.nome} deu um lance de R${lance.valor}.')

avaliador = Avaliador()
avaliador.avalia(leilao)

print(f'O menor lance foi de R${avaliador.menor_lance:.2f} e o maior lance foi de R${avaliador.maior_lance:.2f}')
