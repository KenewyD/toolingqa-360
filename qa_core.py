"""Règles de gestion d'une application fictive d'outillage aéronautique."""
from datetime import date

VALID_STATUSES = {'Disponible', 'Affecté', 'Maintenance'}


def validate_tool(tool):
    errors = []
    if not str(tool.get('reference', '')).strip():
        errors.append('Référence obligatoire')
    if not str(tool.get('designation', '')).strip():
        errors.append('Désignation obligatoire')
    if tool.get('statut') not in VALID_STATUSES:
        errors.append('Statut invalide')
    if tool.get('statut') == 'Affecté' and not str(tool.get('affectation', '')).strip():
        errors.append('Affectation obligatoire pour un outil affecté')
    if tool.get('statut') == 'Maintenance' and str(tool.get('affectation', '')).strip():
        errors.append('Un outil en maintenance ne peut pas être affecté')
    return errors


def can_assign(tool):
    return tool['statut'] == 'Disponible'


def assign_tool(tool, person):
    if not can_assign(tool):
        raise ValueError('Seul un outil disponible peut être affecté')
    if not person.strip():
        raise ValueError('Bénéficiaire obligatoire')
    return {**tool, 'statut': 'Affecté', 'affectation': person.strip()}


def return_tool(tool):
    if tool['statut'] != 'Affecté':
        raise ValueError('Seul un outil affecté peut être retourné')
    return {**tool, 'statut': 'Disponible', 'affectation': ''}
