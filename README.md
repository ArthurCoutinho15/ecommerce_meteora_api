<title>API E-commerce Meteora</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
        }
        h1, h2, h3 {
            color: #2c3e50;
        }
        ul {
            margin: 10px 0;
            padding-left: 20px;
        }
        code {
            background-color: #f4f4f4;
            padding: 2px 4px;
            border-radius: 3px;
            font-size: 1em;
        }
        a {
            color: #3498db;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        .highlight {
            background-color: #f9f9f9;
            border-left: 4px solid #3498db;
            padding: 10px;
            margin: 10px 0;
        }
    </style>
</head>
<body>
    <h1>API E-commerce Meteora 🛍️</h1>
    <p>Esta é uma API desenvolvida com <strong>Django Rest Framework</strong> para gerenciar o catálogo de um e-commerce de roupas, permitindo operações seguras e eficientes.</p>

  <h2>Funcionalidades</h2>
    <ul>
        <li>CRUD completo para produtos e categorias.</li>
        <li>Busca e filtros por nome, categoria e preço.</li>
        <li>Paginação configurada (20 itens por página).</li>
        <li>Autenticação e autorização para usuários.</li>
        <li>Documentação interativa com Swagger.</li>
    </ul>

  <h2>Tecnologias</h2>
    <ul>
        <li><strong>Django Rest Framework</strong></li>
        <li><strong>MySQL</strong> para armazenamento de dados.</li>
        <li><strong>Docker</strong> (opcional) para ambiente isolado.</li>
        <li><strong>Swagger</strong> para documentação.</li>
    </ul>

  <h2>Instalação</h2>
    <ol>
        <li>Clone o repositório:
            <div class="highlight">
                <code>git clone https://github.com/ArthurCoutinho15/ecommerce_meteora_api.git</code>
            </div>
        </li>
        <li>Instale as dependências:
            <div class="highlight">
                <code>pip install -r requirements.txt</code>
            </div>
        </li>
        <li>Configure o banco de dados MySQL no arquivo <code>settings.py</code>:
            <div class="highlight">
                <code>
                    DATABASES = {<br>
                        &nbsp;&nbsp;'default': {<br>
                        &nbsp;&nbsp;&nbsp;&nbsp;'ENGINE': 'django.db.backends.mysql',<br>
                        &nbsp;&nbsp;&nbsp;&nbsp;'NAME': 'ecommerce_meteora',<br>
                        &nbsp;&nbsp;&nbsp;&nbsp;'USER': 'seu_usuario',<br>
                        &nbsp;&nbsp;&nbsp;&nbsp;'PASSWORD': 'sua_senha',<br>
                        &nbsp;&nbsp;&nbsp;&nbsp;'HOST': 'localhost',<br>
                        &nbsp;&nbsp;&nbsp;&nbsp;'PORT': '3306',<br>
                        &nbsp;&nbsp;}<br>
                    }
                </code>
            </div>
        </li>
        <li>Execute as migrações:
            <div class="highlight">
                <code>python manage.py migrate</code>
            </div>
        </li>
        <li>Inicie o servidor:
            <div class="highlight">
                <code>python manage.py runserver</code>
            </div>
        </li>
    </ol>

  <h2>Uso</h2>
    <ul>
        <li>Acesse a API em: <a href="http://127.0.0.1:8000/" target="_blank">http://127.0.0.1:8000/</a></li>
        <li>Explore a documentação em: <a href="http://127.0.0.1:8000/swagger/" target="_blank">http://127.0.0.1:8000/swagger/</a></li>
    </ul>

  <h2>Contribuições</h2>
    <p>Contribuições são bem-vindas! Sinta-se à vontade para abrir um PR ou relatar problemas na aba de Issues.</p>

  <h2>Autor</h2>
    <ul>
        <li><strong>Arthur Coutinho</strong></li>
        <li><a href="https://www.linkedin.com/in/seu-perfil" target="_blank">LinkedIn</a></li>
        <li><a href="https://github.com/ArthurCoutinho15" target="_blank">GitHub</a></li>
    </ul>
</body>
</html>
