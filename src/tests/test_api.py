import os

import pytest
from pytest_voluptuous import S

import umls_api

UMLS_API_KEY = os.environ['UMLS_API_KEY']
CUI = 'C0007107'
TUI = 'T047'
TERM = 'Malignant neoplasm of larynx'


class TestAuth:
    def test_get_single_use_service_ticket(self):
        auth = umls_api.Auth(api_key=UMLS_API_KEY)

        result = auth.get_single_use_service_ticket()

        assert isinstance(result, str)
        assert len(result) == 35
        assert result.startswith('ST-')


class TestAPI:
    def test_get_cui(self):
        result = umls_api.API(api_key=UMLS_API_KEY).get_cui(cui=CUI)

        assert result == S({
            'pageCount': int,
            'pageNumber': int,
            'pageSize': int,
            'result': {
                'atomCount': int,
                'atoms': str,
                'attributeCount': int,
                'classType': 'Concept',
                'cvMemberCount': int,
                'dateAdded': '09-30-1990',
                'defaultPreferredAtom': str,
                'definitions': str,
                'majorRevisionDate': str,
                'name': 'Malignant neoplasm of larynx',
                'relationCount': int,
                'relations': str,
                'semanticTypes': [{
                    'name': 'Neoplastic Process',
                    'uri': str,
                }],
                'status': str,
                'suppressible': bool,
                'ui': 'C0007107'
            }
        })

    def test_get_tui(self):
        result = umls_api.API(api_key=UMLS_API_KEY).get_tui(tui=TUI)

        assert result == S({
            'pageCount': int,
            'pageNumber': int,
            'pageSize': int,
            'result': {
                'abbreviation': 'dsyn',
                'childCount': 2,
                'classType': 'SemanticType',
                'definition': str,
                'example': str,
                'name': 'Disease or Syndrome',
                'nonHuman': str,
                'semanticTypeGroup': {
                    'abbreviation': 'DISO',
                    'classType': 'SemanticGroup',
                    'expandedForm': 'Disorders',
                    'semanticTypeCount': int
                },
                'treeNumber': str,
                'ui': 'T047',
                'usageNote': str
            }
        })

    def test_get_term(self):
        result = umls_api.API(api_key=UMLS_API_KEY).term_search(TERM, umls_api.SearchType.NORMALIZED_STRING)

        assert result == S({
            'pageNumber': int,
            'pageSize': int,
            'result': {
                'classType': 'searchResults',
                'results': [
                    {
                        'ui': 'C0007107',
                        'rootSource': str,
                        'name': 'Malignant neoplasm of larynx',
                        'uri': str

                    }
                ]
            }
        })
