import os
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(201, 168, 76)  # dourado
        self.cell(0, 8, 'Wagner Perfumes - Documentacao do Projeto', 0, 1, 'R')
        self.line(10, 14, 200, 14)
        self.ln(4)

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, f'Pagina {self.page_no()}/{{nb}}', 0, 0, 'C')

    def chapter_title(self, title, level=1):
        if level == 1:
            self.set_font('Helvetica', 'B', 16)
            self.set_text_color(201, 168, 76)
            self.cell(0, 10, title, 0, 1)
            self.set_draw_color(201, 168, 76)
            self.line(10, self.get_y(), 200, self.get_y())
            self.ln(4)
        elif level == 2:
            self.set_font('Helvetica', 'B', 13)
            self.set_text_color(184, 148, 46)
            self.cell(0, 8, title, 0, 1)
            self.ln(2)
        elif level == 3:
            self.set_font('Helvetica', 'B', 11)
            self.set_text_color(50, 50, 50)
            self.cell(0, 7, title, 0, 1)
            self.ln(1)

    def body_text(self, text):
        self.set_font('Helvetica', '', 10)
        self.set_text_color(26, 26, 26)
        self.multi_cell(0, 5.5, text)
        self.ln(2)

    def bullet(self, text, indent=15):
        self.set_font('Helvetica', '', 10)
        self.set_text_color(26, 26, 26)
        x = self.get_x()
        self.set_x(x + indent)
        self.cell(5, 5.5, '-')
        self.multi_cell(0, 5.5, text)
        self.ln(1)

    def table(self, headers, rows, col_widths=None):
        if col_widths is None:
            col_widths = [190 / len(headers)] * len(headers)
        
        # Header row
        self.set_font('Helvetica', 'B', 9)
        self.set_fill_color(201, 168, 76)
        self.set_text_color(255, 255, 255)
        for i, h in enumerate(headers):
            self.cell(col_widths[i], 7, h, 1, 0, 'L', True)
        self.ln()
        
        # Data rows
        self.set_font('Helvetica', '', 9)
        self.set_text_color(26, 26, 26)
        fill = False
        for row in rows:
            if self.get_y() > 260:
                self.add_page()
                self.set_font('Helvetica', 'B', 9)
                self.set_fill_color(201, 168, 76)
                self.set_text_color(255, 255, 255)
                for i, h in enumerate(headers):
                    self.cell(col_widths[i], 7, h, 1, 0, 'L', True)
                self.ln()
                self.set_font('Helvetica', '', 9)
                self.set_text_color(26, 26, 26)
            if fill:
                self.set_fill_color(249, 245, 240)
            else:
                self.set_fill_color(255, 255, 255)
            for i, cell in enumerate(row):
                self.cell(col_widths[i], 6, str(cell), 1, 0, 'L', fill)
            self.ln()
            fill = not fill
        self.ln(3)


pdf = PDF()
pdf.alias_nb_pages()
pdf.set_auto_page_break(auto=True, margin=20)
pdf.add_page()

# -- CAPA --
pdf.ln(40)
pdf.set_font('Helvetica', 'B', 28)
pdf.set_text_color(201, 168, 76)
pdf.cell(0, 15, 'WAGNER PERFUMES', 0, 1, 'C')
pdf.set_font('Helvetica', '', 14)
pdf.set_text_color(100, 100, 100)
pdf.cell(0, 10, 'Webpage de Vendas - E-commerce de Perfumes', 0, 1, 'C')
pdf.ln(5)
pdf.set_draw_color(201, 168, 76)
pdf.line(60, pdf.get_y(), 150, pdf.get_y())
pdf.ln(10)
pdf.set_font('Helvetica', '', 11)
pdf.set_text_color(120, 120, 120)
pdf.cell(0, 7, 'Documentacao do Projeto - Versao 1.0', 0, 1, 'C')
pdf.cell(0, 7, 'JC Infocell - Agente Desenvolvedor', 0, 1, 'C')
pdf.cell(0, 7, '13 de Maio de 2026', 0, 1, 'C')
pdf.ln(40)
pdf.set_font('Helvetica', 'I', 9)
pdf.set_text_color(150, 150, 150)
pdf.cell(0, 7, 'Design minimalista com letras douradas', 0, 1, 'C')

# -- SUMARIO --
pdf.add_page()
pdf.chapter_title('Sumario', 1)
sections = [
    '1. Visao Geral do Projeto',
    '2. Pesquisa de Mercado e Tendencias',
    '3. Referencias e Casos Similares',
    '4. Diretrizes de Design',
    '5. Escopo Tecnico',
    '6. Estrutura do Site (Sitemap)',
    '7. Tecnologias e Stack',
    '8. Roadmap e Proximos Passos',
    'Apendice: Glossario Visual'
]
for s in sections:
    pdf.set_font('Helvetica', '', 11)
    pdf.set_text_color(26, 26, 26)
    pdf.cell(0, 7, f'   {s}', 0, 1)

# -- 1. VISAO GERAL --
pdf.add_page()
pdf.chapter_title('1. Visao Geral do Projeto', 1)

pdf.chapter_title('Cliente', 2)
pdf.body_text('Wagner Perfumes - Loja de perfumes entrando no mercado de vendas web.')

pdf.chapter_title('Objetivo', 2)
pdf.body_text('Criar uma webpage de vendas profissional, elegante e funcional, que transmita sofisticacao atraves de um design minimalista com letras/acabamentos dourados.')

pdf.chapter_title('Publico-Alvo', 2)
pdf.bullet('Consumidores finais que buscam perfumes de qualidade')
pdf.bullet('Faixa etaria: 18-55 anos')
pdf.bullet('Perfil: valoriza apresentacao visual, busca praticidade na compra online')
pdf.bullet('Dispositivo principal: mobile (80% do trafego de e-commerce)')

pdf.chapter_title('Principais Funcionalidades (Fase 1)', 2)
pdf.bullet('Vitrine de produtos com categorias')
pdf.bullet('Carrinho de compras')
pdf.bullet('Checkout simplificado')
pdf.bullet('Responsividade mobile-first')
pdf.bullet('Design minimalista com paleta dourada')

# -- 2. PESQUISA --
pdf.add_page()
pdf.chapter_title('2. Pesquisa de Mercado e Tendencias', 1)

pdf.body_text('E-commerce de Perfumes em 2024-2025:')
pdf.bullet('80% do trafego global de e-commerce vem de smartphones')
pdf.bullet('Apps mobile tem taxa de conversao superior e gastos 10-50% maiores que sites moveis')
pdf.bullet('TikTok #FragranceTok ultrapassou 278M de publicacoes')
pdf.bullet('IA e ferramentas de recomendacao estao reduzindo o risco da "compra cega"')
pdf.bullet('Sustentabilidade em alta: materiais ecologicos, refis, transparencia')

pdf.chapter_title('Tendencias de Design para Perfumaria de Luxo', 2)
pdf.table(
    ['Tendencia', 'Descricao'],
    [
        ['Minimalismo', 'Pureza, linhas limpas, formas geometricas, cores neutras'],
        ['Acabamento Dourado', 'Detalhes metalicos em logos, tipografia e elementos de destaque'],
        ['Tipografia Serifada', 'Fontes elegantes (Didot, Bodoni) com espacamento generoso'],
        ['Foto editorial', 'Frascos como objetos de arte, fundo limpo, iluminacao dramatica'],
        ['Espaco negativo', 'Sensacao de calma, clareza e exclusividade'],
        ['Micro-interacoes', 'Hover effects, transicoes suaves, loading refinados'],
    ],
    [45, 145]
)

# -- 3. REFERENCIAS --
pdf.add_page()
pdf.chapter_title('3. Referencias e Casos Similares', 1)

pdf.table(
    ['Marca', 'Estilo', 'Destaque'],
    [
        ['Tom Ford', 'Luxo minimalista preto & dourado', 'Design ousado, tipografia refinada'],
        ['YSL Libre', 'Dourado como elemento central', 'Detalhes dourados em destaque'],
        ['Dolce & Gabbana', 'Sofisticacao classica', 'Emblemas dourados, artesanal'],
        ['Miller Harris', 'Minimalismo organico', 'Cores pastel, natureza'],
        ['Hiram Green', 'Nicho minimalista', 'Frascos clean, sem excessos'],
        ['Le Galion', 'Luxury vintage refinado', 'Tipografia serifada, dourados discretos'],
    ],
    [40, 60, 90]
)

pdf.chapter_title('Caracteristicas Comuns nos Casos de Sucesso', 2)
pdf.bullet('Fundo predominantemente claro (branco, off-white, creme)')
pdf.bullet('Destaque dourado em logo, titulos e CTAs')
pdf.bullet('Layout limpo com muito espaco em branco')
pdf.bullet('Fotografia profissional de alta qualidade')
pdf.bullet('Navegacao simplificada (poucos itens no menu)')
pdf.bullet('Descricoes sensoriais e poeticas dos perfumes')
pdf.bullet('Mobile-first com adaptacao fluida')

# -- 4. DIRETRIZES DE DESIGN --
pdf.add_page()
pdf.chapter_title('4. Diretrizes de Design', 1)

pdf.chapter_title('Paleta de Cores', 2)
pdf.table(
    ['Uso', 'Cor', 'Codigo Hex'],
    [
        ['Fundo principal', 'Branco', '#FFFFFF'],
        ['Fundo secundario', 'Off-white / Creme suave', '#F5F0EB'],
        ['Texto principal', 'Preto suave', '#1A1A1A'],
        ['Texto secundario', 'Cinza elegante', '#6B6B6B'],
        ['Dourado principal', 'Dourado classico', '#C9A84C'],
        ['Dourado claro', 'Dourado claro / detalhes', '#E8D5A3'],
        ['CTA / Destaque', 'Dourado escuro / hover', '#B8942E'],
        ['Acento', 'Preto elegante', '#2C2C2C'],
    ],
    [50, 80, 50]
)

pdf.chapter_title('Tipografia', 2)
pdf.table(
    ['Uso', 'Fonte', 'Peso', 'Tamanhos'],
    [
        ['Logo / Titulos', 'Playfair Display', 'Bold / SemiBold', '48px a 28px (mobile)'],
        ['Subtitulos', 'Playfair Display', 'Regular', '24px a 18px'],
        ['Corpo / Descricoes', 'Lato', 'Light / Regular', '16px a 14px'],
        ['Precos / CTAs', 'Lato', 'Bold', '18px a 16px'],
        ['Navegacao', 'Lato', 'Regular', '14px'],
    ],
    [40, 40, 35, 65]
)

pdf.chapter_title('Tom de Voz do Site', 2)
pdf.bullet('Sofisticado mas acessivel')
pdf.bullet('Descricoes sensoriais: "Notas amadeiradas com toque citrico"')
pdf.bullet('Evitar texto excessivo - poesia na medida')
pdf.bullet('Portugues formal mas caloroso')

pdf.chapter_title('Elementos Visuais', 2)
pdf.bullet('Icones minimalistas em linha fina (stroke dourado)')
pdf.bullet('Bordas finas 1px douradas em cards e botoes')
pdf.bullet('Sombras suaves e sutis (box-shadow leve)')
pdf.bullet('Botoes com fill dourado e hover com tom mais escuro')
pdf.bullet('Fotografia: frascos isolados em fundo branco/creme')

# -- 5. ESCOPO TECNICO --
pdf.add_page()
pdf.chapter_title('5. Escopo Tecnico', 1)

pdf.chapter_title('Fase 1 - MVP', 2)
pdf.table(
    ['Funcionalidade', 'Descricao'],
    [
        ['Vitrine de produtos', 'Grid responsivo com cards de produto'],
        ['Categorias', 'Filtro por categoria (Masc, Fem, Unissex, Nicho)'],
        ['Pagina do produto', 'Imagem grande, descricao, preco, botao comprar'],
        ['Carrinho lateral', 'Slide-in com itens adicionados'],
        ['Checkout', 'Formulario simplificado (nome, endereco, pagamento)'],
        ['Mobile-first', 'Layout adaptado para celular desde o inicio'],
        ['Design dourado', 'Paleta, tipografia e elementos visuais conforme diretrizes'],
    ],
    [45, 145]
)

pdf.chapter_title('Fase 2 - Pos-MVP', 2)
pdf.table(
    ['Funcionalidade', 'Descricao'],
    [
        ['Busca com autocomplete', 'Campo de busca na header'],
        ['Recomendacao', 'Baseada em notas olfativas'],
        ['Avaliacoes e reviews', 'Sistema de comentarios por produto'],
        ['WhatsApp integrado', 'Botao flutuante de contato direto'],
        ['Painel admin', 'Gerenciamento de produtos e pedidos'],
    ],
    [45, 145]
)

# -- 6. ESTRUTURA DO SITE --
pdf.add_page()
pdf.chapter_title('6. Estrutura do Site (Sitemap)', 1)

pdf.chapter_title('Arvore do Site', 2)
sitemap = [
    'Wagner Perfumes',
    '   +-- Home (vitrine principal)',
    '   |   +-- Hero banner (destaque da semana)',
    '   |   +-- Categorias em grid',
    '   |   +-- Produtos em destaque',
    '   |   +-- Newsletter / Contato',
    '   +-- Produtos',
    '   |   +-- Lista com filtros',
    '   |   +-- Pagina individual',
    '   +-- Categorias',
    '   |   +-- Masculino',
    '   |   +-- Feminino',
    '   |   +-- Unissex',
    '   |   +-- Nicho / Premium',
    '   +-- Contato',
    '   +-- Carrinho / Checkout',
]
for line in sitemap:
    indent = 0
    if line.startswith('   +--'):
        indent = 20
    elif line.startswith('   |'):
        indent = 35
    pdf.set_font('Courier', '', 9)
    pdf.set_text_color(50, 50, 50)
    pdf.set_x(15 + (5 if indent > 20 else 0))
    pdf.cell(0, 5, line.strip(), 0, 1)

# -- 7. TECNOLOGIAS --
pdf.add_page()
pdf.chapter_title('7. Tecnologias e Stack', 1)

pdf.table(
    ['Tecnologia', 'Versao', 'Finalidade'],
    [
        ['HTML5', '-', 'Estrutura semantica das paginas'],
        ['CSS3', '-', 'Estilizacao, grid, responsividade'],
        ['JavaScript Vanilla', 'ES6+', 'Interatividade, carrinho, checkout'],
        ['Python', '3.11+', 'Backend leve (API de produtos)'],
        ['Flask', '3.x', 'Servidor web / API REST'],
        ['JSON', '-', 'Dados de produtos em arquivo local'],
        ['Git', '-', 'Controle de versao'],
    ],
    [40, 20, 125]
)

pdf.chapter_title('Por que essa stack?', 2)
pdf.bullet('Zero dependencias pesadas - entrega rapida, sem framework JS complexo')
pdf.bullet('Flask + JSON - backend leve, roda local, facil de subir')
pdf.bullet('Vanilla JS - controle total sobre o design minimalista')
pdf.bullet('Facil de evoluir - pode migrar para React/Vue depois')

# -- 8. ROADMAP --
pdf.add_page()
pdf.chapter_title('8. Roadmap e Proximos Passos', 1)

pdf.table(
    ['Etapa', 'Prazo', 'Descricao'],
    [
        ['1. HTML + CSS', 'Dia 1-2', 'Template homepage, vitrine, produto'],
        ['2. Grid + Categorias', 'Dia 2-3', 'Dados mockados, filtro funcional'],
        ['3. Pagina do produto', 'Dia 3', 'Descricao, imagens, comprar'],
        ['4. Carrinho', 'Dia 4', 'Adicionar/remover, quantidades, total'],
        ['5. Checkout', 'Dia 5', 'Formulario de pedido'],
        ['6. Responsividade', 'Dia 6', 'Testar mobile, polir dourado'],
        ['7. Backend Flask', 'Dia 7-8', 'API de produtos, dados dinamicos'],
        ['8. Revisao', 'Dia 9', 'Testes finais, deploy preview'],
    ],
    [35, 20, 130]
)

pdf.chapter_title('Proxima Acao Sugerida', 2)
pdf.body_text('Criacao do template HTML da Home + CSS base com paleta dourada minimalista.')

# -- APENDICE --
pdf.add_page()
pdf.chapter_title('Apendice: Glossario Visual', 1)

pdf.table(
    ['Elemento', 'Especificacao'],
    [
        ['Borda dourada', 'border: 1px solid #C9A84C'],
        ['Sombra de card', 'box-shadow: 0 2px 12px rgba(201,168,76,0.1)'],
        ['Botao primario', 'background: #C9A84C; color: #FFF'],
        ['Botao hover', 'background: #B8942E'],
        ['Link dourado', 'color: #C9A84C'],
        ['Texto corpo', "font-family: 'Lato', sans-serif; color: #1A1A1A"],
        ['Titulo elegante', "font-family: 'Playfair Display', serif; color: #1A1A1A"],
    ],
    [40, 145]
)

pdf.ln(10)
pdf.set_font('Helvetica', 'I', 9)
pdf.set_text_color(150, 150, 150)
pdf.cell(0, 7, 'Documento gerado em: 13/05/2026 | Versao: 1.0', 0, 1, 'C')
pdf.cell(0, 7, 'Responsavel: Agente Desenvolvedor - JC Infocell', 0, 1, 'C')

# Save
output = r'C:\Dev\_SISTEMAS\WagnerPerfumes\docs\DOCUMENTACAO_PROJETO_Wagner_Perfumes.pdf'
pdf.output(output)
print(f"PDF gerado com sucesso: {output}")
print(f"Tamanho: {os.path.getsize(output)} bytes")
print(f"Paginas: {pdf.page_no()}")
