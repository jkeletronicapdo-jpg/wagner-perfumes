# Documentação do Projeto — Wagner Perfumes

## Webpage de Vendas — E-commerce de Perfumes

---

## Sumário

1. [Visão Geral do Projeto](#1-visão-geral-do-projeto)
2. [Pesquisa de Mercado e Tendências](#2-pesquisa-de-mercado-e-tendências)
3. [Referências e Casos Similares](#3-referências-e-casos-similares)
4. [Diretrizes de Design](#4-diretrizes-de-design)
5. [Escopo Técnico](#5-escopo-técnico)
6. [Estrutura do Site](#6-estrutura-do-site)
7. [Tecnologias e Stack](#7-tecnologias-e-stack)
8. [Roadmap e Próximos Passos](#8-roadmap-e-próximos-passos)

---

## 1. Visão Geral do Projeto

### Cliente
**Wagner Perfumes** — Loja de perfumes entrando no mercado de vendas web.

### Objetivo
Criar uma webpage de vendas profissional, elegante e funcional, que transmita sofisticação através de um design minimalista com letras/acabamentos dourados.

### Público-Alvo
- Consumidores finais que buscam perfumes de qualidade
- Faixa etária: 18–55 anos
- Perfil: valoriza apresentação visual, busca praticidade na compra online
- Dispositivo principal: mobile (80% do tráfego de e-commerce)

### Principais Funcionalidades (Fase 1)
- Vitrine de produtos com categorias
- Carrinho de compras
- Checkout simplificado
- Responsividade mobile-first
- Design minimalista com paleta dourada

---

## 2. Pesquisa de Mercado e Tendências

### E-commerce de Perfumes em 2024–2025

- **80% do tráfego** global de e-commerce vem de smartphones
- Apps mobile têm **taxa de conversão superior** e gastos **10–50% maiores** que sites móveis
- **TikTok #FragranceTok** ultrapassou 278M de publicações — descoberta de fragrâncias migrou para redes sociais
- **IA e ferramentas de recomendação** estão reduzindo o risco da "compra cega" de perfumes online
- **Sustentabilidade** em alta: materiais ecológicos, refis, transparência

### Tendências de Design para Perfumaria de Luxo

| Tendência | Descrição |
|-----------|-----------|
| **Minimalismo** | Pureza, linhas limpas, formas geométricas, cores neutras (bege, off-white, cinza) |
| **Acabamento Dourado** | Detalhes metálicos em logotipos, tipografia e elementos de destaque |
| **Tipografia Serifada** | Fontes elegantes (Didot, Bodoni) com espaçamento generoso |
| **Foto editorial** | Frascos como objetos de arte, fundo limpo, iluminação dramática |
| **Espaço negativo abundante** | Sensação de calma, clareza e exclusividade |
| **Micro-interações sutis** | Hover effects, transições suaves, loading refinados |

---

## 3. Referências e Casos Similares

### Marcas que Inspiram o Projeto

| Marca | Estilo | Destaque |
|-------|--------|----------|
| **Tom Ford** | Luxo minimalista preto & dourado | Design ousado, tipografia refinada |
| **YSL Libre** | Dourado como elemento central | Detalhes dourados em destaque |
| **Dolce & Gabbana** | Sofisticação clássica | Emblemas dourados, artesanal |
| **Miller Harris** | Minimalismo orgânico | Cores pastel, natureza |
| **Hiram Green** | Nicho minimalista | Frascos clean, sem excessos |
| **Le Galion** | Luxury vintage refinado | Tipografia serifada, dourados discretos |

### Características Comuns nos Casos de Sucesso

- ✅ Fundo predominantemente claro (branco, off-white, creme)
- ✅ Destaque dourado em logo, títulos e CTAs
- ✅ Layout limpo com muito espaço em branco
- ✅ Fotografia profissional de alta qualidade
- ✅ Navegação simplificada (poucos itens no menu)
- ✅ Descrições sensoriais e poéticas dos perfumes
- ✅ Mobile-first com adaptação fluida

---

## 4. Diretrizes de Design

### Paleta de Cores

```
Fundo principal:    #FFFFFF (Branco)
Fundo secundário:   #F5F0EB (Off-white / Creme suave)
Texto principal:    #1A1A1A (Preto suave)
Texto secundário:   #6B6B6B (Cinza elegante)
Dourado principal:  #C9A84C (Dourado clássico)
Dourado claro:      #E8D5A3 (Dourado claro / detalhes)
Destaque/CTA:       #B8942E (Dourado escuro / hover)
Acento:             #2C2C2C (Preto elegante para contrastes)
```

### Tipografia

| Uso | Fonte | Peso | Tamanhos |
|-----|-------|------|----------|
| **Logo / Títulos** | Playfair Display (serifa) | Bold / SemiBold | 48px → 28px (mobile) |
| **Subtítulos** | Playfair Display | Regular | 24px → 18px |
| **Corpo / Descrições** | Lato (sans-serif) | Light / Regular | 16px → 14px |
| **Preços / CTAs** | Lato | Bold | 18px → 16px |
| **Navegação** | Lato | Regular | 14px |

### Tom de Voz do Site
- Sofisticado mas acessível
- Descrições sensoriais: "Notas amadeiradas com toque cítrico"
- Evitar texto excessivo — poesia na medida
- Português formal mas caloroso

### Elementos Visuais
- Ícones minimalistas em linha fina (stroke dourado)
- Bordas finas 1px douradas em cards e botões
- Sombras suaves e sutis (box-shadow leve)
- Botões com fill dourado e hover com tom mais escuro
- Fotografia: frascos isolados em fundo branco/creme

---

## 5. Escopo Técnico

### Fase 1 — MVP (Entrega Inicial)

| Funcionalidade | Descrição |
|---------------|-----------|
| ✅ Vitrine de produtos | Grid responsivo com cards de produto |
| ✅ Categorias | Filtro por categoria (Masculino, Feminino, Unissex, Nicho) |
| ✅ Página do produto | Imagem grande, descrição, preço, botão comprar |
| ✅ Carrinho lateral | Slide-in com itens adicionados |
| ✅ Checkout | Formulário simplificado (nome, endereço, pagamento) |
| ✅ Mobile-first | Layout adaptado para celular desde o início |
| ✅ Design dourado | Paleta, tipografia e elementos visuais conforme diretrizes |

### Fase 2 — Pós-MVP

| Funcionalidade | Descrição |
|---------------|-----------|
| ⏳ Busca com autocomplete | Campo de busca na header |
| ⏳ Recomendação de perfumes | Baseada em notas olfativas |
| ⏳ Avaliações e reviews | Sistema de comentários por produto |
| ⏳ WhatsApp integrado | Botão flutuante de contato direto |
| ⏳ Painel admin | Gerenciamento de produtos e pedidos |

---

## 6. Estrutura do Site (Sitemap)

```
Wagner Perfumes
├── Home (vitrine principal)
│   ├── Hero banner (destaque da semana)
│   ├── Categorias em grid
│   ├── Produtos em destaque
│   └── Newsletter / Contato
├── Produtos
│   ├── Lista com filtros
│   └── Página individual
├── Categorias
│   ├── Masculino
│   ├── Feminino
│   ├── Unissex
│   └── Nicho / Premium
├── Contato
└── Carrinho / Checkout
```

### Wireframe Conceitual (Home)

```
┌─────────────────────────────────────────┐
│  [Logo WAGNER PERFUMES]  ☰ Menu   🛒  │  ← Header minimalista
├─────────────────────────────────────────┤
│  ┌───────────────────────────────────┐  │
│  │                                   │  │
│  │   ✦  Fragrância do Mês  ✦        │  │  ← Hero dourado
│  │   Nome do Perfume                 │  │
│  │   [Descubra →]                    │  │
│  │                                   │  │
│  └───────────────────────────────────┘  │
├─────────────────────────────────────────┤
│  Categorias                             │
│  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐     │  ← Grid limpo
│  │Masc │ │Fem  │ │Uni  │ │Nicho│     │
│  └─────┘ └─────┘ └─────┘ └─────┘     │
├─────────────────────────────────────────┤
│  Mais Vendidos                         │
│  ┌──┐ ┌──┐ ┌──┐ ┌──┐                  │  ← Cards com borda
│  │  │ │  │ │  │ │  │                  │     dourada fina
│  └──┘ └──┘ └──┘ └──┘                  │
├─────────────────────────────────────────┤
│  ✉  Receba novidades                   │  ← Newsletter
├─────────────────────────────────────────┤
│  © Wagner Perfumes  │  Redes Sociais   │  ← Footer clean
└─────────────────────────────────────────┘
```

---

## 7. Tecnologias e Stack

| Tecnologia | Versão | Finalidade |
|-----------|--------|------------|
| **HTML5** | — | Estrutura semântica das páginas |
| **CSS3** | — | Estilização, grid, responsividade |
| **JavaScript (Vanilla)** | ES6+ | Interatividade, carrinho, checkout |
| **Python 3.11** | 3.11+ | Backend leve (API de produtos) |
| **Flask** | 3.x | Servidor web / API REST |
| **JSON** | — | Dados de produtos em arquivo local |
| **Git** | — | Controle de versão |

### Por que essa stack?
- **Zero dependências pesadas** — entrega rápida, sem framework JS complexo
- **Flask + JSON** — backend leve, roda local, fácil de subir
- **Vanilla JS** — controle total sobre o design minimalista
- **Fácil de evoluir** — pode migrar para React/Vue depois se precisar

---

## 8. Roadmap e Próximos Passos

### Etapas

| Etapa | Prazo Estimado | Descrição |
|-------|---------------|-----------|
| **1. Estrutura HTML + CSS** | Dia 1–2 | Template da homepage, vitrine, produto |
| **2. Grid de produtos + categorias** | Dia 2–3 | Dados mockados, filtro funcional |
| **3. Página do produto** | Dia 3 | Descrição, imagens, comprar |
| **4. Carrinho de compras** | Dia 4 | Adicionar/remover, quantidades, preço total |
| **5. Checkout** | Dia 5 | Formulário de pedido |
| **6. Responsividade + ajustes finos** | Dia 6 | Testar mobile, polir dourado |
| **7. Backend (Flask)** | Dia 7–8 | API de produtos, servir dados dinâmicos |
| **8. Revisão e entrega** | Dia 9 | Testes finais, deploy preview |

### Próxima ação sugerida
Criação do **template HTML da Home + CSS base** com paleta dourada minimalista.

---

## Apêndice: Glossário Visual

| Elemento | Especificação |
|----------|--------------|
| Borda dourada | `border: 1px solid #C9A84C` |
| Sombra de card | `box-shadow: 0 2px 12px rgba(201,168,76,0.1)` |
| Botão primário | `background: #C9A84C; color: #FFF; border: none` |
| Botão hover | `background: #B8942E` |
| Link dourado | `color: #C9A84C; text-decoration: none` |
| Texto corpo | `font-family: 'Lato', sans-serif; color: #1A1A1A` |
| Título elegante | `font-family: 'Playfair Display', serif; color: #1A1A1A` |

---

> **Documento gerado em:** 13/05/2026
> **Versão:** 1.0
> **Responsável:** Agente Desenvolvedor — JC Infocell
