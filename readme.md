#API usando Flask

Demonstração simples sobre a utilização do Flask para constituir uma API básica.

Versão do Python: 3.8

### Configurando

Após clonar este repositório e ter a versão do Python compatível instalada, é necessário ativar o _virtualenv_.

Em seguida, execute o comando abaixo para instalar as bibliotecas necessárias:

```
pip install -r requirements.txt
```

O _pip_ se encarregará de instalar as bibliotecas nas versões especificadas pelo arquivo _requirements.txt_.

### Executando

Você utilizará dois terminais - um para rodar a API com o Flask, e outro para enviar requisições HTTP para testar o recebimento pela API.

Lembre-se: em ambos é necessário ter o `virtualenv` habilitado.

Execute na sequência.

```
Terminal 1:

python app.py
```

Ao rodar, deve aparecer o seguinte:

```
Terminal 1:

python app.py
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

O arquivo `requesting.py` possui duas requisições HTTP, um GET e um POST, para a url `http://127.0.0.1:5000/`.

```
Terminal 2:

python requesting.py
```

Você poderá ver no Terminal 1 as requisições recebidas.

```
Terminal 1:

python app.py
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

GET request
127.0.0.1 - - [18/Dec/2019 16:38:06] "GET / HTTP/1.1" 200 -
POST request
127.0.0.1 - - [18/Dec/2019 16:38:11] "POST / HTTP/1.1" 200 -
```