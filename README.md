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
