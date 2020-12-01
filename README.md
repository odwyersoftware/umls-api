# umls-api

Python client for https://documentation.uts.nlm.nih.gov/rest/home.html

## Installation

```bash
pip install umls-api
```

## Example Usage

Get CUI.

```python
import umls_api

resp = umls_api.API(api_key='<UMLS_API_KEY_HERE>').get_cui(cui='C0007107')
print(res)
{
	'pageCount': 1,
	'pageNumber': 1,
	'pageSize': 25,
	'result': {
		'atomCount': 247,
		'atoms': 'https://uts-ws.nlm.nih.gov/rest/content/2020AB/CUI/C0007107/atoms',
		'attributeCount': 0,
		'classType': 'Concept',
		'cvMemberCount': 0,
		'dateAdded': '09-30-1990',
		'defaultPreferredAtom': 'https://uts-ws.nlm.nih.gov/rest/content/2020AB/CUI/C0007107/atoms/preferred',
		'definitions': 'https://uts-ws.nlm.nih.gov/rest/content/2020AB/CUI/C0007107/definitions',
		'majorRevisionDate': '06-25-2020',
		'name': 'Malignant neoplasm of larynx',
		'relationCount': 17,
		'relations': 'https://uts-ws.nlm.nih.gov/rest/content/2020AB/CUI/C0007107/relations',
		'semanticTypes': [{
			'name': 'Neoplastic Process',
			'uri': 'https://uts-ws.nlm.nih.gov/rest/semantic-network/2020AB/TUI/T191'
		}],
		'status': 'R',
		'suppressible': False,
		'ui': 'C0007107'
	}
```

Get TUI.

```python
import umls_api

resp = umls_api.API(api_key='<UMLS_API_KEY_HERE>').get_tui(cui='T047')
print(resp)
{
	'pageCount': 1,
	'pageNumber': 1,
	'pageSize': 25,
	'result': {
		'abbreviation': 'dsyn',
		'childCount': 2,
		'classType': 'SemanticType',
		'definition': 'A condition which alters or interferes with a '
		'normal process, state, or activity of an organism. '
		'It is usually characterized by the abnormal '
		"functioning of one or more of the host's systems, "
		'parts, or organs. Included here is a complex of '
		'symptoms descriptive of a disorder.',
		'example': 'NONE',
		'name': 'Disease or Syndrome',
		'nonHuman': 'NONE',
		'semanticTypeGroup': {
			'abbreviation': 'DISO',
			'classType': 'SemanticGroup',
			'expandedForm': 'Disorders',
			'semanticTypeCount': 12
		},
		'treeNumber': 'B2.2.1.2.1',
		'ui': 'T047',
		'usageNote': 'Any specific disease or syndrome that is modified by '
		'such modifiers as "acute", "prolonged", etc. will '
		'also be assigned to this type. If an anatomic '
		'abnormality has a pathologic manifestation, then it '
		'will be given this type as well as a type from the '
		"'Anatomical Abnormality' hierarchy, e.g., "
		'"Diabetic Cataract" will be double-typed for this '
		'reason.'
	}
}
```

If you wish to add support for other API endpoints on UMLS, they are very simple to add.

Pull requests (with tests) are very welcome.

## Running the tests

```bash
pip install -r requirements-dev.txt
pytest src/tests
flake8
```
