test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Even proportions equal to 0 are important!
          >>> # The array you calculated should have a couple 0's in it.
          >>> apply_q5 != 1
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Our calculation is only looking at the Cash Pay and
          >>> # the Total Pay ($) columns, not any others.
          >>> apply_q5 != 2
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # The nan you see is actually a result of the division.
          >>> # We aren't dividing a nan.
          >>> apply_q5 != 4
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> apply_q5 == 3
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
