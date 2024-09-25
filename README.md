# Sistema de Reservas de Trem

Este projeto é um sistema de reservas de trem desenvolvido em Python, utilizando a arquitetura MVC (Modelo, Visão, Controlador) e um banco de dados SQL Server. O objetivo do sistema é gerenciar reservas de passagens de trem, permitindo aos usuários comprar passagens, cancelar reservas, verificar tarifas e exibir informações sobre trens disponíveis.

## Estrutura do Projeto

O projeto é estruturado em vários módulos, cada um com responsabilidades específicas:

### 1. `main.py`
Este é o arquivo principal que inicializa o sistema. Ele gerencia as interações do usuário, exibe um menu de opções e chama as funções necessárias para realizar as operações de reserva e consulta. O `main.py` importa funções de outros módulos para realizar suas tarefas.

### 2. `__init__.py`
Este arquivo marca o diretório como um pacote Python e permite a importação dos módulos `validacoes`, `utilitarios`, `acoes` e `dados`. Ele facilita a organização do código e a importação de funcionalidades.

### 3. `acoes.py`
Este módulo é responsável por gerenciar as operações relacionadas às reservas de trem. As funções neste arquivo incluem:
- **listar trens**: exibe os trens disponíveis.
- **verificar tarifas**: mostra os preços das passagens.
- **exibir reservas**: lista as reservas feitas pelo usuário.
- **reservar um trem**: permite ao usuário reservar uma passagem.
- **cancelar uma reserva**: cancela uma reserva existente.

A comunicação com o banco de dados é realizada através do módulo `pyodbc`, que permite a execução de consultas SQL.

### 4. `utilitarios.py`
O módulo utilitário contém funções auxiliares que ajudam na operação do sistema. Entre elas:
- **sobre()**: exibe informações sobre o sistema.
- **limpar_tela()**: limpa a tela do terminal.
- **exibir_menu()**: mostra o menu de opções disponíveis para o usuário.

### 5. `validacoes.py`
Este módulo é responsável por validar e garantir que o banco de dados e suas tabelas estejam configurados corretamente. As principais funções incluem:
- **verificar_banco_dados()**: verifica se o banco de dados existe e contém as tabelas necessárias.
- **criar_tabelas()**: cria as tabelas do banco de dados se não existirem.
- **validar_conexao()**: verifica se a conexão com o servidor SQL está funcionando corretamente.

### 6. `dados.py`
O módulo `dados` contém funções que gerenciam a inserção de dados no banco de dados. A função principal é:
- **inserir_dados_trem()**: lê um arquivo CSV contendo informações sobre os trens e insere esses dados na tabela `train_info` do banco de dados.

## Como Usar

1. **Instalação**: Certifique-se de ter o Python e o SQL Server instalados em sua máquina.
2. **Configuração do Banco de Dados**: Altere as configurações de conexão no código para refletir seu ambiente local.
3. **Execução**: Execute o arquivo `main.py` para iniciar o sistema. O menu será exibido, e você poderá escolher entre as opções disponíveis.
4. **Dados de Trens**: Insira os dados dos trens no banco de dados utilizando um arquivo CSV. O caminho do arquivo deve ser atualizado no código `dados.py`.

## Contribuição

Sinta-se à vontade para contribuir com melhorias e correções. Se você encontrar um bug ou tiver uma sugestão, por favor, abra uma issue ou envie um pull request.

## Licença

Este projeto está licenciado sob a MIT License. Consulte o arquivo `LICENSE` para mais detalhes.

---

Esperamos que este sistema de reservas de trem facilite a experiência de compra e gerenciamento de passagens de trem. Agradecemos pelo seu interesse!
