from inoft_vocal_framework.exceptions import raise_if_variable_not_expected_type


class Tracks:
    def __init__(self):
        self._name = None
        self._color = None
        self._gain = None
        self._pan = None
        self._muted = None
        self._solo = None
        self._length = None
        self._buffer = None
        self._file = None
        'name': 'Track 1',
        'color': '#00a0b0',
        'gain': 1,
        'pan': 0.5,
        'muted': False,
        'solo': False,
        'length': 1920,
        'buffer': {},
        'file': {}


class Collections:
    def __init__(self):
        self._Tracks = None

    @property
    def Tracks(self) -> Tracks:
        return self._Tracks

    @Tracks.setter
    def Tracks(self, tracks: Tracks) -> None:
        raise_if_variable_not_expected_type(value=tracks, expected_type=, variable_name="Tracks")
        self._Tracks = tracks


class Audiee:
    def __init__(self):
        self._Collections = None

    @property
    def Collections(self) -> Collections:
        return self._Collections

    @Collections.setter
    def Collections(self, collections: Collections) -> None:
        raise_if_variable_not_expected_type(value=collections, expected_type=Collections, variable_name="Collections")
        self._Collections = Collections

"""
{
  'Collections': {
    'Tracks': [{
      'name': 'Track 1',
      'color': '#00a0b0',
      'gain': 1,
      'pan': 0.5,
      'muted': False,
      'solo': False,
      'length': 1920,
      'buffer': {},
      'file': {}
    }, {
      'name': 'Track 2',
      'color': '#00a0b0',
      'gain': 1,
      'pan': 0.5,
      'muted': False,
      'solo': False,
      'length': 1920,
      'buffer': {},
      'file': {}
    }]
  },
  'Models': {
    'Project': {
      'name': 'Untitled',
      'created': 1593993804257,
      'user': 'Guest',
      'changed': False
    }
  },
  'Views': {
    'Editor': {
      'cid': 'view1',
      'model': {
        'name': 'Untitled',
        'created': 1593993804257,
        'user': 'Guest',
        'changed': False
      },
      'options': {
        'model': {
          'name': 'Untitled',
          'created': 1593993804257,
          'user': 'Guest',
          'changed': False
        }
      },
      'moving': False
    },
    'Timeline': {
      'cid': 'view2',
      'options': {},
      '_callbacks': {
        'Audiee:scroll': {
          'next': {
            'next': {}
          },
          'tail': {}
        },
        'Audiee:zoomChange': {
          'next': {
            'next': {}
          },
          'tail': {}
        }
      }
    },
    'Tracks': {
      'cid': 'view3',
      'collection': [{
        'name': 'Track 1',
        'color': '#00a0b0',
        'gain': 1,
        'pan': 0.5,
        'muted': False,
        'solo': False,
        'length': 1920,
        'buffer': {},
        'file': {}
      }, {
        'name': 'Track 2',
        'color': '#00a0b0',
        'gain': 1,
        'pan': 0.5,
        'muted': False,
        'solo': False,
        'length': 1920,
        'buffer': {},
        'file': {}
      }],
      'el': {},
      'options': {
        'collection': [{
          'name': 'Track 1',
          'color': '#00a0b0',
          'gain': 1,
          'pan': 0.5,
          'muted': False,
          'solo': False,
          'length': 1920,
          'buffer': {},
          'file': {}
        }, {
          'name': 'Track 2',
          'color': '#00a0b0',
          'gain': 1,
          'pan': 0.5,
          'muted': False,
          'solo': False,
          'length': 1920,
          'buffer': {},
          'file': {}
        }],
        'el': '#tracks'
      },
      '_callbacks': {
        'Audiee:scroll': {
          'next': {
            'next': {}
          },
          'tail': {}
        },
        'Audiee:zoomChange': {
          'next': {
            'next': {}
          },
          'tail': {}
        }
      }
    },
    'PlaybackControls': {
      'cid': 'view5',
      'model': {
        'name': 'Untitled',
        'created': 1593993804257,
        'user': 'Guest',
        'changed': False
      },
      'options': {
        'model': {
          'name': 'Untitled',
          'created': 1593993804257,
          'user': 'Guest',
          'changed': False
        }
      },
      'pressingKey': False
    },
    'Menu': {
      'cid': 'view6',
      'options': {},
      'hotkeysEnabled': True
    }
  },
  'Display': {
    'zoomLevel': 1,
    'scale': 20,
    'subpixels': 5,
    'playbackCursorFollowing': True
  },
  'Player': {
    'context': {},
    'nodes': [],
    'gainNodes': {
      'c7': {},
      'c17': {}
    },
    'playing': False
  }
}
"""