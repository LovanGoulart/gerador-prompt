import os
import sys

# Adiciona o diretório raiz ao path para imports
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, base_dir)

from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

# Configuração da aplicação
app = Flask(__name__, 
            template_folder=os.path.join(base_dir, 'frontend', 'templates'),
            static_folder=os.path.join(base_dir, 'frontend', 'static'))

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-2026')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL', 
    'sqlite:///' + os.path.join(base_dir, 'database', 'prompt_generator.db')
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializações
db = SQLAlchemy(app)

# =============================================================================
# MODELOS
# =============================================================================

class Briefing(db.Model):
    __tablename__ = 'briefings'

    id = db.Column(db.Integer, primary_key=True)
    nome_sistema = db.Column(db.String(200), nullable=False)
    empresa = db.Column(db.String(200))
    setor = db.Column(db.String(100))
    data_preenchimento = db.Column(db.DateTime, default=datetime.utcnow)
    prazo_entrega = db.Column(db.String(50))
    responsavel = db.Column(db.String(200))

    # Visão geral
    descricao_problema = db.Column(db.Text)
    objetivo_principal = db.Column(db.Text)
    publico_alvo = db.Column(db.Text)
    diferenciais = db.Column(db.Text)

    # Funcionalidades (JSON)
    modulos = db.Column(db.Text)
    detalhamento_modulos = db.Column(db.Text)

    # Regras de negócio
    regras_negocio = db.Column(db.Text)
    fluxos = db.Column(db.Text)
    calculos = db.Column(db.Text)

    # UI/UX
    tema = db.Column(db.String(20))
    estilo_design = db.Column(db.String(50))
    cores = db.Column(db.Text)
    layout = db.Column(db.String(50))
    telas = db.Column(db.Text)
    componentes_ui = db.Column(db.Text)
    responsividade = db.Column(db.String(50))

    # Dados
    entidades = db.Column(db.Text)
    relacionamentos = db.Column(db.Text)
    tipos_dados = db.Column(db.Text)

    # Técnico
    framework_python = db.Column(db.String(50))
    banco_dados = db.Column(db.String(50))
    hospedagem_bd = db.Column(db.String(50))
    volume_dados = db.Column(db.String(100))
    retencao_dados = db.Column(db.String(50))
    integracoes = db.Column(db.Text)
    tempo_resposta = db.Column(db.String(50))
    usuarios_simultaneos = db.Column(db.String(50))
    uptime = db.Column(db.String(20))
    backup = db.Column(db.String(20))
    seguranca = db.Column(db.Text)

    # Não-funcionais
    idiomas = db.Column(db.Text)
    acessibilidade = db.Column(db.Boolean, default=False)
    documentacao_usuario = db.Column(db.Boolean, default=False)
    tutorial = db.Column(db.Boolean, default=False)
    codigo_comentado = db.Column(db.Boolean, default=True)
    doc_tecnica = db.Column(db.Boolean, default=True)
    testes = db.Column(db.Boolean, default=True)
    logs_erro = db.Column(db.Boolean, default=True)
    arquitetura_modular = db.Column(db.Boolean, default=True)

    # Entregáveis
    entregaveis = db.Column(db.Text)

    # Priorização
    mvp = db.Column(db.Text)
    fase2 = db.Column(db.Text)
    fase3 = db.Column(db.Text)

    # Restrições
    restricoes = db.Column(db.Text)
    suposicoes = db.Column(db.Text)
    observacoes = db.Column(db.Text)

    # Prompt gerado
    prompt_gerado = db.Column(db.Text)

    def to_dict(self):
        return {
            'id': self.id,
            'nome_sistema': self.nome_sistema,
            'empresa': self.empresa,
            'setor': self.setor,
            'data_preenchimento': self.data_preenchimento.isoformat() if self.data_preenchimento else None,
            'prompt_preview': self.prompt_gerado[:200] + '...' if self.prompt_gerado and len(self.prompt_gerado) > 200 else self.prompt_gerado
        }

# =============================================================================
# SERVIÇO DE GERAÇÃO DE PROMPT
# =============================================================================

class PromptGenerator:
    @staticmethod
    def gerar_prompt(briefing_data):
        """Gera o prompt completo baseado nos dados do briefing."""

        d = briefing_data

        prompt = f"""Você é um desenvolvedor sênior full-stack especializado em Python, JavaScript, HTML5 e CSS3.
Sua tarefa é criar um sistema web completo, funcional e pronto para produção baseado nas especificações abaixo.

═══════════════════════════════════════════════════════════════════════════════
CONTEXTO DO PROJETO
═══════════════════════════════════════════════════════════════════════════════
Nome do Sistema: {d.get('nome_sistema', 'Não informado')}
Cliente/Empresa: {d.get('empresa', 'Não informado')}
Segmento/Setor: {d.get('setor', 'Não informado')}
Objetivo Principal: {d.get('objetivo_principal', 'Não informado')}
Público-Alvo: {d.get('publico_alvo', 'Não informado')}
Diferenciais Competitivos: {d.get('diferenciais', 'Não informado')}

═══════════════════════════════════════════════════════════════════════════════
STACK TECNOLÓGICO OBRIGATÓRIO
═══════════════════════════════════════════════════════════════════════════════
- Backend: Python ({d.get('framework_python', 'Flask')})
- Frontend: JavaScript vanilla (sem frameworks como React/Vue/Angular)
- Markup: HTML5 semântico e acessível
- Estilização: CSS3 moderno (Flexbox, CSS Grid, variáveis CSS, animações suaves)
- Banco de Dados: {d.get('banco_dados', 'SQLite')}
- ORM: SQLAlchemy (se aplicável)
- Outras tecnologias: {d.get('outras_tecnologias', 'Nenhuma especificada')}

═══════════════════════════════════════════════════════════════════════════════
MÓDULOS E FUNCIONALIDADES
═══════════════════════════════════════════════════════════════════════════════
"""

        # Adiciona módulos
        modulos = d.get('modulos', [])
        if modulos:
            prompt += "Módulos Principais:\n"
            for i, mod in enumerate(modulos, 1):
                prompt += f"  {i}. {mod}\n"
            prompt += "\n"

        detalhamento = d.get('detalhamento_modulos', [])
        if detalhamento:
            prompt += "Detalhamento por Módulo:\n"
            for mod in detalhamento:
                prompt += f"\n--- Módulo: {mod.get('nome', 'Sem nome')} ---\n"
                funcs = mod.get('funcionalidades', [])
                for j, func in enumerate(funcs, 1):
                    prompt += f"  {j}. {func}\n"
                regras = mod.get('regras', '')
                if regras:
                    prompt += f"  Regras especiais: {regras}\n"

        prompt += """
═══════════════════════════════════════════════════════════════════════════════
REGRAS DE NEGÓCIO E LÓGICA
═══════════════════════════════════════════════════════════════════════════════
"""

        regras = d.get('regras_negocio', [])
        if regras:
            prompt += "Regras de Negócio:\n"
            for i, regra in enumerate(regras, 1):
                prompt += f"  {i}. [{regra.get('prioridade', 'Média')}] {regra.get('descricao', '')}\n"
            prompt += "\n"

        fluxos = d.get('fluxos', [])
        if fluxos:
            prompt += "Fluxos de Trabalho:\n"
            for fluxo in fluxos:
                prompt += f"\n--- Fluxo: {fluxo.get('nome', 'Sem nome')} ---\n"
                passos = fluxo.get('passos', [])
                for j, passo in enumerate(passos, 1):
                    prompt += f"  Passo {j}: {passo}\n"
                if fluxo.get('decisoes'):
                    prompt += f"  Decisões/Condições: {fluxo['decisoes']}\n"

        calculos = d.get('calculos', [])
        if calculos:
            prompt += "\nCálculos e Fórmulas:\n"
            for calc in calculos:
                prompt += f"  - {calc.get('nome', '')}: {calc.get('formula', '')} (usado em: {calc.get('onde', '')})\n"

        prompt += """
═══════════════════════════════════════════════════════════════════════════════
INTERFACE DO USUÁRIO (UI/UX)
═══════════════════════════════════════════════════════════════════════════════
"""

        cores = d.get('cores', {})
        prompt += f"""Estilo Visual:
- Tema: {d.get('tema', 'Claro')}
- Design: {d.get('estilo_design', 'Moderno')}
- Cores: Primária {cores.get('primaria', '#3B82F6')}, Secundária {cores.get('secundaria', '#10B981')}, Destaque {cores.get('destaque', '#F59E0B')}
- Layout: {d.get('layout', 'Sidebar fixa')}
- Responsividade: {d.get('responsividade', 'Desktop + Tablet + Mobile')}

"""

        telas = d.get('telas', [])
        if telas:
            prompt += "Telas Principais:\n"
            for i, tela in enumerate(telas, 1):
                prompt += f"  {i}. {tela.get('nome', '')} - {tela.get('descricao', '')} (acesso: {tela.get('usuarios', '')})\n"
            prompt += "\n"

        componentes = d.get('componentes_ui', [])
        if componentes:
            prompt += "Componentes de UI Necessários:\n"
            for comp in componentes:
                prompt += f"  - {comp}\n"
            prompt += "\n"

        prompt += """Requisitos de UI:
- Interface limpa, intuitiva e profissional
- Feedback visual para todas as ações do usuário
- Estados de loading, erro e sucesso claros
- Navegação consistente em todas as telas
- Formulários com validação em tempo real
- Mensagens de erro amigáveis e específicas

"""

        prompt += """═══════════════════════════════════════════════════════════════════════════════
ESTRUTURA DE DADOS
═══════════════════════════════════════════════════════════════════════════════
"""

        entidades = d.get('entidades', [])
        if entidades:
            prompt += "Entidades Principais:\n"
            for ent in entidades:
                prompt += f"  - {ent.get('nome', '')}: {ent.get('descricao', '')}\n"
                atributos = ent.get('atributos', [])
                if atributos:
                    prompt += f"    Atributos: {', '.join(atributos)}\n"
            prompt += "\n"

        if d.get('relacionamentos'):
            prompt += f"Relacionamentos:\n  {d['relacionamentos']}\n\n"

        tipos_dados = d.get('tipos_dados', [])
        if tipos_dados:
            prompt += f"Tipos de Dados Especiais: {', '.join(tipos_dados)}\n\n"

        prompt += f"""═══════════════════════════════════════════════════════════════════════════════
REQUISITOS TÉCNICOS ESPECÍFICOS
═══════════════════════════════════════════════════════════════════════════════
Banco de Dados: {d.get('banco_dados', 'SQLite')} ({d.get('hospedagem_bd', 'Local')})
Volume Estimado: {d.get('volume_dados', 'Não informado')}
Retenção de Dados: {d.get('retencao_dados', 'Não informado')}

"""

        integracoes = d.get('integracoes', [])
        if integracoes:
            prompt += "Integrações Externas:\n"
            for i, integ in enumerate(integracoes, 1):
                prompt += f"  {i}. {integ.get('servico', '')} - {integ.get('proposito', '')} (auth: {integ.get('auth', 'Não')})\n"
            prompt += "\n"

        prompt += f"""Performance:
- Tempo de resposta: {d.get('tempo_resposta', '< 2 segundos')}
- Usuários simultâneos: {d.get('usuarios_simultaneos', '100')}
- Disponibilidade: {d.get('uptime', '99.9%')}
- Backup: {d.get('backup', 'Diário')}

"""

        seguranca = d.get('seguranca', [])
        if seguranca:
            prompt += "Segurança:\n"
            for item in seguranca:
                prompt += f"  - {item}\n"
            prompt += "\n"

        prompt += """═══════════════════════════════════════════════════════════════════════════════
REQUISITOS NÃO-FUNCIONAIS
═══════════════════════════════════════════════════════════════════════════════
"""

        idiomas = d.get('idiomas', ['Português'])
        prompt += f"Idiomas: {', '.join(idiomas)}\n"

        if d.get('acessibilidade'):
            prompt += "- Acessibilidade WCAG 2.1 AA\n"
        if d.get('documentacao_usuario'):
            prompt += "- Documentação de uso para usuários finais\n"
        if d.get('tutorial'):
            prompt += "- Tutorial interativo de onboarding\n"
        if d.get('codigo_comentado'):
            prompt += "- Código comentado em português\n"
        if d.get('doc_tecnica'):
            prompt += "- Documentação técnica da API\n"
        if d.get('testes'):
            prompt += "- Testes automatizados para funções críticas\n"
        if d.get('logs_erro'):
            prompt += "- Logs de erro detalhados\n"
        if d.get('arquitetura_modular'):
            prompt += "- Arquitetura modular para fácil manutenção\n"

        prompt += """
═══════════════════════════════════════════════════════════════════════════════
ENTREGÁVEIS
═══════════════════════════════════════════════════════════════════════════════
"""

        entregaveis = d.get('entregaveis', [])
        if entregaveis:
            for item in entregaveis:
                prompt += f"- {item}\n"
        else:
            prompt += """- Código fonte completo e documentado
- Banco de dados com dados de exemplo (seed)
- Documentação de instalação e deploy
- Documentação da API
- Manual do usuário
"""

        prompt += f"""
═══════════════════════════════════════════════════════════════════════════════
PRIORIZAÇÃO (MVP - Mínimo Produto Viável)
═══════════════════════════════════════════════════════════════════════════════
{d.get('mvp', 'Não informado')}

Fase 2 (Após MVP):
{d.get('fase2', 'Não informado')}

Fase 3 (Futuro):
{d.get('fase3', 'Não informado')}

═══════════════════════════════════════════════════════════════════════════════
RESTRIÇÕES E SUPOSIÇÕES
═══════════════════════════════════════════════════════════════════════════════
Restrições:
{d.get('restricoes', 'Nenhuma especificada')}

Suposições:
{d.get('suposicoes', 'Nenhuma especificada')}

Observações Finais:
{d.get('observacoes', 'Nenhuma')}

═══════════════════════════════════════════════════════════════════════════════
REGRAS DE IMPLEMENTAÇÃO (OBRIGATÓRIAS)
═══════════════════════════════════════════════════════════════════════════════
Anti-overengineering constraints:
- Solução mínima viável apenas (MVP first)
- Sem novos arquivos além do estritamente necessário
- Sem novas dependências além do padrão + Flask + SQLAlchemy
- Evite grandes refatorações ou redesenhos desnecessários
- Mantenha o código simples, legível e bem comentado

Requisitos de Qualidade:
- Validação de inputs em TODOS os formulários (cliente e servidor)
- Tratamento de erros com mensagens amigáveis e específicas
- Proteção contra SQL Injection e XSS
- Autenticação segura (hash de senhas com bcrypt)
- Sessões seguras com JWT ou Flask-Login
- Logs de operações importantes (quem fez o quê e quando)
- Código organizado em camadas (MVC ou similar)

═══════════════════════════════════════════════════════════════════════════════
ESTRUTURA DE PASTAS ESPERADA
═══════════════════════════════════════════════════════════════════════════════
/project-root
├── /backend
│   ├── app.py                 # Aplicação principal Flask
│   ├── /models
│   │   └── [modelos.py]       # Modelos SQLAlchemy
│   ├── /routes
│   │   └── [rotas.py]         # Blueprints e endpoints
│   ├── /services
│   │   └── [servicos.py]      # Lógica de negócio
│   └── /utils
│       └── [utilitarios.py]   # Funções auxiliares
├── /frontend
│   ├── /static
│   │   ├── /css
│   │   │   └── [estilos.css]  # CSS completo
│   │   ├── /js
│   │   │   └── [scripts.js]   # JavaScript completo
│   │   └── /images
│   └── /templates
│       └── [templates.html]   # Templates Jinja2
├── /database
│   ├── schema.sql             # Script de criação do BD
│   └── seed.sql               # Dados de exemplo
├── requirements.txt
├── .env.example
├── README.md                  # Instruções completas
└── config.py                  # Configurações da aplicação

═══════════════════════════════════════════════════════════════════════════════
INSTRUÇÃO FINAL
═══════════════════════════════════════════════════════════════════════════════
Crie um sistema web COMPLETO, FUNCIONAL e PRONTO PARA USO.

REGRAS ABSOLUTAS:
1. Gere TODO o código necessário - NÃO omita NENHUM arquivo
2. Cada arquivo deve ser COMPLETO e FUNCIONAL - sem placeholders ou "# TODO"
3. Use dados de exemplo (seed) para demonstrar o funcionamento real
4. O sistema deve rodar com um simples "flask run" após instalar dependências
5. Inclua instruções claras de instalação no README.md
6. O código deve seguir PEP 8 para Python e boas práticas web para JS/CSS
7. Interface responsiva: deve funcionar bem em desktop, tablet e mobile
8. Todas as funcionalidades do MVP devem estar 100% implementadas
9. Não use frameworks frontend (React, Vue, Angular) - apenas JS vanilla
10. Use CSS moderno com variáveis, flexbox/grid e animações suaves

O sistema deve ser profissional, com aparência moderna e polida.
Use ícones (Font Awesome CDN ou SVG inline), tipografia limpa e espaçamento adequado.
Todas as interações devem ter feedback visual (loading, sucesso, erro).

Gere o código AGORA."""

        return prompt


# =============================================================================
# ROTAS
# =============================================================================

@app.route('/')
def index():
    """Página principal - formulário de briefing."""
    return render_template('index.html')


@app.route('/historico')
def historico():
    """Página de histórico de briefings."""
    return render_template('historico.html')


@app.route('/api/briefings', methods=['POST'])
def criar_briefing():
    """Cria um novo briefing e gera o prompt."""
    try:
        data = request.get_json()

        if not data or not data.get('nome_sistema'):
            return jsonify({'erro': 'Nome do sistema é obrigatório'}), 400

        # Gera o prompt
        generator = PromptGenerator()
        prompt_gerado = generator.gerar_prompt(data)

        # Cria o briefing no banco
        briefing = Briefing(
            nome_sistema=data.get('nome_sistema', ''),
            empresa=data.get('empresa', ''),
            setor=data.get('setor', ''),
            prazo_entrega=data.get('prazo_entrega', ''),
            responsavel=data.get('responsavel', ''),
            descricao_problema=data.get('descricao_problema', ''),
            objetivo_principal=data.get('objetivo_principal', ''),
            publico_alvo=data.get('publico_alvo', ''),
            diferenciais=data.get('diferenciais', ''),
            modulos=json.dumps(data.get('modulos', [])),
            detalhamento_modulos=json.dumps(data.get('detalhamento_modulos', [])),
            regras_negocio=json.dumps(data.get('regras_negocio', [])),
            fluxos=json.dumps(data.get('fluxos', [])),
            calculos=json.dumps(data.get('calculos', [])),
            tema=data.get('tema', 'Claro'),
            estilo_design=data.get('estilo_design', 'Moderno'),
            cores=json.dumps(data.get('cores', {})),
            layout=data.get('layout', 'Sidebar fixa'),
            telas=json.dumps(data.get('telas', [])),
            componentes_ui=json.dumps(data.get('componentes_ui', [])),
            responsividade=data.get('responsividade', 'Desktop + Tablet + Mobile'),
            entidades=json.dumps(data.get('entidades', [])),
            relacionamentos=data.get('relacionamentos', ''),
            tipos_dados=json.dumps(data.get('tipos_dados', [])),
            framework_python=data.get('framework_python', 'Flask'),
            banco_dados=data.get('banco_dados', 'SQLite'),
            hospedagem_bd=data.get('hospedagem_bd', 'Local'),
            volume_dados=data.get('volume_dados', ''),
            retencao_dados=data.get('retencao_dados', ''),
            integracoes=json.dumps(data.get('integracoes', [])),
            tempo_resposta=data.get('tempo_resposta', '< 2 segundos'),
            usuarios_simultaneos=data.get('usuarios_simultaneos', '100'),
            uptime=data.get('uptime', '99.9%'),
            backup=data.get('backup', 'Diário'),
            seguranca=json.dumps(data.get('seguranca', [])),
            idiomas=json.dumps(data.get('idiomas', ['Português'])),
            acessibilidade=data.get('acessibilidade', False),
            documentacao_usuario=data.get('documentacao_usuario', False),
            tutorial=data.get('tutorial', False),
            codigo_comentado=data.get('codigo_comentado', True),
            doc_tecnica=data.get('doc_tecnica', True),
            testes=data.get('testes', True),
            logs_erro=data.get('logs_erro', True),
            arquitetura_modular=data.get('arquitetura_modular', True),
            entregaveis=json.dumps(data.get('entregaveis', [])),
            mvp=data.get('mvp', ''),
            fase2=data.get('fase2', ''),
            fase3=data.get('fase3', ''),
            restricoes=data.get('restricoes', ''),
            suposicoes=data.get('suposicoes', ''),
            observacoes=data.get('observacoes', ''),
            prompt_gerado=prompt_gerado
        )

        db.session.add(briefing)
        db.session.commit()

        return jsonify({
            'sucesso': True,
            'id': briefing.id,
            'prompt': prompt_gerado,
            'mensagem': 'Briefing criado e prompt gerado com sucesso!'
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'erro': str(e)}), 500


@app.route('/api/briefings', methods=['GET'])
def listar_briefings():
    """Lista todos os briefings salvos."""
    try:
        briefings = Briefing.query.order_by(Briefing.data_preenchimento.desc()).all()
        return jsonify({
            'sucesso': True,
            'briefings': [b.to_dict() for b in briefings]
        }), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500


@app.route('/api/briefings/<int:id>', methods=['GET'])
def obter_briefing(id):
    """Obtém um briefing específico com o prompt completo."""
    try:
        briefing = Briefing.query.get_or_404(id)
        return jsonify({
            'sucesso': True,
            'briefing': {
                'id': briefing.id,
                'nome_sistema': briefing.nome_sistema,
                'prompt': briefing.prompt_gerado,
                'data': briefing.data_preenchimento.isoformat() if briefing.data_preenchimento else None
            }
        }), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500


@app.route('/api/briefings/<int:id>', methods=['DELETE'])
def excluir_briefing(id):
    """Exclui um briefing."""
    try:
        briefing = Briefing.query.get_or_404(id)
        db.session.delete(briefing)
        db.session.commit()
        return jsonify({'sucesso': True, 'mensagem': 'Briefing excluído com sucesso!'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'erro': str(e)}), 500


@app.route('/api/gerar-prompt-preview', methods=['POST'])
def gerar_preview():
    """Gera apenas o preview do prompt sem salvar no banco."""
    try:
        data = request.get_json()
        generator = PromptGenerator()
        prompt = generator.gerar_prompt(data)
        return jsonify({
            'sucesso': True,
            'prompt': prompt
        }), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500


# =============================================================================
# INICIALIZAÇÃO
# =============================================================================

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5000)
