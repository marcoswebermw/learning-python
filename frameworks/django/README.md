# Django
  
Django, segundo sua documentação, é um framework web de alto nível escrito em Python, feito para desenvolvimento de apps de forma rápida, segura, escalável e com menos código.
  
É livre e open source.
  
## Projetos e Apps
  
Um projeto é um conjunto de aplicações e configurações de um website. Um app é uma aplicação web que faz alguma coisa.
  
Um projeto pode conter vários apps. E um App pode estar em vários projetos.
  
Um aplicativo Django na verdade é um pacote python em certa convenção de diretórios. Mas o Django, através de um utilitário, já cria essa estrutura para o programador. Este, somente tem que se preocupar apenas com o código.
  
## Algumas considerações

No servidor, nunca coloque código python no diretório root como em `/var/www`. Por questões de segurança coloque o código fora como em `/home/meu_projeto`. E nunca use palavras reservadas do python ou django em nomes em seus projetos.
  
## Referências
  
* [Django Docs](https://www.djangoproject.com)  
