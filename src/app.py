"""
Wagner Perfumes — Servidor Flask
Landing page promocional + Checkout + Painel Admin
JC Infocell | Agente Desenvolvedor
"""

import json
import os
import io
import base64
import copy
from datetime import datetime
from flask import Flask, render_template, jsonify, request

ASSETS_DIR = os.path.join(os.path.dirname(__file__), '..', 'assets')

app = Flask(__name__, 
            static_folder=os.path.join(os.path.dirname(__file__), '..', 'assets'),
            static_url_path='/static',
            template_folder=os.path.join(os.path.dirname(__file__), '..', 'templates'))

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PRODUTOS_PATH = os.path.join(BASE_DIR, 'produtos.json')
PEDIDOS_DIR = os.path.join(BASE_DIR, 'pedidos')
CONFIG_PATH = os.path.join(BASE_DIR, 'config.json')

def carregar_dados():
    with open(PRODUTOS_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def salvar_dados(dados):
    with open(PRODUTOS_PATH, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

def get_categoria_nome(cat_id, categorias):
    for c in categorias:
        if c['id'] == cat_id:
            return c['nome']
    return cat_id

# ==================== ROTAS PUBLICAS ====================

@app.route('/')
def home():
    dados = carregar_dados()
    categorias = dados['categorias']
    produtos = dados['produtos']
    for cat in categorias:
        cat['count'] = len([p for p in produtos if p['categoria'] == cat['id']])
    for p in produtos:
        p['categoria_nome'] = get_categoria_nome(p['categoria'], categorias)
    return render_template('index.html', categorias=categorias, produtos=produtos)

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

# ==================== API PRODUTOS ====================

@app.route('/api/produto/<int:produto_id>', methods=['GET'])
def api_get_produto(produto_id):
    dados = carregar_dados()
    for p in dados['produtos']:
        if p['id'] == produto_id:
            return jsonify(p)
    return jsonify({'erro': 'Produto nao encontrado'}), 404

@app.route('/api/produto', methods=['POST'])
def api_criar_produto():
    try:
        dados = carregar_dados()
        novo = request.get_json()
        novo_id = max(p['id'] for p in dados['produtos']) + 1 if dados['produtos'] else 1
        novo['id'] = novo_id
        novo['destaque'] = novo.get('destaque', False)
        dados['produtos'].append(novo)
        salvar_dados(dados)
        print(f"  [ADMIN] Produto criado: {novo['nome']} (id={novo_id})")
        return jsonify({'status': 'ok', 'id': novo_id})
    except Exception as e:
        return jsonify({'status': 'erro', 'mensagem': str(e)}), 500

@app.route('/api/produto/<int:produto_id>', methods=['PUT'])
def api_atualizar_produto(produto_id):
    try:
        dados = carregar_dados()
        alterado = request.get_json()
        for p in dados['produtos']:
            if p['id'] == produto_id:
                p.update({k: v for k, v in alterado.items() if k != 'id'})
                salvar_dados(dados)
                print(f"  [ADMIN] Produto atualizado: {p['nome']} (id={produto_id})")
                return jsonify({'status': 'ok'})
        return jsonify({'erro': 'Nao encontrado'}), 404
    except Exception as e:
        return jsonify({'status': 'erro', 'mensagem': str(e)}), 500

@app.route('/api/produto/<int:produto_id>', methods=['DELETE'])
def api_deletar_produto(produto_id):
    try:
        dados = carregar_dados()
        dados['produtos'] = [p for p in dados['produtos'] if p['id'] != produto_id]
        salvar_dados(dados)
        print(f"  [ADMIN] Produto deletado: id={produto_id}")
        return jsonify({'status': 'ok'})
    except Exception as e:
        return jsonify({'status': 'erro', 'mensagem': str(e)}), 500

@app.route('/api/produtos')
def api_listar_produtos():
    dados = carregar_dados()
    return jsonify(dados['produtos'])

# ==================== API PEDIDOS ====================

@app.route('/api/pedido', methods=['POST'])
def api_criar_pedido():
    try:
        pedido = request.get_json()
        os.makedirs(PEDIDOS_DIR, exist_ok=True)
        pedido_id = f"WP-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        pedido['id'] = pedido_id
        pedido['data'] = datetime.now().strftime('%d/%m/%Y %H:%M')
        pedido['status'] = 'recebido'
        caminho = os.path.join(PEDIDOS_DIR, f'{pedido_id}.json')
        with open(caminho, 'w', encoding='utf-8') as f:
            json.dump(pedido, f, indent=2, ensure_ascii=False)
        total = sum(item['preco'] * item['qty'] for item in pedido.get('itens', []))
        print(f"\n=== NOVO PEDIDO: {pedido_id} ===")
        print(f"Cliente: {pedido.get('nome')} | Tel: {pedido.get('telefone')}")
        print(f"Endereco: {pedido.get('endereco')}, {pedido.get('cidade')}")
        print(f"Pagamento: {pedido.get('pagamento')}")
        print(f"Itens: {len(pedido.get('itens', []))} | Total: R$ {total:.2f}")
        print("=" * 40)
        return jsonify({'status': 'ok', 'pedido_id': pedido_id, 'total': total})
    except Exception as e:
        return jsonify({'status': 'erro', 'mensagem': str(e)}), 500

@app.route('/api/pedidos')
def api_listar_pedidos():
    if not os.path.exists(PEDIDOS_DIR):
        return jsonify([])
    pedidos = []
    for fname in sorted(os.listdir(PEDIDOS_DIR), reverse=True):
        if fname.endswith('.json'):
            with open(os.path.join(PEDIDOS_DIR, fname), 'r', encoding='utf-8') as f:
                pedidos.append(json.load(f))
    return jsonify(pedidos)

@app.route('/api/pedido/<pedido_id>/status', methods=['PUT'])
def api_alterar_status(pedido_id):
    try:
        data = request.get_json()
        novo_status = data.get('status', 'recebido')
        caminho = os.path.join(PEDIDOS_DIR, f'{pedido_id}.json')
        if not os.path.exists(caminho):
            return jsonify({'erro': 'Nao encontrado'}), 404
        with open(caminho, 'r', encoding='utf-8') as f:
            pedido = json.load(f)
        pedido['status'] = novo_status
        with open(caminho, 'w', encoding='utf-8') as f:
            json.dump(pedido, f, indent=2, ensure_ascii=False)
        print(f"  [ADMIN] Pedido {pedido_id} -> {novo_status}")
        return jsonify({'status': 'ok'})
    except Exception as e:
        return jsonify({'status': 'erro', 'mensagem': str(e)}), 500

@app.route('/api/pedido/<pedido_id>', methods=['DELETE'])
def api_deletar_pedido(pedido_id):
    try:
        caminho = os.path.join(PEDIDOS_DIR, f'{pedido_id}.json')
        if os.path.exists(caminho):
            os.remove(caminho)
            print(f"  [ADMIN] Pedido deletado: {pedido_id}")
        return jsonify({'status': 'ok'})
    except Exception as e:
        return jsonify({'status': 'erro', 'mensagem': str(e)}), 500

# ==================== API PIX ====================

@app.route('/api/pix/gerar', methods=['POST'])
def api_gerar_pix():
    try:
        import qrcode
        dados = request.get_json()
        pedido_id = dados.get('pedido_id', 'WP-000000')
        valor = dados.get('valor', 0)
        payload = f"00020101021226830014BR.GOV.BCB.PIX2563pix.wagnerperfumes.com/{pedido_id}520400005303986540{int(valor):.0f}5802BR5916Wagner Perfumes6008BRASILIA62070503***6304"
        qr = qrcode.QRCode(version=4, error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=10, border=2)
        qr.add_data(payload)
        qr.make(fit=True)
        img = qr.make_image(fill_color="#3a1f18", back_color="white")
        buf = io.BytesIO()
        img.save(buf, format='PNG')
        buf.seek(0)
        img_b64 = base64.b64encode(buf.getvalue()).decode('utf-8')
        print(f"  [PIX] QR Code gerado para {pedido_id} - R$ {valor:.2f}")
        return jsonify({'status': 'ok', 'qr_code': f"data:image/png;base64,{img_b64}", 'payload': payload, 'copia_e_cola': payload, 'pedido_id': pedido_id, 'valor': valor})
    except ImportError:
        return jsonify({'status': 'erro', 'mensagem': 'QR Code nao disponivel (pip install qrcode[pil])'}), 500
    except Exception as e:
        return jsonify({'status': 'erro', 'mensagem': str(e)}), 500

# ==================== API CONFIG ====================

@app.route('/api/config', methods=['GET'])
def api_get_config():
    with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
        cfg = json.load(f)
    return jsonify(cfg)

@app.route('/api/config', methods=['PUT'])
def api_salvar_config():
    try:
        data = request.get_json()
        with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
            cfg = json.load(f)
        cfg.update({k: v for k, v in data.items()})
        with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
            json.dump(cfg, f, indent=4, ensure_ascii=False)
        print(f"  [ADMIN] Config atualizada")
        return jsonify({'status': 'ok'})
    except Exception as e:
        return jsonify({'status': 'erro', 'mensagem': str(e)}), 500

# ==================== INICIO ====================

if __name__ == '__main__':
    import socket
    
    print("=" * 50)
    print("  WAGNER PERFUMES — Servidor Web + Admin")
    print("=" * 50)
    
    hostname = socket.gethostname()
    ips = set()
    try:
        for info in socket.getaddrinfo(hostname, None):
            ip = info[4][0]
            if not ip.startswith('127.'):
                ips.add(ip)
    except:
        pass
    
    with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
        config = json.load(f)
    
    porta = int(os.environ.get('PORT', config.get('porta', 5000)))
    debug = config.get('debug', False)
    
    print(f"\n  Loja:      http://localhost:{porta}")
    print(f"  Admin:     http://localhost:{porta}/admin")
    for ip in sorted(ips):
        print(f"  Rede:      http://{ip}:{porta}")
    print(f"\n  Ctrl+C para parar")
    print("=" * 50)
    
    app.run(host=config.get('host', '0.0.0.0'), port=porta, debug=debug)
