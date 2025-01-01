# GTFS Analyzer

## Descrição
O **GTFS Analyzer** é uma ferramenta interativa desenvolvida em Python para analisar arquivos GTFS (General Transit Feed Specification) e oferecer insights sobre a eficiência de rotas de transporte público. A ferramenta inclui uma interface gráfica intuitiva, onde os usuários podem carregar arquivos GTFS, realizar análises de frequência de rotas e visualizar áreas de cobertura das paradas.

![Inteface](https://www.screenpresso.com/=J5NSRoI2TOFw)
![Resultado](https://www.screenpresso.com/=O4DgXK93MKHV)

## Funcionalidades
- **Carregamento de Arquivos GTFS**: Suporte para arquivos no formato ZIP contendo dados GTFS.
- **Análise de Frequência de Rotas**: Identifica as 10 rotas mais frequentadas com base nas paradas realizadas.
- **Visualização de Cobertura**: Geração de um mapa que mostra as paradas e a área convexa mínima de cobertura.
- **Interface Gráfica**: Simples e intuitiva, criada com `tkinter`.

## Tecnologias Utilizadas
- **Python**
  - `tkinter`: Para interface gráfica.
  - `gtfs_kit`: Para manipulação e análise de dados GTFS.
  - `matplotlib`: Para visualização de mapas.
  - `shapely`: Para análise espacial.
  - `geopandas`: Para manipulação de dados geoespaciais.

## Instalação
1. Certifique-se de ter o Python 3.8 ou superior instalado.
2. Clone este repositório ou faça o download dos arquivos.
3. Instale as dependências necessárias:
   ```bash
   pip install gtfs-kit matplotlib shapely geopandas
   ```

## Como Usar
1. Execute o script principal:
   ```bash
   python gtfs_analyzer.py
   ```
2. Na interface gráfica:
   - Clique em "Carregar GTFS" para selecionar um arquivo GTFS no formato ZIP.
   - Use o botão "Analisar Rotas" para visualizar as 10 rotas mais frequentes na área de texto.
   - Use o botão "Visualizar Cobertura" para gerar um mapa mostrando as paradas e a área convexa de cobertura.

## Exemplo de Saída
### Análise de Rotas
- Lista das 10 rotas mais frequentadas exibida diretamente na interface.

### Visualização de Cobertura
- Um gráfico gerado com as paradas e a área convexa mínima de cobertura.

## Estrutura do Projeto
- `gtfs_analyzer.py`: Script principal com a interface e lógica de análise.
- `README.md`: Documentação do projeto.
- `gtfs_rio-de-janeiro.zip`: modelo usado para teste.

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Contato
Para dúvidas ou sugestões, entre em contato pelo email: [felipe_germano10@hotmail.com](mailto:felipe_germano10@hotmail.com).

