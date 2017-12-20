## Virtualenv

Á partir da versão 3.3 do Python o virtualenv vem junto com a distribuição do python.  
  

----------------------------------------------------------------------------------------------
### Como usar o virtualenv?
----------------------------------------------------------------------------------------------

* Com o pip, o virtualenv pode ser instalado com o seguinte comando:
  
`sudo pip install virtualenv`  
  
* Criando um ambiente:
  
`virtualenv NomeDoAmbiente`  
  
- Ou coloque `-p` e a versão do python desejada.  
  
`virutalenv -p python3.5 NomeDoAmbiente`  
    
> Será criado um subdiretório chamado `NomeDoAmbiente`.  
  
* Ativando um ambiente:
  
`source ./NomeDoAmbiente/bin/activate`  
  
* Saindo de um ambiente: 
  
`deactivate`  
  
  
----------------------------------------------------------------------------------------------
### Instalando pacotes dentro do ambiente virtual
----------------------------------------------------------------------------------------------

* Com o ambiente virtual ativado. Instalando o framework Django:
  
`pip install Django`  
  
  
----------------------------------------------------------------------------------------------
### Gerando lista de dependências do projeto
----------------------------------------------------------------------------------------------
  
* Gerando a lista de pacotes usados no ambiente e exportando-a para um arquivo.  
   
 `pip freeze > requirements.txt`  
  
* Recuperando os pacotes em outro ambiente através do arquivo `requirements.txt`.  
  
`pip install -r requirements.txt`  
  
  

----------------------------------------------------------------------------------------------
### virtualenvwrapper
----------------------------------------------------------------------------------------------
  
Permite manipular ambientes virtuais de forma mais fácil. Executa em cima do virtualenv.  
[virtualenvwrapper](https://bitbucket.org/dhellmann/virtualenvwrapper).


### Referências:
  
[python.org](http://docs.python.org/dev/library/venv.html)  
[Python help](https://pythonhelp.wordpress.com/2012/10/17/virtualenv-ambientes-virtuais-para-desenvolvimento/)  
[virtualenvwrapper](https://bitbucket.org/dhellmann/virtualenvwrapper).  
