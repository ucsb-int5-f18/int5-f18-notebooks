test = {
  'name': '4.1.1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Fill in the line
          >>> # num_horizontal_blocks = ...
          >>> # in the cell above. 
          >>> num_horizontal_blocks != ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Remember to compute the absolute value of 2-15.  Traveling 
          >>> # "-13 blocks" doesn't really make sense!
          >>> num_horizontal_blocks != -13
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> num_horizontal_blocks
          13
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sannic_freebirds_distance
          1175
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
