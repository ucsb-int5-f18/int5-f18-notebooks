test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> (table_reaction == 'Yes!') or (table_reaction == 'Bleh.') or (table_reaction == 'Alright!')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> (result == 'Yes!') or (result == 'Bleh.') or (result == 'Alright!')
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
