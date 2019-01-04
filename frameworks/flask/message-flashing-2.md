# Message Flashing  

## Categorias
  
Podemos adicionar categorias a uma mensagem passando um segundo parâmetro a função `flash()`. Essas categorias mostram a mensagem com um estilo diferente. A categoria padrão é `message`.  

No template temos que ativar as categorias passando o parâmetro `with_categories=true` na chamada de `get_flashed_messages()`.  

## Exemplo da Documentação  

```py
# Arquivo python.
flash(u'Invalid password provided', 'error')
```  

```html
<!-- html -->
{% with messages = get_flashed_messages(with_categories=true) %}
  {% if messages %}
    <ul class=flashes>
    {% for category, message in messages %}
      <li class="{{ category }}">{{ message }}</li>
    {% endfor %}
    </ul>
  {% endif %}
{% endwith %}
```  

## Filtrando Mensagens  

É possível filtrar as mensagens de acordo com suas categorias. Para isso é necessário indicar as categorias a serem filtradas. Isso pode ser feito no parâmetro `category_filter` da função `get_flashed_messages`.  

```html
{% with errors = get_flashed_messages(category_filter=["error"]) %}
{% if errors %}
<div class="alert-message block-message error">
  <a class="close" href="#">×</a>
  <ul>
    {%- for msg in errors %}
    <li>{{ msg }}</li>
    {% endfor -%}
  </ul>
</div>
{% endif %}
{% endwith %}
```  

## Referências  

[Docs Flask Message-Flashing](flask.pocoo.org/docs/1.0/quickstart/#message-flashing);  

[Docs Flask Message Flashings](http://flask.pocoo.org/docs/1.0/patterns/flashing/#message-flashing-pattern);  
