# Response  

O retorno de uma função view é automaticamente transformado em um objeto do tipo response.  

Um objeto response é retornado diretamente para view. Strings serão convertidas, sendo o corpo da resposta a string, o status 200 OK, e mimetype='text/html'.  

Se os valores obtidos pela função forem tuplas, serão retornados tuplas com no mínimo um item e informações adicionais. Estes itens podem ser: (response, status, headers). O status sobrescreverá o valor do status code, e o cabeçalho pode ser uma lista ou dicionário.  

Se o que vier, não for um objeto response, uma string ou tupla. Será assumido que é um valor vindo de uma aplicação WSGI válida e o converterá em um objeto response.  

## make_response()
  
Funções de views no Flask geralmente retornam uma string para as views, que são consequentemente transformadas em um objeto do tipo `response` implicitamente antes de serem enviadas.  

Para retornar um objeto response explicitamente para a view e fazer alterações nele, use a função `make_response()`.  

## Referências  

[Docs Flask Quick Start](flask.pocoo.org/docs/1.0/quickstart/#about-responses);  
