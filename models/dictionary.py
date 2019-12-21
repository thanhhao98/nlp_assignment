UNKOWN_TOKEN = 'x'
DB_PATH = './input/database.txt'
TOKENS = [
    ('thời gian', 'n_t'),
    ('thành phố', 'n_loc'),
    ('đà nẵng', 'loc'),
    ('hồ chí minh', 'loc'),
    ('huế', 'loc'),
    ('đi', 'v'),
    ('xe', 'pre_n_tra'),
    ('bus', 'sul_n_tra'),
    ('từ', 'prn_l_source'),
    ('lúc', 'prn_t'),
    ('nào', 'w'),
    ('đến', 'v'),
    ('hr', 't_unit'),
    ('\?', 'w'),
    (r'^[0-9][0-9]?:[0-9][0-9]?', 't'),
    (r'^[a-z][0-9]', 'id'),
]

PARTERNS = {
    'loc': [
        [['n_loc', 'loc'], 1]
    ],
    't': [
        [['t', 't_unit'], 0],
        [['prn', 't'], 1]
    ],
    'n_tra': [
        [['pre_n_tra', 'sul_n_tra'], 1],
        [['sul_n_tra'], 0],
        [['pre_n_tra'], 0],
    ],
    'id': [
        [['n_tra', 'id'], 1]
    ],
    'wh_tra': [
        [['n_tra', 'w'], 0]
    ],
    'wh_t': [
        [['n_t', 'w'], 0]
    ],
    's_loc': [
        [['prn_l_source', 'loc'], 1],
        [['prn_l_source', 'n_loc', 'loc'], 2],
    ],
    'v': [
        [['v', 'v'], 1]
    ]

}


RELATIONS = {
    'WH_TRA': [
        ['w', 'n_tra'],
        ['wh_tra']
    ],
    'WH_T': [
        ['w', 'n_t'],
        ['wh_t']
    ],
    'PRED': [
        ['v'],
    ],
    'AGENT': [
        ['v', 'id']
    ],
    'TO_LOC': [
        ['v', 'loc']
    ],
    'FROM_LOC': [
        ['v', 's_loc']
    ],
    'FROM_TIME': [
        ['s_loc', 't']
    ],
    'ARRIVE_TIME': [
        ['prn_t', 't'],
        ['loc', 't']
    ],
}

MAP_RELATION_TO_DB = {
    'PRED': [

    ],
    'WH_TRA': [
        [
            'PRINT-ALL',
            '?b',
        ],
    ],
    'WH_T': [
        [
            'PRINT-ALL',
            '?t',
        ],
    ],
    'AGENT': [
        [
            'BUS',
            '*1b'
        ]
    ],
    'TO_LOC': [
        [
            'ATIME',
            '?b',
            '*1l',
            '?t',
        ],
        [
            'RUN-TIME',
            '?b',
            '?l',
            '*1l',
            '?t',
        ],
    ],
    'FROM_LOC': [
        [
            'DTIME',
            '?b',
            '*1l',
            '?t',
        ],
        [
            'RUN-TIME',
            '?b',
            '*1l',
            '?l',
            '?t',
        ],
    ],
    'FROM_TIME': [
        [
            'DTIME',
            '?b',
            '?l',
            '*1t',
        ],
    ],
    'ARRIVE_TIME': [
        [
            'ATIME',
            '?b',
            '?l',
            '*1t',
        ],
    ]
}
