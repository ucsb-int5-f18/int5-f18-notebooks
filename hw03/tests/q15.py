test = {
  'name': 'Question15',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> import numpy as np
          >>> isinstance(avg_prop, int) or isinstance(avg_prop, float) or isinstance(avg_prop, np.float64) or isinstance(avg_prop, np.int64)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> import numpy as np
          >>> income.num_columns
          5
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
