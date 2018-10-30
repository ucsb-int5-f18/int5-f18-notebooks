test = {
  'name': 'Question17',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> import numpy as np
          >>> isinstance(high_farmers_avg_income, int) or isinstance(high_farmers_avg_income, float) or isinstance(high_farmers_avg_income, np.float64) or isinstance(high_farmers_avg_income, np.int64)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> import numpy as np
          >>> isinstance(low_farmers_avg_income, int) or isinstance(low_farmers_avg_income, float) or isinstance(low_farmers_avg_income, np.float64) or isinstance(low_farmers_avg_income, np.int64)
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
