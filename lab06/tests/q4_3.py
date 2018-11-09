test = {
  'name': 'Question43',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> min(sixes) >= 0
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> max(sixes) <= 6
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(sixes)
          100000
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
