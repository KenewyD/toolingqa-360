import streamlit as st
import pandas as pd
from qa_core import assign_tool, return_tool, validate_tool

st.set_page_config(page_title='ToolingQA 360', page_icon='🛠️', layout='wide')
st.title('🛠️ ToolingQA 360')
st.caption('Démonstration indépendante et fictive de recette logicielle — non affiliée à Dedienne Aerospace / ToolLive')
if 'tools' not in st.session_state:
    st.session_state.tools = [
        {'reference':'TL-001','designation':'Clé dynamométrique','statut':'Disponible','affectation':''},
        {'reference':'TL-002','designation':'Banc de contrôle','statut':'Affecté','affectation':'Atelier A'},
        {'reference':'TL-003','designation':'Calibre de mesure','statut':'Maintenance','affectation':''},
        {'reference':'TL-004','designation':'Kit de montage','statut':'Disponible','affectation':''},
    ]

tab1, tab2, tab3 = st.tabs(['Inventaire & opérations','Tableau de bord QA','À propos de la recette'])
with tab1:
    st.subheader('Inventaire fictif')
    search = st.text_input('Rechercher une référence ou une désignation')
    filtered = [t for t in st.session_state.tools if search.lower() in (t['reference']+' '+t['designation']).lower()]
    st.dataframe(pd.DataFrame(filtered), use_container_width=True, hide_index=True)
    st.subheader('Ajouter un outillage')
    with st.form('add'):
        a,b,c = st.columns(3)
        ref = a.text_input('Référence')
        name = b.text_input('Désignation')
        status = c.selectbox('Statut', ['Disponible','Affecté','Maintenance'])
        assignment = st.text_input('Affectation (si affecté)')
        submitted = st.form_submit_button('Enregistrer')
        if submitted:
            new = {'reference':ref.strip(),'designation':name.strip(),'statut':status,'affectation':assignment.strip()}
            errors = validate_tool(new)
            if any(t['reference'].lower() == ref.strip().lower() for t in st.session_state.tools):
                errors.append('Référence déjà utilisée')
            if errors:
                st.error(' ; '.join(errors))
            else:
                st.session_state.tools.append(new)
                st.success('Outillage ajouté')
                st.rerun()
    st.subheader('Affecter / retourner un outillage')
    selected = st.selectbox('Outillage', [t['reference'] for t in st.session_state.tools])
    person = st.text_input('Bénéficiaire / atelier')
    left, right = st.columns(2)
    def locate():
        return next(i for i,t in enumerate(st.session_state.tools) if t['reference'] == selected)
    if left.button('Affecter'):
        try:
            i=locate(); st.session_state.tools[i] = assign_tool(st.session_state.tools[i], person)
            st.success('Affectation enregistrée'); st.rerun()
        except ValueError as exc:
            st.error(str(exc))
    if right.button('Enregistrer le retour'):
        try:
            i=locate(); st.session_state.tools[i] = return_tool(st.session_state.tools[i])
            st.success('Retour enregistré'); st.rerun()
        except ValueError as exc:
            st.error(str(exc))
with tab2:
    st.subheader('Indicateurs d’inventaire (données de démonstration)')
    counts = pd.Series([t['statut'] for t in st.session_state.tools]).value_counts()
    cols = st.columns(4)
    cols[0].metric('Outillages', len(st.session_state.tools))
    for i, status in enumerate(['Disponible','Affecté','Maintenance'],1):
        cols[i].metric(status, int(counts.get(status,0)))
    st.bar_chart(counts)
    st.info('Les indicateurs de campagne QA figurent dans le dossier docs/. Aucun résultat de test réel n’est inventé.')
with tab3:
    st.markdown('''### Périmètre
Application **fictive** conçue pour illustrer une démarche de testeur logiciel : exigences, cas de tests, anomalies, non-régression et automatisation.

**À tester :** unicité des références, champs obligatoires, transitions de statut, recherche et indicateurs.

Les données sont conservées dans la session Streamlit, pas dans une base de production. Les identifiants sont inventés.''')
