test = {
  'name': 'Question14',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> income.num_rows
          1482
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> int(max(income.column('returns')))
          44600
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> special_zip == "99999"
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
