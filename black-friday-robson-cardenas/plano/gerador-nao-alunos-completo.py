# -*- coding: utf-8 -*-
import csv, io, datetime, re
Y=2026
def d(s):
    dd,mm=s.split('/'); return datetime.date(Y,int(mm),int(dd))
PT=['seg','ter','qua','qui','sex','sáb','dom']
def iso(x): return x.strftime('%d/%m/%Y')
FERIADOS={d('25/10'), d('02/11')}   # 2o turno e Finados
def uteis(a,b):
    out=[];x=a
    while x<=b:
        if x.weekday()<5 and x not in FERIADOS: out.append(x)
        x+=datetime.timedelta(days=1)
    return out

# responsavel por padrao de texto — regra unica, aplicada a todas as 225 subtarefas
REGRAS=[
 (r'^aprovar|^aprova[çc][ãa]o','Kalinne'),
 (r'^copy|^briefing / copy','Henri'),
 (r'^grava[çc][ãa]o','Robson + Nayara'),
 (r'^receber|na pasta para editar|^arrumar nomenclatura','Nayara'),
 (r'^briefing de edi[çc][ãa]o|^briefing edi[çc][ãa]o','Isadora'),
 (r'^entregar.*editad','Jota'),
 (r'^entregar','Maytte'),
 (r'^briefing','Isadora'),
 (r'^liberar para tr[áa]fego|^liberar v[íi]deos|^liberar criativos|^subir criativos|^subir v[íi]deos de dist','Apoena'),
 (r'^implementar|^configurar pixel|^integra[çc][õo]es|^conferir e testar|^criar utms|^solicitar para webdesigner','Ericson'),
 (r'^criar|^programar|^ligar automa|^colocar|^pegar link|^abrir grupos|^trocar','Hugo'),
 (r'^definir','Kalinne'),
]
def resp(s):
    t=s.strip().lower()
    for pat,r in REGRAS:
        if re.search(pat,t): return r
    return 'A DEFINIR'

V9=['Copy para vídeos de {x}','Aprovar copy vídeos de {x}','Gravação vídeos de {x}','Receber vídeos de {x} gravados',
    'Subir vídeos brutos de {x} na pasta para editar','Briefing de edição vídeos de {x}','Entregar vídeos de {x} editados',
    'Aprovar vídeos de {x} editados','Arrumar nomenclatura arquivos vídeos de {x}']
IMG4=['Briefing imagens de {x}','Entregar imagens de {x}','Aprovar imagens de {x}','Arrumar nomenclatura arquivos imagens de {x}']
CL2=['Copy legenda tráfego de {x}','Aprovar copy legenda tráfego de {x}']
CAMP2=['Liberar para tráfego criativos + legenda de {x}','Subir criativos de {x}']
AUT3=['Copy automação {x}','Aprovar copy automação {x}','Criar automação {x}']
MSG3=['Copy {x}','Aprovar copy {x}','Programar {x}']

T=[]
def t(grupo, nome, roda, ini, fim, subs, obs=''):
    T.append(dict(g=grupo,n=nome,roda=roda,ini=d(ini),fim=d(fim),subs=subs,obs=obs))
def f(lst,x): return [s.format(x=x) for s in lst]

# ============ 1. PRÉ LANÇAMENTO (2) ============
G='1. Pré Lançamento'
t(G,'Narrativa','—','28/09','01/10',
  ['Criar narrativa do lançamento','Aprovar narrativa do lançamento'],
  'O fio que amarra tudo. Bloqueia a copy de todas as peças.')
t(G,'Id Visual','—','28/09','02/10',
  ['Briefing id visual do lançamento','Entregar id visual do lançamento','Aprovar id visual do lançamento'],
  'BLOQUEIA todo o design. Hoje não existe identidade visual da Black.')

# ============ 2. CORREDOR POLONÊS – FASE 1 E 2 (6) ============
G='2. Corredor Polonês – Fase 1 e 2'
t(G,'Campanha Distribuição Nível de Consciência fase 1 e 2','29/09 a 19/10','28/09','29/09',
  ['Liberar para tráfego videos + legenda distribuição nível de consciência fase 1 e 2',
   'Subir videos de dist. nível de consciência fase 1 e 2'],
  'Template do Ferrari marcava 14/09. Movido para a nossa janela de fase 1.')
t(G,'[Dist. de Nível de Consciência tráfego] Copy legenda fase 1 e 2','29/09 a 19/10','28/09','29/09',
  ['Copy para tráfego legenda distribuição nível de consciência fase 1 e 2',
   'Aprovar copy tráfego legenda distribuição nível de consciência fase 1 e 2'])
t(G,'[Dist. de Nível de Consciência tráfego] Criativos Vídeos fase 1 e 2','29/09 a 19/10','28/09','09/10',
  ['Copy para videos dist. nível de consciência fase 1 e 2','Aprovar copy videos dist. nível de consciência fase 1 e 2',
   'Gravação videos dist. nível de consciência fase 1 e 2','Receber vídeos dist. nível de consciência fase 1 e 2 gravados',
   'Subir vídeos dist. nível de consciência fase 1 e 2 brutos na pasta para editar',
   'Briefing edição vídeos dist. nível de consciência fase 1 e 2','Entregar vídeos dist. nível de consciência fase 1 e 2 editados',
   'Aprovação vídeos dist. nível de consciência fase 1 e 2','Arrumar nomenclatura arquivos vídeos dist. nível de consciência fase 1 e 2'],
  'ATENÇÃO: o template prevê GRAVAÇÃO nova. Nossa estratégia usa as ~200 aulas do acervo. Decidir se "Gravação" vira "seleção de trechos".')
t(G,'Campanha de tráfego Pré-Captação','19/10 a 25/10','15/10','16/10',
  ['Liberar vídeos + legendas de pré-captação para tráfego','Subir criativos de Pré-Captação'],
  'Template: 05/10–11/10. Movido para a semana anterior à nossa captação (26/10).')
t(G,'[Pré-captação tráfego] Copy legenda','19/10 a 25/10','08/10','14/10',
  ['Copy para legenda tráfego de pré-captação','Aprovar copy legenda tráfego de pré-captação'])
t(G,'[Pré-captação tráfego] Criativos vídeos','19/10 a 25/10','05/10','15/10',
  ['Copy vídeos de pré-captação','Aprovar copy vídeos de pré-captação','Gravação vídeos de pré-captação',
   'Receber vídeos pré-captação gravados','Subir vídeos brutos de pré-captação na pasta para editar',
   'Briefing para edição vídeos de pré-captação','Entregar vídeos de pré-captação editados',
   'Aprovar vídeos de pré-captação editados','Arrumar nomenclatura dos arquivos de vídeos de pré-captação'],
  'Material sai da GRAVAÇÃO 1 (13 e 14/10).')

# ============ 3. CAPTAÇÃO (12) ============
G='3. Captação'
t(G,'Campanha de Captação','26/10 a 09/11','22/10','23/10',
  ['Liberar para tráfego criativos + legenda de captação','Subir criativos de captação'],
  'Template: 12/10–05/11. Nossa captação geral: 15 dias, 26/10 a 09/11.')
t(G,'[Pesquisa de leads] Forms','26/10 a 09/11','05/10','21/10',
  ['Briefing capa da pesquisa','Entregar capa da pesquisa','Aprovar capa da pequisa',
   'Copy perguntas pesquisa leads','Aprovar perguntas pesquisa de leads','Criar forms e colocar capa da pesquisa',
   'Pegar link fechado da pesquisa e colocar no domínio','Colocar o link da pesquisa na descrição dos grupos',
   'Colocar o link da pesquisa na automação de e-mail boas vindas'],
  'NÃO ESTAVA NO MEU PLANO. Diagnóstico da audiência antes de vender.')
t(G,'[Captação tráfego] Página de cadastro e obrigado','26/10 a 09/11','05/10','22/10',
  ['Briefing / Copy para página de cadastro e obrigado','Aprovar briefing / copy página de cadastro e obrigado',
   'Entregar layout página de cadastro e obrigado','Aprovar layout página de cadastro e obrigado',
   'Implementar página de cadastro e obrigado','Configurar pixel página de cadastro e obrigado',
   'Integrações página de cadastro e obrigado','Conferir e testar página de cadastro e obrigado'],
  'CORRENTE CRÍTICA. Pronta e testada 22/10 — 2 dias úteis antes de abrir a captação.')
t(G,'[Automação API] Boas vindas cadastrados','26/10 a 09/11','14/10','23/10',
  f(AUT3,'API boas vindas cadastrados'))
t(G,'[Captação orgânica] Instagram','26/10 a 09/11','19/10','23/10',
  ['Copy bio instagram','Aprovar copy bio instagram','Trocar bio no instagram'])
t(G,'[Grupos WhatsApp] Capa + Configuração','26/10 a 09/11','05/10','21/10',
  ['Briefing imagem capa para grupos whatsapp','Entregar imagem capa para grupos whatsapp',
   'Aprovar imagem capa dos grupos whatsapp','Copy descrição + nome grupos whastapp',
   'Aprovar copy descrição dos grupos whatsapp','Abrir grupos do whatsapp'])
t(G,'[Captação tráfego] Criativos vídeos','26/10 a 09/11','08/10','21/10',
  f(V9,'captação'),
  'Material sai da GRAVAÇÃO 1 (13 e 14/10). 2 dias úteis de folga antes de subir a campanha.')
t(G,'[Captação tráfego] Criativos imagens','26/10 a 09/11','15/10','21/10', f(IMG4,'captação'))
t(G,'[Captação tráfego] Copy legenda','26/10 a 09/11','14/10','20/10', f(CL2,'captação'))
t(G,'[Captação orgânica] Youtube','26/10 a 09/11','05/10','21/10',
  ['Briefing banner capa canal YT','Entregar banner capa canal YT','Aprovar banner capa canal YT','Trocar banner capa canal YT'])
t(G,'[Automação e-mail] Boas vindas cadastrados','26/10 a 09/11','14/10','23/10',
  ['Copy automação de e-mail boas vindas cadastrados','Aprovar copy automação de e-mail boas vindas cadastrados',
   'Criar automação e-mail boas vindas cadastrados'])
t(G,'[Captação orgânica] Página de cadastro e obrigado','26/10 a 09/11','15/10','22/10',
  ['Solicitar para webdesigner página de cadastro orgânica','Aprovar página de cadastro orgânica',
   'Conferir e testar página de cadastro orgânica','Criar UTMs página de cadastro orgânica'])

# ============ 4. CORREDOR POLONÊS – FASE 2 (8) ============
G='4. Corredor Polonês – Fase 2'
t(G,'Campanha Distribuição de Nível de Consciência','20/10 a 09/11','16/10','19/10',
  ['Liberar para tráfego criativos distribuição nível de consciência fase 2',
   'Subir criativos de distribuição de nível de consciência fase 2'])
t(G,'[Dist. de Nível de Consciência tráfego] Copy legenda fase 2','20/10 a 09/11','08/10','15/10',
  ['Copy para tráfego legenda distribuição nível de consciência fase 2',
   'Aprovar copy tráfego legenda distribuição nível de consciência fase 2'])
t(G,'[Dist. de Nível de Consciência tráfego] Criativos Vídeos fase 2','20/10 a 09/11','05/10','16/10',
  ['Copy para videos dist. nível de consciência fase 2','Aprovar copy videos dist. nível de consciência fase 2',
   'Gravação videos dist. nível de consciência fase 2','Receber vídeos dist. nível de consciência fase 2 gravados',
   'Subir vídeos dist. nível de consciência fase 2 brutos na pasta para editar',
   'Briefing edição vídeos dist. nível de consciência fase 2','Entregar vídeos dist. nível de consciência fase 2 editados',
   'Aprovação vídeos dist. nível de consciência fase 2','Arrumar nomenclatura arquivos vídeos dist. nível de consciência fase 2'],
  'COM CTA. Quebra de objeção. Material da GRAVAÇÃO 1.')
t(G,'Campanhas de Manifesto','03/11 a 09/11','28/10','30/10',
  ['Liberar para tráfego criativos + legenda manifesto','Subir criativos manifesto'],
  'Template: 15/10–05/11. Nossa estratégia sobe o Manifesto em 03/11.')
t(G,'[Manifesto tráfego] Copy legenda','03/11 a 09/11','19/10','23/10',
  ['Copy legenda para tráfego manifesto','Aprovar copy legenda tráfego manifesto'])
t(G,'[Manifesto tráfego] Criativos Vídeos','03/11 a 09/11','12/10','30/10',
  ['Copy vídeos de manifesto','Aprovar copy videos de manifesto','Gravação vídeos manifesto',
   'Receber vídeos manifesto gravados','Subir vídeos brutos manifesto na pasta para editar',
   'Briefing edição vídeos de manifesto','Entregar vídeos de manifesto editados',
   'Aprovar vídeos de manifesto editados','Arrumar nomenclatura arquivos vídeos de manifesto'],
  'Material sai da GRAVAÇÃO 2 (26 e 27/10).')
t(G,'[Transmissão aulas] Youtube','09/11','19/10','30/10',
  ['Definir nome da aula','Briefing thumb aula Youtube','Entregar thumb aula Youtube',
   'Aprovar thumb aula Youtube','Criar aula no Youtube'],
  'A aula de NÃO ALUNOS é no YouTube. A de alunos é no Zoom.')
t(G,'[Tráfego] Link transmissão aula Youtube','09/11','30/10','04/11',
  ['Colocar link da aula no Youtube no domínio (redirect)'])

# ============ 5. CONVERSÃO PPL (10) ============
G='5. Conversão PPL'
t(G,'Campanha de Antecipação Aula','03/11 a 09/11','30/10','02/11',
  ['Liberar criativos de antecipação','Subir criativos de antecipação'],
  'Template: 30/10–05/11. Movido para a janela da nossa aula de 09/11.')
t(G,'[Antecipação tráfego] Copy legenda','03/11 a 09/11','21/10','28/10', f(CL2,'antecipação'))
t(G,'[Antecipação tráfego] Criativos Vídeos','03/11 a 09/11','14/10','30/10',
  ['Copy para vídeos de antecipação','Aprovação copy vídeos de antecipação','Gravação vídeos de antecipação',
   'Receber vídeos de antecipação gravados','Subir vídeos brutos de antecipação na pasta para editar',
   'Briefing de edição vídeos de antecipação','Entregar vídeos de antecipação editados',
   'Aprovar vídeos de antecipação editados','Arrumar nomenclatura arquivos vídeos de antecipação'],
  'Material sai da GRAVAÇÃO 2 (26 e 27/10).')
t(G,'[Antecipação tráfego] Criativos imagens','03/11 a 09/11','22/10','29/10', f(IMG4,'antecipação'))
t(G,'[Antecipação orgânico] Imagens','03/11 a 09/11','22/10','29/10',
  ['Briefing imagens de antecipação','Entregar imagens de antecipação','Aprovar imagens de antecipação'])
t(G,'[Antecipação] API','03/11 a 09/11','21/10','29/10',
  ['Copy antecipação aula API','Aprovar copy antecipação aula API','Programar API antecipação aula'])
t(G,'[Antecipação] E-mails','03/11 a 09/11','21/10','29/10',
  ['Copy e-mails de antecipação aula','Aprovar copy e-mails de antecipação aula','Programar e-mails de antecipação aula'])
t(G,'[Antecipação] Mensagens grupos whatsapp','03/11 a 09/11','26/10','29/10',
  ['Copy mensagens antecipação aula grupos whatsapp'])
t(G,'[Antecipação] URA e SMS','03/11 a 09/11','21/10','29/10',
  ['Copy URA e SMS aula','Aprovar URA e SMS aula','Programar URA e SMS aula'],
  'CUSTO DE FORNECEDOR NÃO ORÇADO. Decidir até 21/10 se entra.')
t(G,'[Funil Live Semanal] Temas','29/09 a 03/11','28/09','30/09',
  ['Definir temas das lives semanais'],
  '6 edições, terças 20h30: 29/09, 06/10, 13/10, 20/10, 27/10, 03/11.')

# ============ 6. CONVERSÃO PL (5) ============
G='6. Conversão PL'
t(G,'Campanha Ao Vivo (A jato)','09/11','05/11','06/11',
  ['Liberar criativos estou ao vivo + link da aula para tráfego','Subir criativos de estou ao vivo'])
t(G,'[Estou ao vivo (a jato) tráfego] Criativos Vídeos','09/11','19/10','04/11',
  ['Copy vídeos estou ao vivo aula','Aprovar copy vídeos estou ao vivo aula','Gravação vídeos estou ao vivo aula',
   'Receber vídeos estou ao vivo aula gravados','Subir vídeos brutos de estou ao vivo aulas na pasta para editar',
   'Briefing de edição vídeos estou ao vivo aula','Entregar vídeos de estou ao vivo aula editados',
   'Aprovar vídeos estou ao vivo aula editados','Arrumar nomenclatura arquivos vídeos estou ao vivo aula'],
  'Material sai da GRAVAÇÃO 2 (26 e 27/10).')
t(G,'[Estou ao vivo e Cadê Você] API','09/11','26/10','04/11',
  ['Copy API estou ao vivo aula','Aprovar copy API estou ao vivo aula','Programar API estou ao vivo aula'])
t(G,'[Estou ao vivo e Cadê Você] E-mails','09/11','26/10','04/11',
  ['Copy e-mails estou ao vivo e cadê você aula','Aprovar e-mails estou ao vivo e cadê você aula',
   'Programar e-mails estou ao vivo e cadê você aula'])
t(G,'[Materiais aula]','09/11','12/10','05/11',
  [('Cronômetro aula',['Briefing de edição cronômetro aula','Entregar cronômetro aula editado','Aprovar cronômetro aula']),
   ('Depoimentos',['Briefing depoimentos','Entregar depoimentos','Aprovar depoimentos']),
   ('PPT aula',['Copy conteúdo aula','Aprovar conteúdo aula','Briefing PPT conteúdo aula',
                'Entregar PPT conteúdo aula','Aprovar PPT conteúdo aula'])],
  'O "PPT aula" é a apresentação dos 11 cursos com capa e preço — 30 min do pitch. Pronto 05/11 para o ensaio.')

# ============ 7. CONVERSÃO L (9) ============
G='7. Conversão L'
t(G,'Campanha Abertura de carrinho','09/11 em diante','05/11','06/11',
  ['Liberar para tráfego criativos + legenda + link da página inscrições abertas','Subir criativos de inscrições abertas'])
t(G,'[Inscrições] Checkout','09/11 em diante','12/10','30/10',
  ['Briefing banners checkout (vertical e horizontal)','Entregar banners checkout','Aprovar banners checkout',
   'Criar checkout','Colocar link do checkout na página de vendas'],
  'Checkout geral R$ 1.997. São 3 checkouts na campanha — os outros 2 ficam na lista de alunos e no link privado do grupo A.')
t(G,'[Inscrições tráfego] Página de vendas','09/11 em diante','29/09','30/10',
  ['Briefing / Copy página de vendas','Aprovar briefing / copy página de vendas','Entregar layout página de vendas',
   'Aprovar layout página de vendas','Implementar página de vendas','Configurar pixel página de vendas',
   'Integrações páginas de vendas','Conferir e testar página de vendas'],
  'A CORRENTE MAIS LONGA DA CAMPANHA. Depende do preço de tabela dos 11 cursos. É UMA página só, com preço conforme a origem — não duplicar na lista de alunos.')
t(G,'[Inscrições tráfego] Copy legenda','09/11 em diante','26/10','04/11', f(CL2,'inscrições abertas'))
t(G,'[Inscrições tráfego] Criativos Vídeos','09/11 em diante','19/10','04/11',
  ['Copy para vídeos de inscrições abertas','Aprovar copy vídeos de inscrições abertas',
   'Gravação vídeos de inscrições abertas','Receber vídeos de inscrições abertas gravados',
   'Subir vídeos brutos de inscrições abertas na pasta para editar','Briefing de edição vídeos de inscrições abertas',
   'Entregar vídeos de inscrições abertas editados','Aprovar vídeos de inscrições abertas editados',
   'Arrumar nomenclatura arquivos vídeos inscrições abertas'],
  'Material sai da GRAVAÇÃO 2 (26 e 27/10).')
t(G,'[Inscrições tráfego] Criativos Imagens','09/11 em diante','26/10','04/11',
  ['Copy imagens de inscrições abertas','Aprovar copy imagens de inscrições abertas','Briefing imagens de inscrições abertas',
   'Entregar imagens de inscrições abertas','Aprovar imagens de inscrições abertas',
   'Arrumar nomenclatura arquivos imagens inscrições abertas'])
t(G,'[Inscrições] Banner capa canal do YT','09/11 em diante','26/10','05/11',
  ['Briefing banner canal YT inscrições abertas','Entregar banner canal YT inscrições abertas',
   'Aprovar banner canal YT inscrições abertas','Trocar no YT banner inscrições abertas'])
t(G,'[Inscrições] E-mails','09/11 em diante','26/10','05/11',
  ['Copy e-mails de inscrições','Aprovar copy e-mails de inscrições','Programar e-mails de inscrições'])
t(G,'[Incrições] Automação e-mail compras','09/11 em diante','19/10','30/10',
  ['Copy e-mails automação compras','Aprovar copy e-mails automação compras',
   'Programar automação compras','Ligar automações de compras'],
  'Confirmação e boas-vindas pós-compra. Se falhar, o comprador paga e não recebe nada.')

# ================= GERAÇÃO =================
linhas=[]; nsub=0; nneto=0
for x in T:
    dias=uteis(x['ini'],x['fim'])
    assert dias, x['n']
    flat=[]
    for s in x['subs']:
        if isinstance(s,tuple): flat.append(('P',s[0])); flat += [('F',c) for c in s[1]]
        else: flat.append(('S',s))
    n=len(flat)
    linhas.append(dict(g=x['g'],tar=x['n'],sub='',niv='TAREFA',resp='—',
                       ini=iso(x['ini']),ent=iso(x['fim']),roda=x['roda'],obs=x['obs']))
    for i,(tipo,s) in enumerate(flat):
        dia=dias[min(int(round(i*(len(dias)-1)/max(n-1,1))), len(dias)-1)]
        linhas.append(dict(g=x['g'],tar=x['n'],sub=('    ↳ '+s) if tipo=='F' else s,
                           niv='NETO' if tipo=='F' else ('SUBTAREFA' if tipo=='S' else 'SUBTAREFA (tem filhos)'),
                           resp=('—' if tipo=='P' else resp(s)),ini='',ent=iso(dia),roda='',obs=''))
        if tipo=='F': nneto+=1
        else: nsub+=1

# validação
err=[]
for l in linhas:
    if l['niv']!='TAREFA':
        dt=datetime.datetime.strptime(l['ent'],'%d/%m/%Y').date()
        if dt.weekday()>=5: err.append(l['sub']+' em fim de semana')
        if dt in FERIADOS: err.append(l['sub']+' em feriado')
    if l['resp']=='A DEFINIR': err.append('SEM RESPONSÁVEL: '+l['sub'])
    if l['niv']=='TAREFA' and not l['ent']: err.append('TAREFA sem entrega: '+l['tar'])
print('TAREFAS:',len(T),'| SUBTAREFAS:',nsub,'| NETOS:',nneto,'| LINHAS:',len(linhas))
print('ERROS:', err[:10] if err else 'nenhum')

f2=io.open('plano/bf-NAO-ALUNOS-completo.csv','w',encoding='utf-8-sig',newline='')
w=csv.writer(f2,delimiter=';')
w.writerow(['Grupo','Tarefa','Subtarefa','Nível','Responsável','Início','Entrega','Campanha roda','Observação'])
for l in linhas: w.writerow([l['g'],l['tar'],l['sub'],l['niv'],l['resp'],l['ini'],l['ent'],l['roda'],l['obs']])
f2.close()
from collections import Counter
c=Counter(l['resp'] for l in linhas if l['niv']!='TAREFA')
print('CARGA:',dict(c.most_common()))
