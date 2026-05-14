/* =========================================================
   WAGNER PERFUMES — App JavaScript
   Carrinho + Checkout + PIX + Cartao + Filtros
   ========================================================= */

// === CARRINHO ===
let carrinho = JSON.parse(localStorage.getItem('wagner_carrinho') || '[]');

function salvarCarrinho() {
    localStorage.setItem('wagner_carrinho', JSON.stringify(carrinho));
    atualizarContador();
}

function atualizarContador() {
    const count = carrinho.reduce((s, i) => s + i.qty, 0);
    document.querySelectorAll('.cart-count-h, #cartCount').forEach(el => {
        if (el) { el.textContent = count; el.style.display = count > 0 ? 'grid' : 'none'; }
    });
}

function toggleCart() {
    document.getElementById('cartOverlay')?.classList.toggle('active');
    document.getElementById('cartSidebar')?.classList.toggle('active');
    renderizarCarrinho();
}

function adicionarAoCarrinho(produtoId) {
    fetch(`/api/produto/${produtoId}`)
        .then(r => r.json())
        .then(p => {
            const existente = carrinho.find(i => i.id === produtoId);
            if (existente) { existente.qty += 1; }
            else { carrinho.push({ id: p.id, nome: p.nome, preco: p.preco, qty: 1 }); }
            salvarCarrinho();
            showToast(`${p.nome} adicionado ao carrinho`);
        })
        .catch(() => showToast('Erro ao adicionar'));
}

function removerDoCarrinho(produtoId) {
    carrinho = carrinho.filter(i => i.id !== produtoId);
    salvarCarrinho();
    renderizarCarrinho();
}

function alterarQuantidade(produtoId, delta) {
    const item = carrinho.find(i => i.id === produtoId);
    if (!item) return;
    item.qty += delta;
    if (item.qty <= 0) { removerDoCarrinho(produtoId); return; }
    salvarCarrinho();
    renderizarCarrinho();
}

function renderizarCarrinho() {
    const container = document.getElementById('cartItems');
    const totalEl = document.getElementById('cartTotalVal') || document.getElementById('cartTotalValue');
    if (!container) return;
    if (carrinho.length === 0) {
        container.innerHTML = '<div class="cart-empty-msg">Seu carrinho está vazio</div>';
        if (totalEl) totalEl.textContent = 'R$ 0,00';
        return;
    }
    let html = '', total = 0;
    carrinho.forEach(item => {
        const sub = item.preco * item.qty; total += sub;
        html += `<div class="cart-item-row">
            <div class="ci-info">
                <h4>${item.nome}</h4>
                <div class="ci-price">R$ ${item.preco.toFixed(2)}</div>
                <div class="ci-qty">
                    <button onclick="alterarQuantidade(${item.id},-1)">−</button>
                    <span>${item.qty}</span>
                    <button onclick="alterarQuantidade(${item.id},1)">+</button>
                    <button class="ci-remove" onclick="removerDoCarrinho(${item.id})">Remover</button>
                </div>
            </div>
        </div>`;
    });
    container.innerHTML = html;
    if (totalEl) totalEl.textContent = `R$ ${total.toFixed(2)}`;
}

function irParaCheckout() {
    if (carrinho.length === 0) { showToast('Carrinho vazio!'); return; }
    window.location.href = '/checkout';
}

function irCheckout() { irParaCheckout(); }

// === CHECKOUT ===
function togglePagamento() {
    const sel = document.getElementById('pagamento');
    const cartaoOp = document.getElementById('cartaoOpcoes');
    cartaoOp.style.display = (sel.value === 'credito' || sel.value === 'debito') ? 'block' : 'none';
}

function carregarResumoCheckout() {
    const container = document.getElementById('ckItens');
    const totalEl = document.getElementById('ckTotal');
    if (!container) return;
    if (carrinho.length === 0) { window.location.href = '/'; return; }
    let html = '', total = 0;
    carrinho.forEach(item => {
        const sub = item.preco * item.qty; total += sub;
        html += `<div class="ck-resumo-item"><span>${item.nome} x${item.qty}</span><span>R$ ${sub.toFixed(2)}</span></div>`;
    });
    container.innerHTML = html;
    if (totalEl) totalEl.textContent = `R$ ${total.toFixed(2)}`;
}

function enviarPedido(event) {
    event.preventDefault();
    const btn = document.getElementById('btnFinalizar');
    btn.textContent = '⏳ Enviando...';
    btn.disabled = true;

    const total = carrinho.reduce((s, i) => s + i.preco * i.qty, 0);
    const pagamento = document.getElementById('pagamento').value;

    const pedido = {
        nome: document.getElementById('nome').value,
        telefone: document.getElementById('tel').value,
        email: document.getElementById('email').value,
        cpf: document.getElementById('cpf').value,
        cep: document.getElementById('cep').value,
        endereco: document.getElementById('endereco').value,
        cidade: document.getElementById('cidade').value,
        estado: document.getElementById('estado').value,
        pagamento: pagamento,
        parcelas: pagamento !== 'pix' ? document.getElementById('parcelas')?.value : '1',
        obs: document.getElementById('obs').value,
        itens: carrinho,
        total: total
    };

    // Enviar pedido
    fetch('/api/pedido', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(pedido)
    })
    .then(r => r.json())
    .then(data => {
        if (data.status !== 'ok') throw new Error(data.mensagem || 'Erro ao enviar');

        pedido.pedido_id = data.pedido_id;
        pedido.total = data.total;

        if (pagamento === 'pix') {
            // Gerar QR Code PIX
            return fetch('/api/pix/gerar', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    pedido_id: data.pedido_id,
                    valor: data.total,
                    nome: pedido.nome
                })
            });
        }
        return { json: () => ({ status: 'ok' }) };
    })
    .then(r => r.json())
    .then(pixData => {
        // Limpar carrinho
        carrinho = []; salvarCarrinho();

        document.getElementById('ckForm').style.display = 'none';
        document.getElementById('ckResumo').style.display = 'none';

        if (pagamento === 'pix' && pixData.status === 'ok') {
            document.getElementById('telaPix').style.display = 'block';
            document.getElementById('pixQrImg').src = pixData.qr_code;
            document.getElementById('pixCopiaECola').textContent = 'Código PIX: ' + pixData.payload;
        } else {
            document.getElementById('telaConfirmado').style.display = 'block';
            const msg = pagamento === 'credito' 
                ? `Pedido registrado! Pagamento em ${document.getElementById('parcelas').value}x será processado.` 
                : 'Pedido registrado! Entraremos em contato para confirmar.';
            document.getElementById('confirmadoMsg').textContent = msg;
        }
        showToast('🎉 Pedido realizado com sucesso!');
    })
    .catch(err => {
        showToast('Erro: ' + err.message);
        btn.textContent = '💳 Finalizar Pedido';
        btn.disabled = false;
    });
}

// === TOGGLE MOBILE ===
function toggleMNav() { document.getElementById('mnav')?.classList.toggle('active'); }

// === FILTRO ===
function filtrarCategoria(catId) {
    document.querySelectorAll('.product-card').forEach(c => {
        const p = c.querySelector('h3');
        c.style.display = p && p.textContent.includes(catId) ? 'block' : 'none';
    });
    // Fallback: se for clicar em categoria e nao achar, so rolar pros produtos
    document.getElementById('perfumes')?.scrollIntoView({ behavior: 'smooth' });
}

// === TOAST ===
function showToast(msg) {
    const el = document.getElementById('toast');
    if (!el) return;
    el.textContent = msg;
    el.classList.add('show');
    setTimeout(() => el.classList.remove('show'), 3000);
}

// === INIT ===
document.addEventListener('DOMContentLoaded', () => {
    atualizarContador();
    // Sidebar se nao existir no DOM (fallback pra pagina que nao tem)
    if (!document.getElementById('cartSidebar')) {
        const html = `
        <div class="cart-overlay" id="cartOverlay" onclick="toggleCart()"></div>
        <div class="cart-sidebar" id="cartSidebar">
            <div class="cart-s-hd">
                <h2>Carrinho</h2>
                <button class="cart-s-close" onclick="toggleCart()">✕</button>
            </div>
            <div class="cart-s-items" id="cartItems"></div>
            <div class="cart-s-ft">
                <div class="cart-s-total"><span>Total</span><span id="cartTotalVal">R$ 0,00</span></div>
                <button class="btn-cart-chk" onclick="irCheckout()">Finalizar Compra</button>
            </div>
        </div>`;
        document.body.insertAdjacentHTML('beforeend', html);
    }
});
