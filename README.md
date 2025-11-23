🔐 Descrição do Projeto

Este projeto é um Gerador de Senhas Seguras desenvolvido em Python utilizando Tkinter para a interface gráfica.
O programa permite que o usuário personalize a criação de senhas escolhendo:
	•	Comprimento da senha
	•	Uso de letras maiúsculas
	•	Uso de letras minúsculas
	•	Uso de números
	•	Uso de caracteres especiais
	•	E exibe automaticamente a força da senha gerada (muito fraca → muito forte)

Além disso, utiliza o módulo secrets, ideal para geração segura de senhas, evitando padrões previsíveis.

Esse projeto foi desenvolvido para a prova prática de Python — disciplina Laboratório de Programação — e tem como objetivo demonstrar:

✔ Interface gráfica
✔ Lógica de programação
✔ Boas práticas
✔ Organização de código
✔ Segurança na geração de senhas

⸻

🖥 Tecnologias Utilizadas

Tecnologia	Uso
Python 3.10+	Linguagem principal
Tkinter	Interface gráfica
Secrets	Geração de caracteres criptograficamente seguros
String	Listas de caracteres prontos para uso


⸻

🎯 Funcionalidades

✅ 1. Gerar senhas seguras baseado no que o usuário escolher

✅ 2. Avaliar automaticamente a força da senha

✅ 3. Permitir personalização completa
	•	letras maiúsculas
	•	letras minúsculas
	•	números
	•	caracteres especiais
	•	tamanho configurável

✅ 4. Interface gráfica intuitiva

✅ 5. Código 100% explicado (adequado para apresentação acadêmica)

⸻

📦 Como rodar o projeto

⿡ Instalar o Python

Se ainda não tiver, baixar em:
https://www.python.org/downloads/

⸻

⿢ Baixar ou clonar o repositório

Clonar pelo Git:

git clone https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git

Ou baixar o ZIP clicando em Code → Download ZIP.

⸻

⿣ Abrir o projeto no VS Code

Abra a pasta contendo o arquivo:

gerador_senhas.py


⸻

⿤ Rodar o código

No VS Code:

python gerador_senhas.py

Ou clique em Run ▶ no canto superior.

A interface irá abrir na tela automaticamente.

⸻

📘 Como funciona o código

🔸 1. verificar_forca_senha(senha)

Avalia a senha baseada em:
	•	tamanho
	•	letras minúsculas
	•	letras maiúsculas
	•	números
	•	caracteres especiais

E retorna:

Muito fraca, Fraca, Média, Forte ou Muito forte

⸻

🔸 2. gerar_senha(…)

Monta um conjunto de caracteres baseado nas escolhas do usuário e usa:

secrets.choice()

para garantir segurança e aleatoriedade.

⸻

🔸 3. Interface Tkinter

Inclui:
	•	Labels
	•	Entry (campo para digitar comprimento)
	•	Checkbuttons (seleção de políticas de senha)
	•	Botão “Gerar Senha”
	•	Área para mostrar senha
	•	Área para mostrar força

⸻

📂 Estrutura do Projeto

📁 gerador-senhas
│
├── README.md
└── gerador_senhas.py

Simples, limpo e fácil de apresentar.

⸻

🧪 Exemplo da Interface
	•	Campo para escolher o tamanho da senha
	•	Checkboxes para escolher políticas
	•	Botão “Gerar senha”
	•	Senha aparece na tela
	•	Força aparece logo abaixo

⸻
