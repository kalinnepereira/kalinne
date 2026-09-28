# -*- coding: utf-8 -*-
import csv, io, datetime
Y=2026
def d(s):
    dd,mm=s.split('/'); return datetime.date(Y,int(mm),int(dd))
PT=['seg','ter','qua','qui','sex','sáb','dom']
def iso(x): return x.strftime('%d/%m/%Y') if x else ''
R=[]
def t(nome,resp,ini,pronto,rev,roda,dep,nota):
    R.append(dict(nome=nome,resp=resp,ini=d(ini),pronto=d(pronto),
                  rev=d(rev) if rev else None,roda=roda,dep=dep,nota=nota))

# ---- base, igual à lista de alunos ----
t('Narrativa','Kalinne + Henri','29/09','02/10','05/10','—','F0.7',
  'Mesma narrativa das duas listas. O fio que amarra trailer, pronunciamento, manifesto e aula magna.')
t('Id Visual','Maytte','29/09','01/10','02/10','—','F1.1',
  'Logo/selo + paleta + tipografia. BLOQUEIA todo o design da campanha.')
t('[Grupos WhatsApp] Capa + Configuração','Hugo + Maytte','05/10','15/10','16/10','—','F1.5',
  'Grupos de captação geral. Capa sai do kit da Maytte.')

# ---- corredor polonês / pré-captação ----
t('[Pré-captação orgânico] Vídeos','Nayara (seleção) + Jota (edição)','25/09','30/09','30/09','29/09 a 19/10','F2.2 · F9.3',
  'Corredor Polonês fase 1: cortes das ~200 aulas. SEM CTA. Lotes semanais até 19/10.')
t('[Pré-captação orgânico] API','Henri (copy) + Hugo','05/10','09/10','09/10','06/10 a 19/10','F2.3',
  'Fase 1 para a base que já existe. Sem oferta, sem data.')
t('[Pré-captação] Tráfego fase 1','Apoena','29/09','01/10','','29/09 a 19/10','—',
  'Público quente. Verba R$ 1.500.')
t('[Pré-captação] Funil de Live Semanal','Isadora + Nayara','25/09','29/09','','29/09 a 03/11','—',
  '6 edições, terças 20h30. Verba R$ 1.500.')

# ---- trailer ----
t('[Trailer] Roteiro','Henri','05/10','07/10','08/10','—','F0.7','Revela 09/11.')
t('[Trailer] Gravação','Isadora + Nayara','13/10','14/10','','—','F2.6 · F2.7',
  'GRAVAÇÃO 1, dois dias inteiros. Checklist de cenas fechado em 12/10.')
t('[Trailer] Edição','Jota','15/10','16/10','16/10','no ar 20/10','—',
  'FOLGA ZERO. Gravação fecha 14/10 e o trailer sobe 20/10. Ajustes em 19/10.')

# ---- captação ----
t('[Captação] Página de captura — copy','Henri','05/10','06/10','07/10','—','F0.7','Destrava o layout.')
t('[Captação] Página de captura — layout','Maytte','09/10','13/10','14/10','—','F2.8 · F1.5','Só começa com a copy APROVADA.')
t('[Captação] Página de captura — implementação','Ericson','15/10','19/10','20/10','—','F3.3','')
t('[Captação] Página de captura — integração e teste','Ericson + Hugo','21/10','22/10','22/10','no ar 26/10','F4.1 · F5.5 · F5.8',
  'ManyChat + Funnel + página de obrigado + redirect para o grupo. 2 dias úteis de folga antes de abrir.')
t('[Captação] Criativos — 10 vídeos','Jota + Editor 2','15/10','21/10','21/10','26/10 a 09/11','F2.10 · Gravação 1','')
t('[Captação] Criativos — 10 imagens elaboradas','Maytte','15/10','20/10','20/10','26/10 a 09/11','F2.11','')
t('[Captação] Criativos — 10 imagens nativas','Maytte','15/10','21/10','21/10','26/10 a 09/11','F2.11','Estética de celular, sem cara de anúncio.')
t('[Captação] Tráfego — estrutura, públicos e exclusões','Apoena','01/10','07/10','08/10','—','F0.2',
  'CRÍTICO: alunos excluídos de TODA a mídia. Se um aluno vir o anúncio de R$ 1.997, a oferta de R$ 1.497 morre.')
t('[Captação] Tráfego — subir campanha','Apoena','22/10','23/10','','26/10 a 09/11','F7.1 · criativos · página',
  '15 dias, verba R$ 10.500. Criativos na mão 2 dias antes.')
t('[Captação orgânica] E-mails','Henri (copy) + Hugo (Funnel)','08/10','23/10','23/10','26/10 a 09/11','F2.15 · F5.10','')
t('[Captação orgânica] API','Henri (copy) + Hugo (ManyChat)','08/10','23/10','23/10','26/10 a 09/11','F2.15 · F5.5','')
t('[Captação orgânica] Mensagens grupos whatsapp','Henri (copy) + Hugo','08/10','23/10','23/10','26/10 a 09/11','F2.15','')
t('[Captação] Arrastão 1','Isadora + Hugo','20/10','23/10','','26/10','F5.8 · F5.9',
  'Puxar todo mundo dos grupos antigos para a captação nova.')

# ---- pronunciamento e manifesto ----
t('[Pronunciamento] Roteiro','Henri','05/10','09/10','09/10','—','F0.7','Grava 13-14/10.')
t('[Pronunciamento] Edição','Editor 2','15/10','21/10','21/10','no ar 28/10','Gravação 1','')
t('[Manifesto] Roteiro','Henri','12/10','16/10','19/10','—','—','Grava 26-27/10.')
t('[Manifesto] Gravação','Isadora + Nayara','26/10','27/10','','—','F2.12 · F2.19 · F2.20',
  'GRAVAÇÃO 2. 26/10 é o mesmo dia que abre a captação — Robson grava, a abertura é do time.')
t('[Manifesto] Edição','Jota','28/10','29/10','29/10','no ar 03/11','Gravação 2','Ajustes 30/10.')
t('[Fase 2] Conteúdos de quebra de objeção','Henri + Jota','12/10','22/10','22/10','22/10 a 09/11','F2.13',
  'Roda junto com a captação. COM CTA. Verba menor.')

# ---- antecipação e dia ----
t('[Antecipação]  E-mails','Henri (copy) + Hugo','23/10','30/10','30/10','04/11 a 09/11','F2.19 · F5.11','')
t('[Antecipação]   API','Henri (copy) + Hugo','23/10','30/10','30/10','04/11 a 09/11','F2.19 · F5.11','')
t('[Antecipação] Mensagens grupos whatsapp','Henri (copy) + Hugo','23/10','30/10','30/10','04/11 a 09/11','F2.19','')
t('[Antecipação] Arrastão 2','Isadora + Hugo','30/10','05/11','','06/11 a 08/11','F5.11','')
t('Criar aula no Zoom','Hugo','19/10','28/10','29/10','09/11 20h30','—',
  'Sala, link, capacidade, gravação e teste de transmissão. Dimensionar para a aula maior das duas.')
t('[Materiais aula]','Maytte','16/10','05/11','06/11','09/11','F2.22 · F3.1 · Materiais da aula de alunos',
  'A apresentação dos 11 cursos. Adapta a versão usada em 05/11 na aula de alunos, trocando o bloco de preço.')
t('[Estou ao vivo e Cadê Você] API','Henri (copy) + Hugo','26/10','05/11','06/11','09/11','F2.19 · F5.11','')
t('[Estou ao vivo e Cadê Você] E-mails','Henri (copy) + Hugo','26/10','05/11','06/11','09/11','F2.19 · F5.11','')
t('[Estou ao vivo e Cadê Você] Mensagens grupo whatsapp','Henri (copy) + Hugo','26/10','05/11','06/11','09/11','F2.19','')
t('[Estou ao vivo]  URA e SMS','Henri (copy) + Hugo','26/10','05/11','06/11','09/11','F2.19',
  'Custo de fornecedor não está no orçamento de R$ 15 mil. Decidir até 26/10 se entra.')
t('[Jato] Campanha do dia da aula','Apoena','02/11','06/11','','09/11','F7.5','')

# ---- inscrições ----
t('[Inscrições] Página de vendas','Henri + Maytte + Ericson','29/09','30/10','30/10','09/11 em diante','F2.14b · F3.6b · F4.8',
  'MESMA página da lista de alunos: uma só, com preço conforme a origem do acesso. Não duplicar a tarefa nas duas listas — deixar nesta e referenciar na outra.')
t('[Inscrições] Checkout','Hugo','05/10','20/10','21/10','09/11 em diante','F0.2','Checkout geral a R$ 1.997.')
t('[Inscrições]  API','Henri (copy) + Hugo','26/10','06/11','06/11','09/11 em diante','F2.24','')
t('[Inscrições]  E-mails','Henri (copy) + Hugo','26/10','06/11','06/11','09/11 em diante','F2.24','')
t('[Inscrições]  Mensagens grupo whatsapp','Henri (copy) + Hugo','26/10','06/11','06/11','09/11 em diante','F2.24','')
t('[Incrições] Automação e-mail compras','Henri (copy) + Hugo','22/10','30/10','30/10','09/11 em diante','F5.3','Confirmação e boas-vindas pós-compra.')
t('[Inscrições] Automação API compras','Hugo','22/10','30/10','30/10','09/11 em diante','F5.3','')
t('[Carrinho aberto] Criativos — 30 peças','Henri + Maytte + Editor 2','26/10','04/11','05/11','09/11 em diante','F2.20 · Gravação 2',
  '10 vídeos + 10 imagens elaboradas + 10 nativas.')
t('[Carrinho aberto] Tráfego','Apoena','04/11','06/11','','09/11 em diante','criativos de carrinho','')
t('[Virada de lote] Comunicação e estrutura','Henri + Hugo + Maytte','02/11','11/11','12/11','quando o CPA subir','F2.24 · F5.12',
  '3 dias de urgência, até 10 mensagens/dia, depois sobe R$ 250. Não é data fixa.')

err=[]
for x in R:
    if x['ini']>x['pronto']: err.append(x['nome']+': início depois do pronto')
    if x['rev'] and x['rev']<x['pronto']: err.append(x['nome']+': revisão antes do pronto')
    for k in ('pronto','rev'):
        if x[k] and x[k].weekday()>=5: err.append(x['nome']+f': {k} em fim de semana')
print('TAREFAS:', len(R)); print('ERROS:', err if err else 'nenhum')

f=io.open('plano/bf-NAO-ALUNOS-clickup.csv','w',encoding='utf-8-sig',newline='')
w=csv.writer(f, delimiter=';')
w.writerow(['Task ID','Task Name','Assignee','Start Date','Due Date','Revisão Kalinne até','Quando roda','Depende de (plano)','Confira','Descrição'])
for x in R:
    w.writerow(['', x['nome'], x['resp'], iso(x['ini']), iso(x['pronto']), iso(x['rev']),
                x['roda'], x['dep'], 'existe na sua lista?', x['nota']])
f.close()
print('CSV gravado')
