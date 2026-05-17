/* ============================================
   PROMPT GENERATOR PRO - JAVASCRIPT COMPLETO
   ============================================ */

// Estado global
let currentPrompt = '';
let currentNomeSistema = '';

// Inicialização
document.addEventListener('DOMContentLoaded', function() {
    initForm();
    initColorInputs();
    updateProgress();
});

// ============================================
// FORMULÁRIO
// ============================================

function initForm() {
    const form = document.getElementById('briefingForm');

    // Toggle de seções
    document.querySelectorAll('.section-header').forEach(header => {
        header.addEventListener('click', function(e) {
            if (e.target.closest('.toggle-btn')) return;
            const section = this.closest('.form-section');
            const btn = this.querySelector('.toggle-btn');
            toggleSection(section.id);
        });
    });

    // Atualiza progresso em cada input
    form.addEventListener('input', updateProgress);
    form.addEventListener('change', updateProgress);

    // Submit do formulário
    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        await gerarESalvarPrompt();
    });
}

function toggleSection(sectionId) {
    const section = document.getElementById(sectionId);
    section.classList.toggle('collapsed');
    const btn = section.querySelector('.toggle-btn i');
    if (section.classList.contains('collapsed')) {
        btn.classList.remove('fa-chevron-down');
        btn.classList.add('fa-chevron-right');
    } else {
        btn.classList.remove('fa-chevron-right');
        btn.classList.add('fa-chevron-down');
    }
}

// ============================================
// INPUTS DE COR
// ============================================

function initColorInputs() {
    ['cor_primaria', 'cor_secundaria', 'cor_destaque'].forEach(id => {
        const colorInput = document.getElementById(id);
        const textInput = document.getElementById(id + '_text');

        if (colorInput && textInput) {
            colorInput.addEventListener('input', function() {
                textInput.value = this.value.toUpperCase();
            });
            textInput.addEventListener('input', function() {
                if (/^#[0-9A-F]{6}$/i.test(this.value)) {
                    colorInput.value = this.value;
                }
            });
        }
    });
}

// ============================================
// ADICIONAR/REMOVER ITENS DINÂMICOS
// ============================================

function addModuloCard() {
    const container = document.getElementById('modulosDetalhamento');
    const card = document.createElement('div');
    card.className = 'modulo-card';
    card.innerHTML = `
        <input type="text" class="modulo-nome" placeholder="Nome do Módulo">
        <textarea class="modulo-funcs" rows="2" placeholder="Funcionalidades (uma por linha)"></textarea>
        <textarea class="modulo-regras" rows="1" placeholder="Regras especiais (opcional)"></textarea>
        <button type="button" class="btn-remove" onclick="this.parentElement.remove(); updateProgress();"><i class="fas fa-trash"></i></button>
    `;
    container.appendChild(card);
}

function addRegraRow() {
    const container = document.getElementById('regrasContainer');
    const row = document.createElement('div');
    row.className = 'regra-row';
    row.innerHTML = `
        <input type="text" class="regra-desc" placeholder="Descrição da regra">
        <select class="regra-prio">
            <option value="Alta">Alta</option>
            <option value="Média" selected>Média</option>
            <option value="Baixa">Baixa</option>
        </select>
        <button type="button" class="btn-remove" onclick="this.parentElement.remove(); updateProgress();"><i class="fas fa-trash"></i></button>
    `;
    container.appendChild(row);
}

function addFluxoCard() {
    const container = document.getElementById('fluxosContainer');
    const card = document.createElement('div');
    card.className = 'fluxo-card';
    card.innerHTML = `
        <input type="text" class="fluxo-nome" placeholder="Nome do Fluxo">
        <textarea class="fluxo-passos" rows="3" placeholder="Passos do fluxo (um por linha)"></textarea>
        <textarea class="fluxo-decisoes" rows="1" placeholder="Decisões/Condições (opcional)"></textarea>
        <button type="button" class="btn-remove" onclick="this.parentElement.remove(); updateProgress();"><i class="fas fa-trash"></i></button>
    `;
    container.appendChild(card);
}

function addCalculoRow() {
    const container = document.getElementById('calculosContainer');
    const row = document.createElement('div');
    row.className = 'calculo-row';
    row.innerHTML = `
        <input type="text" class="calc-nome" placeholder="Nome do cálculo">
        <input type="text" class="calc-formula" placeholder="Fórmula/Descrição">
        <input type="text" class="calc-onde" placeholder="Onde é usado">
        <button type="button" class="btn-remove" onclick="this.parentElement.remove(); updateProgress();"><i class="fas fa-trash"></i></button>
    `;
    container.appendChild(row);
}

function addTelaRow() {
    const container = document.getElementById('telasContainer');
    const row = document.createElement('div');
    row.className = 'tela-row';
    row.innerHTML = `
        <input type="text" class="tela-nome" placeholder="Nome da Tela">
        <input type="text" class="tela-desc" placeholder="Descrição">
        <input type="text" class="tela-users" placeholder="Usuários que acessam">
        <button type="button" class="btn-remove" onclick="this.parentElement.remove(); updateProgress();"><i class="fas fa-trash"></i></button>
    `;
    container.appendChild(row);
}

function addEntidadeCard() {
    const container = document.getElementById('entidadesContainer');
    const card = document.createElement('div');
    card.className = 'entidade-card';
    card.innerHTML = `
        <input type="text" class="ent-nome" placeholder="Nome da Entidade">
        <input type="text" class="ent-desc" placeholder="Descrição">
        <input type="text" class="ent-attrs" placeholder="Atributos (separados por vírgula)">
        <button type="button" class="btn-remove" onclick="this.parentElement.remove(); updateProgress();"><i class="fas fa-trash"></i></button>
    `;
    container.appendChild(card);
}

function addIntegracaoRow() {
    const container = document.getElementById('integracoesContainer');
    const row = document.createElement('div');
    row.className = 'integracao-row';
    row.innerHTML = `
        <input type="text" class="int-servico" placeholder="Serviço/API">
        <input type="text" class="int-proposito" placeholder="Propósito">
        <select class="int-auth">
            <option value="Sim">Auth: Sim</option>
            <option value="Não">Auth: Não</option>
        </select>
        <button type="button" class="btn-remove" onclick="this.parentElement.remove(); updateProgress();"><i class="fas fa-trash"></i></button>
    `;
    container.appendChild(row);
}

// ============================================
// COLETAR DADOS DO FORMULÁRIO
// ============================================

function coletarDadosFormulario() {
    const dados = {};

    // Campos simples
    const camposSimples = [
        'nome_sistema', 'empresa', 'setor', 'prazo_entrega', 'responsavel',
        'descricao_problema', 'objetivo_principal', 'publico_alvo', 'diferenciais',
        'tema', 'estilo_design', 'layout', 'responsividade',
        'framework_python', 'banco_dados', 'hospedagem_bd',
        'volume_dados', 'retencao_dados', 'tempo_resposta',
        'usuarios_simultaneos', 'uptime', 'backup',
        'relacionamentos', 'mvp', 'fase2', 'fase3',
        'restricoes', 'suposicoes', 'observacoes'
    ];

    camposSimples.forEach(campo => {
        const el = document.getElementById(campo);
        if (el) dados[campo] = el.value.trim();
    });

    // Cores
    dados.cores = {
        primaria: document.getElementById('cor_primaria')?.value || '#3B82F6',
        secundaria: document.getElementById('cor_secundaria')?.value || '#10B981',
        destaque: document.getElementById('cor_destaque')?.value || '#F59E0B'
    };

    // Checkboxes - Módulos
    dados.modulos = Array.from(document.querySelectorAll('.modulo-check:checked')).map(cb => cb.value);

    // Checkboxes - Componentes UI
    dados.componentes_ui = Array.from(document.querySelectorAll('.comp-check:checked')).map(cb => cb.value);

    // Checkboxes - Tipos de dados
    dados.tipos_dados = Array.from(document.querySelectorAll('.tipo-dado-check:checked')).map(cb => cb.value);

    // Checkboxes - Segurança
    dados.seguranca = Array.from(document.querySelectorAll('.seg-check:checked')).map(cb => cb.value);

    // Checkboxes - Idiomas
    dados.idiomas = Array.from(document.querySelectorAll('.idioma-check:checked')).map(cb => cb.value);

    // Checkboxes - Entregáveis
    dados.entregaveis = Array.from(document.querySelectorAll('.entreg-check:checked')).map(cb => cb.value);

    // Checkboxes não-funcionais
    dados.acessibilidade = document.getElementById('acessibilidade')?.checked || false;
    dados.documentacao_usuario = document.getElementById('documentacao_usuario')?.checked || false;
    dados.tutorial = document.getElementById('tutorial')?.checked || false;
    dados.codigo_comentado = document.getElementById('codigo_comentado')?.checked || false;
    dados.doc_tecnica = document.getElementById('doc_tecnica')?.checked || false;
    dados.testes = document.getElementById('testes')?.checked || false;
    dados.logs_erro = document.getElementById('logs_erro')?.checked || false;
    dados.arquitetura_modular = document.getElementById('arquitetura_modular')?.checked || false;

    // Detalhamento de módulos
    dados.detalhamento_modulos = Array.from(document.querySelectorAll('.modulo-card')).map(card => ({
        nome: card.querySelector('.modulo-nome')?.value || '',
        funcionalidades: (card.querySelector('.modulo-funcs')?.value || '').split('\n').filter(f => f.trim()),
        regras: card.querySelector('.modulo-regras')?.value || ''
    })).filter(m => m.nome);

    // Regras de negócio
    dados.regras_negocio = Array.from(document.querySelectorAll('.regra-row')).map(row => ({
        descricao: row.querySelector('.regra-desc')?.value || '',
        prioridade: row.querySelector('.regra-prio')?.value || 'Média'
    })).filter(r => r.descricao);

    // Fluxos
    dados.fluxos = Array.from(document.querySelectorAll('.fluxo-card')).map(card => ({
        nome: card.querySelector('.fluxo-nome')?.value || '',
        passos: (card.querySelector('.fluxo-passos')?.value || '').split('\n').filter(p => p.trim()),
        decisoes: card.querySelector('.fluxo-decisoes')?.value || ''
    })).filter(f => f.nome);

    // Cálculos
    dados.calculos = Array.from(document.querySelectorAll('.calculo-row')).map(row => ({
        nome: row.querySelector('.calc-nome')?.value || '',
        formula: row.querySelector('.calc-formula')?.value || '',
        onde: row.querySelector('.calc-onde')?.value || ''
    })).filter(c => c.nome);

    // Telas
    dados.telas = Array.from(document.querySelectorAll('.tela-row')).map(row => ({
        nome: row.querySelector('.tela-nome')?.value || '',
        descricao: row.querySelector('.tela-desc')?.value || '',
        usuarios: row.querySelector('.tela-users')?.value || ''
    })).filter(t => t.nome);

    // Entidades
    dados.entidades = Array.from(document.querySelectorAll('.entidade-card')).map(card => ({
        nome: card.querySelector('.ent-nome')?.value || '',
        descricao: card.querySelector('.ent-desc')?.value || '',
        atributos: (card.querySelector('.ent-attrs')?.value || '').split(',').map(a => a.trim()).filter(a => a)
    })).filter(e => e.nome);

    // Integrações
    dados.integracoes = Array.from(document.querySelectorAll('.integracao-row')).map(row => ({
        servico: row.querySelector('.int-servico')?.value || '',
        proposito: row.querySelector('.int-proposito')?.value || '',
        auth: row.querySelector('.int-auth')?.value || 'Não'
    })).filter(i => i.servico);

    return dados;
}

// ============================================
// PROGRESSO
// ============================================

function updateProgress() {
    const dados = coletarDadosFormulario();
    let preenchidos = 0;
    let total = 0;

    // Campos obrigatórios
    const obrigatorios = ['nome_sistema', 'objetivo_principal'];
    obrigatorios.forEach(campo => {
        total++;
        if (dados[campo] && dados[campo].trim()) preenchidos++;
    });

    // Campos importantes
    const importantes = [
        'descricao_problema', 'publico_alvo', 'empresa', 'setor',
        'mvp', 'modulos', 'regras_negocio', 'telas', 'entidades',
        'framework_python', 'banco_dados'
    ];
    importantes.forEach(campo => {
        total++;
        const val = dados[campo];
        if (val && (typeof val === 'string' ? val.trim() : (Array.isArray(val) ? val.length > 0 : val))) {
            preenchidos++;
        }
    });

    const percentual = Math.round((preenchidos / total) * 100);
    document.getElementById('progressBar').style.width = percentual + '%';
    document.getElementById('progressText').textContent = percentual + '%';

    // Marca seções preenchidas
    document.querySelectorAll('.form-section').forEach(section => {
        const inputs = section.querySelectorAll('input, textarea, select');
        let hasValue = false;
        inputs.forEach(input => {
            if (input.type === 'checkbox' || input.type === 'radio') {
                if (input.checked) hasValue = true;
            } else if (input.value.trim()) {
                hasValue = true;
            }
        });
        if (hasValue) {
            section.classList.add('filled');
        } else {
            section.classList.remove('filled');
        }
    });
}

// ============================================
// GERAR PREVIEW
// ============================================

async function gerarPreview() {
    const dados = coletarDadosFormulario();

    if (!dados.nome_sistema) {
        mostrarToast('Preencha pelo menos o Nome do Sistema!', 'error');
        document.getElementById('nome_sistema').focus();
        return;
    }

    mostrarLoading(true);

    try {
        const response = await fetch('/api/gerar-prompt-preview', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(dados)
        });

        const data = await response.json();

        if (data.sucesso) {
            currentPrompt = data.prompt;
            currentNomeSistema = dados.nome_sistema;
            document.getElementById('previewContent').textContent = data.prompt;
            document.getElementById('previewModal').style.display = 'flex';
        } else {
            mostrarToast('Erro: ' + data.erro, 'error');
        }
    } catch (error) {
        mostrarToast('Erro de conexão: ' + error.message, 'error');
    } finally {
        mostrarLoading(false);
    }
}

// ============================================
// GERAR E SALVAR PROMPT
// ============================================

async function gerarESalvarPrompt() {
    const dados = coletarDadosFormulario();

    if (!dados.nome_sistema) {
        mostrarToast('Nome do sistema é obrigatório!', 'error');
        document.getElementById('nome_sistema').focus();
        return;
    }

    if (!dados.objetivo_principal) {
        mostrarToast('Objetivo principal é obrigatório!', 'error');
        document.getElementById('objetivo_principal').focus();
        return;
    }

    mostrarLoading(true);

    try {
        const response = await fetch('/api/briefings', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(dados)
        });

        const data = await response.json();

        if (data.sucesso) {
            currentPrompt = data.prompt;
            currentNomeSistema = dados.nome_sistema;
            document.getElementById('previewContent').textContent = data.prompt;
            document.getElementById('previewModal').style.display = 'flex';
            mostrarToast('Briefing salvo e prompt gerado com sucesso!');
        } else {
            mostrarToast('Erro: ' + data.erro, 'error');
        }
    } catch (error) {
        mostrarToast('Erro de conexão: ' + error.message, 'error');
    } finally {
        mostrarLoading(false);
    }
}

// ============================================
// MODAL
// ============================================

function fecharModal() {
    document.getElementById('previewModal').style.display = 'none';
}

function copiarPrompt() {
    navigator.clipboard.writeText(currentPrompt).then(() => {
        mostrarToast('Prompt copiado para a área de transferência!');
    }).catch(() => {
        // Fallback para navegadores antigos
        const textarea = document.createElement('textarea');
        textarea.value = currentPrompt;
        document.body.appendChild(textarea);
        textarea.select();
        document.execCommand('copy');
        document.body.removeChild(textarea);
        mostrarToast('Prompt copiado!');
    });
}

function downloadPrompt() {
    const blob = new Blob([currentPrompt], { type: 'text/plain;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `prompt_${currentNomeSistema.toLowerCase().replace(/\s+/g, '_')}.txt`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
    mostrarToast('Prompt baixado com sucesso!');
}

// Fecha modal ao clicar fora
window.onclick = function(event) {
    const modal = document.getElementById('previewModal');
    if (event.target === modal) {
        modal.style.display = 'none';
    }
}

// ============================================
// UTILITÁRIOS
// ============================================

function mostrarToast(mensagem, tipo = 'success') {
    const toast = document.getElementById('toast');
    const msgEl = document.getElementById('toastMessage');
    const icon = toast.querySelector('i');

    msgEl.textContent = mensagem;
    toast.className = `toast ${tipo}`;

    if (tipo === 'error') {
        icon.className = 'fas fa-exclamation-circle';
    } else {
        icon.className = 'fas fa-check-circle';
    }

    toast.style.display = 'flex';

    setTimeout(() => {
        toast.style.display = 'none';
    }, 4000);
}

function mostrarLoading(mostrar) {
    document.getElementById('loadingOverlay').style.display = mostrar ? 'flex' : 'none';
}

function limparFormulario() {
    if (!confirm('Tem certeza que deseja limpar todo o formulário?')) return;

    document.getElementById('briefingForm').reset();

    // Limpa cards dinâmicos mantendo apenas o primeiro de cada tipo
    const containers = [
        'modulosDetalhamento', 'regrasContainer', 'fluxosContainer',
        'calculosContainer', 'telasContainer', 'entidadesContainer', 'integracoesContainer'
    ];

    containers.forEach(id => {
        const container = document.getElementById(id);
        if (container) {
            const children = container.children;
            while (children.length > 1) {
                container.removeChild(children[children.length - 1]);
            }
            // Limpa os inputs do primeiro card
            const first = children[0];
            if (first) {
                first.querySelectorAll('input, textarea').forEach(input => input.value = '');
            }
        }
    });

    // Reseta cores
    document.getElementById('cor_primaria').value = '#3B82F6';
    document.getElementById('cor_primaria_text').value = '#3B82F6';
    document.getElementById('cor_secundaria').value = '#10B981';
    document.getElementById('cor_secundaria_text').value = '#10B981';
    document.getElementById('cor_destaque').value = '#F59E0B';
    document.getElementById('cor_destaque_text').value = '#F59E0B';

    updateProgress();
    mostrarToast('Formulário limpo!');
}

// ============================================
// ATALHOS DE TECLADO
// ============================================

document.addEventListener('keydown', function(e) {
    // Ctrl+Enter para gerar preview
    if (e.ctrlKey && e.key === 'Enter') {
        e.preventDefault();
        gerarPreview();
    }

    // Ctrl+S para salvar (previne o save do navegador)
    if (e.ctrlKey && e.key === 's') {
        e.preventDefault();
        document.querySelector('.btn-submit').click();
    }

    // ESC para fechar modal
    if (e.key === 'Escape') {
        fecharModal();
    }
});
