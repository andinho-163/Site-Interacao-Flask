    SiteTeste - Rede de Interação Social Full Stack
O SiteTeste é uma plataforma web dinâmica desenvolvida para facilitar a comunicação e o compartilhamento de conteúdo entre membros de uma comunidade. O projeto destaca-se pela implementação de um ciclo completo de desenvolvimento: desde a lógica de rotas e segurança até o deploy escalável em nuvem com banco de dados relacional.

     Diferenciais Técnicos e Arquitetura
Gestão de Estado e Sessões: Utiliza Flask-Login para gerenciar a persistência de usuários autenticados, permitindo acessos restritos a páginas de edição de perfil e criação de posts.

  Segurança de Dados: Implementação de hashing de senhas com Bcrypt, garantindo que informações sensíveis nunca sejam armazenadas em texto simples no banco de dados.

Engine de Templates: Uso avançado de Jinja2 para renderização dinâmica, com herança de templates (base.html) para manter a consistência visual em todo o portal.

Tratamento de Media: Integração com a biblioteca Pillow para processar uploads de fotos de perfil, garantindo otimização de imagens no servidor.

     Infraestrutura e Deploy (Cloud)
O projeto foi migrado de um ambiente de desenvolvimento local para uma infraestrutura de produção robusta:

Banco de Dados: Migração estratégica para PostgreSQL no Railway, utilizando o driver psycopg2-binary para alta performance em sistemas Linux.

Automação de Schema: O código foi projetado para inicializar automaticamente a estrutura do banco de dados (database.create_all()) ao detectar um novo ambiente, facilitando a escalabilidade.

Servidor WSGI: Configuração profissional via Gunicorn, otimizada com mapeamento de caminhos (--pythonpath .) para suportar a estrutura modular do pacote Python.

    📂 Estrutura de Pastas
/sitetest: O "coração" da aplicação (modelos, rotas, formulários e lógica de negócio).

/templates: Interface do utilizador dividida por funcionalidades (Login, Home, Perfil, Posts).

/static: Assets estáticos e armazenamento de fotos de perfil processadas.

main.py: Script de entrada que configura o contexto da aplicação e inicia o servidor.
