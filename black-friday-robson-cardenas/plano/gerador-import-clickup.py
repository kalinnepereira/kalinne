# -*- coding: utf-8 -*-
import csv, io, datetime, importlib.util, sys
spec=importlib.util.spec_from_file_location('na','/tmp/claude-0/-home-user-kalinne/551a68f2-8a04-57df-8862-4790fa3213ad/scratchpad/na.py')
m=importlib.util.module_from_spec(spec)
_out=io.StringIO(); _o=sys.stdout; sys.stdout=_out
spec.loader.exec_module(m); sys.stdout=_o

T=m.T; uteis=m.uteis; resp=m.resp
def isoD(x): return x.strftime('%Y-%m-%d')

# e-mails do time — a preencher
EMAIL={'Kalinne':'','Henri':'','Nayara':'','Hugo':'','Isadora':'','Apoena':'',
       'Maytte':'','Ericson':'','Jota':'','Robson + Nayara':'','—':''}

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
        sub=novo(nome=nome, grupo=x['g'], due=isoD(dia),
                 resp=('' if tipo=='P' else resp(nome)))
        pai['subids'].append(sub['id']); k+=1
        if filhos:
            for fnome in filhos:
                dia=dias[min(int(round(k*(len(dias)-1)/max(total-1,1))), len(dias)-1)]
                neto=novo(nome=fnome, grupo=x['g'], due=isoD(dia), resp=resp(fnome))
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
print('gerados os 2 arquivos')
