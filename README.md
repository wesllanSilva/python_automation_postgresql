# Python_automation_postgresql

<h1 align="center">Execução de Atualizações em Bancos de Dados PostgreSQL com Python</h1>

<p align="center">Este projeto demonstra uma solução Python para executar atualizações em bancos de dados PostgreSQL e gerar logs detalhados das operações. Ele é útil para automatizar tarefas de manutenção de bancos de dados e registrar informações essenciais sobre cada execução.</p>

<hr>

<h2 align="center">Recursos</h2>

<ul>
  <li>Conecte-se facilmente a vários bancos de dados PostgreSQL.</li>
  <li>Execute atualizações em bancos de dados usando arquivos SQL.</li>
  <li>Registre logs detalhados separados por banco de dados e consulta executada.</li>
  <li>Crie um executável independente para uso em máquinas Windows.</li>
</ul>

<hr>

<h2 align="center">Pré-requisitos</h2>

<ul>
  <li>Python 3.x</li>
  <li>Biblioteca <code>psycopg2</code> para conexão ao PostgreSQL.</li>
  <li>PyInstaller para criar o executável (opcional).</li>
</ul>

<hr>

<h2 align="center">Uso</h2>

<ol>
  <li>Clone este repositório:</li>
</ol>

<pre><code>git clone https://github.com/seu-usuario/seu-repositorio.git</code></pre>

<ol start="2">
  <li>Personalize o arquivo de configuração <code>config.json</code> com as informações dos seus bancos de dados e as queries a serem executadas.</li>
  <li>Execute o script Python <code>main.py</code> para iniciar o processo de atualização e registro de logs.</li>
  <li>Opcionalmente, você pode criar um executável usando o PyInstaller para facilitar a distribuição em máquinas Windows:</li>
</ol>

<pre><code>pyinstaller --onefile main.py</code></pre>

<ol start="5">
  <li>Copie o executável gerado para as máquinas Windows onde deseja executá-lo.</li>
</ol>

<hr>

<h2 align="center">Estrutura do Projeto</h2>

<ul>
  <li><strong>scripts</strong>: Coloque seus arquivos SQL de atualização aqui.</li>
  <li><strong>LOGs</strong>: Os arquivos de log serão gerados aqui, com uma pasta separada para cada banco de dados.</li>
</ul>

<hr>

<h2 align="center">Configuração Avançada</h2>

<p>Você pode personalizar as queries de atualização e os bancos de dados no arquivo <code>config.json</code>. Certifique-se de seguir o formato adequado.</p>

<hr>

<h2 align="center">Licença</h2>

<p>Este projeto é distribuído sob a <a href="LICENSE">Licença MIT</a>.</p>

<hr>

<p align="center">Feito com ❤️ por <a href="https://github.com/wesllanSilva">Wesllan Silva</a></p>
