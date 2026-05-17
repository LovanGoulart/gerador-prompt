-- ============================================
-- DADOS DE EXEMPLO (SEED)
-- ============================================

-- Exemplo de briefing para demonstração
INSERT INTO briefings (
    nome_sistema, empresa, setor, prazo_entrega, responsavel,
    descricao_problema, objetivo_principal, publico_alvo, diferenciais,
    modulos, detalhamento_modulos, regras_negocio, fluxos, calculos,
    tema, estilo_design, cores, layout, telas, componentes_ui, responsividade,
    entidades, relacionamentos, tipos_dados,
    framework_python, banco_dados, hospedagem_bd, volume_dados,
    tempo_resposta, usuarios_simultaneos, uptime, backup, seguranca,
    idiomas, acessibilidade, documentacao_usuario, tutorial,
    codigo_comentado, doc_tecnica, testes, logs_erro, arquitetura_modular,
    entregaveis, mvp, fase2, fase3, restricoes, suposicoes, observacoes,
    prompt_gerado
) VALUES (
    'Sistema de Gestão de Clínica Médica',
    'Saúde Total Clínica',
    'saude',
    '45 dias',
    'Dra. Maria Silva',
    'A clínica atualmente gerencia pacientes, consultas e prontuários em planilhas Excel, causando erros, consultas duplicadas e dificuldade de acesso às informações médicas.',
    'Automatizar o agendamento de consultas, gestão de pacientes e prontuários eletrônicos para uma clínica médica de médio porte',
    'Médicos, recepcionistas, administradores da clínica e pacientes (acesso limitado)',
    'Integração com WhatsApp para lembretes automáticos de consulta, prontuário eletrônico completo com histórico visual, dashboard de ocupação de salas em tempo real',
    '["Autenticação e Autorização", "Dashboard/Painel Principal", "Cadastro de Usuários", "Agendamento/Calendário", "Notificações", "Relatórios e Analytics"]',
    '[{"nome": "Agendamento", "funcionalidades": ["Agendar consultas por especialidade", "Visualização calendário semanal/mensal", "Bloqueio de horários", "Lista de espera"], "regras": "Máximo 3 consultas por horário por médico"}, {"nome": "Prontuário Eletrônico", "funcionalidades": ["Cadastro de pacientes", "Histórico de consultas", "Prescrição digital", "Anexos de exames"], "regras": "Apenas médicos podem editar prontuários"}]',
    '[{"descricao": "Um médico pode ter no máximo 3 consultas simultâneas agendadas", "prioridade": "Alta"}, {"descricao": "Pacientes devem confirmar consulta 24h antes via WhatsApp", "prioridade": "Média"}, {"descricao": "Prontuários devem ser arquivados após 5 anos de inatividade", "prioridade": "Baixa"}]',
    '[{"nome": "Agendamento de Consulta", "passos": ["Paciente solicita consulta", "Recepcionista verifica disponibilidade", "Sistema verifica se médico está ativo", "Consulta é agendada", "WhatsApp envia confirmação"], "decisoes": "Se médico indisponível, oferecer próximo horário ou lista de espera"}]',
    '[{"nome": "Cálculo de Ocupação", "formula": "(Consultas do dia / Capacidade total do dia) * 100", "onde": "Dashboard principal"}]',
    'Claro',
    'Moderno',
    '{"primaria": "#0EA5E9", "secundaria": "#10B981", "destaque": "#F59E0B"}',
    'Sidebar fixa',
    '[{"nome": "Dashboard", "descricao": "Visão geral com métricas do dia", "usuarios": "Todos"}, {"nome": "Agenda", "descricao": "Calendário de consultas", "usuarios": "Recepcionistas, Médicos"}, {"nome": "Pacientes", "descricao": "Cadastro e prontuários", "usuarios": "Médicos, Recepcionistas"}, {"nome": "Relatórios", "descricao": "Relatórios financeiros e operacionais", "usuarios": "Administradores"}]',
    '["Tabelas com ordenação e filtros", "Formulários com validação em tempo real", "Gráficos e dashboards", "Calendário interativo", "Modal/pop-ups", "Tooltips e ajuda contextual"]',
    'Desktop + Tablet + Mobile',
    '[{"nome": "Paciente", "descricao": "Pessoa atendida pela clínica", "atributos": ["nome", "cpf", "data_nascimento", "telefone", "email", "endereco", "alergias", "tipo_sanguineo"]}, {"nome": "Médico", "descricao": "Profissional de saúde", "atributos": ["nome", "crm", "especialidade", "telefone", "email", "status"]}, {"nome": "Consulta", "descricao": "Atendimento médico agendado", "atributos": ["paciente_id", "medico_id", "data_hora", "status", "motivo", "prontuario_id"]}, {"nome": "Prontuario", "descricao": "Registro médico do paciente", "atributos": ["paciente_id", "data", "sintomas", "diagnostico", "prescricao", "anexos"]}]',
    'Um Paciente pode ter várias Consultas. Um Médico pode ter várias Consultas. Um Prontuário pertence a um Paciente.',
    '["Dados sensíveis", "Dados temporais"]',
    'Flask',
    'SQLite',
    'Local',
    'Aproximadamente 500 pacientes, 2000 consultas/ano',
    '< 2 segundos',
    '20',
    '99.5%',
    'Diário',
    '["Criptografia AES-256", "HTTPS/SSL obrigatório", "LGPD/GDPR compliance", "Auditoria de logs"]',
    '["Português"]',
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    '["Código fonte completo e documentado", "Banco de dados com dados de exemplo", "Documentação de instalação e deploy", "Manual do usuário"]',
    '1. Login e autenticação com perfis
2. Dashboard com métricas do dia
3. CRUD de pacientes
4. Agendamento de consultas com calendário
5. Prontuário eletrônico básico
6. Notificações via WhatsApp',
    '1. Relatórios avançados e exportação
2. Integração com convênios médicos
3. Telemedicina (videochamada)
4. App mobile para médicos',
    '1. Inteligência artificial para diagnóstico auxiliar
2. Integração com laboratórios para resultados online
3. Portal do paciente com histórico completo',
    'Não usar frameworks frontend pesados. Manter stack simples: Python Flask + JS vanilla + HTML + CSS. Orçamento limitado para hospedagem.',
    'O cliente já possui servidor próprio. Os médicos têm acesso à internet. O sistema será usado apenas no Brasil.',
    'Sistema deve ser intuitivo para recepcionistas com pouca familiaridade com tecnologia.',
    'PROMPT DE EXEMPLO - ESTE É UM BRIEFING DE DEMONSTRAÇÃO'
);
