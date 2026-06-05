# Design System — Especificação reutilizável

Um sistema de produto analítico **minimalista, calmo e confiante**, na linhagem visual de
ferramentas como **Linear.app**, **dashboard da Vercel** e **Notion**. Duas cores por tela
(neutro + 1 acento), bordas finas de 1px, sem gradientes, sem sombras pesadas, sem ícones
"decorativos". Forte hierarquia tipográfica e muito espaço em branco.

> Este documento descreve **apenas o design** (cores, tipografia, espaçamento, componentes,
> motion, acessibilidade). É agnóstico ao produto — use em qualquer contexto.

---

## 1. Bibliotecas e stack

| Camada | Escolha |
|---|---|
| Framework | React 18 |
| Estilização | Tailwind CSS 3 (utility classes; tokens custom no `tailwind.config`) |
| Tipografia | **Inter** (texto/títulos) + **JetBrains Mono** (números, rótulos técnicos, wordmark) — Google Fonts |
| Ícones | SVG line-icons próprios, traço (`stroke`) **1.5**, estilo neutro (sem "sparkle"/mascotes) |
| Gráficos | SVG desenhado à mão (barras horizontais, linhas) — sem dependência pesada |
| Componentes | Primitivos próprios que espelham a API do shadcn/ui (Button, Input, Card, Badge, Select, Slider, Tabs, Tooltip, Toast) |

Mapeamento shadcn/ui (se for reimplementar com a lib):
```
button input label card badge select slider table tabs toast tooltip dialog progress
```

---

## 2. Cores

Paleta de **duas cores por tela**: neutros + um acento. Verde de sucesso é exceção,
usado no máximo uma vez por tela (ex.: destaque do item de topo).

| Token | Hex | Uso |
|---|---|---|
| `page` | `#fafafa` | Fundo da página |
| `white` | `#ffffff` | Fundo de cards / superfícies |
| `ink` | `#1a1a1a` | Texto primário |
| `muted` | `#6b7280` | Texto secundário / legendas |
| `line` | `#e6e6e6` | Bordas (sempre 1px) |
| `accent` | `#5e6ad2` | Acento (botões, foco, links, seleção) |
| `accent-hover` | `#4f5ac0` | Hover do acento |
| `accent-soft` | `#eef0fb` | Fundo suave do acento (badges, realces) |
| `ok` | `#16a34a` | Sucesso — usado com parcimônia |
| `ok-soft` | `#e7f5ec` | Fundo suave de sucesso |
| `danger` | `#dc2626` | Erro / validação |

**Paleta monocromática do acento** (para segmentos de barra / séries de gráfico — um único matiz):
```
#5e6ad2  #7d87de  #9aa2e8  #b9beef  #d3d6f5  #e6e9fa
```
Texto sobre os dois primeiros: branco. Sobre os demais: `ink`.

### Proibições de cor
- **Sem gradientes** — em nada (botões, fundos, heros).
- Máximo de **2 cores por tela** (neutro + acento); verde só 1x por tela.
- Brancos/pretos levemente tonalizados; nada de saturação alta em superfícies.

---

## 3. Tipografia

Fontes: `Inter` (sans) e `JetBrains Mono` (mono).

| Papel | Tamanho / peso | Notas |
|---|---|---|
| H1 | 28px / 600 | `tracking-tight`, `leading-tight` |
| H2 | 20px / 600 | |
| H3 | 16px / 600 | |
| Corpo | 14px / 400 | `line-height: 1.5` |
| Legenda / dica | 13px / 400 | cor `muted` |
| Micro-rótulo | 11–12px / 500 | frequentemente `uppercase` + `tracking-wider` |
| Numérico | mono, `tabular-nums` | valores, percentuais, scores — sempre em JetBrains Mono |

Wordmark/marca: mono, semibold, `tracking-tight`.
Use `text-balance` em frases curtas de destaque e `text-wrap: pretty` em parágrafos.

---

## 4. Espaçamento, raio e sombra

- **Ritmo de espaçamento:** múltiplos de 4px. Paddings principais: `p-6` (24px) ou `p-8` (32px).
- **Raio:** `rounded-lg` = **8px** (inputs, selects); `rounded-xl` = **12px** (cards); `rounded-md` (botões); `rounded-full` (pills, badges, dots).
- **Sombra:** apenas `shadow-sm` (`0 1px 2px 0 rgba(16,24,40,0.04)`). Sem glow, sem elevação Material, sem drop-shadow em camadas.
- **Larguras de leitura:** coluna única `max-w-3xl` (768px); telas com painel lateral `max-w-5xl` (1024px), centralizadas com `mx-auto`.

### Layout
- Prefira **flex/grid com `gap`** para qualquer grupo de elementos irmãos (nunca margens soltas/whitespace inline).
- Em grids com coluna `1fr` + conteúdo largo (tabelas/gráficos), use `min-w-0` no filho para não estourar o contêiner. Evite `minmax(0,1fr)` arbitrário no Tailwind CDN.
- Conteúdo central, responsivo até 360px (mobile) e 1280px+ (desktop).

---

## 5. Motion

- **150ms ease-out** em hover/press. Nada além disso.
- Curva: `cubic-bezier(0.16, 1, 0.3, 1)`.
- Toasts: leve entrada `translateY(-6px) → 0` + fade, 150ms.
- Spinners apenas para recálculo/carregamento (rotação contínua simples).

---

## 6. Componentes

### Button
- **primary:** fundo `accent`, texto branco, sem borda, sem sombra; hover `accent-hover`; foco `ring-2 ring-accent/40`.
- **secondary / outline:** fundo branco, borda 1px `line`, texto `ink`; hover sutil.
- **ghost:** transparente; hover `bg-page`.
- **danger:** texto `danger`; hover fundo vermelho leve.
- Tamanhos: `h-8` (sm), `h-9` (md), `h-10` (lg), `h-9 w-9` (icon). Raio `rounded-md`. Padding `px-4 py-2`.
- Ícone em botão: 16px. Standalone: 20px.

### Input / Select
- Altura **36–40px** (`h-9`), borda 1px `line`, `rounded-lg`, fundo branco.
- Foco: `ring-2 ring-accent/40` + borda `accent`.
- Inválido: borda `danger` + `ring-1 ring-danger/30`.
- Select: chevron 14px à direita, `appearance-none`.
- Inputs numéricos em mono; spinners nativos ocultos.

### Card
- Branco, borda 1px `line`, `rounded-xl`, **sem sombra** no estado padrão.
- Hover interativo (ex.: card clicável): borda vira `accent`, `cursor-pointer` — sem mudança de sombra.

### Badge / pill
- `rounded-full`, 11px, `uppercase`, `tracking-wide`, `whitespace-nowrap`.
- Tons: `muted` (fundo page + borda), `accent` (fundo accent-soft), `ok` (fundo ok-soft).

### Slider (range nativo estilizado)
- Trilha `h-1.5` (6px) `rounded-full`, fundo `line`; trilha ativa em `accent`.
- Thumb: 16px, círculo branco, borda 2px `accent`, `shadow-sm` leve. **Sem glow.**

### Tabs
- Container `p-1`, borda `line`, fundo `page`, `rounded-lg`.
- Aba ativa: fundo branco, borda `line`, `shadow-sm`. Inativa: texto `muted`.

### Tooltip
- Fundo `ink`, texto branco, 12px, `rounded-md`, aparece no hover/focus. Largura máx ~240px.

### Toast
- Topo-direita. Branco, borda 1px `line`, `shadow-sm`. Ícone à esquerda, mensagem, botão de fechar.
- Tons de ícone: `ok` (check), `danger`/`accent` (info). Auto-dismiss ~2.4s.

### Stepper (navegação multi-etapa)
- Dots de 24px conectados por linha 1px.
  - concluído: preenchido `accent`, check branco.
  - atual: borda 1px `accent`, número/texto `accent`.
  - futuro: borda `line`, número `muted`.
- Rótulos abaixo em 12–13px.

### Tabela
- Sem zebra. Apenas bordas de linha 1px (`border-line`).
- Cabeçalho em `muted`, 13px. Linhas clicáveis com hover `bg-page`.
- Números alinhados à direita, mono, `tabular-nums`.

---

## 7. Ícones

Line-icons SVG, `viewBox="0 0 24 24"`, `fill: none`, `stroke: currentColor`, `stroke-width: 1.5`,
`stroke-linecap/linejoin: round`. Conjunto neutro (setas, +, lixeira, check, chevrons, sliders,
download, info, grip, loader, tendências, alvo). **Nunca** ícones que sinalizem "IA"
(sparkle, varinha mágica, arco-íris) e **sem emojis**.

---

## 8. Imagens / placeholders

Quando faltar imagem real, usar placeholder com **listras diagonais sutis** e um rótulo
em monospace descrevendo o conteúdo esperado. Nunca desenhar ilustrações complexas em SVG
à mão; nada de 3D, isométrico ou "blobs" abstratos.

```css
.stripes {
  background-image: repeating-linear-gradient(135deg, #f4f4f5 0 8px, #fafafa 8px 16px);
}
```

---

## 9. Tailwind config (tokens prontos)

```js
tailwind.config = {
  theme: { extend: {
    colors: {
      page: "#fafafa", ink: "#1a1a1a", muted: "#6b7280", line: "#e6e6e6",
      accent: "#5e6ad2", "accent-hover": "#4f5ac0", "accent-soft": "#eef0fb",
      ok: "#16a34a", "ok-soft": "#e7f5ec", danger: "#dc2626",
    },
    fontFamily: {
      sans: ['Inter','ui-sans-serif','system-ui','-apple-system','Segoe UI','Helvetica','Arial','sans-serif'],
      mono: ['"JetBrains Mono"','ui-monospace','SFMono-Regular','Menlo','monospace'],
    },
    borderRadius: { lg: '8px', xl: '12px' },
    boxShadow: { sm: '0 1px 2px 0 rgba(16,24,40,0.04)' },
    transitionTimingFunction: { out: 'cubic-bezier(0.16, 1, 0.3, 1)' },
  }},
};
```

```html
<!-- Fontes -->
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet" />
```

---

## 10. Acessibilidade

Faz parte do design — não é um extra opcional.

- **Label em todo input** (`<label htmlFor>` associado por `id`). Placeholder nunca substitui label.
- **Foco sempre visível** em qualquer interativo: `ring-2 ring-accent/40`. Nunca `outline: none` sem
  um substituto visível.
- **Sliders** expõem `aria-valuemin` / `aria-valuemax` / `aria-valuenow` e um `aria-valuetext`
  legível (ex.: "Peso 42%").
- **Contraste mínimo AA** — a paleta cumpre (`ink` sobre `page`/`white`, `muted` sobre `white`).
- **Estados de erro** anunciados: `aria-invalid` no campo + `aria-describedby` apontando a mensagem.
- **Ordem de tabulação** segue a ordem visual; `Enter` avança ações primárias quando o form é válido.
- **Alvos de toque** ≥ 36px (`h-9`).
- Respeitar **`prefers-reduced-motion`**: desligar transições e spinners para quem pediu menos movimento.

---

## 11. Checklist de fidelidade

- [ ] Sem gradientes, sem emojis, sem ícones "de IA".
- [ ] No máximo 2 cores por tela (neutro + acento); verde 1x.
- [ ] Bordas sempre 1px `#e6e6e6`; raio 8px (inputs) / 12px (cards).
- [ ] Apenas `shadow-sm`; nenhuma elevação pesada.
- [ ] Inter para texto, JetBrains Mono para números/rótulos técnicos.
- [ ] Espaçamento em múltiplos de 4px; conteúdo centralizado e responsivo (360px → 1280px+).
- [ ] Motion só 150ms ease-out em hover/press.
- [ ] Estados de formulário cobertos: vazio, foco, inválido, desabilitado.
- [ ] Acessibilidade: label em todo input, foco visível, contraste AA, `prefers-reduced-motion`.

---

## Apêndice — Snippets de implementação (CSS)

Trechos reutilizáveis para os componentes que não saem prontos do Tailwind. Agnósticos ao produto;
renomeie os prefixos à vontade.

```css
/* Slider nativo estilizado.
   O linear-gradient aqui NÃO é decorativo: pinta só a porção preenchida da trilha
   (uma cor sólida até --p, neutro depois). Ajuste --p via JS conforme o valor. */
.slider {
  -webkit-appearance: none;
  appearance: none;
  width: 100%;
  height: 6px;
  border-radius: 9999px;
  outline: none;
  cursor: pointer;
  background: linear-gradient(
    to right,
    var(--accent) 0%,
    var(--accent) var(--p, 0%),
    var(--line) var(--p, 0%),
    var(--line) 100%
  );
}
.slider:focus-visible { box-shadow: 0 0 0 3px var(--accent-soft); }
.slider::-webkit-slider-thumb,
.slider::-moz-range-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 16px;
  height: 16px;
  border-radius: 9999px;
  background: #fff;
  border: 2px solid var(--accent);
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.08);
  cursor: pointer;
}

/* Tooltip — fundo ink, fade 120ms, ~240px de largura máx. */
.tt { position: relative; }
.tt-pop {
  position: absolute;
  bottom: calc(100% + 6px);
  left: 50%;
  transform: translateX(-50%);
  width: max-content;
  max-width: 240px;
  padding: 6px 8px;
  border-radius: 6px;
  background: var(--ink);
  color: #fff;
  font-size: 11px;
  line-height: 1.3;
  opacity: 0;
  pointer-events: none;
  transition: opacity 120ms ease-out;
  z-index: 60;
}
.tt:hover .tt-pop,
.tt:focus-visible .tt-pop,
.tt:focus-within .tt-pop { opacity: 1; }

/* Toast — entrada sutil. */
.toast-in { animation: toast-slide-in 180ms ease-out; }
@keyframes toast-slide-in {
  from { transform: translateY(-6px); opacity: 0; }
  to   { transform: translateY(0);    opacity: 1; }
}

@media (prefers-reduced-motion: reduce) {
  .tt-pop { transition: none; }
  .toast-in { animation: none; }
}
```
