# -*- coding: utf-8 -*-
import csv, datetime, io, sys
from collections import OrderedDict

Y=2026
def d(s):
    dd,mm=s.split('/'); return datetime.date(Y,int(mm),int(dd))
WD=['seg','ter','qua','qui','sex','sáb','dom']
def fmt(x): return x.strftime('%d/%m') + ' ' + WD[x.weekday()]
def iso(x): return x.strftime('%Y-%m-%d')

T=[]  # lista de tarefas
def t(id, frente, resp, tarefa, ini, ent, rev, dep='', prio='Normal', obs=''):
    T.append(OrderedDict(
        id=id, frente=frente, tarefa=tarefa, resp=resp,
        ini=d(ini) if ini else None, ent=d(ent), rev=d(rev) if rev else None,
        dep=dep, prio=prio, obs=obs))

# =====================================================================
# F0 — DECISÕES E DADOS QUE DESTRAVAM O RESTO
# =====================================================================
F='0. Decisões e dados'
t('F0.1',F,'Isadora','Levantar o preço de tabela dos 11 cursos (nome oficial + valor cheio de cada um)','25/09','28/09','28/09','', 'Urgente','BLOQUEIA a oferta, a página de vendas, o pitch e a escada de anos. Item nº 1 do plano.')
t('F0.2',F,'Hugo','Exportar as 3 listas sem sobreposição: (a) anuidade PHI ativa, (b) mensalistas PHI ativos, (c) compradores de cursos sem PHI','25/09','30/09','30/09','','Urgente','Regra: vínculo mais profundo com o PHI ganha. Uma pessoa não pode aparecer em duas listas.')
t('F0.3',F,'Hugo','Contar mensalistas ativos do PHI e informar o número','25/09','28/09','28/09','','Urgente','Maior alavanca de receita não dimensionada da campanha.')
t('F0.4',F,'Hugo','Levantar o custo de disparo por API (por mensagem e por lista)','25/09','30/09','30/09','','Alta','Define se a operação de alunos cabe no orçamento.')
t('F0.5',F,'Kalinne','Confirmar com o Robson: 1 ano de PHI em todas as ofertas e 2 anos só para a turma de setembro','25/09','28/09','','','Urgente','')
t('F0.6',F,'Kalinne','Decidir se a camiseta da Black fica ou sai do escopo','25/09','29/09','','','Alta','Se ficar, a arte precisa estar pronta em 07/10 para dar tempo de produção física.')
t('F0.7',F,'Isadora','Reunião de concepção com o time inteiro','29/09','29/09','','F0.1','Urgente','Fecha oferta, preços, verba, responsáveis e o calendário de gravações.')
t('F0.8',F,'Kalinne','Definir o escopo do Agente de IA (o que ele responde, com base em quê, como o comprador acessa)','29/09','02/10','','F0.7','Alta','Sem escopo fechado o Hugo não começa. É o entregável mais arriscado do plano.')
t('F0.9',F,'Kalinne','Definir o bônus dos 30 primeiros (hoje está A DEFINIR no documento)','29/09','09/10','','F0.7','Alta','Precisa entrar no roteiro do trailer e nos criativos de captação.')
t('F0.10',F,'Kalinne + Henri','Montar a escada de anos com os números reais (2, 3 e 5 anos)','29/09','01/10','02/10','F0.1','Urgente','Entra na página de vendas e no pitch da aula magna.')
t('F0.11',F,'Hugo','Definir a regra de cancelamento da recorrência mensal no checkout do grupo 2','01/10','07/10','07/10','F0.2','Alta','Se falhar, o mensalista é cobrado duas vezes: perde-se o cliente e ganha-se um reembolso.')
t('F0.12',F,'Isadora','Bloquear a agenda do Robson até dezembro (FLS, aulas extras, 2 gravações, ensaio, 2 aulas magnas)','25/09','29/09','','','Urgente','')

# =====================================================================
# F1 — IDENTIDADE VISUAL DA BLACK (não existe hoje — nasce do zero)
# =====================================================================
F='1. Identidade visual da Black'
t('F1.1',F,'Kalinne','Briefing de identidade da Black: tom, referências, o que NÃO pode parecer','25/09','28/09','','','Urgente','A Black é de literatura clássica para pais católicos — não pode virar varejo genérico.')
t('F1.2',F,'Maytte','Logo/selo da Black Friday Robson Cardenas — 3 propostas','29/09','01/10','02/10','F1.1','Urgente','BLOQUEIA todo o design: criativos, páginas, cards, banner dos cortes, camiseta.')
t('F1.3',F,'Maytte','Paleta, tipografia e regras de aplicação','29/09','01/10','02/10','F1.1','Urgente','')
t('F1.4',F,'Maytte','Banner de encerramento dos cortes (o selo que fecha cada vídeo da linha editorial)','05/10','05/10','05/10','F1.2','Alta','Entra nos cortes a partir de 06/10. Os cortes da 1ª semana sobem sem banner — fase 1 não tem CTA mesmo.')
t('F1.5',F,'Maytte','Kit de templates: story, feed, thumb do YouTube, capa de grupo, moldura de corte','05/10','07/10','07/10','F1.2','Alta','Sem o kit, cada peça vira trabalho do zero.')
t('F1.6',F,'Maytte','Arte da camiseta da Black','05/10','07/10','07/10','F1.2 · F0.6','Normal','Só se a camiseta ficar no escopo.')
t('F1.7',F,'Isadora','Encomendar a camiseta da Black (produção física)','08/10','09/10','','F1.6','Normal','Prazo de gráfica + entrega. Robson usa em todo story a partir de 20/10.')

# =====================================================================
# F2 — COPY (Henri)
# =====================================================================
F='2. Copy — Henri'
t('F2.1',F,'Henri','Mensagem de agradecimento + promessa à turma de setembro (sem preço, sem data)','25/09','25/09','25/09','','Urgente','Dispara 28/09 junto com o fechamento do carrinho do PHI. Mata por 6 semanas o medo de "comprei cedo e me ferrei".')
t('F2.2',F,'Henri','Roteiros do Corredor Polonês fase 1 — lote 1 (3 peças, semana de 29/09)','25/09','28/09','28/09','','Urgente','SEM CTA. Entrega solução de verdade. Vídeos de até 3 minutos.')
t('F2.3',F,'Henri','Roteiros fase 1 — lote 2 (5 peças, semana de 05/10)','29/09','01/10','02/10','F2.2','Alta','')
t('F2.4',F,'Nayara + Henri','Roteiros fase 1 — lote 3 (5 peças, semana de 13/10)','05/10','08/10','09/10','F2.3','Alta','')
t('F2.5',F,'Nayara + Henri','Roteiros fase 1 — lote 4 (5 peças, semana de 19/10)','12/10','15/10','16/10','F2.4','Alta','')
t('F2.6',F,'Henri','Roteiro do Trailer Hollywood (revela 09/11)','05/10','07/10','08/10','F0.7','Urgente','Grava em 13-14/10, sobe 20/10. É a peça que abre a campanha.')
t('F2.7',F,'Henri','Roteiro do Pronunciamento Oficial','05/10','09/10','09/10','F0.7','Alta','Grava em 13-14/10, sobe 28/10.')
t('F2.8',F,'Henri','Copy da página de captura','05/10','06/10','07/10','F0.7','Urgente','Destrava o layout da Maytte. É o primeiro elo da corrente da página.')
t('F2.9',F,'Henri','Briefing dos 30 criativos de captação: ângulos, dores e promessas','29/09','02/10','05/10','F0.7','Alta','Só não alunos — não há tráfego para alunos.')
t('F2.10',F,'Henri','Copy dos criativos de captação — lote 1 (15 peças)','06/10','08/10','09/10','F2.9','Alta','5 roteiros de vídeo + 5 imagens elaboradas + 5 nativas.')
t('F2.11',F,'Henri','Copy dos criativos de captação — lote 2 (15 peças)','09/10','13/10','14/10','F2.10','Alta','')
t('F2.12',F,'Henri','Roteiro do Manifesto','12/10','16/10','19/10','','Alta','Grava em 26-27/10, sobe 03/11.')
t('F2.13',F,'Henri','Roteiros do Corredor Polonês fase 2 — lote 1 (quebra de objeção + prova social)','12/10','16/10','19/10','','Alta','COM CTA. Roda junto com a captação.')
t('F2.14a',F,'Henri','Copy da página de vendas — PARTE 1: os 11 cursos, um a um, com nome, capa e preço','29/09','07/10','08/10','F0.1','Urgente','Quebrei em duas entregas de propósito: esta parte é o grosso da página e não depende dos argumentos de preço. Destrava o layout da Maytte uma semana antes.')
t('F2.14b',F,'Henri','Copy da página de vendas — PARTE 2: a escada de anos, os 3 argumentos de preço, bônus e fechamento','08/10','14/10','15/10','F2.14a · F0.10','Urgente','Entra no layout já em andamento. Aqui moram os R$ 58,20 do mensalista — o argumento mais forte da campanha.')
t('F2.15',F,'Henri','Sequência API + e-mail — captação GERAL (não alunos)','08/10','14/10','15/10','F2.8','Alta','Entra no ar 26/10.')
t('F2.16',F,'Henri','Sequência API + e-mail — captação ALUNOS (grupo B, R$ 1.497)','16/10','19/10','20/10','F2.14b','Urgente','Alunos não recebem tráfego: esta sequência É a campanha deles.')
t('F2.17',F,'Henri','Sequência API + e-mail — RENOVAÇÃO grupo A (turma de setembro, R$ 997)','16/10','21/10','22/10','F2.14b','Alta','Tom de privilégio, nominal, um a um. Não pode soar como campanha.')
t('F2.18',F,'Henri','Roteiros fase 2 — lote 2','19/10','23/10','26/10','F2.13','Normal','')
t('F2.19',F,'Henri','Sequências de comparecimento — 3 versões (grupo A, alunos, geral)','16/10','22/10','23/10','F2.14b','Alta','')
t('F2.20',F,'Henri','Briefing e copy dos 30 criativos de carrinho aberto','16/10','22/10','23/10','F2.14b','Alta','Rodam a partir de 09/11.')
t('F2.21',F,'Henri','Script da aula de alunos (05/11), com os 30 min de pitch dos 11 cursos','19/10','29/10','30/10','F2.14b','Urgente','')
t('F2.22',F,'Henri','Script da aula magna geral (09/11)','19/10','29/10','30/10','F2.14b','Urgente','')
t('F2.23',F,'Henri','FAQ e respostas prontas do suporte (inclui a resposta se o link do grupo A vazar)','22/10','29/10','30/10','F2.14b','Alta','')
t('F2.24',F,'Henri','Sequência de carrinho aberto (10 a 16/11)','02/11','05/11','06/11','F2.22','Alta','')
t('F2.25',F,'Henri','Sequência de virada de lote — 3 dias de urgência, até 10 mensagens/dia','09/11','11/11','12/11','F2.24','Normal','Dispara quando o CPA subir, não em data fixa.')
t('F2.26',F,'Henri','Copy do Combo de Natal','16/11','27/11','30/11','','Normal','')

# =====================================================================
# F3 — DESIGN (Maytte)
# =====================================================================
F='3. Design — Maytte'
t('F3.1',F,'Maytte','Capas dos 11 cursos do acervo','05/10','13/10','13/10','F1.2 · F0.1','Urgente','Cada curso precisa aparecer com nome, capa e preço. Sem isso o pitch dos cursos não existe.')
t('F3.2',F,'Maytte','Card/motion de anúncio da Black — 2 versões (sem data e com data)','05/10','08/10','09/10','F1.2','Alta','A versão sem data roda no orgânico; a com data entra depois do trailer.')
t('F3.3',F,'Maytte','Layout da página de captura','09/10','13/10','14/10','F2.8 · F1.5','Urgente','Só começa com a copy APROVADA.')
t('F3.4',F,'Maytte','10 criativos de imagem ELABORADA — captação','15/10','20/10','20/10','F2.11','Alta','')
t('F3.5',F,'Maytte','10 criativos de imagem NATIVA — captação','15/10','21/10','21/10','F2.11','Alta','Estética de celular, sem cara de anúncio.')
t('F3.6',F,'Maytte','Layout da página de vendas (11 cursos + escada de anos + 3 blocos de preço)','14/10','20/10','20/10','F2.14a · F3.1','Urgente','Só começa com a copy APROVADA e as capas prontas.')
t('F3.6b',F,'Maytte','Ajustar o layout da página de vendas com o bloco de preço aprovado','21/10','21/10','21/10','F2.14b · F3.6','Urgente','')
t('F3.7',F,'Maytte','Diagramação do PDF Plano de Leitura por Idade','16/10','23/10','26/10','F1.5','Normal','É item da oferta — precisa existir antes de 05/11.')
t('F3.8',F,'Maytte','Cards dos FLS semanais (6 edições) e das 2 aulas extras de alunos','08/10','13/10','13/10','F1.5','Normal','Entrega em lote, um por semana no ar.')
t('F3.9',F,'Maytte','Artes de comparecimento e stories das aulas magnas','26/10','29/10','30/10','F1.5','Alta','')
t('F3.10',F,'Maytte','10 criativos de imagem ELABORADA — carrinho aberto','26/10','29/10','29/10','F2.20','Alta','')
t('F3.11',F,'Maytte','10 criativos de imagem NATIVA — carrinho aberto','26/10','30/10','30/10','F2.20','Alta','')
t('F3.12',F,'Maytte','Artes de virada de lote (novo preço, urgência)','13/11','17/11','18/11','F2.25','Normal','')
# =====================================================================
# F4 — WEB (Ericson)
# =====================================================================
F='4. Web — Ericson'
t('F4.1',F,'Ericson','Implementar a página de captura','15/10','19/10','20/10','F3.3','Urgente','')
t('F4.2',F,'Ericson','Integrar a página de captura com o ManyChat e o Funnel (captura de nome, e-mail e WhatsApp)','21/10','21/10','21/10','F4.1 · F5.5','Urgente','')
t('F4.3',F,'Ericson','Página de obrigado + redirecionamento para o grupo de WhatsApp','21/10','21/10','21/10','F4.1 · F5.8','Alta','')
t('F4.4',F,'Ericson','Teste ponta a ponta da captura: mobile, desktop, formulário, redirect, chegada no ManyChat','22/10','22/10','22/10','F4.2 · F4.3','Urgente','PÁGINA DE CAPTURA PRONTA. Captação abre 26/10 — 1 dia útil de folga.')
t('F4.5',F,'Ericson','Implementar a página de vendas (uma página, 3 preços conforme a origem do acesso)','21/10','27/10','27/10','F3.6b','Urgente','A lógica de preço por origem é o ponto técnico mais delicado da campanha.')
t('F4.6',F,'Ericson','Ligar os botões da página aos 3 checkouts (R$ 1.997 / R$ 1.497 / R$ 997 privado)','28/10','28/10','28/10','F4.5 · F5.1','Urgente','')
t('F4.7',F,'Ericson','Pixel, eventos de conversão e UTMs em todas as páginas','28/10','29/10','29/10','F4.5','Alta','Combinar os eventos com o Apoena antes de subir.')
t('F4.8',F,'Ericson','Teste ponta a ponta da venda: os 3 caminhos de preço, compra real de teste, entrega do acesso','30/10','30/10','30/10','F4.6 · F5.3','Urgente','PÁGINA DE VENDAS PRONTA. Black de alunos é 05/11 — 3 dias úteis de folga.')
t('F4.9',F,'Ericson','Colocar a página de vendas em modo virada de lote (troca de preço sem republicar)','28/10','06/11','09/11','F4.5','Normal','')
t('F4.10',F,'Ericson','Monitoramento das páginas nos dias de abertura (05/11 e 09/11)','05/11','09/11','','F4.8','Urgente','De plantão nas duas noites de aula magna.')

# =====================================================================
# F5 — INFRA (Hugo)
# =====================================================================
F='5. Infra — Hugo'
t('F5.1',F,'Hugo','Configurar os 3 checkouts: R$ 1.997 (geral), R$ 1.497 (alunos), R$ 997 (grupo A, privado)','05/10','20/10','21/10','F0.2','Urgente','O do grupo A não pode ser indexável nem acessível por link público óbvio.')
t('F5.2',F,'Hugo','Regra de cancelamento automático da recorrência mensal na compra do grupo 2','22/10','27/10','28/10','F0.11 · F5.1','Urgente','Somar o saldo do mês em curso ao ano novo.')
t('F5.3',F,'Hugo','Entrega automática dos acessos: acervo vitalício + PHI (1 ou 2 anos) + acesso duplo do cônjuge','22/10','28/10','29/10','F5.1','Urgente','O acesso duplo precisa de um caminho para a pessoa cadastrar o cônjuge.')
t('F5.4',F,'Hugo','Aprovar a 2ª BM e o 2º número na Salvy, e aquecer','29/09','20/10','22/10','','Urgente','Risco de queda da API no dia da abertura. Redundância obrigatória.')
t('F5.5',F,'Hugo','ManyChat — fluxo de captação GERAL (não alunos)','16/10','20/10','20/10','F2.15','Urgente','')
t('F5.6',F,'Hugo','ManyChat — fluxo de captação ALUNOS (grupo B)','21/10','26/10','27/10','F2.16','Urgente','Sem tráfego para alunos, este fluxo é a campanha inteira deles.')
t('F5.7',F,'Hugo','ManyChat — fluxo nominal da RENOVAÇÃO (grupo A, 21 pessoas)','23/10','29/10','30/10','F2.17','Alta','Disparo um a um, com o nome da pessoa. Não é lista, é mensagem.')
t('F5.8',F,'Hugo','Criar e configurar os grupos de WhatsApp (FLS + captação geral + captação alunos)','29/09','15/10','16/10','','Alta','O grupo do FLS #1 precisa existir já em 29/09.')
t('F5.9',F,'Hugo','Reativar os grupos antigos e limpar números inválidos','05/10','15/10','16/10','','Alta','')
t('F5.10',F,'Hugo','Funnel — importar as 3 listas e montar as automações de e-mail','16/10','22/10','23/10','F0.2 · F2.15','Alta','')
t('F5.11',F,'Hugo','ManyChat + Funnel — sequências de comparecimento das 3 frentes','29/10','03/11','04/11','F2.19','Alta','')
t('F5.12',F,'Hugo','Estrutura técnica da virada de lote (subir R$ 250 sem quebrar link)','26/10','04/11','05/11','F5.1','Alta','')
t('F5.13',F,'Hugo','Liberar boleto parcelado no checkout (ativa 16/11)','09/11','13/11','16/11','F5.1','Normal','')
t('F5.14',F,'Hugo','Fila de recuperação: boleto pendente, carrinho abandonado, cartão recusado','26/10','03/11','04/11','F5.1','Alta','')
t('F5.15',F,'Hugo','Plantão técnico nas aberturas (05/11 e 09/11)','05/11','09/11','','F5.3','Urgente','')

# =====================================================================
# F6 — AGENTE DE IA (Hugo — frente separada por ser construção nova)
# =====================================================================
F='6. Agente de IA — Hugo'
t('F6.1',F,'Hugo + Kalinne','Escolher a ferramenta e desenhar a arquitetura do agente','05/10','07/10','08/10','F0.8','Alta','Construção do zero. É o entregável mais arriscado do plano.')
t('F6.2',F,'Nayara','Selecionar o material do acervo que vira base de conhecimento do agente','05/10','16/10','19/10','F0.8','Alta','O agente responde "como o Robson" — a base define se ele soa como ele ou não.')
t('F6.3',F,'Hugo','Preparar a base: transcrever, limpar e estruturar o material selecionado','20/10','26/10','27/10','F6.2','Alta','')
t('F6.4',F,'Hugo','Construir e configurar o agente','28/10','03/11','04/11','F6.1 · F6.3','Alta','')
t('F6.5',F,'Kalinne + Robson','Teste do agente com 30 perguntas reais de pais','04/11','04/11','04/11','F6.4','Urgente','Se ele responder errado sobre formação de filhos, o dano é de reputação, não de conversão.')
t('F6.6',F,'Hugo','Ajustes finais e fluxo de entrega do acesso ao comprador','04/11','05/11','05/11','F6.5','Urgente','Precisa estar no ar na aula de alunos, 05/11 20h30.')

# =====================================================================
# F7 — TRÁFEGO (Apoena) — só não alunos
# =====================================================================
F='7. Tráfego — Apoena'
t('F7.1',F,'Apoena','Montar a estrutura de campanhas, públicos e exclusões (alunos excluídos de TODA a mídia)','01/10','07/10','08/10','F0.2','Urgente','Alunos não recebem tráfego. Se um aluno vir o anúncio de R$ 1.997, a oferta de R$ 1.497 morre.')
t('F7.2',F,'Apoena','Subir a campanha do Corredor Polonês fase 1 (público quente, verba R$ 1.500)','29/09','01/10','','','Alta','Roda de 29/09 a 19/10.')
t('F7.3',F,'Apoena','Subir a campanha do Funil de Live Semanal (verba R$ 1.500)','29/09','01/10','','','Alta','')
t('F7.4',F,'Apoena','Subir a campanha do Trailer','16/10','19/10','','F7.1','Alta','Trailer sobe 20/10.')
t('F7.5',F,'Apoena','Montar e subir a campanha de captação (15 dias, verba R$ 10.500)','22/10','23/10','','F3.4 · F3.5 · F8.9 · F4.4','Urgente','Criativos na mão 2 dias antes. Abre 26/10.')
t('F7.6',F,'Apoena','Subir a campanha do Corredor Polonês fase 2 (verba menor, público já captado)','20/10','23/10','','F2.13','Normal','')
t('F7.7',F,'Apoena','Relatório diário de CPL e volume de leads durante a captação','26/10','09/11','','F7.5','Alta','Gatilho para subir verba se o CPL não estourar.')
t('F7.8',F,'Apoena','Campanha jato das duas aberturas (05/11 e 09/11)','02/11','04/11','','F7.5','Urgente','')
t('F7.9',F,'Apoena','Campanha de carrinho aberto','04/11','06/11','','F3.10 · F3.11','Alta','Ativa 09/11.')
t('F7.10',F,'Apoena','Pausar tráfego de captação na semana do varejo (24 a 30/11)','20/11','23/11','','F7.9','Normal','A maré da Black do varejo é de graça — só API, e-mail, grupos e stories.')

# =====================================================================
# F8 — VÍDEO (Jota + Editor 2)
# =====================================================================
F='8. Vídeo — Jota e Editor 2'
t('F8.1',F,'Jota','Cortes do Corredor Polonês fase 1 — lote 1 (3 peças)','29/09','30/09','30/09','F2.2 · F9.3','Urgente','Sobem sem banner da Black: a identidade só fica pronta em 02/10 e a fase 1 não tem CTA mesmo.')
t('F8.2',F,'Jota','Cortes fase 1 — lote 2 (5 peças, com banner)','06/10','08/10','08/10','F2.3 · F1.4','Alta','')
t('F8.3',F,'Jota','Cortes fase 1 — lote 3 (5 peças)','12/10','14/10','14/10','F2.4','Alta','')
t('F8.4',F,'Jota','Cortes fase 1 — lote 4 (5 peças)','19/10','21/10','21/10','F2.5','Alta','')
t('F8.5',F,'Jota','Editar o Trailer Hollywood','15/10','16/10','16/10','F9.1','Urgente','Gravação termina 14/10. Ajustes 19/10, sobe 20/10. É o gargalo mais apertado da campanha.')
t('F8.6',F,'Jota','Ajustes finais do Trailer','19/10','19/10','19/10','F8.5','Urgente','')
t('F8.7',F,'Editor 2','Editar o Pronunciamento Oficial','15/10','21/10','21/10','F9.1','Alta','Sobe 28/10.')
t('F8.8',F,'Editor 2','10 criativos em VÍDEO — captação — lote 1 (5)','15/10','19/10','20/10','F2.10 · F9.1','Alta','')
t('F8.9',F,'Editor 2','10 criativos em VÍDEO — captação — lote 2 (5)','15/10','21/10','21/10','F2.10 · F9.1','Alta','')
t('F8.10',F,'Jota','Cortes do Corredor Polonês fase 2 — lote 1 (5 peças)','20/10','22/10','22/10','F2.13','Alta','')
t('F8.11',F,'Jota','Editar o Manifesto','28/10','29/10','29/10','F9.2','Urgente','Gravação 26-27/10. Ajustes 30/10, sobe 03/11.')
t('F8.12',F,'Jota','Ajustes finais do Manifesto','30/10','30/10','30/10','F8.11','Urgente','')
t('F8.13',F,'Editor 2','Vídeos de comparecimento das 3 frentes','28/10','30/10','02/11','F2.19 · F9.2','Alta','')
t('F8.14',F,'Jota','Cortes fase 2 — lote 2 (5 peças)','26/10','30/10','02/11','F2.18','Normal','')
t('F8.15',F,'Editor 2','10 criativos em VÍDEO — carrinho aberto','28/10','04/11','05/11','F2.20 · F9.2','Alta','Ativam 09/11.')
t('F8.16',F,'Jota','Cortar os melhores momentos das aulas magnas para o carrinho aberto','10/11','13/11','16/11','','Normal','')

# =====================================================================
# F9 — ROBSON / CONTEÚDO (Nayara)
# =====================================================================
F='9. Conteúdo e Robson — Nayara'
t('F9.1',F,'Isadora + Nayara','GRAVAÇÃO 1 — trailer, pronunciamento e criativos de captação','13/10','14/10','','F2.6 · F2.7 · F2.9','Urgente','Dois dias inteiros. Checklist de cenas fechado em 12/10: nada pode faltar, não há segunda chance antes de 20/10.')
t('F9.2',F,'Isadora + Nayara','GRAVAÇÃO 2 — manifesto, comparecimento e criativos de carrinho','26/10','27/10','','F2.12 · F2.19 · F2.20','Urgente','26/10 é o mesmo dia que abre a captação geral. Robson grava o dia inteiro; a abertura é do time.')
t('F9.3',F,'Nayara','Selecionar trechos do acervo para a linha editorial — lote 1 (timestamps + tema)','25/09','28/09','28/09','','Urgente','É o combustível da fase 1. Sem seleção, o Jota não edita.')
t('F9.4',F,'Nayara','Selecionar trechos do acervo — lotes semanais (5 por semana, até 19/10)','29/09','16/10','','F9.3','Alta','Entrega toda quinta para o lote da semana seguinte.')
t('F9.5',F,'Nayara','Calendário editorial de feed e stories até dezembro','29/09','02/10','02/10','','Alta','')
t('F9.6',F,'Nayara','Orgânico começa a falar de Black Friday, sem data','29/09','29/09','','','Urgente','')
t('F9.7',F,'Nayara','Stories diários de aquecimento e bastidores','29/09','09/11','','','Alta','Tarefa recorrente. Robson de camiseta da Black a partir de 20/10.')
t('F9.8',F,'Nayara','Publicar os cortes da fase 1 no feed e no YouTube','01/10','19/10','','F8.1','Alta','Recorrente, 3 a 5 por semana.')
t('F9.9',F,'Nayara','Publicar os conteúdos da fase 2','23/10','09/11','','F8.10','Alta','Recorrente.')
t('F9.10',F,'Isadora','Confirmar os professores convidados dos FLS #3 (13/10) e #5 (27/10)','29/09','06/10','','','Alta','')
t('F9.11',F,'Isadora','Ensaio da aula magna com o Robson','04/11','04/11','','F2.21 · F2.22','Urgente','Roda o pitch dos 11 cursos inteiro, com a apresentação na tela.')

# =====================================================================
# F10 — COMERCIAL E SUPORTE
# =====================================================================
F='10. Comercial e suporte'
t('F10.1',F,'Isadora','Treinar o suporte nos 3 preços e na regra de classificação','02/11','03/11','04/11','F2.23','Alta','Todo mundo do suporte precisa saber responder por que existem 3 preços.')
t('F10.2',F,'Isadora','Escalar plantão de suporte para as noites de 05/11 e 09/11','04/11','04/11','','F10.1','Alta','')
t('F10.3',F,'Isadora','Operar a fila de recuperação: boleto, abandono e cartão recusado','05/11','16/11','','F5.14','Alta','Começa junto com a primeira abertura.')
t('F10.4',F,'Isadora','Conferir diariamente se os acessos estão sendo entregues corretamente','05/11','16/11','','F5.3','Urgente','Erro de entrega de acesso vira reembolso e reclamação pública.')

# =====================================================================
# VALIDAÇÃO
# =====================================================================
byid={x['id']:x for x in T}
erros=[]
for x in T:
    if x['dep']:
        for dp in [s.strip() for s in x['dep'].split('·')]:
            if dp not in byid: erros.append(f"{x['id']}: dependência inexistente {dp}"); continue
            p=byid[dp]
            libera = p['rev'] or p['ent']
            if x['ini'] and x['ini'] < libera:
                erros.append(f"{x['id']} ({x['tarefa'][:40]}) começa {fmt(x['ini'])} mas {dp} só libera {fmt(libera)}")
    if x['ent'] and x['ent'].weekday()>=5 and x['id'] not in ('F9.1',):
        erros.append(f"{x['id']}: entrega em fim de semana ({fmt(x['ent'])})")
    if x['rev'] and x['rev'].weekday()>=5:
        erros.append(f"{x['id']}: revisão em fim de semana ({fmt(x['rev'])})")
    if x['ini'] and x['ent'] and x['ini']>x['ent']:
        erros.append(f"{x['id']}: início depois da entrega")
    if x['rev'] and x['ent'] and x['rev']<x['ent']:
        erros.append(f"{x['id']}: revisão antes da entrega")

print(f"TAREFAS: {len(T)}")
if erros:
    print(f"\n!!! {len(erros)} PROBLEMAS:")
    for e in erros: print("  -",e)
else:
    print("OK — nenhuma dependência violada, nenhum prazo em fim de semana.")

# carga por responsável
from collections import Counter
c=Counter()
for x in T:
    for r in x['resp'].split(' + '): c[r]+=1
print("\nCARGA:", dict(c.most_common()))

import pickle
pickle.dump(T, open('/tmp/claude-0/-home-user-kalinne/551a68f2-8a04-57df-8862-4790fa3213ad/scratchpad/tarefas.pkl','wb'))
