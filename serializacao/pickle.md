# Pickle
  
Transforma objetos em sequências de strings(bytes). Podem ser tanto objetos built-ins(listas, tuplas, dic, etc) quanto nossos próprios objetos(classes).  

Nem todas as caracteristicas dos objetos, como os métodos, podem ser reconstruídos. Quem for reconstruí-lo deve saber de antemão como trabalhar com o objeto.  

Existe outro módulo chamado `cpickle` que é uma implementação do Pickle em `C`, o que o torna mais performático, mas que o limita em algumas coisas, como ser depurado, e ser extendido.  

Os dados serializados com o Pickle tem formato próprio. Portanto, devem ser usados com o Pickle para serem deserializados. Arquivos gerados pelo Pickle geralmente são gravados com a extensão `.pkl`.  

## Métodos `dump()` e `load()`
  
São métodos usados para trabalhar com `arquivos` serializados.  

O `dump` serializa o objeto em um arquivo, e o `load` deserializa o arquivo em um objeto.  

> Os arquivos `.pkl` tem que ser salvos como binário.  

> E quando formos recriar um objeto de uma classe que nós criamos, devemos recriar a classe(vazia) dentro do arquivo em que o Pickle for chamado. Ele não consegue descobrir as informações automaticamente.  

**Exemplo**
  
```py
import pickle

lista = ['Olá Mundo!', 100, 'ABACAXI']
# O arquivo tem que ser salvo em binário.
# O dump recebe o objeto e o arquivo onde irá gravá-lo.
pickle.dump(lista, open('lista.pkl','wb'))

deserializando = pickle.load(open('lista.pkl','rb'))
print(deserializando)
```

## Métodos `dumps()` e `loads()`
  
São métodos usados para trabalhar com strings(bytes) diretamente.  

O `dumps` serializa o objeto em strings, e o `loads` deserializa a string em objeto.  
**Exemplo**
  
```py

```

## Referências
  
* [Pythonhelp](https://pythonhelp.wordpress.com/2013/07/20/serializacao-de-objetos-em-python/)  
