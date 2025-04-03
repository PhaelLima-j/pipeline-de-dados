# 📊 Dashboard de Temperatura IoT
Este projeto consiste em um Dashboard interativo criado com Streamlit, PostgreSQL e Plotly, que analisa dados de temperatura coletados de sensores IoT. O banco de dados contém informações como data da medição, temperatura registrada, ambiente (interno ou externo) e sala associada.

## 🔍 Funcionalidades
📈 Média de temperatura por tipo (In/Out)

🏢 Última medição registrada por sala

📊 Contagem de registros por data e tipo

## 🗄 Estrutura do Banco de Dados
A base de dados contém a tabela temperature_reading, com as seguintes colunas:

Coluna	Tipo	Descrição
id	TEXT	Identificador único da leitura
room_id/id	TEXT	Identificador da sala onde a medição ocorreu
noted_date	TIMESTAMP	Data e hora da leitura
temp	INTEGER	Temperatura registrada (°C)
out/in	TEXT	Indica se a medição foi feita dentro (In) ou fora (Out)

## 🛠 Views Criadas e Seus Propósitos
📌 avg_temp_by_type – Média de temperatura por tipo (In/Out)
sql
Copiar
Editar
CREATE VIEW avg_temp_by_type AS
SELECT 
    "out/in" AS type,
    AVG(temp) AS avg_temp
FROM temperature_reading
GROUP BY "out/in";

🔎 Propósito:
Esta view calcula a temperatura média para medições internas (In) e externas (Out).

## 📊 Insight possível:

Comparar a variação de temperatura dentro e fora dos ambientes monitorados.

Verificar se há uma grande diferença entre os valores internos e externos, indicando possíveis problemas de ventilação ou isolamento térmico.

📌 last_temp_by_room – Última medição por sala
sql
Copiar
Editar
CREATE VIEW last_temp_by_room AS
SELECT 
    "room_id/id" AS room_id,
    MAX(noted_date) AS last_noted_date,
    temp,
    "out/in" AS type
FROM temperature_reading
GROUP BY "room_id/id", temp, "out/in";
🔎 Propósito:
Esta view obtém a última temperatura registrada em cada sala (room_id).

📊 Insight possível:

Monitorar mudanças bruscas de temperatura dentro das salas.

Identificar salas sem medições recentes, podendo indicar problemas nos sensores.

📌 count_logs_by_date – Contagem de registros por data e tipo
sql
Copiar
Editar
CREATE VIEW count_logs_by_date AS
SELECT 
    DATE(noted_date) AS date,
    "out/in" AS type,
    COUNT(*) AS total_logs
FROM temperature_reading
GROUP BY DATE(noted_date), "out/in";
🔎 Propósito:
Conta quantas medições foram feitas por dia, separadas por tipo (In ou Out).

📊 Insights possíveis:

Identificar padrões de coleta de dados (horários com mais medições).

Descobrir períodos de falta de dados, o que pode indicar falhas nos sensores ou no sistema.

## 🖥 Tecnologias Utilizadas
📊 Banco de Dados: PostgreSQL rodando no Docker

📌 Backend: SQLAlchemy (para conexão com o banco)

📈 Visualização de Dados: Plotly

🌐 Interface Web: Streamlit

## 🚀 Como Rodar o Projeto
Clone o repositório

sh
Copiar
Editar
git clone https://github.com/seu-usuario/dashboard-iot-temp.git
cd dashboard-iot-temp
Crie um ambiente virtual e instale as dependências

sh
Copiar
Editar
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate      # Windows
pip install -r requirements.txt
Configure a conexão com o PostgreSQL no arquivo .env

bash
Copiar
Editar
DATABASE_URL=postgresql://usuario:senha@localhost:5432/postgres-iot
Execute o dashboard

sh
Copiar
Editar
streamlit run main.py
## 📌 Conclusão
Este projeto demonstra como coletar, armazenar e visualizar dados IoT utilizando PostgreSQL, Python e Streamlit. Ele pode ser expandido para outros tipos de sensores e aplicações em monitoramento industrial, eficiência energética ou gestão de ambientes inteligentes.

📬 Contribuições e sugestões são bem-vindas! 😃








