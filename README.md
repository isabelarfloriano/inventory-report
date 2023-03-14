# Projeto Inventory Reports! :page_facing_up: :bar_chart:

Projeto desenvolvido em Python, princípios da Programação Orientada a Objetos e Padrões de Projetos, consistindo em uma aplicação para geração de relatórios que recebe como entrada arquivos nos formatos JSON, CSV e XML com dados de um estoque e gera, como saída, um relatório acerca destes dados.

<details>
  <summary><strong>Objetivos de prática</strong></summary><br />
    <ul>
    <li>Aplicar conceitos de Orientação a Objetos em Python</li>
    <li>Aplicar padrões de projeto. Padrão de projeto escolhido Strategy.</li>
    <li>Leitura e escrita de arquivos (XML, CSV, JSON)</li>
    </ul>
</details>
<details>
  <summary><strong>Rodando Localmente a Aplicação</strong></summary><br />
  
  <p>Para executar a aplicação e os testes, siga os passos abaixo:</p>
  <ol>
    <li>Clone o projeto.</li>
    <li>Abra o terminal e navegue até a raiz do projeto.</li>
    <li>Crie o ambiente virtual com o comando <code>python3 -m venv .venv</code>.</li>
    <li>Ative o ambiente virtual com o comando <code>source .venv/bin/activate</code>.</li>
    <li>Instale as dependências com o comando <code>python3 -m pip install -r dev-requirements.txt</code>.</li>
    <li>Para gerar os relatórios via linha de comando, instale a dependência da linha de comando com o comando <code>pip install .</code>.</li>
    <li>Utilize o comando <code>inventory_report</code> seguido dos argumentos necessários:
      <ul>
        <li>O argumento 1 deve receber o caminho de um arquivo a ser importado.</li>
        <li>O argumento 2 deve receber o formato do relatório (simples ou completo).</li>
        <li>Alternativamente, você pode utilizar o comando <code>python3 -m inventory_report.main</code> seguido dos mesmos argumentos.</li>
      </ul>
    </li>
    <li>Para executar todos os testes, execute o comando <code>python3 -m pytest</code> na raiz do projeto.</li>
    <li>Para executar os testes individualmente, execute um dos comandos a seguir na raiz do projeto:
      <ul>
        <li><code>python3 -m pytest -k test_cria_produto</code></li>
        <li><code>python3 -m pytest -k test_relatorio_produto</code></li>
        <li><code>python3 -m pytest -k test_decorar_relatorio</code></li>
      </ul>
    </li>
    <li>Para executar a aplicação com Docker, execute os comandos a seguir na raiz do projeto:
      <ul>
        <li><code>docker-compose up -d</code> para subir o container.</li>
        <li><code>docker-compose down</code> para parar o container.</li>
        <li>Alternativamente, você pode rodar os testes utilizando Docker, utilize o comando <code>docker-compose run --rm inventory pytest</code>.</li>
      </ul>
    </li>
  </ol>
</details>
<details>
  <summary><strong>Estrutura do Projeto</strong></summary><br />

  ```
.
├── inventory_report
│   ├── data
│   │   ├── 🔸inventory.csv
│   │   ├── 🔸inventory.json
│   │   └── 🔸inventory.xml
│   ├── importer
│   │   ├── 🔹csv_importer.py
│   │   ├── 🔹importer.py
│   │   ├── 🔹json_importer.py
│   │   └── 🔹xml_importer.py
│   ├── inventory
│   │   ├── 🔹inventory_iterator.py
│   │   ├── 🔹inventory_refactor.py
│   │   └── 🔹inventory.py
│   │   └── 🔸product.py
│   ├── reports
│   │   ├── 🔸colored_report.py
│   │   ├── 🔹complete_report.py
│   │   └── 🔹simple_report.py
│   └── 🔹main.py
└── tests
│   ├── factories
│   │   ├── 🔸__init__.py
│   │   └── 🔸product_factory.py
│   ├── product
│   │   ├── 🔸__init__.py
│   │   └── 🔹test_product.py
│   ├── product_report
│   │   ├── 🔸__init__.py
│   │   └── 🔹test_product_report.py
│   ├── report_decorator
│   │   ├── 🔸__init__.py
│   │   └── 🔹test_report_decorator.py
│   └── 🔸__init__.py
├── 🔹dev-requirements.txt
├── 🔸docker-compose.yml
├── 🔸Dockerfile
├── 🔸pyproject.toml
├── 🔹README.md
├── 🔸requirements.txt
├── 🔸setup.cfg
└── 🔸setup.py
  
    Legenda:
  🔸Arquivos de propriedade intelectual da Trybe
  🔹Arquivos desenvolvidos por mim
  ```
</details>
<details>
  <summary><strong>Detalhes sobre Testes Desenvolvidos</strong></summary><br />
  <p>tests/product/test_product.py</p>
    <ul>
      <li>Implementação dos testes para a classe Product</li>
      <li>Verificao correto preenchimento dos seguintes atributos:</li>
            <ul>
                 <li>id (int)</li>
                 <li>nome_da_empresa (string)</li>
                 <li>nome_do_produto (string)</li>
                 <li>data_de_fabricacao (string)</li>
                 <li>data_de_validade (string)</li>
                 <li>numero_de_serie (string)</li>
                 <li>instrucoes_de_armazenamento (string)</li>
             </ul>
      <li>Garante a criação de um novo produto com todos os atributos corretamente preenchidos.</li>
    </ul>	
  <p>tests/product_report/test_product_report.py</p>
    <ul>
      <li>Implementação dos testes para a a criação do relatório presente na classe Product</li>
      <li>Garante a formulação de uma frase construída com as informações do produto, que será muito útil para etiquetarmos o estoque.</li>
      <li>Exemplo da frase:</li>
            <ul>
                 <li>O produto `farinha` fabricado em `01-05-2021` por `Farinini` com validade até `02-06-2023` precisa ser armazenado `ao abrigo de luz`.</li>
             </ul>
    </ul>
  <p>tests/report_decorator/test_report_decorator.py</p>
    <ul>
      <li>Implementação dos testes para a classe ColoredReport</li>
      <li>Garante o retorno do relatório devidamente colorido:
            <ul>
                 <li>🟩 Verde:</li>
                      <ul>
                          <li>"Data de fabricação mais antiga:"</li>
                          <li>"Data de validade mais próxima:"</li>
                          <li>"Empresa com mais produtos:"</li>
                      </ul>
                 <li>🟦 Azul: As datas</li>
                 <li>🟥 Vermelho: Nome da empresa com mais produtos</li>
             </ul>
       </li>
    </ul>	
</details>

