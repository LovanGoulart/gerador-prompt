-- ============================================
-- SCHEMA DO BANCO DE DADOS - PROMPT GENERATOR PRO
-- SQLite
-- ============================================

-- Tabela principal de briefings
CREATE TABLE IF NOT EXISTS briefings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_sistema VARCHAR(200) NOT NULL,
    empresa VARCHAR(200),
    setor VARCHAR(100),
    data_preenchimento TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    prazo_entrega VARCHAR(50),
    responsavel VARCHAR(200),

    -- Visão geral
    descricao_problema TEXT,
    objetivo_principal TEXT,
    publico_alvo TEXT,
    diferenciais TEXT,

    -- Funcionalidades (JSON)
    modulos TEXT,
    detalhamento_modulos TEXT,

    -- Regras de negócio
    regras_negocio TEXT,
    fluxos TEXT,
    calculos TEXT,

    -- UI/UX
    tema VARCHAR(20),
    estilo_design VARCHAR(50),
    cores TEXT,
    layout VARCHAR(50),
    telas TEXT,
    componentes_ui TEXT,
    responsividade VARCHAR(50),

    -- Dados
    entidades TEXT,
    relacionamentos TEXT,
    tipos_dados TEXT,

    -- Técnico
    framework_python VARCHAR(50),
    banco_dados VARCHAR(50),
    hospedagem_bd VARCHAR(50),
    volume_dados VARCHAR(100),
    retencao_dados VARCHAR(50),
    integracoes TEXT,
    tempo_resposta VARCHAR(50),
    usuarios_simultaneos VARCHAR(50),
    uptime VARCHAR(20),
    backup VARCHAR(20),
    seguranca TEXT,

    -- Não-funcionais
    idiomas TEXT,
    acessibilidade BOOLEAN DEFAULT 0,
    documentacao_usuario BOOLEAN DEFAULT 0,
    tutorial BOOLEAN DEFAULT 0,
    codigo_comentado BOOLEAN DEFAULT 1,
    doc_tecnica BOOLEAN DEFAULT 1,
    testes BOOLEAN DEFAULT 1,
    logs_erro BOOLEAN DEFAULT 1,
    arquitetura_modular BOOLEAN DEFAULT 1,

    -- Entregáveis
    entregaveis TEXT,

    -- Priorização
    mvp TEXT,
    fase2 TEXT,
    fase3 TEXT,

    -- Restrições
    restricoes TEXT,
    suposicoes TEXT,
    observacoes TEXT,

    -- Prompt gerado
    prompt_gerado TEXT
);

-- Índices para performance
CREATE INDEX IF NOT EXISTS idx_briefings_data ON briefings(data_preenchimento DESC);
CREATE INDEX IF NOT EXISTS idx_briefings_nome ON briefings(nome_sistema);
