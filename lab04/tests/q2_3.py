test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Is there something else we should remember about how
          >>> # to change a variable?  Maybe we need to set it again?
          >>> disemvowel("Datascience rules!") != "Datascience rules!"
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> disemvowel("Datascience rules!") == "Dtscnc rls!"
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
