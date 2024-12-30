<title>API E-commerce Meteora</title>
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
                    DATABASES = 
                        &nbsp;'default': {
                        &nbsp;'ENGINE': 'django.db.backends.mysql',
                        &nbsp;'NAME': 'ecommerce_meteora',
                        &nbsp;'USER': 'seu_usuario',
                        &nbsp;'PASSWORD': 'sua_senha',
                        &nbsp;'HOST': 'localhost',
                        &nbsp;'PORT': '3306',
                        &nbsp;}
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
