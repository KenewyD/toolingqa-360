import pytest
from qa_core import validate_tool, assign_tool, return_tool

@pytest.fixture
def available():
    return {'reference':'A-001','designation':'Outil','statut':'Disponible','affectation':''}

def test_valid_tool(available):
    assert validate_tool(available) == []

def test_missing_reference(available):
    available['reference'] = ''
    assert 'Référence obligatoire' in validate_tool(available)

def test_missing_designation(available):
    available['designation'] = ''
    assert 'Désignation obligatoire' in validate_tool(available)

def test_invalid_status(available):
    available['statut'] = 'Perdu'
    assert 'Statut invalide' in validate_tool(available)

def test_assigned_without_beneficiary(available):
    available['statut'] = 'Affecté'
    assert validate_tool(available)

def test_maintenance_with_assignment(available):
    available.update(statut='Maintenance', affectation='Atelier')
    assert validate_tool(available)

def test_assign(available):
    result = assign_tool(available,'Atelier A')
    assert result['statut'] == 'Affecté' and result['affectation'] == 'Atelier A'

def test_assign_blank_beneficiary(available):
    with pytest.raises(ValueError): assign_tool(available,'  ')

def test_cannot_assign_twice(available):
    with pytest.raises(ValueError): assign_tool(assign_tool(available,'Atelier A'),'Atelier B')

def test_return(available):
    result = return_tool(assign_tool(available,'Atelier A'))
    assert result['statut'] == 'Disponible' and result['affectation'] == ''

def test_cannot_return_available(available):
    with pytest.raises(ValueError): return_tool(available)
