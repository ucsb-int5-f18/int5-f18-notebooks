test = {
  'name': 'Question41',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> import numpy as np
          >>> len(my_dice)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> min(my_dice) >= 1
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> max(my_dice) <= 6
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
