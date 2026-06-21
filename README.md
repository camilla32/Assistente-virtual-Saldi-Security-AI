# Saldi Security AI - Bradesco Portal Interno 🛡️🤖

O **Saldi Security AI** é um protótipo funcional de assistente virtual (GenIA) integrado a um motor de regras de cybersegurança focado em simulações de crédito seguro. O projeto simula um ambiente de portal interno bancário, demonstrando como agentes de IA podem atuar em conformidade com políticas rígidas de compliance, LGPD e prevenção a fraudes em tempo real.

---

## 🚀 O que o Agente Faz?

O Saldi auxilia o usuário (neste cenário, simulando a cliente *Mariana Almeida*) a consultar dados financeiros e realizar simulações de empréstimos, aplicando camadas automáticas de proteção:

*   **Simulação de Crédito Dinâmica:** Guia o usuário passo a passo (valor, parcelas e confirmação) com base em um perfil analítico simulado.
*   **Modos de Operação (Controle do Funcionário):** Permite alternar a sensibilidade da IA entre os modos *Comercial*, *Alta Segurança (Restritivo)* e *Auditoria/Logs*.
*   **Prevenção contra Prompt Injection / Jailbreak:** Intercepta ativamente tentativas de burlar ou reescrever as regras do sistema através do chat.
*   **Trava Antifraude em Modo Restritivo:** Bloqueia e congela visualmente a interface (alerta vermelho) caso requisições suspeitas estourem os limites de segurança configurados (ex: solicitações acima de R$ 85.000 no modo de Alta Segurança).
*   **Mascaramento de Dados Sensíveis:** Ofusca visualmente dados confidenciais na tela (`[DADO PROTEGIDO]`) como senhas, tokens ou padrões de cartões.
*   **Logs de Auditoria:** Exibe em tempo real o hardening (endurecimento de segurança) das interceptações do motor quando o modo auditoria está ativo.

---

## ⚡ Arquitetura: 100% Serverless & Zero Backend

O grande diferencial deste protótipo é que ele foi projetado para rodar **totalmente no lado do cliente (Client-Side)**.

*   **Sem Backend / Sem Servidor:** Não há necessidade de configurar bancos de dados, APIs externas ou servidores Node.js/Python para testar a interface.
*   **Lógica de IA Simulada:** A árvore de decisão, o fluxo de máquina de estados da simulação e o motor de segurança foram desenvolvidos inteiramente em **JavaScript Vanilla**, rodando direto no motor do navegador.
*   **Portabilidade Máxima:** Toda a experiência — incluindo o design em Glassmorphism, os componentes de Gauge (gráficos) e a inteligência do chat — está contida em um único arquivo estruturado.

> 💡 **Por que essa abordagem?** Isso permite que o projeto seja hospedado instantaneamente em serviços estáticos gratuitos (como GitHub Pages, Vercel ou Netlify) ou aberto localmente com apenas um duplo clique no arquivo, funcionando perfeitamente como um demonstrativo ágil de portfólio.

---

## 🛠️ Tecnologias Utilizadas

*   **HTML5** (Estruturação semântica)
*   **CSS3** (Layout responsivo, variáveis nativas e estilizações neon/glassmorphism)
*   **JavaScript (ES6+)** (Motor de regras de segurança, higienização de inputs e controle de estados)

---

## 📦 Como Rodar o Projeto

1. Faça o clone deste repositório:
```bash
   git clone [https://github.com/camilla32/Assistente-virtual-Saldi-Security-AI.git]
```

2. Navegue até a pasta do projeto e abra o arquivo principal (ex: index.html) diretamente em qualquer navegador web de sua preferência.

   Não é necessário rodar npm install, configurar servidores locais ou injetar chaves de API.
