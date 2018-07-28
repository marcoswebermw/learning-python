# Virtualenvwrapper
  
É um assistente usado em conjunto com o virtualenv. Ele permite que o gerenciamento de ambientes virtuais seja feito de forma mais fácil.  

## Configuração
  
```sh
# Instalando.
pip3 install virtualenvwrapper

# Criando diretório para os ambientes criados.
mkdir ~/.meus_ambientes_virtuais

# Exportamos uma variável de ambiente indicando onde se encontram os ambientes virtuais.
export WORKON_HOME=~/.meus_ambientes_virtuais

# Abra o arquivo '.bashrc' para edição.
vim /home/$USER/.bashrc
```  

Depois adicione algumas linhas ao '.bashrc':  

```sh
# Definindo diretório de trabalho do virtualenvwrapper.
export WORKON_HOME=$HOME/.meus_ambientes_virtuais

# Usando o python3.
VIRTUALENVWRAPPER_PYTHON='/usr/bin/python3'

# Caminho para chamar o virtualenvwrapper.
source /usr/local/bin/virtualenvwrapper.sh
```  

> Reinicie o terminal.  

## Usando o virtualenvwrapper
  
Dentro do terminal digite:  

```sh
# Criar ambiente virtual.
mkvirtualenv meu_ambiente_virtual

# Usar o ambiente virtual.
workon meu_ambiente_virtual

# Desativando ambiente.
deactivate meu_ambiente_virtual

# Excluindo ambiente.
rmvirtualenv meu_ambiente_virtual
```  

## Referências
  
[cadernoscicomp.com.br](https://cadernoscicomp.com.br/ubuntu-virtualenvwrapper-com-python-3/)  