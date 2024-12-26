# OilCycle API

## Visão Geral
O projeto **OilCycle** propõe o desenvolvimento de um eletrodoméstico inovador para a reciclagem de óleo de cozinha, utilizando tecnologias emergentes como robótica e Internet das Coisas (IoT). Este dispositivo automatiza a produção de sabão a partir de óleo residual, promovendo a sustentabilidade e a economia circular.

Esta API foi desenvolvida utilizando **FastAPI** e serve como interface para o controle remoto do dispositivo OilCycle, oferecendo conectividade com a nuvem para gerenciamento eficiente e seguro.

## Funcionalidades da API
- Controle remoto do dispositivo via comandos HTTP.
- Monitoramento dos sensores do dispositivo.
- Registro de eventos e estados do dispositivo na nuvem.

## Tecnologias Utilizadas
- **FastAPI**: Framework de desenvolvimento para APIs rápidas e modernas.
- **NodeMCU ESP8266**: Para gerenciamento de hardware e conectividade IoT.
- **Python**: Linguagem de programação principal.
- **Uvicorn**: Servidor ASGI para executar a aplicação FastAPI.

## Estrutura do Projeto
```
OilCycle/
├── app/
│   ├── app.py
│   ├── models/
│   │   ├── example_model.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   └── example_controller.py
│   ├── uploads/
│       ├── rqcode_exemplo.png
│   ├── utils/
│       ├── example_util.py
└── requirements.txt
```

## Configuração e Execução
### Pré-requisitos
- **Python 3.8+**
- Gerenciador de pacotes `pip`

### Instalação
1. Clone o repositório:
   ```bash
   git clone https://github.com/adjailsonferreira/oilcycle.git
   cd oilcycle
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

### Executando o Servidor
1. Execute o servidor FastAPI usando o Uvicorn:
   ```bash
   uvicorn app:api --reload

   ```

2. Acesse a aplicação em seu navegador:
   - Interface padrão: [http://127.0.0.1:8000](http://127.0.0.1:8000)
   - Documentação Swagger: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Documentação Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Próximos Passos
- Integrar rotas específicas para controle do dispositivo OilCycle.
- Desenvolver modelos para dados de sensores e estados do dispositivo.
- Adicionar autenticação e segurança para acesso remoto.

## Contribuição
Contribuições são bem-vindas! Por favor, envie um pull request ou crie uma issue no repositório GitHub.

## Licença
Este projeto está licenciado sob a [MIT License](LICENSE).

