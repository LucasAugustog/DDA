from django.shortcuts import render
from django.http import HttpResponse
import requests
from datetime import datetime
import schedule
import time
from django.shortcuts import render



with open("estoque/token.txt", "r") as token:
    token = token.read()

with open("estoque/refresh_token.txt", "r") as refresh_token:
    refresh_token = refresh_token.read() 



headers = {
    'Content-Type': "application/json",
    'Authorization': token
}

refresh_token = {
    "refresh_token": refresh_token
}


urlRefresh_token = ("http://129.151.33.48:8343/api/v1/auth/refresh-token")
responseLogin = requests.request("POST", urlRefresh_token, headers=headers, json=refresh_token)
teste = responseLogin.json()

newToken = teste['access_token']
newToken = "bearer " + newToken
newRefresh_token = teste['refresh_token']

#print(refresh_token)
#print(token)

with open("estoque/token.txt", "w") as arquivo:
    arquivo.write(newToken)
    

with open("estoque/refresh_token.txt", "w") as arquivo:
    arquivo.write(newRefresh_token)

#time.sleep(60) #10800
#7894900010015

description = 7894900010015
description = str(description)



def estoque(request):
    description = 7894900010015
    description = str(description)

    descricaoCompleta = " "
    estq1 = " "
    pedido1 = " "
    estq3 = " "
    pedido3 = " "
    estq4 = " "
    pedido4 = " "
    estq5 = " "
    pedido5 = " "
    estq99 = " "
    pedido99 = " "
    promo3 = " "
    precoVenda1 = " "
    precoVenda3 = " "
    promo4 = " "
    precoVenda4 = " "
    promo5 = " "
    precoVenda5 = " "
    promo99 = " "
    precoVenda99 = " "
    responseErro = None
    ultimaCompraMov1 = " "
    ultimaCompraMov3 = " "
    ultimaCompraMov4 = " "
    ultimaCompraMov5 = " "
    ultimaCompraMov99 = " "
    ultimoCGO1 = " "
    ultimoCGO3 = " "
    ultimoCGO4 = " "
    ultimoCGO5 = " "
    ultimoCGO99 = " "

    response = None
    if request.method == 'POST':
        unit = request.POST.get('unit')
        description = request.POST.get('description')
        # Aqui você pode processar os dados como desejar
        response = f"Último Código digitado: {description}"
    

    headers = {
        'Content-Type': "application/json",
        'Authorization': token
        }
    
    contador = len(description)
    
    if contador >= 15:
        description = description[:15]
      

    if description == None:
        codigoScaneado = str(7894900010015)

    else:
        codigoScaneado = description
        

    


   
    urlCodigoAcesso = ("http://129.151.33.48:8343/SMProdutosAPI/api/v4/produtos/codigos-acesso-prod?CodigoAcesso=" +  codigoScaneado + "&_pageSize=999")
    responseCodigoAcesso = requests.request("GET", urlCodigoAcesso, headers=headers)
    CodigoAcesso = responseCodigoAcesso.json()
    validador = CodigoAcesso
    validador = str(validador)

    
    if validador == "[]":
        codigoScaneado = str(7894900010015)
        urlCodigoAcesso = ("http://129.151.33.48:8343/SMProdutosAPI/api/v4/produtos/codigos-acesso-prod?CodigoAcesso=" +  codigoScaneado + "&_pageSize=999")
        responseCodigoAcesso = requests.request("GET", urlCodigoAcesso, headers=headers)
        CodigoAcesso = responseCodigoAcesso.json()  
        responseErro = f"Este Código {description} Não existe, tente novamente, ou consulte o seu administrador"
        
    
    #print(CodigoAcesso)

    for x in CodigoAcesso:
        codigoProduto = (x['IdProduto'])
        codigoProduto = str(codigoProduto)


    urlProdutoCadastro = ("http://129.151.33.48:8343/SMProdutosAPI/api/v4/produtos/dados-cadastrais?idProduto=" + codigoProduto + "&_pageSize=999")


    responseProdutoCadastro = requests.request("GET", urlProdutoCadastro, headers=headers)
    ProdutoCadastro = responseCodigoAcesso.json()
    

    for i in ProdutoCadastro:
        if(i['IdProdutoBase'] != None):
            produtoBase = i['IdProdutoBase']
            produtoBase = str(produtoBase)
            urlProdutoCadastro = ("http://129.151.33.48:8343/SMProdutosAPI/api/v4/produtos/dados-cadastrais?idProduto=" + produtoBase + "&_pageSize=999")
            responseProdutoCadastro = requests.request("GET", urlProdutoCadastro, headers=headers)
            ProdutoCadastro = responseProdutoCadastro.json()
            
            for i in ProdutoCadastro:
                codigoProduto = i['IdProduto']
                codigoProduto = str(codigoProduto)
               
            

    ulrEstoque = ("http://129.151.33.48:8343/SMProdutosAPI/api/v4/produtos/estoque-produtos?IdProduto=" + codigoProduto + "&_pageSize=999")
    urlEmbalagem = ("http://129.151.33.48:8343/SMProdutosAPI/api/v4/produtos/embalagens-produtos?idProduto=" + codigoProduto + "&_pageSize=999")


    responseEstoque = requests.request("GET", ulrEstoque, headers=headers)
    estoque = responseEstoque.json()
    descProduto = responseProdutoCadastro.json()

    #QtdPendCompras Possivelmente o EstoquePedido seja essa info 

    for x in descProduto:
        print(x['DescricaoCompleta'])
        descricaoCompleta = (x['DescricaoCompleta'])

    for i in estoque:
        if(i['NroEmpresa'] == 1):
            estq1 = i['EstoqueLoja']
            pedido1 = i['QtdPendCompras']
            #DataUltimaEntrada1 = i['DataUltimaEntrada']
            #if(DataUltimaEntrada1 != None):
            #    DataUltimaEntrada1 = DataUltimaEntrada1[:10]
        
        if(i['NroEmpresa'] == 3):
            estq3 = i['EstoqueLoja']
            pedido3 = i['QtdPendCompras']
            #DataUltimaEntrada3 = i['DataUltimaEntrada']
            #if(DataUltimaEntrada3 != None):
            #    DataUltimaEntrada3 = DataUltimaEntrada3[:10]

        if(i['NroEmpresa'] == 4):
            estq4 = i['EstoqueLoja']
            pedido4 = i['QtdPendCompras']
            #DataUltimaEntrada4 = i['DataUltimaEntrada']
            #if(DataUltimaEntrada4 != None):
            #    DataUltimaEntrada4 = DataUltimaEntrada4[:10]

        if(i['NroEmpresa'] == 5):
            estq5 = i['EstoqueLoja']
            pedido5 = i['QtdPendCompras']
            #DataUltimaEntrada5 = i['DataUltimaEntrada']
            #if(DataUltimaEntrada5 != None):
            #    DataUltimaEntrada5 = DataUltimaEntrada5[:10]

        if(i['NroEmpresa'] == 99):
            estq99 = i['EstoqueDeposito']
            pedido99 = i['QtdPendCompras']
            #DataUltimaEntrada99 = i['DataUltimaEntrada']
            #if(DataUltimaEntrada99 != None):
            #    DataUltimaEntrada99 = DataUltimaEntrada99[:10]
           




    #Venda Produto por data
    #http://129.151.33.48:8343/SMVendasApi/api/v1/vendas-por-dia?cNPJ=06316466000187&idProduto=755&nroEmpresa=1&dataVenda=05-05-2024 

    #Venda media geral & Promocional
    #http://129.151.33.48:8343/SMProdutosAPI/api/v4/produtos/venda-media-produtos?idProduto=755


    urlMediaVenda = ("http://129.151.33.48:8343/SMProdutosAPI/api/v4/produtos/venda-media-produtos?idProduto=" + codigoProduto + "&_pageSize=999")
    respondeMediaVenda = requests.request("GET", urlMediaVenda, headers=headers)
    JsonMediaVenda = respondeMediaVenda.json()
    #print(JsonMediaVenda)

    for mv in JsonMediaVenda:
        MediaGeral = mv['MediaGeral']
        NR = mv['NumeroEmpresa']
        MediaGeral = "{:.2f}".format(MediaGeral)
        #print(NR, '|', MediaGeral)






            
    urlPreco = ("http://129.151.33.48:8343/SMProdutosAPI/api/v4/produtos/precos-produtos?idProduto=" + codigoProduto + "&_pageSize=999")
    print(codigoProduto)
    respondePreco = requests.request("GET", urlPreco, headers=headers)
    testePreceo = respondePreco.json()

    for p in testePreceo:
        if(p['NumeroEmpresa'] == 1):
            if p['PrecoPromocao'] != 0:
                precoVenda1 = (p['PrecoPromocao']) 
                promo1 = 'S'
            else: 
                promo1 = 'N'
            precoVenda1 = p['PrecoVenda'] 
        

        if(p['NumeroEmpresa'] == 3):
            if p['PrecoPromocao'] != 0: 
                precoVenda3 = (p['PrecoPromocao'])
                promo3 = 'S'
            else: 
                promo3 = 'N'
            precoVenda3 = p['PrecoVenda']

        if(p['NumeroEmpresa'] == 4):
            if p['PrecoPromocao'] != 0: 
                precoVenda4 = (p['PrecoPromocao'])
                promo4 = 'S'
            else: 
                promo4 = 'N'
            precoVenda4 = p['PrecoVenda']

        if(p['NumeroEmpresa'] == 5):
            if p['PrecoPromocao'] != 0: 
                precoVenda5 = (p['PrecoPromocao'])
                promo5 = 'S'
            else: 
                promo5 = 'N'
            precoVenda5 = p['PrecoVenda']

        if(p['NumeroEmpresa'] == 99):
            if p['PrecoPromocao'] != 0: 
                precoVenda99 = (p['PrecoPromocao'])
                promo99 = 'S'
            else: 
                promo99 = 'N'
                precoVenda99 = p['PrecoVenda']


    urlUltimaEntrada = ("http://129.151.33.48:8343/SMProdutosAPI/api/v4/produtos/ultima-entrada-produtos?idProduto=" + codigoProduto + "&_pageSize=999")
    responseUrlUltimaEntrada = requests.request("GET", urlUltimaEntrada, headers=headers)
    ultimaCompra = responseUrlUltimaEntrada.json()
    #print(ultimaCompra)
    for k in ultimaCompra:
        if(k['NroEmpresa'] == 1):
            ultimaCompraMov1 = k['DataUltimaEntrada']
            ultimaCompraMov1 = ultimaCompraMov1[:10]

            ultimoCGO1 = k['CGO']
            if(ultimoCGO1 == 1): ultimoCGO1 = 'https://i.imgur.com/TcfqxOq.png' #compra
            if(ultimoCGO1 == 8): ultimoCGO1 = 'https://i.imgur.com/TcfqxOq.png' #compra
            if(ultimoCGO1 == 12): ultimoCGO1 = 'https://i.imgur.com/TcfqxOq.png' #compra
            if(ultimoCGO1 == 13): ultimoCGO1 = 'https://i.imgur.com/TcfqxOq.png' #compra
            if(ultimoCGO1 == 21): ultimoCGO1 = 'https://i.imgur.com/TcfqxOq.png' #compra
            if(ultimoCGO1 == 22): ultimoCGO1 = 'https://i.imgur.com/TcfqxOq.png' #compra

            if(ultimoCGO1 == 20): ultimoCGO1 = 'https://i.imgur.com/vQedMFG.png' #transferencia
            if(ultimoCGO1 == 24): ultimoCGO1 = 'https://i.imgur.com/vQedMFG.png' #transferencia
            if(ultimoCGO1 == 30): ultimoCGO1 = 'https://i.imgur.com/vQedMFG.png' #transferencia
            if(ultimoCGO1 == 34): ultimoCGO1 = 'https://i.imgur.com/vQedMFG.png' #transferencia
            if(ultimoCGO1 == 50): ultimoCGO1 = 'https://i.imgur.com/vQedMFG.png' #transferencia
            if(ultimoCGO1 == 51): ultimoCGO1 = 'https://i.imgur.com/vQedMFG.png' #transferencia
            if(ultimoCGO1 == 52): ultimoCGO1 = 'https://i.imgur.com/vQedMFG.png' #transferencia




        if(k['NroEmpresa'] == 3):
            ultimaCompraMov3 = k['DataUltimaEntrada']
            ultimaCompraMov3 = ultimaCompraMov3[:10]

            ultimoCGO3 = k['CGO']
            if(ultimoCGO3 == 1): ultimoCGO3 = 'https://i.imgur.com/TcfqxOq.png' #compra
            if(ultimoCGO3 == 8): ultimoCGO3 = 'https://i.imgur.com/TcfqxOq.png' #compra
            if(ultimoCGO3 == 12): ultimoCGO3 = 'https://i.imgur.com/TcfqxOq.png' #compra
            if(ultimoCGO3 == 13): ultimoCGO3 = 'https://i.imgur.com/TcfqxOq.png' #compra
            if(ultimoCGO3 == 21): ultimoCGO3 = 'https://i.imgur.com/TcfqxOq.png' #compra
            if(ultimoCGO3 == 22): ultimoCGO3 = 'https://i.imgur.com/TcfqxOq.png' #compra

            if(ultimoCGO3 == 20): ultimoCGO3 = 'https://i.imgur.com/vQedMFG.png' #transferencia
            if(ultimoCGO3 == 24): ultimoCGO3 = 'https://i.imgur.com/vQedMFG.png' #transferencia
            if(ultimoCGO3 == 30): ultimoCGO3 = 'https://i.imgur.com/vQedMFG.png' #transferencia
            if(ultimoCGO3 == 34): ultimoCGO3 = 'https://i.imgur.com/vQedMFG.png' #transferencia
            if(ultimoCGO3 == 50): ultimoCGO3 = 'https://i.imgur.com/vQedMFG.png' #transferencia
            if(ultimoCGO3 == 51): ultimoCGO3 = 'https://i.imgur.com/vQedMFG.png' #transferencia
            if(ultimoCGO3 == 52): ultimoCGO3 = 'https://i.imgur.com/vQedMFG.png' #transferencia


        if(k['NroEmpresa'] == 4):
            ultimaCompraMov4 = k['DataUltimaEntrada']
            ultimaCompraMov4 = ultimaCompraMov4[:10]
            
            ultimoCGO4 = k['CGO']
            if(ultimoCGO4 == 1): ultimoCGO4 = 'https://i.imgur.com/TcfqxOq.png' #compra
            if(ultimoCGO4 == 8): ultimoCGO4 = 'https://i.imgur.com/TcfqxOq.png' #compra
            if(ultimoCGO4 == 12): ultimoCGO4 = 'https://i.imgur.com/TcfqxOq.png' #compra
            if(ultimoCGO4 == 13): ultimoCGO4 = 'https://i.imgur.com/TcfqxOq.png' #compra
            if(ultimoCGO4 == 21): ultimoCGO4 = 'https://i.imgur.com/TcfqxOq.png' #compra
            if(ultimoCGO4 == 22): ultimoCGO4 = 'https://i.imgur.com/TcfqxOq.png' #compra

            if(ultimoCGO4 == 20): ultimoCGO4 = 'https://i.imgur.com/vQedMFG.png' #transferencia
            if(ultimoCGO4 == 24): ultimoCGO4 = 'https://i.imgur.com/vQedMFG.png' #transferencia
            if(ultimoCGO4 == 30): ultimoCGO4 = 'https://i.imgur.com/vQedMFG.png' #transferencia
            if(ultimoCGO4 == 34): ultimoCGO4 = 'https://i.imgur.com/vQedMFG.png' #transferencia
            if(ultimoCGO4 == 50): ultimoCGO4 = 'https://i.imgur.com/vQedMFG.png' #transferencia
            if(ultimoCGO4 == 51): ultimoCGO4 = 'https://i.imgur.com/vQedMFG.png' #transferencia
            if(ultimoCGO4 == 52): ultimoCGO4 = 'https://i.imgur.com/vQedMFG.png' #transferencia

        if(k['NroEmpresa'] == 5):
            ultimaCompraMov5 = k['DataUltimaEntrada']
            ultimaCompraMov5 = ultimaCompraMov5[:10]
            
            ultimoCGO5 = k['CGO']
            if(ultimoCGO5 == 1): ultimoCGO5 = 'https://i.imgur.com/TcfqxOq.png' #compra
            if(ultimoCGO5 == 8): ultimoCGO5 = 'https://i.imgur.com/TcfqxOq.png' #compra
            if(ultimoCGO5 == 12): ultimoCGO5 = 'https://i.imgur.com/TcfqxOq.png' #compra
            if(ultimoCGO5 == 13): ultimoCGO5 = 'https://i.imgur.com/TcfqxOq.png' #compra
            if(ultimoCGO5 == 21): ultimoCGO5 = 'https://i.imgur.com/TcfqxOq.png' #compra
            if(ultimoCGO5 == 22): ultimoCGO5 = 'https://i.imgur.com/TcfqxOq.png' #compra

            if(ultimoCGO5 == 20): ultimoCGO5 = 'https://i.imgur.com/vQedMFG.png' #transferencia
            if(ultimoCGO5 == 24): ultimoCGO5 = 'https://i.imgur.com/vQedMFG.png' #transferencia
            if(ultimoCGO5 == 30): ultimoCGO5 = 'https://i.imgur.com/vQedMFG.png' #transferencia
            if(ultimoCGO5 == 34): ultimoCGO5 = 'https://i.imgur.com/vQedMFG.png' #transferencia
            if(ultimoCGO5 == 50): ultimoCGO5 = 'https://i.imgur.com/vQedMFG.png' #transferencia
            if(ultimoCGO5 == 51): ultimoCGO5 = 'https://i.imgur.com/vQedMFG.png' #transferencia
            if(ultimoCGO5 == 52): ultimoCGO5 = 'https://i.imgur.com/vQedMFG.png' #transferencia

        if(k['NroEmpresa'] == 99):
            ultimaCompraMov99 = k['DataUltimaEntrada']
            ultimaCompraMov99 = ultimaCompraMov99[:10]
            
            ultimoCGO99 = k['CGO']
            if(ultimoCGO99 == 1): ultimoCGO99 = 'https://i.imgur.com/TcfqxOq.png' #compra
            if(ultimoCGO99 == 8): ultimoCGO99 = 'https://i.imgur.com/TcfqxOq.png' #compra
            if(ultimoCGO99 == 12): ultimoCGO99 = 'https://i.imgur.com/TcfqxOq.png' #compra
            if(ultimoCGO99 == 13): ultimoCGO99 = 'https://i.imgur.com/TcfqxOq.png' #compra
            if(ultimoCGO99 == 21): ultimoCGO99 = 'https://i.imgur.com/TcfqxOq.png' #compra
            if(ultimoCGO99 == 22): ultimoCGO99 = 'https://i.imgur.com/TcfqxOq.png' #compra

            if(ultimoCGO99 == 20): ultimoCGO99 = 'https://i.imgur.com/vQedMFG.png' #transferencia
            if(ultimoCGO99 == 24): ultimoCGO99 = 'https://i.imgur.com/vQedMFG.png' #transferencia
            if(ultimoCGO99 == 30): ultimoCGO99 = 'https://i.imgur.com/vQedMFG.png' #transferencia
            if(ultimoCGO99 == 34): ultimoCGO99 = 'https://i.imgur.com/vQedMFG.png' #transferencia
            if(ultimoCGO99 == 50): ultimoCGO99 = 'https://i.imgur.com/vQedMFG.png' #transferencia
            if(ultimoCGO99 == 51): ultimoCGO99 = 'https://i.imgur.com/vQedMFG.png' #transferencia
            if(ultimoCGO99 == 52): ultimoCGO99 = 'https://i.imgur.com/vQedMFG.png' #transferencia



    
    return render(request, 'estoque.html', {
        'ultimaCompraMov1': ultimaCompraMov1,
        'ultimaCompraMov3': ultimaCompraMov3,
        'ultimaCompraMov4': ultimaCompraMov4,
        'ultimaCompraMov5': ultimaCompraMov5,
        'ultimaCompraMov99': ultimaCompraMov99,
        'ultimoCGO1': ultimoCGO1,
        'ultimoCGO3': ultimoCGO3,
        'ultimoCGO4': ultimoCGO4,
        'ultimoCGO5': ultimoCGO5,
        'ultimoCGO99': ultimoCGO99,
        'responseErro': responseErro,
        'response': response,
        'descricaoCompleta': descricaoCompleta,
        'estq1': estq1,
        'pedido1': pedido1,
        'estq3': estq3,
        'pedido3': pedido3,
        'estq4': estq4,
        'pedido4': pedido4,
        'estq5': estq5,
        'pedido5': pedido5,
        'estq99': estq99,
        'pedido99': pedido99,
        'promo3': promo3,
        'precoVenda1': precoVenda1,
        'precoVenda3': precoVenda3,
        'promo4': promo4,
        'precoVenda4': precoVenda4,
        'promo5': promo5,
        'precoVenda5': precoVenda5,
        'promo99': promo99,
        'precoVenda99': precoVenda99,
        })