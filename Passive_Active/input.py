# *** what I think will be ok for input structure is like this dict. ***
# Number of Soil Layer can be 4 for every side ( active or passive )
input_values = {
    'information': {'title': '1', 'jobNo': '1', 'designer': '1', 'checker': '11', 'company': '1', 'client': '1',
                    'unit': 'us', 'date': None, 'comment': None, 'other': None}, 'product_id': 25, 'user_id': 44,
    'data': {'Active Side': {'Number of Soil Layer': {'value': '2', 'unit': 'ft'}, 'Δh': {'value': '0.1', 'unit': None},
                             'Theory': {
                                 'value': '{"id":1237,"item":"Rankine","section_product_item":"37_84"}', 'unit': None},
                             'H': {'value': '0', 'unit': None}, 'ɣ': {'value': '1', 'unit': 'ft'},
                             'ɸ': {'value': '0', 'unit': None},
                             'Theory ': {'value': '{"id":1243,"item":"Coulomb","section_product_item":"37_84"}',
                                         'unit': None},
                             'H ': {'value': '0', 'unit': None}, 'ɣ ': {'value': '1', 'unit': 'ft'},
                             'ɸ ': {'value': '0', 'unit': None}, 'δ ': {'value': '0', 'unit': None}},
             'Passive Side': {'Number of Soil Layer': {'value': '2', 'unit': 'ft'},
                              'Δh': {'value': '0.1', 'unit': None},
                              'Theory': {
                                  'value': '{"id":1237,"item":"Rankine","section_product_item":"37_84"}', 'unit': None},
                              'H': {'value': '0', 'unit': None}, 'ɣ': {'value': '1', 'unit': 'ft'},
                              'ɸ': {'value': '0', 'unit': None},
                              'Theory ': {'value': '{"id":1243,"item":"Coulomb","section_product_item":"37_84"}',
                                          'unit': None},
                              'H ': {'value': '0', 'unit': None}, 'ɣ ': {'value': '1', 'unit': 'ft'},
                              'ɸ ': {'value': '0', 'unit': None}, 'δ ': {'value': '0', 'unit': None}}},
    'type': 1, 'number_of_projects': 1}
