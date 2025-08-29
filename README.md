# 🛒 Axio - Gestão de Pedidos

[![Python Version](https://img.shields.io/badge/python-3.12-blue.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-5.2-green.svg)](https://djangoproject.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/status-em%20desenvolvimento-orange.svg)]()

Sistema ERP completo para gestão de compras empresariais, desenvolvido para otimizar e automatizar processos de aquisição, desde solicitações até aprovações finais.

## 📋 Índice

- [Visão Geral](#-visão-geral)
- [Funcionalidades](#-funcionalidades)
- [Tecnologias](#-tecnologias)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Instalação](#-instalação)
- [Uso](#-uso)
- [Roadmap](#-roadmap)
- [Contribuição](#-contribuição)
- [Licença](#-licença)
- [Contato](#-contato)

## 🎯 Visão Geral

O **Axio - Gestão de Pedidos** é uma solução robusta desenvolvida para empresas que buscam modernizar e otimizar seus processos de compra. O sistema oferece controle completo sobre o ciclo de compras, desde a solicitação inicial até a aprovação final, incluindo gestão de fornecedores e análise de custos.

### Principais Benefícios

- ✅ **Automação Completa**: Reduza processos manuais e elimine erros
- 📊 **Controle Total**: Visibilidade completa sobre todas as etapas
- 🚀 **Eficiência Operacional**: Acelere aprovações e tomadas de decisão
- 💰 **Gestão de Custos**: Controle orçamentário por centro de custo
- 🔒 **Segurança**: Sistema de aprovações hierárquicas

## 🚀 Funcionalidades

### ✅ **Implementadas**

- **Solicitações de Compra**
  - Cadastro com validação automática
  - Listagem com filtros avançados
  - Status em tempo real
- **Pedidos de Compra**

  - Conversão automática de solicitações
  - Geração de documentos PDF
  - Controle de status e prazos

- **Interface Responsiva**
  - Design moderno com Bootstrap 4
  - Compatibilidade mobile
  - UX otimizada

### 🔄 **Em Desenvolvimento**

- **Sistema de Aprovações Online**
  - Workflow configurável
  - Notificações automáticas
  - Histórico de aprovações

### 📅 **Planejadas**

- **Gestão de Fornecedores**

  - Cadastro completo
  - Avaliação de performance
  - Histórico de transações

- **Centros de Custo**

  - Controle orçamentário
  - Relatórios financeiros
  - Análise de gastos

- **Dashboard Analytics**
  - Métricas em tempo real
  - Gráficos interativos
  - Relatórios personalizados

## 🛠 Tecnologias

### **Backend**

- **Python 3.12** - Linguagem principal
- **Django 5.2** - Framework web
- **SQLite** - Banco de dados (desenvolvimento)
- **Django REST Framework** - APIs (futuro)

### **Frontend**

- **Bootstrap 4** - Framework CSS
- **FontAwesome** - Biblioteca de ícones
- **JavaScript ES6** - Interatividade
- **Chart.js** - Gráficos (planejado)

### **Ferramentas de Desenvolvimento**

- **Git** - Controle de versão
- **pip** - Gerenciador de pacotes
- **virtualenv** - Ambiente virtual

## 📁 Estrutura do Projeto

```
ERP_Compras/
├── 📦 erp_compras/          # Configurações principais do Django
│   ├── settings.py          # Configurações do projeto
│   ├── urls.py             # URLs principais
│   └── wsgi.py             # Configuração WSGI
├── 📋 solicitacoes/         # App de solicitações de compra
│   ├── models.py           # Modelos de dados
│   ├── views.py            # Lógica de negócio
│   ├── forms.py            # Formulários
│   └── templates/          # Templates HTML
├── 🛍️ pedidos/             # App de pedidos de compra
│   ├── models.py           # Modelos de pedidos
│   ├── views.py            # Views de pedidos
│   └── templates/          # Templates de pedidos
├── 👥 cadastro/            # App de cadastros (futuro)
├── 📊 static/              # Arquivos estáticos (CSS, JS, imagens)
├── 📋 templates/           # Templates base
├── 📄 requirements.txt     # Dependências do projeto
└── 🔧 manage.py           # Utilitário Django
```

## 🚀 Instalação

### **Pré-requisitos**

- Python 3.12 ou superior
- pip (gerenciador de pacotes Python)
- Git

### **Passo a Passo**

1. **Clone o repositório**

   ```bash
   git clone https://github.com/VanthuirMaia/ERP_Compras.git
   cd ERP_Compras
   ```

2. **Crie o ambiente virtual**

   ```bash
   # Windows
   python -m venv .venv
   .venv\Scripts\activate

   # Linux/macOS
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Instale as dependências**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure o banco de dados**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Crie um superusuário** (opcional)

   ```bash
   python manage.py createsuperuser
   ```

6. **Execute o servidor**

   ```bash
   python manage.py runserver
   ```

7. **Acesse a aplicação**
   ```
   http://127.0.0.1:8000/
   ```

## 💡 Uso

### **Dashboard Principal**

Acesse a tela principal para visualizar:

- Resumo de solicitações pendentes
- Status dos pedidos em andamento
- Métricas de performance

### **Solicitações de Compra**

1. Navegue até "Solicitações"
2. Clique em "Nova Solicitação"
3. Preencha os dados obrigatórios
4. Salve e acompanhe o status

### **Pedidos de Compra**

1. Acesse "Pedidos de Compra"
2. Converta solicitações aprovadas
3. Gere documentos em PDF
4. Acompanhe entregas

## 🗺️ Próximos Passos

### **Funcionalidades Prioritárias**

- [ ] Sistema de aprovações online para pedidos
- [ ] Gestão completa de fornecedores
- [ ] Controle de centros de custo
- [ ] Notificações por email

### **Melhorias Futuras**

- [ ] Dashboard com métricas e relatórios
- [ ] API REST para integrações
- [ ] Sistema de usuários e permissões
- [ ] Relatórios em PDF/Excel

## 🤝 Contribuição

Contribuições são sempre bem-vindas! Siga estas etapas:

1. **Fork** o projeto
2. **Crie** uma branch para sua feature
   ```bash
   git checkout -b feature/minha-nova-feature
   ```
3. **Commit** suas alterações
   ```bash
   git commit -m "Adiciona nova feature incrível"
   ```
4. **Push** para a branch
   ```bash
   git push origin feature/minha-nova-feature
   ```
5. **Abra** um Pull Request

### **Diretrizes de Contribuição**

- Siga o padrão de código PEP 8
- Inclua testes para novas funcionalidades
- Documente alterações no README
- Use mensagens de commit descritivas

## 📝 Licença

Este projeto está licenciado sob a **MIT License** - veja o arquivo [LICENSE](LICENSE) para detalhes.

```
MIT License

Copyright (c) 2024 Vanthuir Maia

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software")...
```

## 📞 Contato

**Gestto – Softwares de Gestão**  
🚀 Transformando processos em resultados

**_Vanthuir Maia_**

- 📱 **WhatsApp:** [+55 87 99607 5897](https://wa.me/5587996075897)
- 📧 **Email:** [vanmaiasf@gmail.com](mailto:vanmaiasf@gmail.com)
- 💼 **LinkedIn:** [linkedin.com/in/vanthuirmaia](https://linkedin.com/in/vanthuirmaia)
- 🐙 **GitHub:** [github.com/vanthuirmaia](https://github.com/vanthuirmaia)

---

<div align="center">

**⭐ Dê uma estrela se este projeto foi útil para você!**

[![GitHub stars](https://img.shields.io/github/stars/seu-usuario/ERP_Compras.svg?style=social&label=Star)](https://github.com/seu-usuario/ERP_Compras)
[![GitHub forks](https://img.shields.io/github/forks/seu-usuario/ERP_Compras.svg?style=social&label=Fork)](https://github.com/seu-usuario/ERP_Compras/fork)

</div>
