# -*- coding: utf-8 -*-
import csv, io, datetime
Y=2026
def d(s):
    dd,mm=s.split('/'); return datetime.date(Y,int(mm),int(dd))
PT=['seg','ter','qua','qui','sex','sáb','dom']
def brd(x): return (x.strftime('%d/%m')+' '+PT[x.weekday()]) if x else '—'
def iso(x): return x.strftime('%d/%m/%Y') if x else ''

R=[]
def t(cid, nome, resp, ini, pronto, rev, roda, dep, nota, novo=False):
    R.append(dict(cid=cid, nome=nome, resp=resp, ini=d(ini), pronto=d(pronto),
                  rev=d(rev) if rev else None, roda=roda, dep=dep, nota=nota, novo=novo))

# ---- tarefas que JÁ EXISTEM na lista do Ferrari (Task ID real do export) ----
t('86akmc9mt','Narrativa','Kalinne + Henri','29/09','02/10','05/10','—','F0.7',
  'NOVO NO PLANO. O fio que amarra trailer, pronunciamento, manifesto e aula. Sem ele cada peça conta uma história diferente.', True)
t('86akmc9kd','Id Visual','Maytte','29/09','01/10','02/10','—','F1.1',
  'Logo/selo + paleta + tipografia. BLOQUEIA todo o design da campanha.')
t('86akmc9nt','[Grupos WhatsApp] Capa + Configuração','Hugo + Maytte','05/10','15/10','16/10','—','F1.5',
  'Grupo de captação de alunos. Capa sai do kit de templates da Maytte.')
t('86akmc9f5','[Pré-captação orgânico] API','Henri (copy) + Hugo (disparo)','12/10','16/10','19/10','20/10 a 28/10','F2.13',
  'Aquecimento antes de abrir a captação. Conteúdo de fase 2: quebra de objeção, sem oferta.')
t('86akmc9f7','[Pré-captação orgânico] Vídeos','Jota','12/10','16/10','19/10','20/10 a 28/10','F2.13',
  'Cortes de fase 2 direcionados a quem já é aluno.')
t('86akmc9f8','[Captação orgânica] E-mails','Henri (copy) + Hugo (Funnel)','16/10','27/10','28/10','29/10 a 05/11','F2.16 · F5.10',
  'Captação de alunos: 8 dias, conforme orientação do Leandro Duarte. O template do Ferrari usa 16 dias.')
t('86akmc9gk','[Captação orgânica] API','Henri (copy) + Hugo (ManyChat)','16/10','27/10','28/10','29/10 a 05/11','F2.16 · F5.6',
  'SEM TRÁFEGO. Esta sequência É a campanha de alunos inteira. Se falhar, não há plano B de mídia.')
t('86akmc9f9','[Captação orgânica] Mensagens grupos whatsapp','Henri (copy) + Hugo','16/10','27/10','28/10','29/10 a 05/11','F2.16',
  '')
t('86akmc9fa','[Captação orgânica] Área de membros','Henri (copy) + Ericson','19/10','27/10','28/10','29/10 a 05/11','F2.16',
  'NOVO NO PLANO. Banner e aviso dentro da área de membros — canal que eu tinha citado mas não virou tarefa.', True)
t('86akmc9n2','Criar aula no Zoom','Hugo','19/10','28/10','29/10','05/11 20h30','—',
  'NOVO NO PLANO. Sala, link, capacidade, gravação e teste de transmissão. Eu tinha o ensaio, não tinha a sala.', True)
t('86akmc9m4','[Materiais aula]','Maytte','16/10','02/11','03/11','05/11','F2.14b · F3.1 · F2.21',
  'NOVO NO PLANO, E ERA A MAIOR FALHA MINHA. São 30 minutos mostrando 11 cursos com capa e preço: isso é uma apresentação. Esqueleto sai da copy da página e das capas; o script fecha. Pronta 02/11 para ensaiar em 04/11.', True)
t('86akmc9gq','[Antecipação]  E-mails','Henri (copy) + Hugo','23/10','30/10','30/10','02/11 a 05/11','F2.19 · F5.11','')
t('86akmc9gm','[Antecipação]   API','Henri (copy) + Hugo','23/10','30/10','30/10','02/11 a 05/11','F2.19 · F5.11','')
t('86akmc9gr','[Antecipação] Mensagens grupos whatsapp','Henri (copy) + Hugo','23/10','30/10','30/10','02/11 a 05/11','F2.19','')
t('86akmc9hn','[Estou ao vivo e Cadê Você] API','Henri (copy) + Hugo','26/10','03/11','03/11','05/11','F2.19 · F5.11',
  'Disparo no dia, durante a aula. Separado da antecipação de propósito — o Ferrari tem razão em quebrar em dois momentos.')
t('86akmc9hy','[Estou ao vivo e Cadê Você] E-mails','Henri (copy) + Hugo','26/10','03/11','03/11','05/11','F2.19 · F5.11','')
t('86akmc9hw','[Estou ao vivo e Cadê Você] Mensagens grupo whatsapp','Henri (copy) + Hugo','26/10','03/11','03/11','05/11','F2.19','')
t('86akmc9hz','[Estou ao vivo]  URA e SMS','Henri (copy) + Hugo','26/10','03/11','03/11','05/11','F2.19',
  'NOVO NO PLANO. Dois canais de comparecimento que eu não tinha considerado. Verificar custo e fornecedor antes de 26/10.', True)
t('86akmc9mc','[Inscrições] Checkout','Hugo','05/10','20/10','21/10','05/11 em diante','F0.2',
  'Checkout de alunos a R$ 1.497. Precisa identificar o mensalista para disparar o cancelamento da recorrência.')
t('86akmc9mk','[Inscrições] Página de vendas','Henri + Maytte + Ericson','29/09','30/10','30/10','05/11 em diante','F2.14b · F3.6b · F4.8',
  'A corrente mais longa da campanha: preço dos cursos → copy em 2 partes → capas → layout → implementação → 3 checkouts → teste com compra real.')
t('86akmc9jw','[Inscrições]  API','Henri (copy) + Hugo','26/10','03/11','03/11','05/11 em diante','F2.24','')
t('86akmc9j7','[Inscrições]  E-mails','Henri (copy) + Hugo','26/10','03/11','03/11','05/11 em diante','F2.24','')
t('86akmc9k3','[Inscrições]  Mensagens grupo whatsapp','Henri (copy) + Hugo','26/10','03/11','03/11','05/11 em diante','F2.24','')
t('86akmc9k7','[Incrições] Automação e-mail compras','Henri (copy) + Hugo','22/10','30/10','30/10','05/11 em diante','F5.3',
  'NOVO NO PLANO. Confirmação e boas-vindas pós-compra. Eu tinha a entrega do acesso, não a comunicação que vai junto.', True)
t('86akmc9k5','[Inscrições] Automação API compras','Hugo','22/10','30/10','30/10','05/11 em diante','F5.3',
  'NOVO NO PLANO. Idem, pelo WhatsApp.', True)

# ---- validação ----
err=[]
for x in R:
    if x['ini']>x['pronto']: err.append(x['cid']+': início depois do pronto')
    if x['rev'] and x['rev']<x['pronto']: err.append(x['cid']+': revisão antes do pronto')
    for k in ('pronto','rev'):
        if x[k] and x[k].weekday()>=5: err.append(x['cid']+f': {k} em fim de semana')
    if x['pronto']>d('05/11') and 'em diante' not in x['roda'] and x['roda']!='—':
        err.append(x['cid']+': pronto depois do evento')
print('TAREFAS:', len(R), '| NOVAS:', sum(1 for x in R if x['novo']))
print('ERROS:', err if err else 'nenhum')

# ---- CSV ----
f=io.open('plano/bf-ALUNOS-clickup.csv','w',encoding='utf-8-sig',newline='')
w=csv.writer(f, delimiter=';')
w.writerow(['Task ID','Task Name','Assignee','Start Date','Due Date','Revisão Kalinne até','Quando roda','Depende de (plano)','Faltava no meu plano?','Descrição'])
for x in R:
    w.writerow([x['cid'], x['nome'], x['resp'], iso(x['ini']), iso(x['pronto']),
                iso(x['rev']), x['roda'], x['dep'], 'SIM — eu não tinha previsto' if x['novo'] else '', x['nota']])
f.close()
print('CSV gravado')
