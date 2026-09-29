# -*- coding: utf-8 -*-
import csv, io, datetime, importlib.util, sys
spec=importlib.util.spec_from_file_location('na','/tmp/claude-0/-home-user-kalinne/551a68f2-8a04-57df-8862-4790fa3213ad/scratchpad/na.py')
m=importlib.util.module_from_spec(spec)
_out=io.StringIO(); _o=sys.stdout; sys.stdout=_out
spec.loader.exec_module(m); sys.stdout=_o

T=m.T; uteis=m.uteis; resp=m.resp
def isoD(x): return x.strftime('%Y-%m-%d')

# e-mails do time — a preencher
# e-mails reais, lidos na tela "Gerenciar pessoas" (9 usuarios no workspace)
EMAIL={
 'Kalinne':'kalinnepereira@gmail.com',      # conta "Gestao | Brand" — operada pela Isadora
 'Isadora':'kalinnepereira@gmail.com',      # idem: ela usa a conta da Kalinne
 'Henri':'henri.d.oliveira@gmail.com',
 'Maytte':'maytteteixeira@gmail.com',
 'Nayara':'bitzernayara@gmail.com',
 'Ericson':'ericsonsilva.dsg@gmail.com',
 'Jota':'joathana02@gmail.com',             # confirmado pela Kalinne
 'Robson + Nayara':'bitzernayara@gmail.com',# Robson nao tem conta; Nayara conduz
 'Felipe':'',                                # 2o editor — falta e-mail
 'Hugo':'',                                  # SEM CONTA no ClickUp
 'Apoena':'',                                # SEM CONTA no ClickUp
 '—':''}
SEM_CONTA={'Hugo','Apoena','Felipe'}

rows=[]; nid=0
def novo(**kw):
    global nid; nid+=1
    r=dict(id=nid, nome='', subids=[], resp='', ini='', due='', grupo='', desc='')
    r.update(kw); rows.append(r); return r

for x in T:
    dias=uteis(x['ini'],x['fim'])
    pai=novo(nome=x['n'], grupo=x['g'], ini=isoD(x['ini']), due=isoD(x['fim']),
             desc=(x['obs']+(' | ' if x['obs'] else '')+'Campanha roda: '+x['roda']).strip(' |'))
    flat=[]
    for s in x['subs']:
        if isinstance(s,tuple): flat.append(('P',s[0],s[1]))
        else: flat.append(('S',s,None))
    # posicoes das subtarefas diretas dentro da janela
    total=sum(1+(len(c) if c else 0) for _,_,c in flat)
    k=0
    for tipo,nome,filhos in flat:
        dia=dias[min(int(round(k*(len(dias)-1)/max(total-1,1))), len(dias)-1)]
        _r=('' if tipo=='P' else resp(nome))
        sub=novo(nome=nome, grupo=x['g'], due=isoD(dia), resp=_r,
                 desc=(('📲 '+_r+' — prestador de serviço, fora do ClickUp. A Isadora passa por WhatsApp') if _r in SEM_CONTA
                       else ('Responsável: '+_r if _r else '')))
        pai['subids'].append(sub['id']); k+=1
        if filhos:
            for fnome in filhos:
                dia=dias[min(int(round(k*(len(dias)-1)/max(total-1,1))), len(dias)-1)]
                _rf=resp(fnome)
                neto=novo(nome=fnome, grupo=x['g'], due=isoD(dia), resp=_rf,
                          desc=(('📲 '+_rf+' — prestador de serviço, fora do ClickUp. A Isadora passa por WhatsApp') if _rf in SEM_CONTA
                                else ('Responsável: '+_rf if _rf else '')))
                sub['subids'].append(neto['id']); k+=1

# validação
err=[]
byid={r['id']:r for r in rows}
for r in rows:
    if not r['nome']: err.append('linha sem nome: %s'%r['id'])
    for s in r['subids']:
        if s not in byid: err.append('subid inexistente %s em %s'%(s,r['id']))
    if r['due']:
        dt=datetime.date.fromisoformat(r['due'])
        if dt.weekday()>=5 or dt in m.FERIADOS: err.append('data inválida em '+r['nome'])
filhos_ref=[s for r in rows for s in r['subids']]
if len(filhos_ref)!=len(set(filhos_ref)): err.append('alguma linha é filha de dois pais')
raiz=[r for r in rows if r['id'] not in set(filhos_ref)]
print('LINHAS:',len(rows),'| tarefas raiz:',len(raiz),'| relações pai-filho:',len(filhos_ref))
from collections import Counter
cc=Counter(r['resp'] for r in rows if r['resp'])
print('com e-mail :', sum(v for k,v in cc.items() if EMAIL.get(k)))
print('SEM e-mail :', {k:v for k,v in cc.items() if not EMAIL.get(k)})
print('ERROS:', err[:5] if err else 'nenhum')

f=io.open('plano/IMPORTAR-NO-CLICKUP-nao-alunos.csv','w',encoding='utf-8-sig',newline='')
w=csv.writer(f)   # virgula: padrao do importador
w.writerow(['Task ID','Task Name','Subtask IDs','Assignee','Start Date','Due Date','Desafio Black Friday','Description'])
for r in rows:
    w.writerow([r['id'], r['nome'], ','.join(str(i) for i in r['subids']),
                EMAIL.get(r['resp'],''), r['ini'], r['due'], r['grupo'], r['desc']])
f.close()

# arquivo espelho, legivel, com os NOMES em vez de e-mail
f2=io.open('plano/CONFERENCIA-nao-alunos.csv','w',encoding='utf-8-sig',newline='')
w2=csv.writer(f2,delimiter=';')
w2.writerow(['Task ID','Tarefa / Subtarefa','Subtask IDs','Responsável','Início','Entrega','Grupo'])
for r in rows:
    ident='' if not r['subids'] and r['resp'] else ''
    w2.writerow([r['id'], r['nome'], ','.join(str(i) for i in r['subids']),
                 r['resp'] or '—', r['ini'], r['due'], r['grupo']])
f2.close()

import datetime as _dt, collections
PT=['seg','ter','qua','qui','sex','sáb','dom']
for quem in ('Hugo','Apoena','Felipe'):
    itens=[r for r in rows if r['resp']==quem]
    itens.sort(key=lambda r: r['due'])
    por=collections.OrderedDict()
    for r in itens:
        dt=_dt.date.fromisoformat(r['due'])
        seg=dt-_dt.timedelta(days=dt.weekday())
        por.setdefault(seg,[]).append((dt,r))
    L=[f'*BLACK FRIDAY — DEMANDAS {quem.upper()}*',
       f'_{len(itens)} entregas · lista Não alunos · aula magna 09/11_','']
    for seg,lst in por.items():
        L.append(f'*Semana de {seg.strftime("%d/%m")}*')
        for dt,r in lst:
            pai=next((p["nome"] for p in rows if r["id"] in p["subids"]), '')
            L.append(f'{dt.strftime("%d/%m")} {PT[dt.weekday()]} — {r["nome"]}')
            if pai: L.append(f'      ({pai})')
        L.append('')
    io.open(f'plano/WHATSAPP-{quem}.txt','w',encoding='utf-8').write('\n'.join(L))
    print(f'WHATSAPP-{quem}.txt: {len(itens)} entregas')
print('gerados os arquivos')
