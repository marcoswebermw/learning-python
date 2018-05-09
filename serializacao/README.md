# Serialização
  
Consiste do processo de gravar `estruturas de dados` em arquivo, ou memória de forma contínua. Sendo que essas estruturas poderão ser reconstruídas de forma indêntica a estrutura original posteriormente. É uma maneira simples mas poderosa de armazenamento.  

É muito usada quando estruturas precisam ser transportadas pela rede, principalmente através de sockets, pelo fato de, geralmente, terem um tamanho menor do que se gravados em arquivo convencional.  

Um problema da serialização é que como os dados são guardados de forma serial, também tem quer ser lidos de forma serial. Então para conseguir obter algum dado do arquivo; o arquivo terá que ser lido por completo.  

## Módulos para serialização em Python
  
- Pickle
- Marshal
- Struct
- Shelve
- JSON
  
## Referências
  
* [Docs Python](https://docs.python.org/3/library/pickle.html)  

* [Pythonhelp](https://pythonhelp.wordpress.com/2013/07/20/serializacao-de-objetos-em-python/)  

* [Wikipedia](https://pt.wikipedia.org/wiki/Serialização)