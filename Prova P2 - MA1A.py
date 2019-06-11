# Exercício 1: Cálculo das Médias

def media(nota_netflix, nota_imbd):
    media = (nota_imdb + nota_netflix))/2)
    return media 

media()



# Exercício 2: Lista para armazenar os episódios dos datasets analisados

with open('series.csv','series_novas.csv', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        episodes = [lista [0]] #lista com o index que possui o episódio avaliado, que no caso nao foi separado resultando em apenas um 
        print(episodes)



# Exercício 3: Nome da série e total de episódios

with open('series.csv','series_novas.csv', 'r', encoding='utf-8') as file:
    for line in file.readlines(0,1000): #até mil porque não foi contado a quantadade de episódios, num total, avaliados - margem de segurança.
        lista = line.split(',')
        series = lista[0]
        c = 0

        if series == 'Suits'
            eps = c+1
            return print(series,':', eps)
        if series == 'Narcos'
            eps = c+1
            return print(series,':', eps)
        if series == 'Fuller House'
            eps = c+1
            return print(series,':', eps)
        if series == 'Lucifer'
            eps = c+1
            return print(series,':', eps)
        if series == 'Designated Survivor'
            eps = c+1
            return print(series,':', eps)
        if series == 'The Big Bang Theory'
            eps = c+1
            return print(series,':', eps)
        if series == 'Friends'
            eps = c+1
            return print(series,':', eps)
        if series == 'Breaking Bad'
            eps = c+1
            return print(series,':', eps)
        if series == 'Black Mirror'
            eps = c+1
            return print(series,':', eps)



# Exercício 4: Série e nota média
with open('series.csv','series_novas.csv', 'r', encoding='utf-8') as file:

    for line in file.readlines():
        lista = line.split(',')
        imdb = lista[5]
        netflix = lista[6]
        media = float((imdb+netflix)/2)


catalogo = {
    Black Mirror: media
    Breaking Bad: media
    Friends: media
    The Big Bang Theory: media
    Designated Survivor: media
    Lucifer: media
    Fuller House: media
    Narcos: media
    Suits: media

}



# Exercício 5: Novo catálogo sem Narcos e The Big Bang Theory

with open('series.csv','series_novas.csv', 'r', encoding='utf-8') as file:

    for line in file.readlines():
        lista = line.split(',')
        serie = lista[0]

        if serie == 'Narcos' or 'The Big Bang Theory'
            lista.pop[0, 1, 2, 3, 4, 5, 6]
            return lista 




    



























