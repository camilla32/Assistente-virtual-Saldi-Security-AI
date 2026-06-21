import http.server
import socketserver
import json
import csv

PORT = 8000

# =====================================================================
# FUNÇÃO PARA LER OS DADOS DO CLIENTE (Módulo de Dados)
# =====================================================================
def buscar_score_cliente(nome_procurado="Carlos Silva"):
    """
    Procura o cliente no arquivo 'cliente.csv' e retorna o seu score.
    Se o arquivo não existir ou o cliente não for encontrado, retorna um score padrão.
    """
    try:
        with open('cliente.csv', mode='r', encoding='utf-8') as file:
            # Detecta automaticamente se o CSV usa vírgula ou ponto e vírgula
            conteudo = file.read(2048)
            dialeto = csv.Sniffer().sniff(conteudo)
            file.seek(0)
            
            leitor = csv.DictReader(file, dialect=dialeto)
            
            # Normaliza os nomes das colunas para evitar erros de espaços ou maiúsculas
            leitor.fieldnames = [col.strip().lower() for col in leitor.fieldnames]
            
            for linha in leitor:
                # Busca por aproximação ou nome exato na coluna 'nome' ou 'cliente'
                nome_linha = linha.get('nome') or linha.get('cliente') or list(linha.values())[0]
                if nome_linha and nome_procurado.lower() in nome_linha.lower():
                    # Captura o score (procura coluna 'score' ou 'pontuacao')
                    score = linha.get('score') or linha.get('pontuacao')
                    return int(score) if score else 600
    except Exception as e:
        print(f"⚠️ Erro ao ler cliente.csv: {e}. Usando score padrão.")
    
    return 600 # Score padrão de segurança caso não ache no CSV

# =====================================================================
# BASE DE CONHECIMENTO (Expanda aqui para 30/40 perguntas depois)
# =====================================================================
BASE_CONHECIMENTO = {
    "credito_pessoal": "O Crédito Pessoal Bradesco permite parcelamento em até 72x com taxas customizadas para o seu perfil.",
    "seguranca_fraude": "Atenção: O Bradesco NUNCA solicita senhas ou tokens por chat ou telefone. Ative a verificação em duas etapas.",
    "score_baixo": "Para o seu perfil atual, recomendamos linhas com garantia, como o Crédito Consignado, ou regularização de pendências.",
    "score_alto": "Seu perfil possui excelente histórico! Você tem direito a taxas exclusivas a partir de 1.99% a.m. e liberação imediata.",
    "lgpd": "Seus dados estão protegidos sob as diretrizes da LGPD e criptografados de ponta a ponta durante esta simulação."
}

# =====================================================================
# LÓGICA DO AGENTE INTELIGENTE (GenIA Simulada & Validação)
# =====================================================================
def processar_IA(mensagem, score_usuario):
    msg = mensagem.lower().strip()
    
    # 1. Defesa de Cybersegurança
    if any(palavra in msg for palavra in ["senha", "password", "token", "cvv", "cartao"]):
        return (
            "🚨 **ALERTA DE SEGURANÇA:** Detectamos uma tentativa de digitação de dado sensível. "
            "Por motivos de Cybersegurança e LGPD, **nunca** envie senhas. Reformule sua dúvida."
        )

    # 2. Resposta Inteligente baseada em Dados Cruzados (Mensagem + Score do CSV)
    if any(p in msg for p in ["credito", "emprestimo", "dinheiro", "financiar", "simulação", "simulacao"]):
        if score_usuario < 600:
            return (
                f"{BASE_CONHECIMENTO['credito_pessoal']}\n\n"
                f"⚠️ **Análise de Dados:** Identificamos que seu Score atual ({score_usuario}) apresenta restrições para linhas tradicionais. "
                f"{BASE_CONHECIMENTO['score_baixo']}\n\n"
                "**Próxima decisão:** Deseja que eu faça uma simulação na modalidade Consignado?"
            )
        else:
            return (
                f"{BASE_CONHECIMENTO['credito_pessoal']}\n\n"
                f"📊 **Análise de Dados:** Parabéns! Seu Score é de {score_usuario} (Alto Potencial). "
                f"{BASE_CONHECIMENTO['score_alto']}\n\n"
                "**Próxima decisão:** Deseja simular um valor específico (ex: R$ 10.000) agora?"
            )

    if any(p in msg for p in ["segurança", "seguro", "fraude", "vazamento", "lgpd"]):
        return f"{BASE_CONHECIMENTO['seguranca_fraude']}\n\n🔒 **Cybersegurança:** {BASE_CONHECIMENTO['lgpd']}"

    # 3. Tratamento para evitar Alucinação
    return (
        "Desculpe, eu sou um assistente especializado em **Crédito Seguro e Proteção de Dados**. "
        "Não tenho informações suficientes na minha base de conhecimento para responder sobre isso.\n\n"
        "**Como posso te ajudar agora?** Pergunte sobre: 'Como pedir crédito com segurança?' ou 'Qual o impacto do meu Score?'"
    )

# =====================================================================
# SERVIDOR CONTROLLER
# =====================================================================
class CustomHandler(http.server.SimpleHTTPRequestHandler):
    
    def do_GET(self):
        if self.path == '/' or self.path == '/index.html':
            try:
                with open('index.html', 'r', encoding='utf-8') as file:
                    conteudo_html = file.read()
                self.send_response(200)
                self.send_header('Content-Type', 'text/html; charset=utf-8')
                self.end_headers()
                self.wfile.write(conteudo_html.encode('utf-8'))
            except FileNotFoundError:
                self.send_error(404, "Arquivo index.html nao encontrado.")
        else:
            super().do_GET()

    def do_POST(self):
        if self.path.startswith('/api/chat'):
            try:
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length)
                dados_recebidos = json.loads(post_data.decode('utf-8'))
                
                mensagem_usuario = dados_recebidos.get('mensagem', '')
                
                # 🔍 AQUI ESTÁ A MÁGICA: O Python lê o CSV dinamicamente!
                # Altere "Carlos Silva" para testar com outro cliente que esteja no seu arquivo .csv
                score_usuario = buscar_score_cliente("Carlos Silva")
                
                resposta_ia = processar_IA(mensagem_usuario, score_usuario)
                
                self.send_response(200)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.end_headers()
                
                response = {"resposta": resposta_ia}
                self.wfile.write(json.dumps(response, ensure_ascii=False).encode('utf-8'))
                
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                response = {"resposta": f"Erro interno no servidor: {str(e)}"}
                self.wfile.write(json.dumps(response).encode('utf-8'))
        else:
            self.send_error(404)

if __name__ == '__main__':
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
        print(f"🚀 Servidor com integração de Dados (.CSV) ativo!")
        print(f"👉 Acesse: http://localhost:{PORT}")
        httpd.serve_forever()