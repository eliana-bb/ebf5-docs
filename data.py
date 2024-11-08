equips = {
    "heavensgate": {
        "SID": "heavensgate",
        "type": "SWORD",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            15,
            30,
            40,
            50,
            65
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            15,
            30,
            40,
            50,
            65
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            5,
            5,
            10,
            10
        ],
        "resistance": {
            "holy": "long50",
            "weak": "long100",
            "dispel": "long100"
        },
        "element": "Element.HOLY",
        "statusEffect": "Status.NONE",
        "buffEffect": "Stats.NONE",
        "specials": [
            [
                "Equip.BOOST",
                "Element.HOLY"
            ],
            None,
            [
                "Equip.CAST",
                "Spells.holysword",
                0.2
            ],
            None,
            [
                "Equip.COUNTER",
                "Spells.unleash"
            ]
        ],
        "materials": [
            [
                "Items.feather",
                3
            ],
            [
                "Items.steel",
                4
            ],
            [
                "Items.gold",
                2,
                "Items.steel",
                4
            ],
            [
                "Items.mythril",
                1,
                "Summons.MirrorAngel",
                1
            ]
        ]
    },
    "inferno": {
        "SID": "inferno",
        "type": "SWORD",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            15,
            25,
            35,
            45,
            60
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            15,
            25,
            35,
            45,
            60
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            5,
            10,
            15
        ],
        "evade": [
            0,
            0,
            5,
            10,
            15
        ],
        "resistance": {
            "bomb": "long50",
            "ice": "long50",
            "freeze": "long100"
        },
        "element": "Element.FIRE",
        "statusEffect": "Status.BURN",
        "statusChance": [
            30,
            50,
            70,
            85,
            100
        ],
        "statusDegree": [
            2,
            2,
            2,
            3,
            3
        ],
        "buffEffect": "Stats.NONE",
        "buffChance": [
            0
        ],
        "buffDegree": [
            0
        ],
        "specials": [
            [
                "Equip.BOOST",
                "Element.FIRE"
            ],
            None,
            [
                "Equip.CAST",
                "Spells.fume",
                0.4
            ]
        ],
        "materials": [
            [
                "Items.glass",
                2
            ],
            [
                "Items.magma",
                4
            ],
            [
                "Items.magma",
                4,
                "Items.ruby",
                2
            ],
            [
                "Summons.FallenBurned",
                1,
                "Items.magma",
                8,
                "Items.ruby",
                2
            ]
        ]
    },
    "chopper": {
        "SID": "thechopper",
        "type": "SWORD",
        "HP": [
            5,
            5,
            10,
            10,
            10
        ],
        "attack": [
            20,
            30,
            40,
            50,
            60
        ],
        "defence": [
            5,
            10,
            15,
            15,
            20
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            5,
            10,
            15,
            15,
            20
        ],
        "accuracy": [
            -5,
            -5,
            -5,
            -5,
            -5
        ],
        "evade": [
            -5,
            -5,
            -5,
            -5,
            -5
        ],
        "resistance": {
            "water": "long50",
            "bio": "long50"
        },
        "element": "Element.EARTH",
        "statusEffect": "Status.NONE",
        "buffEffect": "Stats.NONE",
        "specials": [
            [
                "Equip.SCARE",
                "Foe.TREES"
            ],
            None,
            [
                "Equip.CAST",
                "Spells.log",
                1
            ],
            None,
            [
                "Equip.BOOST",
                "Element.EARTH"
            ]
        ],
        "materials": [
            [
                "Items.wood",
                2
            ],
            [
                "Items.steel",
                4
            ],
            [
                "Items.steel",
                15,
                "Items.emerald",
                3
            ],
            [
                "Items.titanium",
                1,
                "Items.wood",
                30
            ]
        ]
    },
    "sapphiresaint": {
        "SID": "sapphiresaint",
        "type": "SWORD",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            15,
            30,
            45,
            60,
            75
        ],
        "defence": [
            0,
            5,
            10,
            15,
            20
        ],
        "magicAttack": [
            0,
            5,
            10,
            15,
            20
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "holy": "long50",
            "fire": "long50",
            "burn": "long100"
        },
        "element": "Element.WATER",
        "buffEffect": "Stats.NONE",
        "statusEffect": "Status.WET",
        "statusChance": [
            30,
            40,
            60,
            80,
            100
        ],
        "statusDegree": [
            1,
            1,
            2,
            2,
            2
        ],
        "specials": [
            [
                "Equip.BOOST",
                "Element.WATER"
            ],
            None,
            [
                "Equip.CAST",
                "Spells.pouringpike",
                0.35
            ]
        ],
        "materials": [
            [
                "Items.glass",
                1
            ],
            [
                "Items.ice",
                1,
                "Items.water",
                1
            ],
            [
                "Items.rune2",
                2,
                "Items.sapphire",
                1
            ],
            [
                "Items.diamond",
                1,
                "Items.sapphire",
                3
            ]
        ]
    },
    "giantslayer": {
        "SID": "giantslayer",
        "type": "SWORD",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            40,
            60,
            80,
            100,
            120
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            -30,
            -30,
            -30,
            -30,
            -30
        ],
        "evade": [
            -10,
            -10,
            -10,
            -10,
            -10
        ],
        "resistance": {
            "wind": "long50",
            "stagger": "long100",
            "weight": "long100"
        },
        "element": "Element.NONE",
        "statusEffect": "Status.NONE",
        "buffEffect": "Stats.NONE",
        "specials": [
            [
                "Equip.IGNORE_BUFFS"
            ],
            None,
            [
                "Equip.INTIMIDATE"
            ],
            None,
            [
                "Equip.COUNTER",
                "Spells.slash"
            ]
        ],
        "materials": [
            [
                "Items.iron",
                2
            ],
            [
                "Items.iron",
                2,
                "Items.pipe",
                2
            ],
            [
                "Items.steel",
                25,
                "Items.pipe",
                5
            ],
            [
                "Items.titanium",
                1,
                "Items.steel",
                15,
                "Items.iron",
                10
            ]
        ]
    },
    "iceneedle": {
        "SID": "iceneedle",
        "type": "SWORD",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            15,
            30,
            45,
            60,
            75
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            15,
            30,
            40,
            50,
            60
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "ice": "long50",
            "water": "long50",
            "wet": "long100"
        },
        "element": "Element.ICE",
        "statusEffect": "Status.FREEZE",
        "statusChance": [
            10,
            10,
            15,
            15,
            25
        ],
        "statusDegree": [
            2,
            2,
            2,
            2,
            2
        ],
        "buffEffect": "Stats.NONE",
        "specials": [
            [
                "Equip.BOOST",
                "Element.ICE"
            ],
            None,
            [
                "Equip.CAST",
                "Spells.frostfragment",
                0.33
            ]
        ],
        "materials": [
            [
                "Items.snowball",
                3
            ],
            [
                "Items.ice",
                1,
                "Items.water",
                1
            ],
            [
                "Items.sapphire",
                3,
                "Items.ice",
                2,
                "Items.water",
                2
            ],
            [
                "Items.sapphire",
                10,
                "Items.ice",
                10,
                "Items.water",
                10
            ]
        ]
    },
    "hyperdrill": {
        "SID": "hypderdrill",
        "type": "SWORD",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            20,
            35,
            50,
            70,
            85
        ],
        "defence": [
            0,
            0,
            0,
            5,
            10
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "earth": "long50",
            "thunder": "down30"
        },
        "element": "Element.EARTH",
        "buffEffect": "Stats.DEFENCE",
        "buffChance": [
            60,
            70,
            80,
            90,
            100
        ],
        "buffDegree": [
            -20,
            -25,
            -25,
            -25,
            -30
        ],
        "statusEffect": "Status.HEAVY",
        "statusChance": [
            30,
            40,
            60,
            80,
            100
        ],
        "statusDegree": [
            1,
            1,
            2,
            2,
            2
        ],
        "specials": [
            [
                "Equip.BOOST",
                "Element.EARTH"
            ],
            None,
            [
                "Equip.CAST",
                "Spells.stalactite2",
                0.25
            ],
            None,
            [
                "Equip.IGNORE_BUFFS"
            ]
        ],
        "materials": [
            [
                "Items.turd",
                4
            ],
            [
                "Items.steel",
                1,
                "Items.pipe",
                2
            ],
            [
                "Items.silver",
                5,
                "Items.pipe",
                2
            ],
            [
                "Items.titanium",
                1,
                "Items.silver",
                5,
                "Items.turd",
                50
            ]
        ]
    },
    "emeraldsmasher": {
        "SID": "emeraldsmasher",
        "type": "SWORD",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            20,
            30,
            45,
            60,
            70
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            20,
            30,
            45,
            60,
            70
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            -5,
            -5,
            -5,
            -5,
            -5
        ],
        "evade": [
            -5,
            -5,
            -5,
            -5,
            -5
        ],
        "resistance": {
            "earth": "long50",
            "bomb": "long50",
            "stagger": "long100"
        },
        "element": "Element.BIO",
        "statusEffect": "Status.STAGGER",
        "statusChance": [
            20,
            40,
            60,
            80,
            100
        ],
        "statusDegree": [
            2,
            2,
            2,
            2,
            2
        ],
        "buffEffect": "Stats.NONE",
        "specials": [
            [
                "Equip.BOOST",
                "Element.BIO"
            ],
            None,
            [
                "Equip.COUNTER",
                "Spells.nettleknife"
            ],
            None,
            [
                "Equip.CAST",
                "Spells.earthquake",
                0.3
            ]
        ],
        "materials": [
            [
                "Items.iron",
                2
            ],
            [
                "Items.iron",
                6,
                "Items.pipe",
                2
            ],
            [
                "Items.emerald",
                3,
                "Items.virus",
                3
            ],
            [
                "Items.titanium",
                1,
                "Items.emerald",
                3
            ]
        ]
    },
    "devilsfork": {
        "SID": "devilsfork",
        "type": "SWORD",
        "HP": [
            0,
            0,
            0,
            5,
            10
        ],
        "attack": [
            0,
            0,
            10,
            20,
            30
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            20,
            30,
            45,
            60,
            75
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "fire": "long50",
            "ice": "long50",
            "dark": "long50"
        },
        "element": "Element.FIRE",
        "statusEffect": "Status.DRY",
        "statusChance": [
            20,
            40,
            60,
            80,
            100
        ],
        "statusDegree": [
            2,
            2,
            2,
            3,
            3
        ],
        "buffEffect": "Stats.NONE",
        "specials": [
            [
                "Equip.SCARE",
                "Foe.SLIMES"
            ],
            [
                "Equip.BOOST_BUFFS",
                10
            ],
            [
                "Equip.CAST",
                "Spells.blackspikes",
                0.5
            ],
            None,
            [
                "Equip.BOOST",
                "Element.FIRE"
            ]
        ],
        "materials": [
            [
                "Items.iron",
                2
            ],
            [
                "Items.powder",
                2,
                "Items.magma",
                2
            ],
            [
                "Summons.SlimeLava",
                1,
                "Items.magma",
                8
            ],
            [
                "Summons.SlimeBigLava",
                1,
                "Items.magma",
                16
            ]
        ]
    },
    "berzerker": {
        "SID": "berzerker",
        "type": "SWORD",
        "HP": [
            0,
            0,
            5,
            10,
            15
        ],
        "attack": [
            40,
            50,
            60,
            75,
            100
        ],
        "defence": [
            0,
            0,
            5,
            10,
            15
        ],
        "magicAttack": [
            0,
            5,
            10,
            15,
            20
        ],
        "magicDefence": [
            0,
            0,
            5,
            10,
            15
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "earth": "long50",
            "wind": "long50",
            "weak": "long100"
        },
        "element": "Element.NONE",
        "statusEffect": "Status.DISPEL",
        "statusChance": [
            20,
            25,
            30,
            35,
            50
        ],
        "statusDegree": [
            1
        ],
        "buffEffect": "Stats.NONE",
        "specials": [
            [
                "Equip.STATUS",
                "Status.TIRED",
                1,
                0.5
            ],
            None,
            [
                "Equip.COUNTER",
                "Spells.revenge"
            ],
            None,
            [
                "Equip.BOOST",
                "Element.NONE"
            ]
        ],
        "materials": [
            [
                "Items.brick",
                5
            ],
            [
                "Items.brick",
                10,
                "Items.turd",
                10
            ],
            [
                "Items.rune2",
                5,
                "Items.brick",
                10
            ],
            [
                "Items.mythril",
                1,
                "Items.rune2",
                4
            ]
        ]
    },
    "ultrapro9000": {
        "SID": "ultrapro9000",
        "type": "SWORD",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            0,
            10,
            20,
            30,
            40
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            10,
            20,
            30,
            40
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            30,
            35,
            40,
            45,
            50
        ],
        "evade": [
            0,
            5,
            10,
            20,
            30
        ],
        "resistance": {
            "ice": "long50",
            "freeze": "long100",
            "water": "long50"
        },
        "element": "Element.NONE",
        "statusEffect": "Status.CHILL",
        "statusChance": [
            30,
            40,
            60,
            80,
            100
        ],
        "statusDegree": [
            2,
            2,
            2,
            3,
            3
        ],
        "buffEffect": "Stats.NONE",
        "specials": [
            None,
            None,
            [
                "Equip.STEAL"
            ],
            [
                "Equip.BOOST_STATUS"
            ],
            [
                "Equip.BOOST_FOOD"
            ]
        ],
        "materials": [
            [
                "Items.wood",
                1
            ],
            [
                "Items.wood",
                4
            ],
            [
                "Items.lego",
                1,
                "Items.leather",
                5
            ],
            [
                "Items.gamechild",
                1,
                "Items.chips",
                1,
                "Items.beer",
                1
            ]
        ]
    },
    "dragonfeather": {
        "SID": "dragonsfeather",
        "type": "SWORD",
        "HP": [
            -25,
            -25,
            -25,
            -25,
            -25
        ],
        "attack": [
            20,
            30,
            40,
            60,
            70
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            10,
            20,
            30,
            40,
            50
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            20,
            25,
            30,
            40,
            45
        ],
        "evade": [
            20,
            25,
            30,
            40,
            45
        ],
        "resistance": {
            "wind": "long50",
            "holy": "long50",
            "ice": "long50"
        },
        "element": "Element.WIND",
        "statusEffect": "Status.LIGHT",
        "statusChance": [
            30,
            40,
            60,
            80,
            100
        ],
        "statusDegree": [
            1,
            1,
            2,
            2,
            2
        ],
        "buffEffect": "Stats.NONE",
        "specials": [
            [
                "Equip.STATUS",
                "Status.HASTE",
                2,
                0.2
            ],
            [
                "Equip.BOOST",
                "Element.WIND"
            ],
            [
                "Equip.CAST",
                "Spells.gale",
                0.5
            ],
            None,
            [
                "Equip.COUNTER",
                "Spells.slash"
            ]
        ],
        "materials": [
            [
                "Items.shuriken",
                2
            ],
            [
                "Items.shuriken",
                8
            ],
            [
                "Summons.FallenLost",
                1
            ],
            [
                "Items.mythril",
                1,
                "Items.feather",
                4
            ]
        ]
    },
    "souleater": {
        "SID": "souleather",
        "type": "SWORD",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            70,
            90,
            110,
            130,
            150
        ],
        "defence": [
            -40,
            -40,
            -40,
            -40,
            -40
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            -40,
            -40,
            -40,
            -40,
            -40
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "holy": "down30",
            "dark": "down30"
        },
        "element": "Element.DARK",
        "statusEffect": "Status.CURSE",
        "statusChance": [
            30,
            40,
            50,
            60,
            70
        ],
        "statusDegree": [
            2,
            2,
            2,
            2,
            2
        ],
        "buffEffect": "Stats.NONE",
        "specials": [
            [
                "Equip.STATUS",
                "Status.CURSE",
                1,
                0.5
            ],
            None,
            [
                "Equip.COUNTER",
                "Spells.slash"
            ],
            None,
            [
                "Equip.DRAIN_HP"
            ]
        ],
        "materials": [
            [
                "Items.iron",
                3
            ],
            [
                "Items.claw",
                3
            ],
            [
                "Items.amber",
                4,
                "Items.spike",
                6
            ],
            [
                "Items.darkmatter",
                1,
                "Summons.MirrorDemon",
                1
            ]
        ]
    },
    "poisonfang": {
        "SID": "poisonfang",
        "type": "SWORD",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            10,
            20,
            30,
            40,
            55
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            10,
            20,
            30,
            40,
            55
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            5,
            10,
            15,
            20
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "dark": "long100",
            "bio": "long100",
            "curse": "long100"
        },
        "element": "Element.BIO",
        "statusEffect": "Status.POISON",
        "statusChance": [
            30,
            40,
            60,
            80,
            100
        ],
        "statusDegree": [
            2,
            3,
            3,
            3,
            4
        ],
        "buffEffect": "Stats.NONE",
        "specials": [
            [
                "Equip.BOOST",
                "Element.BIO"
            ],
            None,
            [
                "Equip.DRAIN_HP"
            ],
            None,
            [
                "Equip.CAST",
                "Spells.shreddingshrub",
                0.25
            ]
        ],
        "materials": [
            [
                "Items.shuriken",
                2
            ],
            [
                "Items.butterflywing",
                4
            ],
            [
                "Items.opal",
                1,
                "Items.butterflywing",
                6
            ],
            [
                "Items.opal",
                4,
                "Items.butterflywing",
                8
            ]
        ]
    },
    "lightningbolt": {
        "SID": "lightningbolt",
        "type": "SWORD",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            10,
            25,
            35,
            50,
            60
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            10,
            25,
            35,
            50,
            60
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            5,
            10,
            15,
            20
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "thunder": "long50",
            "ice": "long50",
            "stun": "long100"
        },
        "element": "Element.THUNDER",
        "statusEffect": "Status.STUN",
        "statusChance": [
            10,
            10,
            15,
            15,
            25
        ],
        "statusDegree": [
            2,
            2,
            2,
            2,
            2
        ],
        "buffEffect": "Stats.NONE",
        "specials": [
            [
                "Equip.BOOST",
                "Element.THUNDER"
            ],
            None,
            [
                "Equip.CAST",
                "Spells.thunder",
                0.5
            ],
            None,
            [
                "Equip.COUNTER",
                "Spells.slicingcyclone"
            ]
        ],
        "materials": [
            [
                "Items.seashell",
                2
            ],
            [
                "Items.seashell",
                3,
                "Items.geode",
                2
            ],
            [
                "Items.topaz",
                2,
                "Items.geode",
                2
            ],
            [
                "Items.starfragment",
                1,
                "Items.seashell",
                3
            ]
        ]
    },
    "crimsonrazorback": {
        "SID": "crimsonrazorback",
        "type": "SWORD",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            10,
            20,
            30
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            20,
            40,
            60,
            80,
            100
        ],
        "magicDefence": [
            0,
            5,
            10,
            15,
            20
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "wind": "long50",
            "thunder": "long50",
            "syphon": "long100"
        },
        "element": "Element.WIND",
        "buffEffect": "Stats.MAGIC_ATTACK",
        "buffChance": [
            60,
            70,
            80,
            90,
            100
        ],
        "buffDegree": [
            -20,
            -25,
            -25,
            -25,
            -30
        ],
        "statusEffect": "Status.LIGHT",
        "statusChance": [
            30,
            50,
            70,
            85,
            100
        ],
        "statusDegree": [
            2,
            2,
            2,
            3,
            3
        ],
        "specials": [
            [
                "Equip.BOOST",
                "Element.WIND"
            ],
            None,
            [
                "Equip.CAST",
                "Spells.gust",
                0.5
            ],
            None,
            [
                "Equip.SUMMON",
                "Spells.powermetal",
                0.66
            ]
        ],
        "materials": [
            [
                "Items.spring",
                2
            ],
            [
                "Items.spring",
                5,
                "Items.beer",
                1
            ],
            [
                "Items.cpu",
                2,
                "Items.beer",
                3
            ],
            [
                "Items.gamechild",
                1,
                "Items.cpu",
                2
            ]
        ]
    },
    "fusionblade": {
        "SID": "fusionblade",
        "type": "SWORD",
        "HP": [
            0,
            5,
            5,
            10,
            10
        ],
        "attack": [
            15,
            30,
            40,
            55,
            70
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            15,
            30,
            40,
            55,
            70
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "bomb": "long50",
            "bio": "long50",
            "fire": "long50"
        },
        "element": "Element.BOMB",
        "statusEffect": "Status.BURN",
        "statusChance": [
            30,
            50,
            70,
            85,
            100
        ],
        "statusDegree": [
            1,
            1,
            2,
            2,
            2
        ],
        "buffEffect": "Stats.NONE",
        "specials": [
            [
                "Equip.BOOST",
                "Element.BOMB"
            ],
            None,
            [
                "Equip.CAST",
                "Spells.bullet",
                0.33
            ],
            None,
            [
                "Equip.IGNORE_BUFFS"
            ]
        ],
        "materials": [
            [
                "Items.powder",
                2
            ],
            [
                "Items.gear",
                2,
                "Items.steel",
                1
            ],
            [
                "Items.cpu",
                2,
                "Items.gear",
                2
            ],
            [
                "Items.plutonium",
                1,
                "Summons.FishJet",
                1
            ]
        ]
    },
    "goldenaxe": {
        "SID": "goldenaxe",
        "type": "SWORD",
        "HP": [
            5,
            5,
            10,
            10,
            20
        ],
        "attack": [
            15,
            30,
            40,
            50,
            65
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            10,
            20,
            30,
            40,
            50
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "thunder": "long50",
            "dispel": "long100",
            "death": "long100"
        },
        "element": "Element.THUNDER",
        "statusEffect": "Status.BAD_LUCK",
        "statusChance": [
            30,
            50,
            70,
            85,
            100
        ],
        "statusDegree": [
            2,
            2,
            2,
            2,
            3
        ],
        "buffEffect": "Stats.NONE",
        "specials": [
            [
                "Equip.STATUS",
                "Status.GOOD_LUCK",
                2,
                0.5
            ],
            None,
            [
                "Equip.BOOST",
                "Element.THUNDER"
            ],
            None,
            [
                "Equip.CAST",
                "Spells.bigspark",
                0.4
            ]
        ],
        "materials": [
            [
                "Items.pipe",
                2
            ],
            [
                "Items.pipe",
                4,
                "Items.leather",
                1
            ],
            [
                "Items.gold",
                3,
                "Items.leather",
                2
            ],
            [
                "Items.grail",
                1,
                "Summons.FishGold",
                1
            ]
        ]
    },
    "darkstalker": {
        "SID": "darkstalker",
        "type": "SWORD",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            5,
            15,
            25,
            35,
            45
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            5,
            15,
            25,
            35,
            45
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "dark": "long50",
            "bio": "long50",
            "syphon": "long100"
        },
        "element": "Element.DARK",
        "statusEffect": "Status.SYPHON",
        "statusChance": [
            30,
            35,
            40,
            45,
            50
        ],
        "statusDegree": [
            2,
            2,
            2,
            2,
            3
        ],
        "buffEffect": "Stats.ATTACK",
        "buffChance": [
            60,
            70,
            80,
            90,
            100
        ],
        "buffDegree": [
            -30,
            -35,
            -40,
            -45,
            -50
        ],
        "specials": [
            [
                "Equip.BOOST",
                "Element.DARK"
            ],
            None,
            [
                "Equip.CAST",
                "Spells.bonestar",
                0.5
            ],
            None,
            None
        ],
        "materials": [
            [
                "Items.claw",
                1
            ],
            [
                "Items.claw",
                2
            ],
            [
                "Items.rune",
                1,
                "Items.spike",
                4
            ],
            [
                "Items.darkmatter",
                1,
                "Items.spike",
                4
            ]
        ]
    },
    "loveblade": {
        "SID": "loveblade",
        "type": "SWORD",
        "HP": [
            10,
            15,
            20,
            25,
            30
        ],
        "attack": [
            -50,
            -50,
            -50,
            -50,
            -50
        ],
        "defence": [
            10,
            15,
            20,
            25,
            30
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            10,
            15,
            20,
            25,
            30
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            5,
            10,
            15,
            20,
            20
        ],
        "resistance": {
            "holy": "long50",
            "dark": "long50",
            "death": "long100"
        },
        "element": "Element.HOLY",
        "statusEffect": "Status.NONE",
        "buffEffect": "Stats.ACCURACY",
        "buffChance": [
            60,
            70,
            80,
            90,
            100
        ],
        "buffDegree": [
            -10,
            -10,
            -15,
            -15,
            -20
        ],
        "specials": [
            [
                "Equip.BOOST_HEALING"
            ],
            None,
            [
                "Equip.BOOST_BUFFS",
                10
            ],
            None,
            [
                "Equip.DEFEND_STATUS",
                "Status.LOVED",
                1
            ]
        ],
        "materials": [
            [
                "Items.cupcake",
                1
            ],
            [
                "Items.flower",
                4
            ],
            [
                "Items.dragonfruit",
                4,
                "Items.cloudberries",
                4
            ],
            [
                "Items.moonpearl",
                2,
                "Items.flower",
                8
            ]
        ]
    },
    "clubofwithering": {
        "SID": "clubofwithering",
        "type": "SWORD",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            5,
            10,
            20,
            30,
            45
        ],
        "defence": [
            0,
            5,
            5,
            10,
            10
        ],
        "magicAttack": [
            5,
            10,
            20,
            30,
            45
        ],
        "magicDefence": [
            0,
            5,
            5,
            10,
            10
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "stagger": "long100",
            "weak": "long100",
            "curse": "long100"
        },
        "element": "Element.NONE",
        "statusEffect": "Status.WEAKEN",
        "statusChance": [
            60,
            70,
            80,
            90,
            100
        ],
        "statusDegree": [
            1,
            2,
            2,
            3,
            3
        ],
        "buffEffect": "Stats.MAGIC_DEFENCE",
        "buffChance": [
            40,
            40,
            40,
            40,
            40
        ],
        "buffDegree": [
            -20,
            -25,
            -30,
            -35,
            -40
        ],
        "specials": [
            [
                "Equip.BOOST_DEBUFFS"
            ],
            None,
            [
                "Equip.CAST",
                "Spells.bones",
                0.6
            ],
            None,
            [
                "Equip.SUMMON",
                "Spells.bonestar",
                0.66
            ]
        ],
        "materials": [
            [
                "Items.claw",
                1
            ],
            [
                "Items.claw",
                2
            ],
            [
                "Items.spike",
                3,
                "Items.leather",
                2
            ],
            [
                "Items.moonpearl",
                2,
                "Summons.HandSkeleton",
                1
            ]
        ]
    },
    "solspear": {
        "SID": "solspear",
        "type": "STAFF",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            10,
            20,
            30,
            45,
            60
        ],
        "defence": [
            0,
            5,
            5,
            10,
            15
        ],
        "magicAttack": [
            10,
            20,
            30,
            45,
            60
        ],
        "magicDefence": [
            0,
            5,
            5,
            10,
            15
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "fire": "long50",
            "ice": "long50",
            "freeze": "long100"
        },
        "element": "Element.FIRE",
        "statusEffect": "Status.DRY",
        "statusChance": [
            50,
            60,
            80,
            100,
            120
        ],
        "statusDegree": [
            2,
            2,
            3,
            3,
            3
        ],
        "buffEffect": "Stats.NONE",
        "specials": [
            [
                "Equip.BOOST",
                "Element.FIRE"
            ],
            None,
            [
                "Equip.CAST",
                "Spells.fireblast",
                0.5
            ],
            None,
            [
                "Equip.SUMMON",
                "Spells.flare",
                0.66
            ]
        ],
        "materials": [
            [
                "Items.wood",
                2
            ],
            [
                "Items.magma",
                3
            ],
            [
                "Items.gold",
                2,
                "Items.satin",
                2
            ],
            [
                "Items.starfragment",
                1,
                "Items.gold",
                1
            ]
        ]
    },
    "darktooth": {
        "SID": "darktooth",
        "type": "STAFF",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            10,
            20,
            30,
            45,
            60
        ],
        "defence": [
            0,
            0,
            5,
            5,
            10
        ],
        "magicAttack": [
            10,
            20,
            30,
            45,
            60
        ],
        "magicDefence": [
            0,
            0,
            5,
            5,
            10
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "dark": "long50",
            "curse": "long100",
            "dispel": "long100"
        },
        "element": "Element.DARK",
        "buffEffect": "Stats.NONE",
        "statusEffect": "Status.DISPEL",
        "statusChance": [
            20,
            30,
            40,
            40,
            50
        ],
        "statusDegree": [
            1,
            1,
            1,
            1,
            1
        ],
        "specials": [
            [
                "Equip.BOOST",
                "Element.DARK"
            ],
            None,
            [
                "Equip.CAST",
                "Spells.geometry2",
                0.33
            ],
            None,
            [
                "Equip.COUNTER",
                "Spells.pulse"
            ]
        ],
        "materials": [
            [
                "Items.gems",
                1
            ],
            [
                "Items.gems",
                4
            ],
            [
                "Items.rune",
                3
            ],
            [
                "Items.darkmatter",
                1,
                "Items.satin",
                3
            ]
        ]
    },
    "druidstaff": {
        "SID": "druidstaff",
        "type": "STAFF",
        "HP": [
            0,
            5,
            5,
            10,
            10
        ],
        "attack": [
            0,
            10,
            20,
            30,
            45
        ],
        "defence": [
            5,
            5,
            10,
            15,
            25
        ],
        "magicAttack": [
            10,
            20,
            30,
            40,
            55
        ],
        "magicDefence": [
            5,
            5,
            10,
            15,
            25
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "bio": "long50",
            "water": "long50",
            "poison": "long100"
        },
        "element": "Element.BIO",
        "statusEffect": "Status.TIRED",
        "statusChance": [
            40,
            60,
            80,
            100,
            120
        ],
        "statusDegree": [
            2,
            2,
            3,
            3,
            3
        ],
        "buffEffect": "Stats.NONE",
        "specials": [
            [
                "Equip.BOOST",
                "Element.BIO"
            ],
            None,
            [
                "Equip.CAST",
                "Spells.vines",
                0.33
            ],
            [
                "Equip.STATUS",
                "Status.REGEN",
                2,
                0.2
            ],
            [
                "Equip.SUMMON",
                "Spells.mushroom",
                1.5
            ]
        ],
        "materials": [
            [
                "Items.wood",
                1,
                "Items.cactus",
                1
            ],
            [
                "Items.wood",
                3,
                "Items.cactus",
                3
            ],
            [
                "Items.spike",
                5,
                "Items.root",
                10
            ],
            [
                "Items.opal",
                4,
                "Items.root",
                10
            ]
        ]
    },
    "arctictrident": {
        "SID": "arctictrident",
        "type": "STAFF",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            5,
            20,
            35,
            50,
            65
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            5,
            20,
            35,
            50,
            65
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            5,
            5,
            10,
            10,
            10
        ],
        "evade": [
            5,
            5,
            10,
            10,
            10
        ],
        "resistance": {
            "ice": "long50",
            "wind": "long50",
            "burn": "long100"
        },
        "element": "Element.ICE",
        "statusEffect": "Status.CHILL",
        "statusChance": [
            30,
            50,
            70,
            85,
            100
        ],
        "statusDegree": [
            2,
            2,
            2,
            2,
            2
        ],
        "buffEffect": "Stats.NONE",
        "specials": [
            [
                "Equip.BOOST",
                "Element.ICE"
            ],
            [
                "Equip.STATUS",
                "Status.CHILL",
                2,
                0.5
            ],
            [
                "Equip.CAST",
                "Spells.deepfreeze",
                0.5
            ],
            None,
            [
                "Equip.COUNTER",
                "Spells.iceshard"
            ]
        ],
        "materials": [
            [
                "Items.steel",
                1
            ],
            [
                "Items.steel",
                1,
                "Items.water",
                1,
                "Items.ice",
                1
            ],
            [
                "Items.sapphire",
                3,
                "Items.steel",
                3
            ],
            [
                "Items.sapphire",
                6,
                "Items.moonpearl",
                1
            ]
        ]
    },
    "zeuswrath": {
        "SID": "wrathofzeus",
        "type": "STAFF",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            0,
            5,
            10,
            20,
            30
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            10,
            25,
            40,
            55,
            70
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            5,
            5,
            10,
            10
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "thunder": "long50",
            "wind": "long50",
            "stun": "long100"
        },
        "element": "Element.THUNDER",
        "statusEffect": "Status.NONE",
        "buffEffect": "Stats.NONE",
        "specials": [
            [
                "Equip.BOOST",
                "Element.THUNDER"
            ],
            None,
            [
                "Equip.CAST",
                "Spells.plasmacage",
                0.5
            ],
            None,
            [
                "Equip.SUMMON",
                "Spells.thunderbolt",
                1
            ]
        ],
        "materials": [
            [
                "Items.seashell",
                2
            ],
            [
                "Items.gems",
                4
            ],
            [
                "Summons.DogZap",
                1
            ],
            [
                "Items.starfragment",
                1
            ]
        ]
    },
    "dragonwings": {
        "SID": "dragonwings",
        "type": "STAFF",
        "HP": [
            0,
            5,
            10,
            15,
            20
        ],
        "attack": [
            10,
            20,
            30,
            40,
            50
        ],
        "defence": [
            0,
            5,
            5,
            10,
            10
        ],
        "magicAttack": [
            10,
            20,
            30,
            40,
            50
        ],
        "magicDefence": [
            0,
            5,
            5,
            10,
            10
        ],
        "accuracy": [
            5,
            10,
            15,
            20,
            25
        ],
        "evade": [
            5,
            10,
            15,
            20,
            25
        ],
        "resistance": {
            "fire": "long50",
            "dark": "long50",
            "dispel": "long100"
        },
        "element": "Element.FIRE",
        "statusEffect": "Status.BURN",
        "statusChance": [
            30,
            50,
            70,
            85,
            100
        ],
        "statusDegree": [
            2,
            2,
            3,
            3,
            3
        ],
        "buffEffect": "Stats.NONE",
        "specials": [
            [
                "Equip.BOOST",
                "Element.FIRE"
            ],
            None,
            [
                "Equip.SUMMON",
                "Summons.DragonOmega",
                0.15
            ],
            None,
            [
                "Equip.COUNTER",
                "Spells.fireball"
            ]
        ],
        "materials": [
            [
                "Items.magma",
                1
            ],
            [
                "Items.amber",
                1
            ],
            [
                "Items.scales",
                1
            ],
            [
                "Items.scales",
                2,
                "Items.amber",
                1,
                "Items.magma",
                2
            ]
        ]
    },
    "nimbusrod": {
        "SID": "nimbusrod",
        "type": "STAFF",
        "HP": [
            0,
            5,
            5,
            10,
            15
        ],
        "attack": [
            0,
            5,
            10,
            15,
            20
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            10,
            20,
            30,
            45,
            60
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "water": "long50",
            "fire": "long50",
            "holy": "long50"
        },
        "element": "Element.WATER",
        "statusEffect": "Status.CHILL",
        "statusChance": [
            70,
            80,
            90,
            100,
            120
        ],
        "statusDegree": [
            2,
            2,
            2,
            2,
            3
        ],
        "buffEffect": "Stats.NONE",
        "specials": [
            [
                "Equip.BOOST",
                "Element.WATER"
            ],
            None,
            [
                "Equip.CAST",
                "Spells.bubbleringP",
                0.33
            ],
            None,
            [
                "Equip.SUMMON",
                "Spells.rain",
                1
            ]
        ],
        "materials": [
            [
                "Items.snowball",
                3
            ],
            [
                "Items.ice",
                2,
                "Items.snowball",
                2
            ],
            [
                "Items.sapphire",
                2,
                "Items.ice",
                2
            ],
            [
                "Items.moonpearl",
                2,
                "Items.sapphire",
                2
            ]
        ]
    },
    "alchemyset": {
        "SID": "alchemyset",
        "type": "STAFF",
        "HP": [
            0,
            5,
            5,
            10,
            15
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            10,
            20,
            30,
            45,
            60
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            5,
            5,
            10,
            15
        ],
        "resistance": {
            "weak": "long100",
            "curse": "long100"
        },
        "element": "Element.NONE",
        "statusEffect": "Status.RANDOM",
        "statusChance": [
            70,
            80,
            90,
            100,
            120
        ],
        "statusDegree": [
            2,
            2,
            2,
            2,
            3
        ],
        "buffEffect": "Stats.ACCURACY",
        "buffChance": [
            60,
            70,
            80,
            90,
            100
        ],
        "buffDegree": [
            -20,
            -25,
            -30,
            -35,
            -40
        ],
        "specials": [
            [
                "Equip.BOOST_STATUS"
            ],
            None,
            [
                "Equip.COUNTER",
                "Spells.spectrum"
            ],
            None,
            [
                "Equip.BOOST_DEBUFFS"
            ]
        ],
        "materials": [
            [
                "Items.glass",
                1
            ],
            [
                "Items.butterflywing",
                3,
                "Items.powder",
                3
            ],
            [
                "Summons.WormFuzzy",
                1,
                "Summons.WormPutrid",
                1,
                "Summons.WormScaly",
                1
            ],
            [
                "Items.darkmatter",
                1,
                "Items.glass",
                10
            ]
        ]
    },
    "kaladanda": {
        "SID": "kaladanda",
        "type": "STAFF",
        "HP": [
            0,
            5,
            10,
            15,
            20
        ],
        "attack": [
            15,
            30,
            45,
            60,
            80
        ],
        "defence": [
            0,
            5,
            5,
            10,
            15
        ],
        "magicAttack": [
            15,
            30,
            45,
            60,
            80
        ],
        "magicDefence": [
            0,
            5,
            5,
            10,
            15
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "stagger": "long100",
            "weak": "long100",
            "curse": "long100"
        },
        "element": "Element.NONE",
        "statusEffect": "Status.WEAKEN",
        "statusChance": [
            60,
            70,
            80,
            90,
            100
        ],
        "statusDegree": [
            1,
            2,
            2,
            3,
            3
        ],
        "buffEffect": "Stats.DEFENCE",
        "buffChance": [
            60,
            70,
            80,
            90,
            100
        ],
        "buffDegree": [
            -30,
            -35,
            -40,
            -45,
            -50
        ],
        "specials": [
            [
                "Equip.STATUS",
                "Status.WEAKEN",
                1,
                0.5
            ],
            None,
            [
                "Equip.CAST",
                "Spells.bones",
                0.5
            ],
            None,
            [
                "Equip.COUNTER",
                "Spells.staffstrike"
            ]
        ],
        "materials": [
            [
                "Items.feather",
                2
            ],
            [
                "Items.claw",
                2
            ],
            [
                "Items.spike",
                3,
                "Items.silk",
                2
            ],
            [
                "Items.moonpearl",
                2,
                "Items.spike",
                5
            ]
        ]
    },
    "knife": {
        "SID": "knife",
        "type": "STAFF",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            30,
            60,
            90,
            120,
            150
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            5,
            10,
            15,
            20,
            25
        ],
        "evade": [
            5,
            10,
            15,
            20,
            25
        ],
        "resistance": {
            "death": "long100",
            "curse": "long100"
        },
        "element": "Element.NONE",
        "statusEffect": "Status.DEATH",
        "statusChance": [
            10,
            20,
            30,
            40,
            50
        ],
        "statusDegree": [
            1
        ],
        "buffEffect": "Stats.NONE",
        "specials": [
            [
                "Equip.BOOST_FOOD"
            ],
            None,
            [
                "Equip.BOOST_BUFFS"
            ],
            None,
            [
                "Equip.COUNTER",
                "Spells.staffstrike"
            ]
        ],
        "materials": [
            [
                "Items.pumpkin",
                2
            ],
            [
                "Items.pineapple",
                4
            ],
            [
                "Items.watermelon",
                6,
                "Items.blueberries",
                4
            ],
            [
                "Items.dragonfruit",
                18,
                "Items.cloudberries",
                6
            ]
        ]
    },
    "celticcross": {
        "SID": "celticcross",
        "type": "STAFF",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            10,
            20,
            30,
            40,
            55
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            10,
            20,
            30,
            40,
            55
        ],
        "magicDefence": [
            0,
            5,
            5,
            10,
            10
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            5,
            5,
            10,
            10
        ],
        "resistance": {
            "holy": "long50",
            "dark": "long50",
            "water": "long50"
        },
        "element": "Element.HOLY",
        "statusEffect": "Status.NONE",
        "buffEffect": "Stats.NONE",
        "specials": [
            [
                "Equip.SCARE",
                "Foe.GHOSTS"
            ],
            [
                "Equip.BOOST",
                "Element.HOLY"
            ],
            [
                "Equip.CAST",
                "Spells.talisman",
                0.5
            ],
            None,
            [
                "Equip.COUNTER",
                "Spells.shine"
            ]
        ],
        "materials": [
            [
                "Items.brick",
                4
            ],
            [
                "Items.silk",
                2,
                "Items.brick",
                1
            ],
            [
                "Items.rune2",
                5,
                "Items.silk",
                2
            ],
            [
                "Items.grail",
                1,
                "Items.satin",
                3
            ]
        ]
    },
    "obsidianstaff": {
        "SID": "obsidianstaff",
        "type": "STAFF",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            10,
            20,
            30,
            40,
            50
        ],
        "defence": [
            -20,
            -20,
            -20,
            -20,
            -20
        ],
        "magicAttack": [
            30,
            45,
            60,
            85,
            110
        ],
        "magicDefence": [
            -20,
            -20,
            -20,
            -20,
            -20
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "fire": "long50",
            "syphon": "long100"
        },
        "element": "Element.DARK",
        "statusEffect": "Status.DRY",
        "statusChance": [
            30,
            50,
            70,
            85,
            100
        ],
        "statusDegree": [
            2,
            2,
            2,
            2,
            2
        ],
        "buffEffect": "Stats.NONE",
        "specials": [
            [
                "Equip.BOOST",
                "Element.DARK"
            ],
            None,
            [
                "Equip.CAST",
                "Spells.darken",
                0.5
            ]
        ],
        "materials": [
            [
                "Items.powder",
                2
            ],
            [
                "Items.amber",
                2
            ],
            [
                "Items.powder",
                10,
                "Items.rune",
                1
            ],
            [
                "Items.darkmatter",
                1,
                "Summons.BoulderObsidian",
                1,
                "Items.amber",
                3
            ]
        ]
    },
    "paperfan": {
        "SID": "paperfan",
        "type": "STAFF",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            -50,
            -50,
            -50,
            -50,
            -50
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            15,
            25,
            40,
            55,
            75
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            5,
            5,
            10,
            10
        ],
        "resistance": {
            "bomb": "long50",
            "wind": "long50",
            "holy": "long50"
        },
        "element": "Element.WIND",
        "statusEffect": "Status.NONE",
        "buffEffect": "Stats.NONE",
        "specials": [
            [
                "Equip.BOOST",
                "Element.WIND"
            ],
            None,
            [
                "Equip.CAST",
                "Spells.whirlwind",
                0.5
            ],
            [
                "Equip.STATUS",
                "Status.HASTE",
                2,
                0.2
            ]
        ],
        "materials": [
            [
                "Items.feather",
                2
            ],
            [
                "Items.tape",
                3,
                "Items.shuriken",
                3
            ],
            [
                "Items.tape",
                10,
                "Items.kevlar",
                1
            ],
            [
                "Items.kevlar",
                4,
                "Items.tape",
                10
            ]
        ]
    },
    "wreckingrod": {
        "SID": "wreckingrod",
        "type": "STAFF",
        "HP": [
            5,
            10,
            15,
            20,
            25
        ],
        "MP": [
            0
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            10,
            15,
            20,
            25,
            30
        ],
        "magicAttack": [
            15,
            25,
            40,
            55,
            70
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            -10,
            -10,
            -10,
            -10,
            -10
        ],
        "evade": [
            -20,
            -20,
            -20,
            -20,
            -20
        ],
        "resistance": {
            "bomb": "long50",
            "stagger": "long100",
            "thunder": "long50"
        },
        "element": "Element.BOMB",
        "statusEffect": "Status.STAGGER",
        "statusChance": [
            50,
            60,
            70,
            85,
            100
        ],
        "statusDegree": [
            1,
            1,
            1,
            1,
            1
        ],
        "buffEffect": "Stats.NONE",
        "specials": [
            [
                "Equip.BOOST",
                "Element.BOMB"
            ],
            None,
            [
                "Equip.CAST",
                "Spells.bigblast",
                0.5
            ],
            None,
            [
                "Equip.COUNTER",
                "Spells.staffstrike"
            ]
        ],
        "materials": [
            [
                "Items.iron",
                1,
                "Items.spring",
                1
            ],
            [
                "Items.iron",
                4,
                "Items.spring",
                4
            ],
            [
                "Items.cpu",
                2,
                "Items.steel",
                2,
                "Items.floppy",
                1
            ],
            [
                "Items.plutonium",
                1,
                "Items.powder",
                10
            ]
        ]
    },
    "slimestaff": {
        "SID": "slimestaff",
        "type": "STAFF",
        "HP": [
            5,
            10,
            15,
            20,
            25
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            5,
            10,
            15,
            20,
            25
        ],
        "magicAttack": [
            5,
            10,
            15,
            20,
            25
        ],
        "magicDefence": [
            5,
            10,
            15,
            20,
            25
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "holy": "long50",
            "ice": "long50",
            "syphon": "long100"
        },
        "element": "Element.HOLY",
        "statusEffect": "Status.NONE",
        "buffEffect": "Stats.NONE",
        "specials": [
            [
                "Equip.SCARE",
                "Foe.SLIMES"
            ],
            [
                "Equip.BOOST_HEALING"
            ],
            [
                "Equip.BOOST",
                "Element.HOLY"
            ],
            None,
            [
                "Equip.SUMMON",
                "Summons.SlimeBunny",
                0.5
            ]
        ],
        "materials": [
            [
                "Items.wool",
                3
            ],
            [
                "Items.plastic",
                3
            ],
            [
                "Items.plastic",
                10,
                "Items.satin",
                3,
                "Items.flower",
                5
            ],
            [
                "Items.grail",
                1,
                "Summons.SlimeBunny",
                1
            ]
        ]
    },
    "elderswisdom": {
        "SID": "elderswisdom",
        "type": "STAFF",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            0,
            10,
            20,
            30,
            40
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            10,
            20,
            30,
            45,
            60
        ],
        "magicDefence": [
            0,
            5,
            10,
            15,
            20
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "earth": "long50",
            "holy": "long50",
            "weight": "long100"
        },
        "element": "Element.EARTH",
        "statusEffect": "Status.NONE",
        "buffEffect": "Stats.NONE",
        "specials": [
            [
                "Equip.BOOST",
                "Element.EARTH"
            ],
            None,
            [
                "Equip.SUMMON",
                "Spells.bigroot",
                1.25
            ],
            [
                "Equip.BOOST_BUFFS"
            ],
            [
                "Equip.CAST",
                "Spells.lighten",
                0.5
            ]
        ],
        "materials": [
            [
                "Items.wood",
                2
            ],
            [
                "Items.root",
                2,
                "Items.claw",
                2
            ],
            [
                "Items.spike",
                2,
                "Items.claw",
                6
            ],
            [
                "Items.opal",
                3,
                "Items.moonpearl",
                1
            ]
        ]
    },
    "gigavolt": {
        "SID": "gigavolt",
        "type": "STAFF",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            20,
            40,
            70,
            100,
            130
        ],
        "defence": [
            0,
            5,
            5,
            10,
            10
        ],
        "magicAttack": [
            10,
            20,
            35,
            50,
            65
        ],
        "magicDefence": [
            0,
            5,
            5,
            10,
            10
        ],
        "accuracy": [
            5,
            10,
            15,
            20,
            25
        ],
        "evade": [
            5,
            10,
            15,
            20,
            25
        ],
        "resistance": {
            "thunder": "long50",
            "bomb": "long50",
            "dispel": "long100"
        },
        "element": "Element.THUNDER",
        "statusEffect": "Status.NONE",
        "buffEffect": "Stats.NONE",
        "specials": [
            [
                "Equip.BOOST",
                "Element.THUNDER"
            ],
            None,
            [
                "Equip.CAST",
                "Spells.lasersword",
                0.33
            ],
            None,
            [
                "Equip.COUNTER",
                "Spells.staffstrike"
            ]
        ],
        "materials": [
            [
                "Items.seashell",
                2
            ],
            [
                "Items.amber",
                2
            ],
            [
                "Items.topaz",
                2,
                "Items.ruby",
                2
            ],
            [
                "Items.topaz",
                6,
                "Items.ruby",
                6
            ]
        ]
    },
    "soulcrusher": {
        "SID": "soulcrusher",
        "type": "STAFF",
        "HP": [
            5,
            5,
            10,
            15,
            20
        ],
        "attack": [
            40,
            80,
            120,
            160,
            200
        ],
        "defence": [
            10,
            15,
            20,
            25,
            30
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            10,
            15,
            20,
            25,
            30
        ],
        "accuracy": [
            -20,
            -20,
            -20,
            -20,
            -20
        ],
        "evade": [
            -20,
            -20,
            -20,
            -20,
            -20
        ],
        "resistance": {
            "thunder": "long50",
            "wind": "long50"
        },
        "element": "Element.NONE",
        "statusEffect": "Status.CURSE",
        "statusChance": [
            60,
            70,
            80,
            90,
            100
        ],
        "statusDegree": [
            3,
            3,
            4,
            4,
            5
        ],
        "buffEffect": "Stats.NONE",
        "specials": [
            [
                "Equip.INTIMIDATE"
            ],
            None,
            [
                "Equip.SUMMON",
                "Summons.WraithSteel",
                0.66
            ],
            None,
            [
                "Equip.BOOST_BUFFS"
            ]
        ],
        "materials": [
            [
                "Items.iron",
                2
            ],
            [
                "Items.steel",
                2
            ],
            [
                "Items.rune",
                2,
                "Items.steel",
                2
            ],
            [
                "Items.titanium",
                1,
                "Summons.WraithSteel",
                1,
                "Items.steel",
                2
            ]
        ]
    },
    "oakstaff": {
        "SID": "oakstaff",
        "type": "STAFF",
        "HP": [
            10,
            20,
            30,
            40,
            50
        ],
        "attack": [
            -50,
            -50,
            -50,
            -50,
            -50
        ],
        "defence": [
            10,
            15,
            20,
            30,
            40
        ],
        "magicAttack": [
            -50,
            -50,
            -50,
            -50,
            -50
        ],
        "magicDefence": [
            10,
            15,
            20,
            30,
            40
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "earth": "long50",
            "wind": "long50",
            "bio": "long50"
        },
        "element": "Element.EARTH",
        "elementDegree": 50,
        "statusEffect": "Status.NONE",
        "statusChance": [
            0
        ],
        "statusDegree": [
            0
        ],
        "buffEffect": "Stats.NONE",
        "buffChance": [
            0
        ],
        "buffDegree": [
            0
        ],
        "specials": [
            [
                "Equip.SCARE",
                "Foe.TREES"
            ],
            None,
            [
                "Equip.BOOST_HEALING"
            ],
            None,
            [
                "Equip.SUMMON",
                "Summons.GloopWood",
                0.25
            ]
        ],
        "materials": [
            [
                "Items.wood",
                1,
                "Items.turd",
                1
            ],
            [
                "Items.root",
                3,
                "Items.herb",
                3,
                "Items.flower",
                3
            ],
            [
                "Summons.IdolWood",
                1,
                "Items.root",
                15,
                "Items.flower",
                15
            ],
            [
                "Summons.GloopWood",
                1,
                "Items.emerald",
                6,
                "Items.opal",
                1
            ]
        ]
    },
    "shootingstar": {
        "SID": "shootingstar",
        "type": "STAFF",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            10,
            25,
            45,
            65,
            85
        ],
        "magicDefence": [
            5,
            10,
            15,
            20,
            25
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "dispel": "long100",
            "syphon": "long100",
            "death": "long100"
        },
        "element": "Element.NONE",
        "statusEffect": "Status.NONE",
        "buffEffect": "Stats.NONE",
        "specials": [
            [
                "Equip.BOOST",
                "Element.NONE"
            ],
            None,
            [
                "Equip.CAST",
                "Spells.luckystar",
                0.33
            ],
            [
                "Equip.STATUS",
                "Status.GOOD_LUCK",
                2,
                0.3
            ],
            [
                "Equip.SUMMON",
                "Spells.starshower",
                0.5
            ]
        ],
        "materials": [
            [
                "Items.gems",
                1
            ],
            [
                "Items.gems",
                4
            ],
            [
                "Items.ruby",
                1,
                "Items.sapphire",
                1,
                "Items.emerald",
                1
            ],
            [
                "Items.starfragment",
                1,
                "Items.gems",
                10
            ]
        ]
    },
    "beholdingeye": {
        "SID": "beholdingeye",
        "type": "STAFF",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            0,
            5,
            10,
            15,
            20
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            5,
            10,
            15,
            20
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            20,
            40,
            60,
            80,
            100
        ],
        "evade": [
            10,
            20,
            30,
            40,
            50
        ],
        "resistance": {
            "dark": "long50",
            "bio": "long50",
            "syphon": "long100"
        },
        "element": "Element.NONE",
        "statusEffect": "Status.VIRUS",
        "statusChance": [
            30,
            50,
            70,
            85,
            100
        ],
        "statusDegree": [
            2,
            2,
            3,
            3,
            3
        ],
        "buffEffect": "Stats.NONE",
        "specials": [
            [
                "Equip.BOOST_DEBUFFS"
            ],
            None,
            [
                "Equip.CAST",
                "Spells.tentacles",
                0.5
            ],
            None,
            [
                "Equip.BOOST_BUFFS"
            ]
        ],
        "materials": [
            [
                "Items.iron",
                2
            ],
            [
                "Items.virus",
                2
            ],
            [
                "Items.scales",
                1,
                "Items.virus",
                1
            ],
            [
                "Summons.ChomperMutant",
                1,
                "Items.rune",
                1
            ]
        ]
    },
    "shadowblaster": {
        "SID": "shadowblaster",
        "type": "GUN",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            0,
            5,
            10,
            15,
            20
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            15,
            30,
            45,
            60,
            80
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "dark": "long50",
            "thunder": "long50",
            "death": "long100"
        },
        "element": "Element.DARK",
        "statusEffect": "Status.NONE",
        "buffEffect": "Stats.NONE",
        "specials": [
            [
                "Equip.BOOST",
                "Element.DARK"
            ],
            None,
            [
                "Equip.COUNTER",
                "Spells.darkblast"
            ],
            None,
            [
                "Equip.CAST",
                "Spells.gravitysurge",
                0.2
            ]
        ],
        "materials": [
            [
                "Items.bomb",
                2
            ],
            [
                "Items.rune",
                1
            ],
            [
                "Summons.FlybotRed",
                1,
                "Items.bomb",
                2
            ],
            [
                "Items.darkmatter",
                1,
                "Items.rune",
                1
            ]
        ]
    },
    "biohazardblaster": {
        "SID": "biohazardblaster",
        "type": "GUN",
        "HP": [
            0,
            5,
            10,
            15,
            20
        ],
        "attack": [
            10,
            20,
            30,
            40,
            50
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            10,
            20,
            30,
            40,
            50
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "bio": "long150",
            "water": "long50"
        },
        "element": "Element.BIO",
        "statusEffect": "Status.VIRUS",
        "statusChance": [
            60,
            70,
            80,
            90,
            100
        ],
        "statusDegree": [
            1,
            2,
            2,
            3,
            3
        ],
        "buffEffect": "Stats.NONE",
        "specials": [
            [
                "Equip.BOOST",
                "Element.BIO"
            ],
            None,
            [
                "Equip.DRAIN_HP"
            ],
            None,
            [
                "Equip.STATUS",
                "Status.POISON",
                2,
                1
            ]
        ],
        "materials": [
            [
                "Items.glass",
                1
            ],
            [
                "Items.glass",
                4,
                "Items.plastic",
                1
            ],
            [
                "Items.virus",
                4,
                "Items.kevlar",
                2
            ],
            [
                "Items.darkmatter",
                1,
                "Items.virus",
                4
            ]
        ]
    },
    "coconutshooter": {
        "SID": "coconutshooter",
        "type": "GUN",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            15,
            25,
            40,
            55,
            70
        ],
        "defence": [
            5,
            5,
            5,
            5,
            10
        ],
        "magicAttack": [
            5,
            10,
            20,
            30,
            40
        ],
        "magicDefence": [
            5,
            5,
            5,
            5,
            10
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            -10,
            -10,
            -10,
            -10,
            -10
        ],
        "resistance": {
            "bio": "long50",
            "earth": "long50",
            "water": "long50"
        },
        "element": "Element.EARTH",
        "statusEffect": "Status.STAGGER",
        "statusChance": [
            30,
            35,
            40,
            45,
            50
        ],
        "statusDegree": [
            1,
            1,
            1,
            1,
            1
        ],
        "buffEffect": "Stats.NONE",
        "specials": [
            [
                "Equip.BOOST",
                "Element.EARTH"
            ],
            None,
            [
                "Equip.CAST",
                "Spells.stonefist",
                0.5
            ],
            None,
            [
                "Equip.SUMMON",
                "Spells.lumber",
                1
            ]
        ],
        "materials": [
            [
                "Items.wood",
                1,
                "Items.herb",
                1,
                "Items.cactus",
                1
            ],
            [
                "Items.wood",
                4,
                "Items.herb",
                4,
                "Items.cactus",
                4
            ],
            [
                "Items.emerald",
                2,
                "Items.root",
                3
            ],
            [
                "Items.opal",
                2,
                "Summons.MirrorWise",
                1
            ]
        ]
    },
    "gungnir": {
        "SID": "gungnir",
        "type": "GUN",
        "HP": [
            0,
            5,
            5,
            10,
            10
        ],
        "attack": [
            15,
            30,
            45,
            60,
            80
        ],
        "defence": [
            0,
            5,
            5,
            10,
            10
        ],
        "magicAttack": [
            15,
            30,
            45,
            60,
            80
        ],
        "magicDefence": [
            0,
            5,
            5,
            10,
            10
        ],
        "accuracy": [
            0,
            5,
            10,
            15,
            20
        ],
        "evade": [
            0,
            5,
            10,
            15,
            20
        ],
        "resistance": {
            "death": "long100",
            "syphon": "long100",
            "dispel": "long100"
        },
        "element": "Element.NONE",
        "statusEffect": "Status.STAGGER",
        "statusChance": [
            50,
            60,
            70,
            90,
            100
        ],
        "statusDegree": [
            1,
            1,
            1,
            1,
            1
        ],
        "buffEffect": "Stats.NONE",
        "specials": [],
        "materials": [
            [
                "Items.spring",
                3
            ],
            [
                "Items.plastic",
                3
            ],
            [
                "Items.lego",
                1,
                "Items.plastic",
                4
            ],
            [
                "Items.plutonium",
                1,
                "Items.plastic",
                6
            ]
        ]
    },
    "heartstopper": {
        "SID": "heartstopper",
        "type": "GUN",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            10,
            25,
            40,
            55,
            70
        ],
        "defence": [
            0,
            5,
            5,
            10,
            10
        ],
        "magicAttack": [
            10,
            15,
            20,
            25,
            30
        ],
        "magicDefence": [
            0,
            5,
            5,
            10,
            10
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "stun": "long100",
            "bomb": "long50",
            "thunder": "long50"
        },
        "element": "Element.THUNDER",
        "statusEffect": "Status.DOOM",
        "statusChance": [
            30,
            35,
            40,
            45,
            50
        ],
        "statusDegree": [
            3,
            3,
            3,
            3,
            2
        ],
        "buffEffect": "Stats.NONE",
        "specials": [
            [
                "Equip.BOOST",
                "Element.THUNDER"
            ],
            None,
            [
                "Equip.CAST",
                "Spells.spark",
                0.5
            ],
            None,
            [
                "Equip.COUNTER",
                "Spells.doubleshot"
            ]
        ],
        "materials": [
            [
                "Items.turd",
                3
            ],
            [
                "Items.amber",
                2
            ],
            [
                "Items.topaz",
                3,
                "Items.amber",
                4
            ],
            [
                "Items.topaz",
                10,
                "Items.amber",
                8
            ]
        ]
    },
    "heavyclaw": {
        "SID": "heavyclaw",
        "type": "GUN",
        "HP": [
            5,
            5,
            5,
            10,
            10
        ],
        "attack": [
            20,
            35,
            50,
            60,
            80
        ],
        "defence": [
            0,
            5,
            5,
            10,
            10
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            -20,
            -20,
            -20,
            -20,
            -20
        ],
        "resistance": {
            "bomb": "long50",
            "earth": "long50",
            "dispel": "long100"
        },
        "element": "Element.BOMB",
        "statusEffect": "Status.NONE",
        "buffEffect": "Stats.DEFENCE",
        "buffChance": [
            30,
            40,
            50,
            60,
            70
        ],
        "buffDegree": [
            -20,
            -20,
            -25,
            -25,
            -30
        ],
        "specials": [
            [
                "Equip.BOOST",
                "Element.BOMB"
            ],
            None,
            [
                "Equip.STATUS",
                "Status.HEAVY",
                2,
                0.5
            ],
            None,
            [
                "Equip.SUMMON",
                "Spells.bullet",
                1
            ]
        ],
        "materials": [
            [
                "Items.steel",
                2
            ],
            [
                "Items.steel",
                3
            ],
            [
                "Items.cpu",
                2,
                "Items.gear",
                10
            ],
            [
                "Items.diamond",
                1,
                "Items.steel",
                10
            ]
        ]
    },
    "hellfireshotgun": {
        "SID": "hellfireshotgun",
        "type": "GUN",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            10,
            25,
            35,
            50,
            65
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            10,
            20,
            30,
            45,
            60
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            5,
            10,
            15,
            20,
            25
        ],
        "evade": [
            5,
            5,
            5,
            10,
            15
        ],
        "resistance": {
            "fire": "long50",
            "bio": "long50",
            "dark": "long50"
        },
        "element": "Element.FIRE",
        "statusEffect": "Status.DRY",
        "statusChance": [
            50,
            60,
            80,
            90,
            100
        ],
        "statusDegree": [
            2,
            2,
            2,
            2,
            3
        ],
        "buffEffect": "Stats.NONE",
        "specials": [
            [
                "Equip.BOOST",
                "Element.FIRE"
            ],
            None,
            [
                "Equip.CAST",
                "Spells.flameburst",
                0.5
            ],
            None,
            [
                "Equip.COUNTER",
                "Spells.snipe"
            ]
        ],
        "materials": [
            [
                "Items.pipe",
                2
            ],
            [
                "Items.pipe",
                4
            ],
            [
                "Items.lego",
                1,
                "Items.powder",
                5
            ],
            [
                "Items.lego",
                3,
                "Items.powder",
                5
            ]
        ]
    },
    "crystalwing": {
        "SID": "crystalwing",
        "type": "GUN",
        "HP": [
            0,
            0,
            5,
            10,
            15
        ],
        "attack": [
            0,
            10,
            20,
            30,
            40
        ],
        "defence": [
            5,
            5,
            5,
            10,
            15
        ],
        "magicAttack": [
            0,
            10,
            30,
            45,
            60
        ],
        "magicDefence": [
            5,
            5,
            5,
            10,
            15
        ],
        "accuracy": [
            0,
            5,
            5,
            10,
            15
        ],
        "evade": [
            0,
            5,
            5,
            10,
            15
        ],
        "resistance": {
            "holy": "long50",
            "bomb": "long50",
            "ice": "long50"
        },
        "element": "Element.HOLY",
        "statusEffect": "Status.SYPHON",
        "statusChance": [
            30,
            35,
            40,
            45,
            50
        ],
        "statusDegree": [
            2,
            2,
            2,
            3,
            3
        ],
        "buffEffect": "Stats.NONE",
        "specials": [
            [
                "Equip.BOOST",
                "Element.HOLY"
            ],
            None,
            [
                "Equip.BOOST_HEALING"
            ],
            [
                "Equip.BOOST_BUFFS"
            ],
            [
                "Equip.SUMMON",
                "Spells.healmore",
                0.66
            ]
        ],
        "materials": [
            [
                "Items.butterflywing",
                1
            ],
            [
                "Items.butterflywing",
                3,
                "Items.glass",
                1
            ],
            [
                "Items.silver",
                5,
                "Items.butterflywing",
                5
            ],
            [
                "Items.diamond",
                1,
                "Items.silver",
                2
            ]
        ]
    },
    "spinesnapper": {
        "SID": "spinesnapper",
        "type": "GUN",
        "HP": [
            -10,
            -10,
            -10,
            -10,
            -10
        ],
        "attack": [
            0,
            5,
            10,
            20,
            30
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            5,
            10,
            20,
            30
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            20,
            25,
            30,
            35,
            40
        ],
        "resistance": {
            "dark": "long50",
            "death": "long100",
            "holy": "down30"
        },
        "element": "Element.DARK",
        "statusEffect": "Status.DEATH",
        "statusChance": [
            10,
            15,
            20,
            25,
            30
        ],
        "statusDegree": [
            1
        ],
        "buffEffect": "Stats.NONE",
        "specials": [
            [
                "Equip.BOOST",
                "Element.DARK"
            ],
            None,
            [
                "Equip.BOOST_DEBUFFS"
            ],
            [
                "Equip.SUMMON",
                "Summons.FallenBeheaded",
                0.4
            ],
            [
                "Equip.BOOST_STATUS"
            ]
        ],
        "materials": [
            [
                "Items.claw",
                1
            ],
            [
                "Items.claw",
                3
            ],
            [
                "Items.spike",
                2,
                "Summons.BatBone",
                1
            ],
            [
                "Items.spike",
                12,
                "Items.claw",
                12,
                "Items.rune",
                1
            ]
        ]
    },
    "soulpistol": {
        "SID": "soulpistol",
        "type": "GUN",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            10,
            25,
            40,
            60,
            80
        ],
        "defence": [
            0,
            0,
            5,
            10,
            15
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            5,
            10,
            15
        ],
        "accuracy": [
            0,
            5,
            5,
            10,
            10
        ],
        "evade": [
            0,
            5,
            5,
            10,
            10
        ],
        "resistance": {
            "wind": "long50",
            "holy": "long50",
            "weak": "long100"
        },
        "element": "Element.HOLY",
        "statusEffect": "Status.WEAKEN",
        "statusChance": [
            60,
            70,
            80,
            90,
            100
        ],
        "statusDegree": [
            2,
            2,
            2,
            2,
            3
        ],
        "buffEffect": "Stats.NONE",
        "specials": [
            [
                "Equip.DRAIN_HP"
            ],
            [
                "Equip.BOOST",
                "Element.HOLY"
            ],
            [
                "Equip.CAST",
                "Spells.soularrow",
                0.5
            ],
            None,
            [
                "Equip.COUNTER",
                "Spells.doubleshot"
            ]
        ],
        "materials": [
            [
                "Items.spring",
                2
            ],
            [
                "Items.spring",
                2,
                "Items.pipe",
                5
            ],
            [
                "Items.silver",
                3,
                "Items.pipe",
                5,
                "Items.gear",
                5
            ],
            [
                "Summons.FishSteam",
                1,
                "Items.silver",
                3,
                "Items.gold",
                3
            ]
        ]
    },
    "thundercore": {
        "SID": "thundercore",
        "type": "GUN",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            0,
            5,
            10,
            20,
            30
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            10,
            20,
            30,
            45,
            60
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "thunder": "long50",
            "stun": "long100",
            "syphon": "long100"
        },
        "element": "Element.THUNDER",
        "statusEffect": "Status.STUN",
        "statusChance": [
            10,
            15,
            15,
            20,
            25
        ],
        "statusDegree": [
            1,
            1,
            1,
            1,
            2
        ],
        "buffEffect": "Stats.NONE",
        "specials": [
            [
                "Equip.BOOST",
                "Element.THUNDER"
            ],
            None,
            [
                "Equip.STATUS",
                "Status.CHARGE",
                1,
                0.2
            ],
            None,
            [
                "Equip.COUNTER",
                "Spells.plasma"
            ]
        ],
        "materials": [
            [
                "Items.glass",
                1
            ],
            [
                "Items.glass",
                4,
                "Items.tape",
                1
            ],
            [
                "Summons.FlybotYellow",
                1,
                "Items.tape",
                6
            ],
            [
                "Items.starfragment",
                1,
                "Items.glass",
                5
            ]
        ]
    },
    "deepblue": {
        "SID": "deepblue",
        "type": "GUN",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            20,
            35,
            50,
            70,
            90
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            10,
            20,
            30,
            40
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            -10,
            -10,
            -10,
            -10,
            -10
        ],
        "resistance": {
            "water": "long50",
            "fire": "long50",
            "wet": "long100"
        },
        "element": "Element.WATER",
        "statusEffect": "Status.WET",
        "statusChance": [
            30,
            35,
            40,
            45,
            50
        ],
        "statusDegree": [
            1,
            1,
            1,
            1,
            2
        ],
        "buffEffect": "Stats.NONE",
        "specials": [
            [
                "Equip.BOOST",
                "Element.WATER"
            ],
            None,
            [
                "Equip.CAST",
                "Spells.surgingskewer",
                0.15
            ],
            None,
            [
                "Equip.COUNTER",
                "Spells.crush"
            ]
        ],
        "materials": [
            [
                "Items.steel",
                1
            ],
            [
                "Items.ice",
                2,
                "Items.steel",
                1
            ],
            [
                "Items.ice",
                5,
                "Items.sapphire",
                2
            ],
            [
                "Items.mythril",
                1,
                "Items.ice",
                5
            ]
        ]
    },
    "subzero": {
        "SID": "subzero",
        "type": "GUN",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            10,
            20,
            30,
            45,
            60
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            10,
            20,
            30,
            45,
            60
        ],
        "magicDefence": [
            10,
            10,
            15,
            15,
            20
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "ice": "long50",
            "water": "long50",
            "burn": "long100"
        },
        "element": "Element.ICE",
        "statusEffect": "Status.FREEZE",
        "statusChance": [
            5,
            10,
            15,
            20,
            25
        ],
        "statusDegree": [
            1,
            1,
            1,
            1,
            2
        ],
        "buffEffect": "Stats.NONE",
        "specials": [
            [
                "Equip.BOOST",
                "Element.ICE"
            ],
            None,
            [
                "Equip.CAST",
                "Spells.glacialglaive",
                0.25
            ],
            None,
            [
                "Equip.STATUS",
                "Status.CHARGE",
                1,
                0.2
            ]
        ],
        "materials": [
            [
                "Items.floppy",
                1
            ],
            [
                "Items.water",
                2,
                "Items.spring",
                2
            ],
            [
                "Summons.FlybotBlue",
                1,
                "Items.spring",
                2
            ],
            [
                "Items.floppy",
                52
            ]
        ]
    },
    "vortexcannon": {
        "SID": "vortexcannon",
        "type": "GUN",
        "HP": [
            0,
            5,
            5,
            10,
            10
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            0,
            5,
            5,
            10,
            10
        ],
        "magicAttack": [
            25,
            40,
            55,
            65,
            90
        ],
        "magicDefence": [
            0,
            5,
            5,
            10,
            10
        ],
        "accuracy": [
            -10,
            -10,
            -10,
            -10,
            -10
        ],
        "evade": [
            -10,
            -10,
            -10,
            -10,
            -10
        ],
        "resistance": {
            "wind": "long50",
            "weight": "long100",
            "stagger": "long100"
        },
        "element": "Element.WIND",
        "statusEffect": "Status.DISPEL",
        "statusChance": [
            20,
            30,
            40,
            40,
            50
        ],
        "statusDegree": [
            1,
            1,
            1,
            1,
            1
        ],
        "buffEffect": "Stats.NONE",
        "specials": [
            [
                "Equip.BOOST",
                "Element.WIND"
            ],
            None,
            [
                "Equip.CAST",
                "Spells.whirlwind",
                0.66
            ],
            None,
            [
                "Equip.COUNTER",
                "Spells.airwave"
            ]
        ],
        "materials": [
            [
                "Items.pipe",
                2
            ],
            [
                "Items.steel",
                4
            ],
            [
                "Items.steel",
                16,
                "Items.gear",
                4
            ],
            [
                "Items.cpu",
                2,
                "Items.steel",
                60
            ]
        ]
    },
    "chainsawgun": {
        "SID": "chainsawgun",
        "type": "GUN",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "MP": [
            0
        ],
        "attack": [
            40,
            60,
            80,
            100,
            120
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            5,
            5,
            10,
            10
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            5,
            5,
            10,
            10
        ],
        "resistance": {
            "bomb": "long50",
            "stagger": "long100",
            "death": "long100"
        },
        "element": "Element.NONE",
        "statusEffect": "Status.NONE",
        "buffEffect": "Stats.NONE",
        "specials": [
            [
                "Equip.SCARE",
                "Foe.TREES"
            ],
            [
                "Equip.BOOST",
                "Element.NONE"
            ],
            [
                "Equip.CAST",
                "Spells.sawblade",
                1
            ],
            None,
            [
                "Equip.IGNORE_BUFFS"
            ]
        ],
        "materials": [
            [
                "Items.gear",
                1
            ],
            [
                "Items.gear",
                3
            ],
            [
                "Items.gear",
                6,
                "Items.spike",
                8
            ],
            [
                "Items.diamond",
                1,
                "Items.gear",
                6
            ]
        ]
    },
    "nitrobomber": {
        "SID": "nitrobomber",
        "type": "GUN",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            5,
            5,
            10,
            20,
            30
        ],
        "defence": [
            0,
            0,
            0,
            5,
            10
        ],
        "magicAttack": [
            10,
            25,
            40,
            55,
            70
        ],
        "magicDefence": [
            0,
            0,
            0,
            5,
            10
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "bomb": "long50",
            "fire": "long50",
            "thunder": "long50"
        },
        "element": "Element.BOMB",
        "statusEffect": "Status.STAGGER",
        "statusChance": [
            30,
            35,
            40,
            45,
            50
        ],
        "statusDegree": [
            1,
            1,
            1,
            1,
            1
        ],
        "buffEffect": "Stats.NONE",
        "specials": [
            [
                "Equip.BOOST",
                "Element.BOMB"
            ],
            [
                "Equip.SUMMON",
                "Spells.airstrike2",
                1
            ],
            [
                "Equip.CAST",
                "Spells.nitro",
                0.44
            ],
            None,
            [
                "Equip.COUNTER",
                "Spells.energybomb"
            ]
        ],
        "materials": [
            [
                "Items.bomb",
                2
            ],
            [
                "Items.powder",
                5,
                "Items.bomb",
                2
            ],
            [
                "Items.cpu",
                3,
                "Items.bomb",
                5
            ],
            [
                "Items.plutonium",
                1,
                "Items.bomb",
                5
            ]
        ]
    },
    "desertscorpion": {
        "SID": "desertscorpion",
        "type": "GUN",
        "HP": [
            0,
            5,
            10,
            15,
            20
        ],
        "attack": [
            10,
            20,
            30,
            40,
            55
        ],
        "defence": [
            0,
            5,
            10,
            15,
            20
        ],
        "magicAttack": [
            10,
            20,
            30,
            40,
            55
        ],
        "magicDefence": [
            0,
            5,
            10,
            15,
            20
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "earth": "long50",
            "wet": "long100",
            "fire": "long50"
        },
        "element": "Element.BOMB",
        "statusEffect": "Status.DRY",
        "statusChance": [
            50,
            60,
            70,
            85,
            100
        ],
        "statusDegree": [
            2,
            2,
            2,
            3,
            3
        ],
        "buffEffect": "Stats.ATTACK",
        "buffChance": [
            60,
            70,
            80,
            90,
            100
        ],
        "buffDegree": [
            -20,
            -25,
            -30,
            -35,
            -40
        ],
        "specials": [
            [
                "Equip.BOOST",
                "Element.BOMB"
            ],
            None,
            [
                "Equip.CAST",
                "Spells.sandduneP",
                0.25
            ],
            None,
            [
                "Equip.SUMMON",
                "Spells.sandstorm",
                0.66
            ]
        ],
        "materials": [
            [
                "Items.turd",
                4
            ],
            [
                "Items.amber",
                1
            ],
            [
                "Items.kevlar",
                1,
                "Items.amber",
                2
            ],
            [
                "Items.kevlar",
                4,
                "Items.turd",
                36
            ]
        ]
    },
    "accelerator": {
        "SID": "accelerator",
        "type": "GUN",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            10,
            20,
            30,
            40,
            55
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            10,
            20,
            30,
            40,
            55
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            5,
            10,
            10,
            15
        ],
        "evade": [
            0,
            5,
            10,
            10,
            15
        ],
        "resistance": {
            "fire": "long50",
            "ice": "long50",
            "thunder": "long50"
        },
        "element": "Element.NONE",
        "statusEffect": "Status.BAD_LUCK",
        "statusChance": [
            30,
            50,
            70,
            85,
            100
        ],
        "statusDegree": [
            2,
            2,
            2,
            2,
            3
        ],
        "buffEffect": "Stats.ACCURACY",
        "buffChance": [
            60,
            70,
            80,
            90,
            100
        ],
        "buffDegree": [
            -20,
            -25,
            -30,
            -35,
            -40
        ],
        "specials": [
            [
                "Equip.CAST",
                "Spells.slowdown",
                0.33
            ],
            None,
            [
                "Equip.SUMMON",
                "Spells.speedup",
                0.66
            ],
            None,
            [
                "Equip.STATUS",
                "Status.HASTE",
                2,
                0.2
            ]
        ],
        "materials": [
            [
                "Items.gear",
                1
            ],
            [
                "Items.gear",
                2,
                "Items.spring",
                2
            ],
            [
                "Items.cpu",
                2,
                "Items.gear",
                2,
                "Items.spring",
                2
            ],
            [
                "Items.plutonium",
                1,
                "Items.gear",
                2,
                "Items.spring",
                4
            ]
        ]
    },
    "supersnipe": {
        "SID": "supersnipe",
        "type": "GUN",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "MP": [
            0
        ],
        "attack": [
            15,
            30,
            45,
            60,
            80
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            5,
            10,
            20,
            30
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            25,
            30,
            35,
            40,
            50
        ],
        "evade": [
            0,
            5,
            10,
            15,
            20
        ],
        "resistance": {
            "wind": "long50",
            "weak": "long100",
            "syphon": "long100"
        },
        "element": "Element.NONE",
        "statusEffect": "Status.DEATH",
        "statusChance": [
            10,
            20,
            30,
            40,
            50
        ],
        "statusDegree": [
            1,
            1,
            1,
            1,
            1
        ],
        "buffEffect": "Stats.NONE",
        "specials": [
            [
                "Equip.BOOST",
                "Element.WIND"
            ],
            None,
            [
                "Equip.SUMMON",
                "Spells.lockon",
                1
            ],
            [
                "Equip.COUNTER",
                "Spells.snipe"
            ],
            [
                "Equip.CAST",
                "Spells.geometryP",
                0.2
            ]
        ],
        "materials": [
            [
                "Items.floppy",
                1
            ],
            [
                "Items.pipe",
                4
            ],
            [
                "Items.cpu",
                2,
                "Items.glass",
                3
            ],
            [
                "Items.gamechild",
                1,
                "Items.cpu",
                2
            ]
        ]
    },
    "greengoliath": {
        "SID": "greengoliath",
        "type": "GUN",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "MP": [
            0
        ],
        "attack": [
            25,
            35,
            50,
            75,
            100
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            25,
            35,
            50,
            75,
            100
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            -10,
            -10,
            -10,
            -10,
            -10
        ],
        "evade": [
            -10,
            -10,
            -10,
            -10,
            -10
        ],
        "resistance": {
            "wind": "long50",
            "weak": "long100",
            "syphon": "long100"
        },
        "element": "Element.NONE",
        "statusEffect": "Status.TIRED",
        "statusChance": [
            30,
            35,
            40,
            45,
            50
        ],
        "statusDegree": [
            2,
            2,
            2,
            2,
            3
        ],
        "buffEffect": "Stats.NONE",
        "specials": [
            [
                "Equip.STATUS",
                "Status.TIRED",
                1,
                0.5
            ],
            [
                "Equip.BOOST",
                "Element.BIO"
            ],
            None,
            None,
            [
                "Equip.CAST",
                "Spells.bamboo2",
                0.5
            ]
        ],
        "materials": [
            [
                "Items.herb",
                4
            ],
            [
                "Items.floppy",
                2
            ],
            [
                "Items.cpu",
                1,
                "Items.kevlar",
                1,
                "Items.herb",
                12
            ],
            [
                "Items.titanium",
                1,
                "Items.cpu",
                1
            ]
        ]
    },
    "flametitan": {
        "SID": "flametitan",
        "type": "GUN",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            0,
            5,
            10,
            15,
            20
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            20,
            35,
            55,
            70,
            90
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            -10,
            -10,
            -10,
            -10,
            -10
        ],
        "evade": [
            -10,
            -10,
            -10,
            -10,
            -10
        ],
        "resistance": {
            "earth": "long50",
            "wind": "long50",
            "weight": "long100"
        },
        "element": "Element.FIRE",
        "statusEffect": "Status.BURN",
        "statusChance": [
            50,
            65,
            80,
            90,
            100
        ],
        "statusDegree": [
            2,
            2,
            2,
            2,
            3
        ],
        "buffEffect": "Stats.NONE",
        "specials": [
            [
                "Equip.BOOST",
                "Element.FIRE"
            ],
            None,
            [
                "Equip.STATUS",
                "Status.HEAVY",
                2,
                0.5
            ]
        ],
        "materials": [
            [
                "Items.pipe",
                2
            ],
            [
                "Items.pipe",
                8
            ],
            [
                "Items.scales",
                1,
                "Items.pipe",
                6
            ],
            [
                "Items.scales",
                2,
                "Summons.SpriteFire",
                1
            ]
        ]
    },
    "fairybow": {
        "SID": "fairybow",
        "type": "BOW",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            15,
            25,
            35,
            50,
            65
        ],
        "defence": [
            5,
            5,
            10,
            10,
            15
        ],
        "magicAttack": [
            15,
            25,
            35,
            50,
            65
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "bio": "long50",
            "earth": "long50",
            "water": "long50"
        },
        "element": "Element.BIO",
        "statusEffect": "Status.POISON",
        "statusChance": [
            50,
            60,
            70,
            80,
            100
        ],
        "statusDegree": [
            2,
            2,
            2,
            2,
            2
        ],
        "specials": [
            [
                "Equip.BOOST",
                "Element.BIO"
            ],
            None,
            [
                "Equip.CAST",
                "Spells.razorleaf",
                0.5
            ],
            None,
            [
                "Equip.SUMMON",
                "Spells.lumber",
                1
            ]
        ],
        "materials": [
            [
                "Items.wood",
                2
            ],
            [
                "Items.wood",
                4,
                "Items.herb",
                1
            ],
            [
                "Items.emerald",
                1,
                "Items.virus",
                3,
                "Items.root",
                10
            ],
            [
                "Items.emerald",
                3,
                "Items.opal",
                3,
                "Items.virus",
                3
            ]
        ]
    },
    "emeraldcyclone": {
        "SID": "emeraldcyclone",
        "type": "BOW",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            10,
            25,
            40,
            55,
            70
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            10,
            25,
            40,
            55,
            70
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            5,
            5,
            10,
            15
        ],
        "resistance": {
            "wind": "long50",
            "earth": "long50",
            "weak": "long100"
        },
        "element": "Element.WIND",
        "statusEffect": "Status.DISPEL",
        "statusChance": [
            20,
            30,
            40,
            40,
            50
        ],
        "statusDegree": [
            1,
            1,
            1,
            1,
            1
        ],
        "specials": [
            [
                "Equip.BOOST",
                "Element.WIND"
            ],
            None,
            [
                "Equip.SUMMON",
                "Spells.hurricane",
                0.75
            ],
            None,
            [
                "Equip.COUNTER",
                "Spells.piercingshot"
            ]
        ],
        "materials": [
            [
                "Items.cactus",
                2
            ],
            [
                "Items.cactus",
                8
            ],
            [
                "Items.emerald",
                3,
                "Items.cactus",
                16
            ],
            [
                "Items.emerald",
                10,
                "Items.leather",
                8
            ]
        ]
    },
    "crimsondragon": {
        "SID": "crimsondragon",
        "type": "BOW",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "MP": [
            0
        ],
        "attack": [
            15,
            30,
            45,
            60,
            75
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            15,
            30,
            45,
            60,
            75
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "fire": "long50",
            "water": "down30",
            "ice": "long50"
        },
        "element": "Element.FIRE",
        "statusEffect": "Status.BURN",
        "statusChance": [
            50,
            60,
            70,
            80,
            100
        ],
        "statusDegree": [
            2,
            2,
            2,
            2,
            2
        ],
        "specials": [
            [
                "Equip.BOOST",
                "Element.FIRE"
            ],
            None,
            [
                "Equip.CAST",
                "Spells.firecrystals",
                0.33
            ],
            None,
            [
                "Equip.SUMMON",
                "Spells.firespin",
                1
            ]
        ],
        "materials": [
            [
                "Items.magma",
                1
            ],
            [
                "Items.magma",
                3
            ],
            [
                "Items.scales",
                1,
                "Items.magma",
                1
            ],
            [
                "Items.ruby",
                10,
                "Items.magma",
                2
            ]
        ]
    },
    "coldsteel": {
        "SID": "coldsteel",
        "type": "BOW",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "MP": [
            0
        ],
        "attack": [
            15,
            30,
            40,
            55,
            70
        ],
        "defence": [
            0,
            5,
            5,
            10,
            10
        ],
        "magicAttack": [
            10,
            20,
            30,
            40,
            55
        ],
        "magicDefence": [
            0,
            5,
            5,
            10,
            10
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            -10,
            -10,
            -10,
            -10,
            -10
        ],
        "resistance": {
            "water": "long50",
            "ice": "long50",
            "freeze": "long100"
        },
        "element": "Element.ICE",
        "statusEffect": "Status.FREEZE",
        "statusChance": [
            10,
            15,
            20,
            25,
            30
        ],
        "statusDegree": [
            2,
            2,
            2,
            2,
            2
        ],
        "specials": [
            [
                "Equip.BOOST",
                "Element.ICE"
            ],
            None,
            [
                "Equip.CAST",
                "Spells.iceshard",
                0.5
            ],
            None,
            [
                "Equip.COUNTER",
                "Spells.arrowcut"
            ]
        ],
        "materials": [
            [
                "Items.steel",
                1
            ],
            [
                "Items.steel",
                2,
                "Items.water",
                2
            ],
            [
                "Summons.CreepIcicle",
                1,
                "Items.water",
                5
            ],
            [
                "Items.sapphire",
                10,
                "Items.steel",
                15
            ]
        ]
    },
    "thorshammer": {
        "SID": "thorshammer",
        "type": "BOW",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "MP": [
            0
        ],
        "attack": [
            10,
            20,
            30,
            40,
            50
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            10,
            20,
            30,
            45,
            60
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            10,
            15,
            15,
            15,
            20
        ],
        "evade": [
            0,
            5,
            5,
            10,
            10
        ],
        "resistance": {
            "wind": "long50",
            "thunder": "long50",
            "stun": "long100"
        },
        "element": "Element.THUNDER",
        "statusEffect": "Status.STUN",
        "statusChance": [
            10,
            20,
            40,
            60,
            80
        ],
        "statusDegree": [
            1,
            1,
            1,
            1,
            1
        ],
        "specials": [
            [
                "Equip.BOOST",
                "Element.THUNDER"
            ],
            None,
            [
                "Equip.SUMMON",
                "Spells.thunderstorm",
                0.35
            ],
            [
                "Equip.CAST",
                "Spells.thunderbolt",
                0.45
            ],
            [
                "Equip.COUNTER",
                "Spells.piercingshot"
            ]
        ],
        "materials": [
            [
                "Items.seashell",
                2
            ],
            [
                "Items.seashell",
                8
            ],
            [
                "Items.topaz",
                3,
                "Items.amber",
                6
            ],
            [
                "Items.topaz",
                10,
                "Items.amber",
                10
            ]
        ]
    },
    "gaiasgift": {
        "SID": "gaiasgift",
        "type": "BOW",
        "HP": [
            5,
            5,
            10,
            15,
            20
        ],
        "MP": [
            0
        ],
        "attack": [
            0,
            5,
            10,
            20,
            30
        ],
        "defence": [
            5,
            5,
            5,
            5,
            10
        ],
        "magicAttack": [
            0,
            5,
            10,
            20,
            30
        ],
        "magicDefence": [
            5,
            5,
            5,
            5,
            10
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "earth": "long50",
            "bio": "long50",
            "dark": "long50"
        },
        "element": "Element.EARTH",
        "statusEffect": "Status.HEAVY",
        "statusChance": [
            50,
            60,
            70,
            80,
            100
        ],
        "statusDegree": [
            2,
            2,
            2,
            2,
            2
        ],
        "specials": [
            [
                "Equip.BOOST",
                "Element.EARTH"
            ],
            None,
            [
                "Equip.CAST",
                "Spells.darken",
                0.33
            ],
            [
                "Equip.STATUS",
                "Status.REGEN",
                2,
                0.2
            ],
            [
                "Equip.BOOST_HEALING"
            ]
        ],
        "materials": [
            [
                "Items.turd",
                3
            ],
            [
                "Items.gems",
                4
            ],
            [
                "Items.emerald",
                2,
                "Summons.BitPoison",
                1
            ],
            [
                "Items.emerald",
                3,
                "Items.opal",
                3
            ]
        ]
    },
    "irontusk": {
        "SID": "irontusk",
        "type": "BOW",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "MP": [
            0
        ],
        "attack": [
            25,
            35,
            50,
            70,
            90
        ],
        "defence": [
            0,
            5,
            10,
            10,
            10
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            5,
            10,
            10,
            10
        ],
        "accuracy": [
            -10,
            -10,
            -10,
            -10,
            -10
        ],
        "evade": [
            -10,
            -10,
            -10,
            -10,
            -10
        ],
        "resistance": {
            "stagger": "long100",
            "bomb": "long50",
            "thunder": "long50"
        },
        "element": "Element.BOMB",
        "statusEffect": "Status.STAGGER",
        "statusChance": [
            50,
            60,
            70,
            80,
            100
        ],
        "statusDegree": [
            1,
            1,
            1,
            1,
            1
        ],
        "specials": [
            [
                "Equip.BOOST",
                "Element.BOMB"
            ],
            None,
            [
                "Equip.CAST",
                "Spells.energybomb",
                0.5
            ],
            None,
            [
                "Equip.COUNTER",
                "Spells.bowwhack"
            ]
        ],
        "materials": [
            [
                "Items.iron",
                2
            ],
            [
                "Items.steel",
                3
            ],
            [
                "Items.silver",
                5,
                "Items.steel",
                12
            ],
            [
                "Items.titanium",
                1,
                "Items.silver",
                5
            ]
        ]
    },
    "chiefshorns": {
        "SID": "chieftainshorns",
        "type": "BOW",
        "HP": [
            5,
            10,
            15,
            20,
            25
        ],
        "MP": [
            0
        ],
        "attack": [
            0,
            5,
            10,
            20,
            30
        ],
        "defence": [
            0,
            5,
            5,
            5,
            10
        ],
        "magicAttack": [
            0,
            5,
            10,
            20,
            30
        ],
        "magicDefence": [
            0,
            5,
            5,
            5,
            10
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "earth": "long50",
            "holy": "long50",
            "bomb": "long50"
        },
        "element": "Element.WIND",
        "statusEffect": "Status.LIGHT",
        "statusChance": [
            50,
            60,
            70,
            80,
            100
        ],
        "statusDegree": [
            2,
            2,
            2,
            2,
            2
        ],
        "buffEffect": "Stats.MAGIC_DEFENCE",
        "buffChance": [
            60,
            70,
            80,
            90,
            100
        ],
        "buffDegree": [
            -20,
            -25,
            -25,
            -25,
            -30
        ],
        "specials": [
            [
                "Equip.BOOST",
                "Element.WIND"
            ],
            None,
            [
                "Equip.SUMMON",
                "Spells.remedy",
                1
            ],
            [
                "Equip.BOOST_BUFFS"
            ],
            [
                "Equip.COUNTER",
                "Spells.arrowcut"
            ]
        ],
        "materials": [
            [
                "Items.feather",
                2
            ],
            [
                "Items.claw",
                2
            ],
            [
                "Items.spike",
                4,
                "Items.claw",
                6
            ],
            [
                "Items.opal",
                4,
                "Items.spike",
                4,
                "Items.feather",
                6
            ]
        ]
    },
    "juggernaught": {
        "SID": "juggernaut",
        "type": "BOW",
        "HP": [
            0,
            5,
            5,
            10,
            10
        ],
        "MP": [
            0
        ],
        "attack": [
            10,
            20,
            30,
            40,
            50
        ],
        "defence": [
            5,
            10,
            15,
            20,
            25
        ],
        "magicAttack": [
            10,
            20,
            30,
            40,
            50
        ],
        "magicDefence": [
            5,
            10,
            15,
            20,
            25
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            -10,
            -10,
            -10,
            -10,
            -10
        ],
        "resistance": {
            "dispel": "long100",
            "stagger": "long100",
            "stun": "long100"
        },
        "element": "Element.BOMB",
        "statusEffect": "Status.DISPEL",
        "statusChance": [
            30,
            50,
            60,
            70,
            80
        ],
        "statusDegree": [
            1,
            1,
            1,
            1,
            1
        ],
        "specials": [
            [
                "Equip.BOOST",
                "Element.BOMB"
            ],
            None,
            [
                "Equip.INTIMIDATE"
            ],
            None,
            [
                "Equip.CAST",
                "Spells.blast",
                0.5
            ]
        ],
        "materials": [
            [
                "Items.bomb",
                2
            ],
            [
                "Items.powder",
                3,
                "Items.bomb",
                3
            ],
            [
                "Items.kevlar",
                2,
                "Items.cpu",
                1
            ],
            [
                "Items.titanium",
                1,
                "Items.powder",
                10,
                "Items.bomb",
                10
            ]
        ]
    },
    "aquamarine": {
        "SID": "aquamarine",
        "type": "BOW",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            10,
            20,
            30,
            45,
            60
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            20,
            30,
            40,
            50,
            60
        ],
        "magicDefence": [
            0,
            5,
            5,
            10,
            10
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "water": "long50",
            "fire": "long50",
            "ice": "long50"
        },
        "element": "Element.WATER",
        "statusEffect": "Status.CHILL",
        "statusChance": [
            30,
            40,
            50,
            60,
            70
        ],
        "statusDegree": [
            2,
            2,
            2,
            3,
            3
        ],
        "specials": [
            [
                "Equip.BOOST",
                "Element.WATER"
            ],
            None,
            [
                "Equip.COUNTER",
                "Spells.aquaarrow"
            ],
            None,
            [
                "Equip.CAST",
                "Spells.lighten",
                0.25
            ]
        ],
        "materials": [
            [
                "Items.snowball",
                5
            ],
            [
                "Items.ice",
                2
            ],
            [
                "Items.sapphire",
                3,
                "Summons.BitWater",
                1
            ],
            [
                "Items.moonpearl",
                2,
                "Items.sapphire",
                2
            ]
        ]
    },
    "eagleeye": {
        "SID": "eagleeye",
        "type": "BOW",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            10,
            20,
            35,
            50,
            65
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            10,
            20,
            30,
            40
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            30,
            45,
            60,
            75,
            100
        ],
        "evade": [
            10,
            15,
            20,
            25,
            30
        ],
        "resistance": {
            "stagger": "long100",
            "syphon": "long100",
            "weak": "long100"
        },
        "element": "Element.NONE",
        "elementDegree": 100,
        "statusEffect": "Status.BAD_LUCK",
        "statusChance": [
            30,
            40,
            60,
            80,
            100
        ],
        "statusDegree": [
            2,
            2,
            2,
            3,
            3
        ],
        "specials": [
            [
                "Equip.COUNTER",
                "Spells.piercingshot"
            ],
            None,
            [
                "Equip.STATUS",
                "Status.GOOD_LUCK",
                2,
                0.3
            ],
            None,
            [
                "Equip.SUMMON",
                "Spells.bind",
                1
            ]
        ],
        "materials": [
            [
                "Items.gear",
                1
            ],
            [
                "Items.gear",
                3
            ],
            [
                "Items.cpu",
                1,
                "Items.gear",
                5,
                "Items.pipe",
                5
            ],
            [
                "Items.gamechild",
                1,
                "Items.cpu",
                1
            ]
        ]
    },
    "thestinger": {
        "SID": "thestinger",
        "type": "BOW",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            25,
            40,
            55,
            65,
            90
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            -20,
            -20,
            -20,
            -20,
            -20
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            5,
            5,
            10,
            10
        ],
        "resistance": {
            "bio": "long50",
            "dark": "long50",
            "burn": "down30"
        },
        "element": "Element.BIO",
        "statusEffect": "Status.STUN",
        "statusChance": [
            10,
            20,
            30,
            40,
            50
        ],
        "statusDegree": [
            1,
            1,
            1,
            1,
            1
        ],
        "specials": [
            [
                "Equip.BOOST",
                "Element.BIO"
            ],
            None,
            [
                "Equip.CAST",
                "Spells.vines",
                0.33
            ],
            None,
            [
                "Equip.SUMMON",
                "Spells.razorleaf2",
                0.66
            ]
        ],
        "materials": [
            [
                "Items.cactus",
                2
            ],
            [
                "Items.cactus",
                8
            ],
            [
                "Items.root",
                12,
                "Items.virus",
                10
            ],
            [
                "Summons.ChomperLeafy",
                1,
                "Items.emerald",
                4
            ]
        ]
    },
    "thedeceased": {
        "SID": "thedeceased",
        "type": "BOW",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "MP": [
            0
        ],
        "attack": [
            5,
            15,
            30,
            45,
            60
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            5,
            15,
            30,
            45,
            60
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            10,
            15,
            20,
            25,
            30
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "weak": "long100",
            "curse": "long100",
            "death": "long100"
        },
        "element": "Element.NONE",
        "statusEffect": "Status.DOOM",
        "statusChance": [
            30,
            35,
            40,
            45,
            50
        ],
        "statusDegree": [
            3,
            3,
            3,
            3,
            2
        ],
        "buffEffect": "Stats.DEFENCE",
        "buffChance": [
            50,
            70,
            80,
            90,
            100
        ],
        "buffDegree": [
            -20,
            -20,
            -25,
            -25,
            -30
        ],
        "specials": [
            [
                "Equip.BOOST_DEBUFFS"
            ],
            None,
            [
                "Equip.SUMMON",
                "Summons.HandZombie",
                0.8
            ],
            None,
            [
                "Equip.CAST",
                "Spells.bonestar",
                0.5
            ]
        ],
        "materials": [
            [
                "Items.claw",
                1
            ],
            [
                "Items.claw",
                2
            ],
            [
                "Items.spike",
                3,
                "Items.virus",
                2
            ],
            [
                "Items.darkmatter",
                1,
                "Items.spike",
                5
            ]
        ]
    },
    "blackwidow": {
        "SID": "blackwidow",
        "type": "BOW",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            15,
            25,
            35,
            55,
            70
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            5,
            10,
            20,
            30
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "dark": "long50",
            "curse": "long100",
            "death": "long100"
        },
        "element": "Element.DARK",
        "statusEffect": "Status.CURSE",
        "statusChance": [
            20,
            40,
            60,
            80,
            100
        ],
        "statusDegree": [
            3,
            3,
            3,
            3,
            3
        ],
        "specials": [
            [
                "Equip.BOOST",
                "Element.DARK"
            ],
            [
                "Equip.INTIMIDATE"
            ],
            [
                "Equip.COUNTER",
                "Spells.arrowcut"
            ],
            None,
            [
                "Equip.SUMMON",
                "Spells.spiders",
                0.66
            ]
        ],
        "materials": [
            [
                "Items.powder",
                2
            ],
            [
                "Items.powder",
                3,
                "Items.claw",
                2
            ],
            [
                "Items.rune",
                2,
                "Items.virus",
                2
            ],
            [
                "Items.darkmatter",
                1,
                "Items.virus",
                2
            ]
        ]
    },
    "sharanga": {
        "SID": "sharanga",
        "type": "BOW",
        "HP": [
            0,
            5,
            5,
            10,
            10
        ],
        "attack": [
            15,
            30,
            45,
            60,
            80
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            15,
            30,
            45,
            60,
            80
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            5,
            10,
            15,
            20
        ],
        "evade": [
            0,
            5,
            10,
            15,
            20
        ],
        "resistance": {
            "weight": "long100",
            "wet": "long100",
            "dispel": "long100"
        },
        "element": "Element.NONE",
        "statusEffect": "Status.DISPEL",
        "statusChance": [
            20,
            30,
            40,
            40,
            50
        ],
        "statusDegree": [
            1,
            1,
            1,
            1,
            1
        ],
        "buffEffect": "Stats.NONE",
        "specials": [
            None,
            None,
            [
                "Equip.CAST",
                "Spells.geometryP",
                0.2
            ]
        ],
        "materials": [
            [
                "Items.geode",
                2
            ],
            [
                "Items.geode",
                6
            ],
            [
                "Items.opal",
                2,
                "Items.geode",
                4
            ],
            [
                "Items.diamond",
                1,
                "Items.opal",
                1
            ]
        ]
    },
    "heavensvoice": {
        "SID": "heavensvoice",
        "type": "BOW",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            10,
            20,
            30,
            40,
            50
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            5,
            10,
            20,
            30
        ],
        "magicDefence": [
            0,
            5,
            10,
            15,
            20
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "weight": "long100",
            "syphon": "long100",
            "holy": "long100"
        },
        "element": "Element.HOLY",
        "statusEffect": "Status.SYPHON",
        "statusChance": [
            20,
            30,
            40,
            40,
            50
        ],
        "statusDegree": [
            2,
            2,
            2,
            2,
            2
        ],
        "buffEffect": "Stats.NONE",
        "specials": [
            [
                "Equip.BOOST",
                "Element.HOLY"
            ],
            None,
            [
                "Equip.CAST",
                "Spells.judgement",
                0.33
            ],
            None,
            [
                "Equip.COUNTER",
                "Spells.piercingshot"
            ]
        ],
        "materials": [
            [
                "Items.feather",
                2
            ],
            [
                "Items.gems",
                5
            ],
            [
                "Items.gold",
                2,
                "Items.ruby",
                1
            ],
            [
                "Items.grail",
                1,
                "Items.gold",
                2,
                "Items.ruby",
                1
            ]
        ]
    },
    "fenrirsjaw": {
        "SID": "fenrirsjaw",
        "type": "BOW",
        "HP": [
            0,
            5,
            5,
            10,
            10
        ],
        "attack": [
            20,
            35,
            50,
            65,
            80
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            5,
            5,
            10,
            10
        ],
        "evade": [
            0,
            5,
            5,
            10,
            10
        ],
        "resistance": {
            "death": "long100",
            "poison": "long100"
        },
        "element": "Element.NONE",
        "statusEffect": "Status.TIRED",
        "statusChance": [
            20,
            30,
            40,
            40,
            50
        ],
        "statusDegree": [
            2,
            2,
            2,
            2,
            2
        ],
        "specials": [
            [
                "Equip.DRAIN_HP"
            ],
            [
                "Equip.BOOST",
                "Element.NONE"
            ],
            [
                "Equip.COUNTER",
                "Spells.arrowcut"
            ],
            None,
            [
                "Equip.SUMMON",
                "Summons.FallenLost",
                0.3
            ]
        ],
        "materials": [
            [
                "Items.spring",
                2
            ],
            [
                "Items.spring",
                8
            ],
            [
                "Items.silver",
                6
            ],
            [
                "Items.mythril",
                1,
                "Items.spring",
                5
            ]
        ]
    },
    "alchemistsbow": {
        "SID": "alchemistsbow",
        "type": "BOW",
        "HP": [
            5,
            5,
            5,
            10,
            15
        ],
        "attack": [
            0,
            5,
            15,
            25,
            35
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            5,
            15,
            25,
            35
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "syphon": "long100",
            "poison": "long100",
            "burn": "long100"
        },
        "element": "Element.NONE",
        "statusEffect": "Status.RANDOM",
        "statusChance": [
            60,
            70,
            80,
            90,
            100
        ],
        "statusDegree": [
            1,
            1,
            1,
            1,
            1
        ],
        "buffEffect": "Stats.NONE",
        "specials": [
            [
                "Equip.BOOST_STATUS"
            ],
            None,
            [
                "Equip.BOOST_FOOD"
            ],
            None,
            [
                "Equip.COUNTER",
                "Spells.arrowcut"
            ]
        ],
        "materials": [
            [
                "Items.glass",
                2
            ],
            [
                "Items.glass",
                8
            ],
            [
                "Summons.SlimeSand",
                1,
                "Summons.SlimeWater",
                1,
                "Summons.SlimeMouse",
                1
            ],
            [
                "Items.emerald",
                3,
                "Items.sapphire",
                3,
                "Items.ruby",
                3
            ]
        ]
    },
    "angelwing": {
        "SID": "angelwing",
        "type": "BOW",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "MP": [
            0
        ],
        "attack": [
            10,
            20,
            30,
            45,
            60
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            10,
            20,
            30,
            45,
            60
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0,
            5,
            15
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "holy": "long50",
            "fire": "long50",
            "weak": "long100"
        },
        "element": "Element.HOLY",
        "statusEffect": "Status.WEAKEN",
        "statusChance": [
            20,
            40,
            60,
            80,
            100
        ],
        "statusDegree": [
            3,
            3,
            3,
            3,
            3
        ],
        "specials": [
            [
                "Equip.BOOST",
                "Element.HOLY"
            ],
            None,
            [
                "Equip.SUMMON",
                "Spells.arrowrain",
                0.66
            ],
            None,
            [
                "Equip.STATUS",
                "Status.AUTOLIFE",
                1,
                0.3
            ]
        ],
        "materials": [
            [
                "Items.feather",
                1,
                "Items.butterflywing",
                1
            ],
            [
                "Items.feather",
                3,
                "Items.butterflywing",
                3
            ],
            [
                "Items.silver",
                7,
                "Items.feather",
                2
            ],
            [
                "Items.diamond",
                1,
                "Items.silver",
                5
            ]
        ]
    },
    "earthswhisper": {
        "SID": "earthswhisper",
        "type": "BOW",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            0,
            10,
            20,
            30,
            40
        ],
        "defence": [
            0,
            5,
            10,
            15,
            20
        ],
        "magicAttack": [
            10,
            20,
            30,
            40,
            50
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "bio": "long100",
            "earth": "long100"
        },
        "element": "Element.EARTH",
        "statusEffect": "Status.HEAVY",
        "statusChance": [
            20,
            30,
            40,
            40,
            50
        ],
        "statusDegree": [
            2,
            2,
            2,
            2,
            2
        ],
        "buffEffect": "Stats.NONE",
        "specials": [
            [
                "Equip.BOOST",
                "Element.EARTH"
            ],
            None,
            [
                "Equip.CAST",
                "Spells.cataclysmiccut",
                0.33
            ],
            None,
            [
                "Equip.SUMMON",
                "Spells.remedy",
                1.25
            ]
        ],
        "materials": [
            [
                "Items.root",
                2
            ],
            [
                "Items.root",
                4,
                "Items.wood",
                4
            ],
            [
                "Items.opal",
                1,
                "Items.rune2",
                1
            ],
            [
                "Items.opal",
                4,
                "Items.rune2",
                3
            ]
        ]
    },
    "regalturtle": {
        "SID": "regalturtle",
        "type": "BOW",
        "HP": [
            10,
            15,
            20,
            30,
            40
        ],
        "MP": [
            0
        ],
        "attack": [
            0,
            5,
            5,
            10,
            10
        ],
        "defence": [
            10,
            15,
            20,
            30,
            40
        ],
        "magicAttack": [
            -50,
            -50,
            -50,
            -50,
            -50
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "holy": "long50",
            "fire": "long50",
            "bomb": "long50"
        },
        "element": "Element.HOLY",
        "specials": [
            [
                "Equip.BOOST_HEALING"
            ],
            None,
            [
                "Equip.STATUS",
                "Status.DEFEND",
                1,
                0.33
            ],
            None,
            [
                "Equip.BOOST",
                "Element.HOLY"
            ]
        ],
        "materials": [
            [
                "Items.seashell",
                1,
                "Items.iron",
                1
            ],
            [
                "Items.buckle",
                4
            ],
            [
                "Summons.CreepRed",
                1
            ],
            [
                "Items.grail",
                1,
                "Items.gold",
                1,
                "Items.silver",
                1
            ]
        ]
    },
    "steelbuckler": {
        "SID": "steelbuckler",
        "type": "TOYS",
        "HP": [
            0,
            5,
            5,
            5,
            10
        ],
        "MP": [
            0
        ],
        "attack": [
            10,
            20,
            35,
            50,
            65
        ],
        "defence": [
            10,
            15,
            20,
            25,
            30
        ],
        "magicAttack": [
            0,
            10,
            10,
            20,
            30
        ],
        "magicDefence": [
            10,
            15,
            20,
            25,
            30
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "earth": "long50",
            "wind": "long50",
            "weight": "long100"
        },
        "element": "Element.NONE",
        "statusEffect": None,
        "specials": [
            [
                "Equip.BOOST",
                "Element.NONE"
            ],
            None,
            [
                "Equip.COUNTER",
                "Spells.rapidslash2"
            ],
            None,
            None
        ],
        "materials": [
            [
                "Items.steel",
                1
            ],
            [
                "Items.steel",
                3
            ],
            [
                "Items.rune2",
                2,
                "Items.silver",
                6
            ],
            [
                "Items.titanium",
                1,
                "Items.silver",
                6
            ]
        ]
    },
    "elvenshield": {
        "SID": "elvenshield",
        "type": "TOYS",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            10,
            20,
            30,
            45,
            60
        ],
        "defence": [
            0,
            5,
            5,
            10,
            15
        ],
        "magicAttack": [
            10,
            20,
            30,
            45,
            60
        ],
        "magicDefence": [
            0,
            5,
            5,
            10,
            15
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "bio": "long100",
            "earth": "long100",
            "holy": "long100"
        },
        "element": "Element.EARTH",
        "statusEffect": "Status.BAD_LUCK",
        "statusChance": [
            30,
            50,
            70,
            85,
            100
        ],
        "statusDegree": [
            2,
            2,
            2,
            2,
            3
        ],
        "specials": [
            [
                "Equip.BOOST",
                "Element.EARTH"
            ],
            None,
            [
                "Equip.SUMMON",
                "Spells.fairybomb",
                1.5
            ],
            [
                "Equip.CAST",
                "Spells.stonefist",
                0.35
            ],
            [
                "Equip.STATUS",
                "Status.GOOD_LUCK",
                2,
                0.3
            ]
        ],
        "materials": [
            [
                "Items.wood",
                2
            ],
            [
                "Items.wood",
                8
            ],
            [
                "Items.rune2",
                2,
                "Items.silver",
                3
            ],
            [
                "Items.mythril",
                1,
                "Items.silver",
                1
            ]
        ]
    },
    "vikingbuckler": {
        "SID": "vikingbuckler",
        "type": "TOYS",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            20,
            40,
            60,
            80,
            100
        ],
        "defence": [
            10,
            15,
            20,
            25,
            30
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "water": "long50",
            "ice": "long50",
            "wind": "long50"
        },
        "element": "Element.NONE",
        "statusEffect": "Status.STAGGER",
        "statusChance": [
            20,
            30,
            40,
            50,
            60
        ],
        "statusDegree": [
            1
        ],
        "specials": [
            [
                "Equip.STATUS",
                "Status.BERSERK",
                1,
                2
            ],
            None,
            [
                "Equip.COUNTER",
                "Spells.sworddance2"
            ],
            None,
            [
                "Equip.CAST",
                "Spells.groundblade",
                0.33
            ]
        ],
        "materials": [
            [
                "Items.wood",
                1,
                "Items.iron",
                1
            ],
            [
                "Items.wood",
                4,
                "Items.iron",
                4
            ],
            [
                "Items.rune2",
                4,
                "Items.wood",
                8
            ],
            [
                "Items.diamond",
                1,
                "Items.rune",
                2
            ]
        ]
    },
    "pixelpopper": {
        "SID": "pixelpopper",
        "type": "TOYS",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            15,
            30,
            45,
            60,
            80
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            15,
            30,
            45,
            60,
            80
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            5,
            10,
            15,
            25,
            30
        ],
        "resistance": {
            "weight": "long100",
            "thunder": "long50",
            "stun": "long100"
        },
        "element": "Element.NONE",
        "statusEffect": "Status.RANDOM",
        "statusChance": [
            60,
            70,
            80,
            90,
            100
        ],
        "statusDegree": [
            1
        ],
        "specials": [
            [
                "Equip.BOOST",
                "Element.NONE"
            ],
            None,
            [
                "Equip.CAST",
                "Spells.pixelfish",
                0.25
            ],
            None,
            [
                "Equip.SUMMON",
                "Spells.pixelriceball",
                0.66
            ]
        ],
        "materials": [
            [
                "Items.floppy",
                1
            ],
            [
                "Items.tape",
                8
            ],
            [
                "Items.cpu",
                1,
                "Items.tape",
                2
            ],
            [
                "Items.gamechild",
                2
            ]
        ]
    },
    "godlybook": {
        "SID": "godlybook",
        "type": "TOYS",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            0,
            10,
            20,
            30,
            40
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            20,
            30,
            40,
            50,
            60
        ],
        "magicDefence": [
            0,
            5,
            10,
            15,
            20
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "holy": "long50",
            "dark": "long50",
            "syphon": "long100"
        },
        "element": "Element.HOLY",
        "statusEffect": "Status.CURSE",
        "statusChance": [
            30,
            50,
            70,
            85,
            100
        ],
        "statusDegree": [
            2,
            3,
            3,
            4,
            5
        ],
        "specials": [
            [
                "Equip.BOOST",
                "Element.HOLY"
            ],
            None,
            [
                "Equip.CAST",
                "Spells.talisman",
                0.5
            ],
            None,
            [
                "Equip.STATUS",
                "Status.AUTOLIFE",
                1,
                0.5
            ]
        ],
        "materials": [
            [
                "Items.leather",
                1
            ],
            [
                "Items.leather",
                3
            ],
            [
                "Items.gold",
                2,
                "Items.silver",
                2
            ],
            [
                "Items.grail",
                1,
                "Items.leather",
                3
            ]
        ]
    },
    "humanskull": {
        "SID": "humanskull",
        "type": "TOYS",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            0,
            10,
            20,
            30,
            40
        ],
        "defence": [
            0,
            5,
            10,
            20,
            30
        ],
        "magicAttack": [
            0,
            5,
            10,
            20,
            30
        ],
        "magicDefence": [
            0,
            5,
            10,
            20,
            30
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            5,
            10,
            20,
            30
        ],
        "resistance": {
            "bio": "long100",
            "dark": "long50",
            "curse": "long100"
        },
        "element": "Element.NONE",
        "statusEffect": "Status.BAD_LUCK",
        "statusChance": [
            30,
            50,
            70,
            85,
            100
        ],
        "statusDegree": [
            2,
            2,
            2,
            2,
            3
        ],
        "buffEffect": "Stats.DEFENCE",
        "buffChance": [
            30,
            40,
            50,
            60,
            70
        ],
        "buffDegree": [
            -20,
            -20,
            -25,
            -25,
            -30
        ],
        "specials": [
            [
                "Equip.BOOST_DEBUFFS"
            ],
            None,
            [
                "Equip.SUMMON",
                "Spells.deathP",
                1
            ],
            None,
            [
                "Equip.BOOST_STATUS"
            ]
        ],
        "materials": [
            [
                "Items.claw",
                1
            ],
            [
                "Items.claw",
                3
            ],
            [
                "Items.spike",
                4,
                "Items.claw",
                4
            ],
            [
                "Items.moonpearl",
                1,
                "Items.rune",
                3
            ]
        ]
    },
    "devilssunrise": {
        "SID": "devilssunrise",
        "type": "TOYS",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            25,
            35,
            50,
            70,
            90
        ],
        "defence": [
            0,
            5,
            10,
            15,
            20
        ],
        "magicAttack": [
            -30,
            -30,
            -30,
            -30,
            -30
        ],
        "magicDefence": [
            0,
            5,
            10,
            15,
            20
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            -10,
            -10,
            -10,
            -10,
            -10
        ],
        "resistance": {
            "holy": "long100",
            "burn": "long100",
            "weak": "long100"
        },
        "element": "Element.DARK",
        "statusEffect": "Status.DOOM",
        "statusChance": [
            30,
            35,
            40,
            45,
            50
        ],
        "statusDegree": [
            3,
            3,
            3,
            3,
            2
        ],
        "specials": [
            [
                "Equip.BOOST",
                "Element.DARK"
            ],
            None,
            None,
            None,
            [
                "Equip.CAST",
                "Spells.blackspikes",
                0.5
            ]
        ],
        "materials": [
            [
                "Items.iron",
                2
            ],
            [
                "Items.iron",
                4,
                "Items.shuriken",
                4
            ],
            [
                "Items.rune",
                2,
                "Items.shuriken",
                3
            ],
            [
                "Items.rune",
                5,
                "Summons.FallenBeheaded",
                1
            ]
        ]
    },
    "kingsguard": {
        "SID": "kingsguard",
        "type": "TOYS",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            15,
            25,
            40,
            55,
            70
        ],
        "defence": [
            0,
            5,
            10,
            15,
            20
        ],
        "magicAttack": [
            15,
            25,
            40,
            55,
            70
        ],
        "magicDefence": [
            0,
            5,
            10,
            15,
            20
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            -10,
            -10,
            -10,
            -10,
            -10
        ],
        "resistance": {
            "death": "long100",
            "dark": "long100",
            "curse": "long100"
        },
        "element": "Element.HOLY",
        "statusEffect": "Status.NONE",
        "buffEffect": "Stats.ACCURACY",
        "buffChance": [
            30,
            40,
            50,
            60,
            70
        ],
        "buffDegree": [
            -20,
            -20,
            -25,
            -25,
            -30
        ],
        "specials": [
            [
                "Equip.BOOST",
                "Element.HOLY"
            ],
            None,
            [
                "Equip.DEFEND_STATUS",
                "Status.BRAVE",
                2
            ],
            None,
            [
                "Equip.STATUS",
                "Status.BRAVE",
                1,
                0.3
            ]
        ],
        "materials": [
            [
                "Items.buckle",
                1
            ],
            [
                "Items.buckle",
                3
            ],
            [
                "Items.gold",
                3,
                "Items.ruby",
                1
            ],
            [
                "Items.gold",
                7,
                "Summons.FallenCrucified",
                1
            ]
        ]
    },
    "masamune": {
        "SID": "masamune",
        "type": "TOYS",
        "HP": [
            -50,
            -50,
            -50,
            -50,
            -50
        ],
        "attack": [
            70,
            90,
            110,
            130,
            150
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            70,
            90,
            110,
            130,
            150
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            5,
            10,
            15,
            20
        ],
        "evade": [
            0,
            5,
            10,
            15,
            20
        ],
        "resistance": {
            "wind": "long50",
            "thunder": "long50",
            "stun": "long100"
        },
        "element": "Element.WIND",
        "statusEffect": "Status.NONE",
        "specials": [
            [
                "Equip.BOOST",
                "Element.WIND"
            ],
            None,
            [
                "Equip.COUNTER",
                "Spells.backstab"
            ],
            None,
            [
                "Equip.CAST",
                "Spells.tempest",
                0.3
            ]
        ],
        "materials": [
            [
                "Items.shuriken",
                2
            ],
            [
                "Items.shuriken",
                8
            ],
            [
                "Items.gold",
                3,
                "Items.shuriken",
                16
            ],
            [
                "Items.mythril",
                1,
                "Items.shuriken",
                32
            ]
        ]
    },
    "leafshield": {
        "SID": "leafshield",
        "type": "TOYS",
        "HP": [
            0,
            0,
            5,
            10,
            20
        ],
        "attack": [
            -50,
            -50,
            -50,
            -50,
            -50
        ],
        "defence": [
            10,
            15,
            20,
            30,
            40
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            10,
            15,
            20,
            30,
            40
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            20,
            20,
            20,
            20,
            20
        ],
        "resistance": {
            "earth": "long50",
            "water": "long50",
            "bio": "long50"
        },
        "element": "Element.EARTH",
        "specials": [
            [
                "Equip.BOOST_HEALING"
            ],
            None,
            [
                "Equip.SUMMON",
                "Summons.IdolWood",
                0.5
            ],
            None,
            [
                "Equip.STATUS",
                "Status.REGEN",
                2,
                0.2
            ]
        ],
        "materials": [
            [
                "Items.herb",
                2
            ],
            [
                "Items.herb",
                8,
                "Items.root",
                2
            ],
            [
                "Items.root",
                10,
                "Items.emerald",
                2
            ],
            [
                "Items.emerald",
                6,
                "Items.opal",
                2
            ]
        ]
    },
    "dogsausage": {
        "SID": "dogsausage",
        "type": "TOYS",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            5,
            10,
            20,
            30,
            40
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            15,
            25,
            40,
            55,
            75
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            20,
            20,
            20,
            20,
            20
        ],
        "resistance": {
            "fire": "long50",
            "burn": "long100",
            "freeze": "long100"
        },
        "element": "Element.FIRE",
        "statusEffect": "Status.BURN",
        "statusChance": [
            50,
            60,
            70,
            80,
            100
        ],
        "statusDegree": [
            2,
            2,
            2,
            2,
            2
        ],
        "specials": [
            [
                "Equip.SCARE",
                "Foe.BEASTS"
            ],
            [
                "Equip.BOOST",
                "Element.FIRE"
            ],
            [
                "Equip.BOOST_FOOD"
            ],
            None,
            [
                "Equip.BOOST_BUFFS"
            ]
        ],
        "materials": [
            [
                "Items.beer",
                1
            ],
            [
                "Items.crisps",
                2
            ],
            [
                "Items.chips",
                1,
                "Summons.DogTanuki",
                1
            ],
            [
                "Items.chips",
                12,
                "Items.beer",
                8
            ]
        ]
    },
    "bloodbank": {
        "SID": "bloodbank",
        "type": "TOYS",
        "HP": [
            10,
            15,
            20,
            25,
            30
        ],
        "attack": [
            20,
            30,
            45,
            60,
            75
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            10,
            20,
            30,
            40
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            5,
            5,
            10,
            10
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "poison": "long100",
            "death": "long100",
            "weak": "long100"
        },
        "element": "Element.BIO",
        "statusEffect": "Status.POISON",
        "statusChance": [
            50,
            60,
            70,
            80,
            100
        ],
        "statusDegree": [
            2,
            2,
            2,
            2,
            2
        ],
        "specials": [
            [
                "Equip.BOOST",
                "Element.BIO"
            ],
            None,
            [
                "Equip.DRAIN_HP"
            ],
            None,
            [
                "Equip.STATUS",
                "Status.REGEN",
                2,
                0.3
            ]
        ],
        "materials": [
            [
                "Items.raspberries",
                2
            ],
            [
                "Items.blueberries",
                4
            ],
            [
                "Items.cloudberries",
                4,
                "Items.virus",
                4
            ],
            [
                "Items.darkmatter",
                1,
                "Items.virus",
                2
            ]
        ]
    },
    "bookofspells": {
        "SID": "bookofspells",
        "type": "TOYS",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            15,
            25,
            35,
            45,
            60
        ],
        "magicDefence": [
            10,
            20,
            25,
            30,
            40
        ],
        "accuracy": [
            -10,
            -10,
            -10,
            -10,
            -10
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "ice": "long50",
            "wind": "long50",
            "water": "long50"
        },
        "element": "Element.ICE",
        "statusEffect": "Status.FREEZE",
        "statusChance": [
            30,
            40,
            50,
            60,
            75
        ],
        "statusDegree": [
            2,
            2,
            2,
            2,
            2
        ],
        "specials": [
            [
                "Equip.BOOST",
                "Element.ICE"
            ],
            None,
            [
                "Equip.CAST",
                "Spells.lighten",
                0.25
            ],
            None,
            [
                "Equip.SUMMON",
                "Spells.hail",
                0.66
            ]
        ],
        "materials": [
            [
                "Items.snowball",
                5
            ],
            [
                "Items.snowball",
                25
            ],
            [
                "Items.ice",
                20,
                "Items.water",
                20
            ],
            [
                "Items.diamond",
                1,
                "Items.sapphire",
                2
            ]
        ]
    },
    "turtleshell": {
        "SID": "turtleshell",
        "type": "TOYS",
        "HP": [
            0,
            5,
            5,
            10,
            10
        ],
        "attack": [
            20,
            35,
            50,
            65,
            80
        ],
        "defence": [
            5,
            10,
            15,
            20,
            25
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            5,
            10,
            15,
            20,
            25
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "water": "long50",
            "wet": "long100",
            "fire": "long50"
        },
        "element": "Element.WATER",
        "specials": [
            [
                "Equip.BOOST",
                "Element.WATER"
            ],
            None,
            [
                "Equip.CAST",
                "Spells.pouringpike",
                0.4
            ],
            None,
            [
                "Equip.BOOST_FOOD"
            ]
        ],
        "materials": [
            [
                "Items.seashell",
                2
            ],
            [
                "Items.seashell",
                7,
                "Items.tape",
                1
            ],
            [
                "Summons.CreepGreen",
                1,
                "Items.seashell",
                12
            ],
            [
                "Items.moonpearl",
                2,
                "Items.sapphire",
                2
            ]
        ]
    },
    "icecreamsandwich": {
        "SID": "icecreamsandwich",
        "type": "TOYS",
        "HP": [
            0,
            5,
            5,
            10,
            15
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            5,
            10,
            15,
            20,
            30
        ],
        "magicAttack": [
            10,
            20,
            30,
            40,
            50
        ],
        "magicDefence": [
            5,
            10,
            15,
            20,
            30
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            5,
            5,
            10,
            10
        ],
        "resistance": {
            "water": "long50",
            "wet": "long100",
            "fire": "long50"
        },
        "element": "Element.ICE",
        "statusEffect": "Status.CHILL",
        "statusChance": [
            50,
            60,
            70,
            80,
            100
        ],
        "statusDegree": [
            2,
            2,
            2,
            2,
            2
        ],
        "specials": [
            [
                "Equip.BOOST_BUFFS"
            ],
            [
                "Equip.BOOST",
                "Element.ICE"
            ],
            [
                "Equip.CAST",
                "Spells.wafer",
                0.5
            ],
            None,
            [
                "Equip.BOOST_HEALING"
            ]
        ],
        "materials": [
            [
                "Items.snowball",
                2,
                "Items.raspberries",
                1
            ],
            [
                "Items.cupcake",
                2,
                "Items.snowball",
                4
            ],
            [
                "Items.moonpearl",
                1,
                "Summons.SlimeIcecream",
                1
            ],
            [
                "Items.moonpearl",
                1,
                "Summons.SlimeBigIcecream",
                1
            ]
        ]
    },
    "neonlightbulb": {
        "SID": "neonlightbulb",
        "type": "TOYS",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            10,
            20,
            30,
            40,
            50
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            10,
            20,
            30,
            40,
            50
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            10,
            20,
            35,
            50
        ],
        "resistance": {
            "thunder": "long50",
            "dark": "long50",
            "earth": "down30"
        },
        "element": "Element.THUNDER",
        "statusEffect": "Status.STUN",
        "statusChance": [
            10,
            20,
            30,
            40,
            50
        ],
        "statusDegree": [
            2,
            2,
            2,
            2,
            2
        ],
        "specials": [
            [
                "Equip.BOOST",
                "Element.THUNDER"
            ],
            None,
            [
                "Equip.CAST",
                "Spells.plasmacage",
                0.25
            ],
            None,
            [
                "Equip.COUNTER",
                "Spells.backstab"
            ]
        ],
        "materials": [
            [
                "Items.spring",
                2
            ],
            [
                "Items.glass",
                5
            ],
            [
                "Items.topaz",
                2,
                "Items.glass",
                20,
                "Items.plastic",
                2
            ],
            [
                "Items.topaz",
                7,
                "Summons.BatThunder",
                1
            ]
        ]
    },
    "riotshield": {
        "SID": "riotshield",
        "type": "TOYS",
        "HP": [
            30,
            35,
            40,
            45,
            50
        ],
        "attack": [
            10,
            20,
            35,
            50,
            65
        ],
        "defence": [
            10,
            20,
            30,
            40,
            50
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            10,
            20,
            30,
            40,
            50
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            -50,
            -50,
            -50,
            -50,
            -50
        ],
        "resistance": {
            "dark": "long50",
            "stagger": "long100",
            "death": "long100"
        },
        "element": "Element.DARK",
        "statusEffect": "Status.WEAKEN",
        "statusChance": [
            30,
            50,
            70,
            85,
            100
        ],
        "statusDegree": [
            2,
            2,
            2,
            2,
            3
        ],
        "specials": [
            [
                "Equip.BOOST",
                "Element.DARK"
            ],
            None,
            [
                "Equip.COUNTER",
                "Spells.backstab"
            ],
            None,
            [
                "Equip.SUMMON",
                "Spells.bind",
                1
            ]
        ],
        "materials": [
            [
                "Items.bomb",
                2
            ],
            [
                "Items.plastic",
                3
            ],
            [
                "Items.kevlar",
                2,
                "Items.plastic",
                15
            ],
            [
                "Items.rune",
                2,
                "Items.cpu",
                1,
                "Items.kevlar",
                1
            ]
        ]
    },
    "banditblade": {
        "SID": "banditblade",
        "type": "TOYS",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            10,
            20,
            30,
            45,
            60
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            10,
            20,
            30,
            45,
            60
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            5,
            10,
            15,
            20,
            25
        ],
        "resistance": {
            "wind": "long50",
            "stun": "long100",
            "stagger": "long100"
        },
        "element": "Element.WATER",
        "specials": [
            [
                "Equip.BOOST",
                "Element.WATER"
            ],
            None,
            [
                "Equip.STEAL"
            ],
            None,
            [
                "Equip.STATUS",
                "Status.HASTE",
                2,
                0.2
            ]
        ],
        "materials": [
            [
                "Items.buckle",
                1
            ],
            [
                "Items.buckle",
                2,
                "Items.leather",
                1
            ],
            [
                "Items.silver",
                4,
                "Items.leather",
                4
            ],
            [
                "Items.moonpearl",
                2,
                "Items.silver",
                4,
                "Items.buckle",
                8
            ]
        ]
    },
    "powerpaw": {
        "SID": "powerpaw",
        "type": "TOYS",
        "HP": [
            0,
            5,
            5,
            10,
            10
        ],
        "attack": [
            20,
            35,
            45,
            60,
            75
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            10,
            20,
            30,
            40
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            5,
            10,
            15,
            20,
            25
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "bomb": "long50",
            "thunder": "long50",
            "bio": "long50"
        },
        "element": "Element.BOMB",
        "statusEffect": "Status.STAGGER",
        "statusChance": [
            30,
            35,
            40,
            45,
            50
        ],
        "statusDegree": [
            1
        ],
        "specials": [
            [
                "Equip.BOOST",
                "Element.BOMB"
            ],
            None,
            [
                "Equip.CAST",
                "Spells.bullet",
                0.66
            ],
            None,
            [
                "Equip.SUMMON",
                "Summons.PixelIdol",
                0.8
            ]
        ],
        "materials": [
            [
                "Items.spring",
                1,
                "Items.tape",
                1
            ],
            [
                "Items.floppy",
                2,
                "Items.tape",
                2
            ],
            [
                "Items.cpu",
                1,
                "Summons.IdolMetal",
                1
            ],
            [
                "Items.gamechild",
                1,
                "Items.cpu",
                1,
                "Items.floppy",
                2
            ]
        ]
    },
    "starhammer": {
        "SID": "starhammer",
        "type": "TOYS",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            20,
            40,
            60,
            80,
            100
        ],
        "defence": [
            0,
            5,
            10,
            15,
            20
        ],
        "magicAttack": [
            20,
            40,
            60,
            80,
            100
        ],
        "magicDefence": [
            0,
            5,
            10,
            15,
            20
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "fire": "long50",
            "ice": "long50",
            "thunder": "long50"
        },
        "element": "Element.NONE",
        "statusEffect": "Status.DISPEL",
        "statusChance": [
            20,
            40,
            60,
            80,
            100
        ],
        "statusDegree": [
            1
        ],
        "specials": [
            [
                "Equip.BOOST",
                "Element.NONE"
            ],
            None,
            [
                "Equip.CAST",
                "Spells.starpow",
                1
            ],
            None,
            [
                "Equip.SUMMON",
                "Spells.luckystar2",
                1
            ]
        ],
        "materials": [
            [
                "Items.lego",
                1,
                "Items.wood",
                10
            ],
            [
                "Items.lego",
                2,
                "Items.wood",
                20
            ],
            [
                "Items.grail",
                1,
                "Items.gold",
                5
            ],
            [
                "Items.starfragment",
                3,
                "Items.darkmatter",
                1
            ]
        ]
    },
    "bustersword": {
        "SID": "bustersword",
        "type": "TOYS",
        "HP": [
            5,
            10,
            15,
            20,
            25
        ],
        "attack": [
            30,
            40,
            50,
            60,
            75
        ],
        "defence": [
            5,
            5,
            5,
            10,
            10
        ],
        "magicAttack": [
            30,
            40,
            50,
            60,
            75
        ],
        "magicDefence": [
            5,
            5,
            5,
            10,
            10
        ],
        "accuracy": [
            5,
            5,
            5,
            10,
            10
        ],
        "evade": [
            5,
            5,
            5,
            10,
            10
        ],
        "resistance": {
            "fire": "down30",
            "water": "down30",
            "wind": "down30"
        },
        "element": "Element.NONE",
        "specials": [
            [
                "Equip.CAST",
                "Spells.paperStars",
                0.2
            ],
            None,
            [
                "Equip.COUNTER",
                "Spells.backstab"
            ],
            None,
            [
                "Equip.BOOST_BUFFS"
            ]
        ],
        "materials": [
            [
                "Items.wool",
                2
            ],
            [
                "Items.brick",
                4
            ],
            [
                "Items.turd",
                5
            ],
            [
                "Items.snowball",
                1
            ]
        ]
    },
    "captainhat": {
        "SID": "captainshat",
        "type": "HAT_MALE",
        "HP": [
            5,
            5,
            5,
            5,
            10
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            0,
            5,
            10,
            15,
            20
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            5,
            10,
            15,
            20
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            5,
            10
        ],
        "resistance": {
            "dark": "long50",
            "bomb": "long50"
        },
        "specials": [
            None,
            None,
            [
                "Equip.BOOST_STATUS"
            ]
        ],
        "materials": [
            [
                "Items.wool",
                1
            ],
            [
                "Items.feather",
                3,
                "Items.seashell",
                1
            ],
            [
                "Items.satin",
                1,
                "Items.seashell",
                6
            ],
            [
                "Items.moonpearl",
                1,
                "Items.rune2",
                1,
                "Items.feather",
                3
            ]
        ]
    },
    "scottishcap": {
        "SID": "scottishcap",
        "type": "HAT_MALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            0,
            5,
            10,
            15,
            20
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            5,
            10,
            15,
            20
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "water": "long50",
            "wind": "long50",
            "death": "long100"
        },
        "specials": [
            [
                "Equip.STATUS",
                "Status.BLESS",
                2,
                0.25
            ],
            None,
            None,
            None,
            [
                "Equip.DEFEND_STATUS",
                "Status.BLESS",
                2
            ]
        ],
        "materials": [
            [
                "Items.wool",
                1
            ],
            [
                "Items.silk",
                1
            ],
            [
                "Items.silk",
                4
            ],
            [
                "Items.opal",
                2,
                "Items.silk",
                1
            ]
        ]
    },
    "dragonhelm": {
        "SID": "dragonhelm",
        "type": "HAT_MALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            0,
            5,
            5,
            5,
            10
        ],
        "defence": [
            5,
            10,
            15,
            20,
            25
        ],
        "magicAttack": [
            0,
            5,
            5,
            5,
            10
        ],
        "magicDefence": [
            5,
            10,
            15,
            20,
            25
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "fire": "long50",
            "earth": "long50",
            "burn": "long100"
        },
        "specials": [
            None,
            None,
            [
                "Equip.STATUS",
                "Status.BRAVE",
                2,
                0.15
            ]
        ],
        "materials": [
            [
                "Items.brick",
                2
            ],
            [
                "Items.magma",
                1,
                "Items.brick",
                1
            ],
            [
                "Items.topaz",
                1,
                "Items.magma",
                2
            ],
            [
                "Items.scales",
                1,
                "Items.topaz",
                1
            ]
        ]
    },
    "deathmask": {
        "SID": "deathmask",
        "type": "HAT_MALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            15,
            20,
            30,
            40,
            50
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            -25,
            -25,
            -25,
            -25,
            -25
        ],
        "evade": [
            -25,
            -25,
            -25,
            -25,
            -25
        ],
        "resistance": {
            "fire": "down30",
            "burn": "down30"
        },
        "specials": [],
        "materials": [
            [
                "Items.wood",
                1
            ],
            [
                "Items.wood",
                5
            ],
            [
                "Items.spike",
                2,
                "Items.root",
                4
            ],
            [
                "Items.darkmatter",
                1
            ]
        ]
    },
    "spacehelmet": {
        "SID": "spacehelmet",
        "type": "HAT_MALE",
        "HP": [
            5,
            5,
            10,
            10,
            15
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            10,
            15,
            20,
            25,
            30
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            10,
            15,
            20,
            25,
            30
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "poison": "long100",
            "burn": "long100",
            "wet": "long100"
        },
        "specials": [
            None,
            None,
            [
                "Equip.STATUS",
                "Status.REGEN",
                1,
                0.5
            ]
        ],
        "materials": [
            [
                "Items.glass",
                1
            ],
            [
                "Items.glass",
                3
            ],
            [
                "Items.plastic",
                8,
                "Items.satin",
                1
            ],
            [
                "Items.cpu",
                1,
                "Items.plastic",
                2
            ]
        ]
    },
    "headband": {
        "SID": "headband",
        "type": "HAT_MALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            0,
            5,
            5,
            10,
            10
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            5,
            5,
            10,
            10
        ],
        "accuracy": [
            5,
            10,
            10,
            15,
            15
        ],
        "evade": [
            5,
            5,
            10,
            10,
            15
        ],
        "resistance": {
            "fire": "long50",
            "bomb": "long50",
            "holy": "long50"
        },
        "specials": [
            [
                "Equip.STATUS",
                "Status.BRAVE",
                2,
                0.5
            ],
            None,
            [
                "Equip.DEFEND_BUFF",
                "Stats.MAGIC_DEFENCE",
                80
            ]
        ],
        "materials": [
            [
                "Items.wool",
                2
            ],
            [
                "Items.silk",
                1
            ],
            [
                "Items.satin",
                1,
                "Items.silk",
                3
            ],
            [
                "Items.satin",
                6
            ]
        ]
    },
    "cardboardbox": {
        "SID": "cardboardbox",
        "type": "HAT_MALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            0,
            5,
            5,
            10,
            10
        ],
        "magicAttack": [
            0,
            5,
            5,
            10,
            10
        ],
        "magicDefence": [
            0,
            5,
            10,
            15,
            20
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "thunder": "long50",
            "dispel": "long100",
            "syphon": "long100"
        },
        "specials": [
            [
                "Equip.BOOST_BUFFS",
                10
            ],
            None,
            None,
            None,
            [
                "Equip.BOOST_DEBUFFS",
                10
            ]
        ],
        "materials": [
            [
                "Items.wool",
                1
            ],
            [
                "Items.floppy",
                1
            ],
            [
                "Items.cpu",
                1
            ],
            [
                "Items.cpu",
                2,
                "Items.floppy",
                1
            ]
        ]
    },
    "puppyhat": {
        "SID": "puppyhat",
        "type": "HAT_MALE",
        "HP": [
            0,
            0,
            5,
            5,
            10
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            0,
            5,
            10,
            15,
            20
        ],
        "magicAttack": [
            5,
            5,
            10,
            15,
            20
        ],
        "magicDefence": [
            0,
            5,
            10,
            15,
            20
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "freeze": "long100",
            "stun": "long100",
            "dispel": "long100"
        },
        "specials": [
            [
                "Equip.BOOST_CATCH"
            ],
            None,
            [
                "Equip.SUMMON",
                "Summons.DogMaxi",
                0.5
            ]
        ],
        "materials": [
            [
                "Items.fur",
                1
            ],
            [
                "Items.fur",
                2,
                "Items.crisps",
                1
            ],
            [
                "Items.satin",
                1,
                "Items.buckle",
                1,
                "Items.fur",
                8
            ],
            [
                "Items.lego",
                1,
                "Items.burger",
                2
            ]
        ]
    },
    "armyhelmet": {
        "SID": "armyhelmet",
        "type": "HAT_MALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            5,
            10,
            15,
            20,
            25
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            5,
            10,
            15,
            20,
            25
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "bomb": "long50",
            "stagger": "long100",
            "stun": "long100"
        },
        "specials": [
            None,
            None,
            [
                "Equip.SUMMON",
                "Spells.medipack",
                1
            ]
        ],
        "materials": [
            [
                "Items.plastic",
                1
            ],
            [
                "Items.plastic",
                2
            ],
            [
                "Items.cpu",
                1
            ],
            [
                "Items.lego",
                1,
                "Items.plastic",
                4
            ]
        ]
    },
    "gasmask": {
        "SID": "gasmask",
        "type": "HAT_MALE",
        "HP": [
            0,
            5,
            5,
            10,
            10
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            0,
            5,
            10,
            15,
            20
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            5,
            10,
            15,
            20
        ],
        "accuracy": [
            -10,
            -10,
            -10,
            -10,
            -10
        ],
        "evade": [
            -10,
            -10,
            -10,
            -10,
            -10
        ],
        "resistance": {
            "bio": "long100",
            "poison": "long100"
        },
        "specials": [
            None,
            None,
            [
                "Equip.SUMMON",
                "Spells.poisongas",
                0.66
            ]
        ],
        "materials": [
            [
                "Items.glass",
                1
            ],
            [
                "Items.glass",
                2,
                "Items.plastic",
                1
            ],
            [
                "Items.plastic",
                1,
                "Items.cpu",
                1
            ],
            [
                "Items.cpu",
                2,
                "Items.plastic",
                1
            ]
        ]
    },
    "spelunkinghat": {
        "SID": "spelunkinghat",
        "type": "HAT_MALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "MP": [
            0
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            0,
            5,
            10,
            15,
            20
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            5,
            10,
            15,
            20
        ],
        "accuracy": [
            20,
            25,
            30,
            35,
            40
        ],
        "evade": [
            0,
            5,
            5,
            10,
            10
        ],
        "resistance": {
            "dark": "long50",
            "earth": "long50",
            "stagger": "long100"
        },
        "specials": [
            None,
            None,
            [
                "Equip.BOOST_CATCH"
            ],
            None,
            None
        ],
        "materials": [
            [
                "Items.wool",
                1
            ],
            [
                "Items.silk",
                1,
                "Items.wool",
                2
            ],
            [
                "Items.satin",
                2,
                "Items.buckle",
                1
            ],
            [
                "Items.satin",
                6,
                "Items.buckle",
                2
            ]
        ]
    },
    "genjihelmet": {
        "SID": "genjihelmet",
        "type": "HAT_MALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            5,
            5,
            10,
            15,
            20
        ],
        "defence": [
            5,
            10,
            15,
            20,
            25
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            5,
            5,
            5,
            5,
            5
        ],
        "resistance": {
            "earth": "long50",
            "wind": "long50"
        },
        "specials": [
            None,
            None,
            None,
            None,
            [
                "Equip.DEFEND_STATUS",
                "Status.GOOD_LUCK",
                3
            ]
        ],
        "materials": [
            [
                "Items.shuriken",
                1
            ],
            [
                "Items.shuriken",
                4
            ],
            [
                "Items.kevlar",
                1,
                "Items.buckle",
                1
            ],
            [
                "Items.kevlar",
                2
            ]
        ]
    },
    "pumpkinhead": {
        "SID": "pumpkinhead",
        "type": "HAT_MALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            5,
            10,
            15,
            20,
            25
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            5,
            10,
            15,
            20,
            25
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "holy": "long50",
            "bio": "long50",
            "curse": "long100"
        },
        "specials": [
            [
                "Equip.INTIMIDATE"
            ],
            None,
            None,
            [
                "Equip.SUMMON",
                "Summons.BatBlood",
                0.8
            ]
        ],
        "materials": [
            [
                "Items.pumpkin",
                1
            ],
            [
                "Items.pumpkin",
                4
            ],
            [
                "Items.watermelon",
                6
            ],
            [
                "Items.dragonfruit",
                8,
                "Items.pumpkin",
                8
            ]
        ]
    },
    "wizardhat": {
        "SID": "wizardhat",
        "type": "HAT_MALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            5,
            10,
            15,
            20,
            25
        ],
        "magicDefence": [
            5,
            10,
            15,
            20,
            25
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "holy": "long50",
            "syphon": "long100",
            "dispel": "long100"
        },
        "specials": [
            [
                "Equip.BOOST_HEALING"
            ]
        ],
        "materials": [
            [
                "Items.wool",
                1
            ],
            [
                "Items.wool",
                2,
                "Items.buckle",
                1
            ],
            [
                "Items.satin",
                2,
                "Items.buckle",
                1
            ],
            [
                "Items.satin",
                6,
                "Items.silk",
                1,
                "Items.herb",
                1
            ]
        ]
    },
    "baskethat": {
        "SID": "baskethat",
        "type": "HAT_MALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            0,
            5,
            10,
            10,
            10
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            5,
            5,
            10,
            10
        ],
        "accuracy": [
            5,
            10,
            15,
            20,
            25
        ],
        "evade": [
            5,
            10,
            15,
            20,
            25
        ],
        "resistance": {
            "weak": "long100",
            "death": "long100",
            "thunder": "long50"
        },
        "specials": [
            None,
            None,
            [
                "Equip.BOOST_THROWS"
            ]
        ],
        "materials": [
            [
                "Items.shuriken",
                1
            ],
            [
                "Items.shuriken",
                2,
                "Items.herb",
                1
            ],
            [
                "Items.leather",
                4,
                "Items.butterflywing",
                2
            ],
            [
                "Items.kevlar",
                2,
                "Items.butterflywing",
                2
            ]
        ]
    },
    "hornedhelmet": {
        "SID": "hornedhelmet",
        "type": "HAT_MALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            10,
            15,
            20,
            25,
            30
        ],
        "defence": [
            5,
            10,
            15,
            20,
            25
        ],
        "magicAttack": [
            -20,
            -20,
            -20,
            -20,
            -20
        ],
        "magicDefence": [
            5,
            10,
            15,
            20,
            25
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "ice": "long50",
            "wind": "long50"
        },
        "specials": [
            [
                "Equip.STATUS",
                "Status.BERSERK",
                1,
                2
            ]
        ],
        "materials": [
            [
                "Items.iron",
                1
            ],
            [
                "Items.claw",
                1
            ],
            [
                "Items.spike",
                3,
                "Items.beer",
                1
            ],
            [
                "Items.spike",
                8,
                "Items.beer",
                2
            ]
        ]
    },
    "santahat": {
        "SID": "santahat",
        "type": "HAT_MALE",
        "HP": [
            0,
            0,
            0,
            5,
            10
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            0,
            5,
            10,
            15,
            20
        ],
        "magicAttack": [
            0,
            0,
            0,
            5,
            10
        ],
        "magicDefence": [
            0,
            5,
            10,
            15,
            20
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "ice": "long50",
            "freeze": "long100",
            "holy": "long50"
        },
        "specials": [
            [
                "Equip.SUMMON",
                "Spells.present",
                1.5
            ],
            None,
            None,
            None,
            [
                "Equip.BOOST_FOOD"
            ]
        ],
        "materials": [
            [
                "Items.wool",
                1,
                "Items.snowball",
                1
            ],
            [
                "Items.silk",
                1,
                "Items.snowball",
                1
            ],
            [
                "Items.satin",
                2,
                "Items.snowball",
                1
            ],
            [
                "Items.satin",
                7,
                "Items.snowball",
                5
            ]
        ]
    },
    "knighthelmet": {
        "SID": "knightshelmet",
        "type": "HAT_MALE",
        "HP": [
            5,
            5,
            5,
            10,
            15
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            15,
            20,
            25,
            30,
            40
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            5,
            10,
            15,
            20,
            25
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "fire": "down30",
            "water": "down30",
            "thunder": "long50"
        },
        "specials": [
            None,
            None,
            [
                "Equip.SUMMON",
                "Summons.CatWarrior",
                0.66
            ]
        ],
        "materials": [
            [
                "Items.iron",
                1
            ],
            [
                "Items.steel",
                1
            ],
            [
                "Items.silver",
                3,
                "Items.steel",
                2
            ],
            [
                "Items.silver",
                8,
                "Items.steel",
                2
            ]
        ]
    },
    "officerhat": {
        "SID": "officershat",
        "type": "HAT_MALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            5,
            10,
            15
        ],
        "defence": [
            0,
            5,
            5,
            10,
            10
        ],
        "magicAttack": [
            0,
            0,
            5,
            10,
            15
        ],
        "magicDefence": [
            0,
            5,
            10,
            10,
            10
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "dark": "long50",
            "thunder": "long50",
            "fire": "long50"
        },
        "specials": [
            None,
            None,
            None,
            None,
            [
                "Equip.SUMMON",
                "Spells.tankcannon",
                0.66
            ]
        ],
        "materials": [
            [
                "Items.wool",
                1
            ],
            [
                "Items.silk",
                1
            ],
            [
                "Items.satin",
                1,
                "Items.silk",
                4
            ],
            [
                "Items.satin",
                5,
                "Items.powder",
                10,
                "Items.bomb",
                10
            ]
        ]
    },
    "spartanhelmet": {
        "SID": "spartanhelmet",
        "type": "HAT_MALE",
        "HP": [
            0,
            5,
            5,
            10,
            10
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            5,
            10,
            15,
            20,
            25
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            5,
            10,
            15,
            20,
            25
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "fire": "long50",
            "death": "long100"
        },
        "specials": [
            [
                "Equip.DEFEND_BUFF",
                "Stats.HP",
                20
            ],
            None,
            [
                "Equip.STATUS",
                "Status.MORALE",
                2,
                0.5
            ]
        ],
        "materials": [
            [
                "Items.iron",
                1
            ],
            [
                "Items.buckle",
                1
            ],
            [
                "Items.gold",
                1,
                "Items.buckle",
                1
            ],
            [
                "Items.gold",
                3,
                "Items.amber",
                1
            ]
        ]
    },
    "skullhelmet": {
        "SID": "necromandershelmet",
        "type": "HAT_MALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            10,
            15,
            20,
            25,
            30
        ],
        "defence": [
            10,
            15,
            20,
            25,
            30
        ],
        "magicAttack": [
            10,
            15,
            20,
            25,
            30
        ],
        "magicDefence": [
            10,
            15,
            20,
            25,
            30
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "holy": "down30",
            "fire": "down30"
        },
        "specials": [
            [
                "Equip.STATUS",
                "Status.CURSE",
                2,
                0.5
            ]
        ],
        "materials": [
            [
                "Items.seashell",
                1
            ],
            [
                "Items.claw",
                1
            ],
            [
                "Items.spike",
                2,
                "Items.gems",
                2
            ],
            [
                "Items.spike",
                5,
                "Items.rune",
                1
            ]
        ]
    },
    "bunnyears": {
        "SID": "bunnyears",
        "type": "HAT_FEMALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            10,
            15,
            20,
            25,
            35
        ],
        "resistance": {
            "stun": "long100",
            "stagger": "long100"
        },
        "specials": [
            [
                "Equip.STATUS",
                "Status.HASTE",
                2,
                0.125
            ],
            None,
            [
                "Equip.DEFEND_BUFF",
                "Stats.EVADE",
                30
            ],
            None,
            [
                "Equip.BOOST_CATCH"
            ]
        ],
        "materials": [
            [
                "Items.feather",
                1
            ],
            [
                "Items.silk",
                1,
                "Items.feather",
                1
            ],
            [
                "Items.silk",
                2,
                "Items.amber",
                4
            ],
            [
                "Items.moonpearl",
                1,
                "Items.silk",
                2
            ]
        ]
    },
    "redribbon": {
        "SID": "redribbon",
        "type": "HAT_FEMALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0,
            5,
            10
        ],
        "defence": [
            0,
            5,
            10,
            15,
            20
        ],
        "magicAttack": [
            0,
            0,
            0,
            5,
            10
        ],
        "magicDefence": [
            0,
            5,
            10,
            15,
            20
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "fire": "long50",
            "ice": "long50",
            "thunder": "long50"
        },
        "specials": [
            None,
            None,
            None,
            None,
            [
                "Equip.STATUS",
                "Status.AUTOLIFE",
                2,
                0.15
            ]
        ],
        "materials": [
            [
                "Items.wool",
                1
            ],
            [
                "Items.silk",
                1
            ],
            [
                "Items.satin",
                1,
                "Items.gems",
                10
            ],
            [
                "Items.satin",
                3,
                "Items.gems",
                20
            ]
        ]
    },
    "catears": {
        "SID": "kittyears",
        "type": "HAT_FEMALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            0,
            5,
            5,
            10,
            10
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            5,
            5,
            10,
            10
        ],
        "accuracy": [
            5,
            5,
            10,
            10,
            15
        ],
        "evade": [
            5,
            5,
            10,
            10,
            15
        ],
        "resistance": {
            "curse": "long100",
            "weak": "long100"
        },
        "specials": [
            None,
            [
                "Equip.DEFEND_STATUS",
                "Status.GOOD_LUCK",
                3
            ],
            None,
            [
                "Equip.SUMMON",
                "Summons.CatWizard",
                1
            ]
        ],
        "materials": [
            [
                "Items.shuriken",
                1
            ],
            [
                "Items.powder",
                2,
                "Items.wool",
                1
            ],
            [
                "Items.satin",
                2,
                "Items.powder",
                2
            ],
            [
                "Items.rune",
                1,
                "Items.satin",
                3
            ]
        ]
    },
    "cowhorns": {
        "SID": "curlyhorns",
        "type": "HAT_FEMALE",
        "HP": [
            0,
            5,
            5,
            10,
            15
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            0,
            5,
            10,
            15,
            20
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            5,
            10,
            15,
            20
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "dispel": "long100",
            "syphon": "long100",
            "stagger": "long100"
        },
        "specials": [
            None,
            None,
            [
                "Equip.DEFEND_BUFF",
                "Stats.DEFENCE",
                80
            ],
            None,
            [
                "Equip.BOOST_CATCH"
            ]
        ],
        "materials": [
            [
                "Items.brick",
                1
            ],
            [
                "Items.coffee",
                1
            ],
            [
                "Items.coffee",
                3,
                "Items.spike",
                2
            ],
            [
                "Items.coffee",
                10,
                "Items.spike",
                6
            ]
        ]
    },
    "nursehat": {
        "SID": "nursehat",
        "type": "HAT_FEMALE",
        "HP": [
            0,
            0,
            0,
            0,
            5
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            0,
            5,
            10,
            15,
            20
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            5
        ],
        "magicDefence": [
            0,
            5,
            10,
            15,
            20
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "stun": "long100",
            "death": "long100",
            "dark": "long50"
        },
        "specials": [
            [
                "Equip.BOOST_HEALING"
            ],
            None,
            [
                "Equip.SUMMON",
                "Spells.heal",
                0.66
            ]
        ],
        "materials": [
            [
                "Items.apple",
                1
            ],
            [
                "Items.cupcake",
                1
            ],
            [
                "Items.coffee",
                2,
                "Items.satin",
                2
            ],
            [
                "Items.lego",
                1,
                "Items.burger",
                2
            ]
        ]
    },
    "iceshards": {
        "SID": "iceshards",
        "type": "HAT_FEMALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            5,
            10,
            15,
            20,
            25
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            5,
            10,
            15,
            20,
            25
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            5,
            10,
            15,
            20
        ],
        "resistance": {
            "ice": "long50",
            "fire": "long50",
            "freeze": "long100"
        },
        "specials": [
            None,
            None,
            [
                "Equip.SUMMON",
                "Summons.CreepIcicle",
                0.6
            ]
        ],
        "materials": [
            [
                "Items.snowball",
                2
            ],
            [
                "Items.water",
                1
            ],
            [
                "Items.water",
                6,
                "Items.ice",
                6
            ],
            [
                "Items.sapphire",
                4,
                "Items.water",
                7
            ]
        ]
    },
    "leafclip": {
        "SID": "leafyhairclip",
        "type": "HAT_FEMALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "MP": [
            0
        ],
        "attack": [
            5,
            5,
            5,
            10,
            10
        ],
        "defence": [
            0,
            5,
            10,
            15,
            20
        ],
        "magicAttack": [
            5,
            5,
            5,
            10,
            10
        ],
        "magicDefence": [
            0,
            5,
            10,
            15,
            20
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "bio": "long50",
            "earth": "long50",
            "poison": "long100"
        },
        "specials": [
            None,
            None,
            [
                "Equip.DEFEND_STATUS",
                "Status.BLESS",
                2
            ],
            None,
            [
                "Equip.SUMMON",
                "Summons.WraithLeaf",
                0.33
            ]
        ],
        "materials": [
            [
                "Items.herb",
                1
            ],
            [
                "Items.herb",
                2,
                "Items.flower",
                2
            ],
            [
                "Items.flower",
                8,
                "Items.amber",
                6
            ],
            [
                "Items.emerald",
                3,
                "Items.amber",
                3
            ]
        ]
    },
    "robotears": {
        "SID": "robotears",
        "type": "HAT_FEMALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "MP": [
            0
        ],
        "attack": [
            0,
            5,
            5,
            10,
            15
        ],
        "defence": [
            5,
            5,
            10,
            15,
            20
        ],
        "magicAttack": [
            0,
            5,
            5,
            10,
            15
        ],
        "magicDefence": [
            5,
            5,
            10,
            15,
            20
        ],
        "accuracy": [
            10,
            15,
            20,
            25,
            30
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "bio": "long50",
            "bomb": "long50",
            "thunder": "down30"
        },
        "specials": [
            [
                "Equip.SUMMON",
                "Summons.CatSniper",
                1
            ]
        ],
        "materials": [
            [
                "Items.spring",
                1
            ],
            [
                "Items.tape",
                2
            ],
            [
                "Items.cpu",
                1,
                "Items.floppy",
                1
            ],
            [
                "Items.cpu",
                2
            ]
        ]
    },
    "rubberduck": {
        "SID": "rubberduck",
        "type": "HAT_FEMALE",
        "HP": [
            5,
            5,
            5,
            5,
            10
        ],
        "attack": [
            0,
            5,
            5,
            10,
            10
        ],
        "defence": [
            0,
            5,
            5,
            10,
            10
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "water": "long50",
            "fire": "long50",
            "burn": "long100"
        },
        "specials": [
            [
                "Equip.BOOST_BUFFS",
                10
            ],
            None,
            None,
            None,
            [
                "Equip.BOOST_DEBUFFS",
                10
            ]
        ],
        "materials": [
            [
                "Items.feather",
                1
            ],
            [
                "Items.ice",
                1
            ],
            [
                "Items.ice",
                8
            ],
            [
                "Items.moonpearl",
                1,
                "Items.ice",
                8
            ]
        ]
    },
    "darkbauble": {
        "SID": "darkbobble",
        "type": "HAT_FEMALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            10,
            15,
            20,
            25,
            30
        ],
        "magicDefence": [
            10,
            15,
            20,
            25,
            30
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "dark": "long50",
            "syphon": "long100"
        },
        "specials": [
            None,
            None,
            [
                "Equip.DEFEND_BUFF",
                "Stats.MAGIC_ATTACK",
                80
            ]
        ],
        "materials": [
            [
                "Items.powder",
                1
            ],
            [
                "Items.powder",
                3
            ],
            [
                "Items.rune",
                1
            ],
            [
                "Items.rune",
                2,
                "Items.opal",
                1
            ]
        ]
    },
    "popehat": {
        "SID": "popehat",
        "type": "HAT_FEMALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            20,
            30,
            40,
            50,
            60
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "holy": "long50",
            "water": "long50",
            "curse": "long100"
        },
        "specials": [
            [
                "Equip.SCARE",
                "Foe.GHOSTS"
            ]
        ],
        "materials": [
            [
                "Items.wool",
                1
            ],
            [
                "Items.silk",
                1,
                "Items.butterflywing",
                1
            ],
            [
                "Items.satin",
                1,
                "Items.gold",
                1
            ],
            [
                "Items.satin",
                3,
                "Items.gold",
                3
            ]
        ]
    },
    "hollyhairpin": {
        "SID": "hollyhairpin",
        "type": "HAT_FEMALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "MP": [
            0
        ],
        "attack": [
            0,
            5,
            5,
            10,
            10
        ],
        "defence": [
            5,
            10,
            15,
            20,
            25
        ],
        "magicAttack": [
            0,
            5,
            5,
            10,
            10
        ],
        "magicDefence": [
            5,
            10,
            15,
            20,
            25
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "holy": "long50",
            "dispel": "long100",
            "freeze": "long100"
        },
        "specials": [
            [
                "Equip.SUMMON",
                "Spells.candycane",
                1
            ],
            None,
            None,
            None,
            [
                "Equip.BOOST_FOOD"
            ]
        ],
        "materials": [
            [
                "Items.snowball",
                2
            ],
            [
                "Items.snowball",
                8
            ],
            [
                "Items.satin",
                1,
                "Items.silk",
                4
            ],
            [
                "Items.lego",
                1,
                "Items.satin",
                1
            ]
        ]
    },
    "flowerbobble": {
        "SID": "flowerbobble",
        "type": "HAT_FEMALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "MP": [
            0
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            0,
            5,
            10,
            15,
            20
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            5,
            10,
            15,
            20,
            25
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            5,
            10
        ],
        "resistance": {
            "earth": "long50",
            "weak": "long100",
            "holy": "long50"
        },
        "specials": [
            None,
            [
                "Equip.STATUS",
                "Status.LOVED",
                1,
                0.3
            ],
            None,
            [
                "Equip.SUMMON",
                "Spells.remedy",
                0.66
            ]
        ],
        "materials": [
            [
                "Items.flower",
                1
            ],
            [
                "Items.flower",
                3
            ],
            [
                "Items.rune2",
                3
            ],
            [
                "Items.opal",
                1,
                "Items.rune2",
                2
            ]
        ]
    },
    "drillbits": {
        "SID": "drillbits",
        "type": "HAT_FEMALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "MP": [
            0
        ],
        "attack": [
            15,
            20,
            25,
            30,
            35
        ],
        "defence": [
            15,
            20,
            25,
            30,
            35
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "earth": "long50",
            "thunder": "down30",
            "stun": "down30"
        },
        "specials": [
            None
        ],
        "materials": [
            [
                "Items.turd",
                2
            ],
            [
                "Items.turd",
                4,
                "Items.iron",
                3
            ],
            [
                "Items.silver",
                3,
                "Items.steel",
                4
            ],
            [
                "Items.silver",
                8
            ]
        ]
    },
    "spiderbobble": {
        "SID": "spiderbobble",
        "type": "HAT_FEMALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            0,
            5,
            5,
            10,
            10
        ],
        "defence": [
            5,
            5,
            10,
            15,
            20
        ],
        "magicAttack": [
            0,
            5,
            5,
            10,
            10
        ],
        "magicDefence": [
            5,
            5,
            10,
            15,
            20
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            5,
            5,
            10,
            10
        ],
        "resistance": {
            "death": "long100",
            "dark": "long50",
            "curse": "long100"
        },
        "specials": [
            [
                "Equip.INTIMIDATE"
            ],
            None,
            [
                "Equip.SUMMON",
                "Spells.spiders",
                0.66
            ]
        ],
        "materials": [
            [
                "Items.powder",
                1
            ],
            [
                "Items.powder",
                3
            ],
            [
                "Items.virus",
                6
            ],
            [
                "Items.virus",
                6,
                "Items.rune",
                2
            ]
        ]
    },
    "royalcrown": {
        "SID": "royalcrown",
        "type": "HAT_FEMALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "MP": [
            0
        ],
        "attack": [
            5,
            10,
            10,
            15,
            20
        ],
        "defence": [
            0,
            5,
            5,
            10,
            10
        ],
        "magicAttack": [
            5,
            10,
            10,
            15,
            20
        ],
        "magicDefence": [
            0,
            5,
            5,
            10,
            10
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "thunder": "long50",
            "water": "long50"
        },
        "specials": [
            None,
            None,
            [
                "Equip.STATUS",
                "Status.BRAVE",
                2,
                0.15
            ]
        ],
        "materials": [
            [
                "Items.silver",
                1
            ],
            [
                "Items.gold",
                1
            ],
            [
                "Items.gold",
                1,
                "Items.gems",
                1
            ],
            [
                "Items.gold",
                1,
                "Items.sapphire",
                2
            ]
        ]
    },
    "slimebunny": {
        "SID": "slimebunny",
        "type": "HAT_FEMALE",
        "HP": [
            10,
            15,
            20,
            25,
            30
        ],
        "MP": [
            0
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            5,
            5,
            10,
            15,
            20
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            5,
            5,
            10,
            15,
            20
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "death": "down30",
            "dark": "down30",
            "curse": "long100"
        },
        "specials": [
            [
                "Equip.STATUS",
                "Status.REGEN",
                2,
                0.15
            ],
            None,
            None,
            None,
            [
                "Equip.SUMMON",
                "Spells.cleanse",
                1
            ]
        ],
        "materials": [
            [
                "Items.flower",
                1
            ],
            [
                "Items.flower",
                3
            ],
            [
                "Items.amber",
                10
            ],
            [
                "Items.moonpearl",
                1,
                "Items.cupcake",
                5
            ]
        ]
    },
    "furhat": {
        "SID": "furhat",
        "type": "HAT_FEMALE",
        "HP": [
            0,
            5,
            5,
            10,
            10
        ],
        "MP": [
            0
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            10,
            15,
            20,
            25,
            30
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            10,
            15,
            20,
            25,
            30
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "ice": "long50",
            "water": "long50",
            "wind": "long50"
        },
        "specials": [
            None,
            None,
            [
                "Equip.SUMMON",
                "Summons.MammothWooly",
                0.15
            ]
        ],
        "materials": [
            [
                "Items.fur",
                1
            ],
            [
                "Items.fur",
                3
            ],
            [
                "Items.fur",
                20
            ],
            [
                "Items.satin",
                4,
                "Items.fur",
                20
            ]
        ]
    },
    "blueelephant": {
        "SID": "blueelephant",
        "type": "HAT_FEMALE",
        "HP": [
            10,
            15,
            15,
            20,
            20
        ],
        "attack": [
            0,
            0,
            0,
            0,
            5
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            5
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "bomb": "long50",
            "water": "long50",
            "bio": "long50"
        },
        "specials": [
            None,
            None,
            [
                "Equip.BOOST_STATUS"
            ],
            None,
            [
                "Equip.SUMMON",
                "Summons.MammothWar",
                0.15
            ]
        ],
        "materials": [
            [
                "Items.tape",
                2
            ],
            [
                "Items.pretzel",
                2
            ],
            [
                "Items.burger",
                1
            ],
            [
                "Items.gamechild",
                1
            ]
        ]
    },
    "ninjachopsticks": {
        "SID": "ninjachopsticks",
        "type": "HAT_FEMALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            0,
            5,
            10,
            10,
            10
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            5,
            5,
            10,
            10
        ],
        "accuracy": [
            5,
            10,
            15,
            20,
            25
        ],
        "evade": [
            5,
            10,
            15,
            20,
            25
        ],
        "resistance": {
            "weak": "long100",
            "wind": "long50",
            "thunder": "long50"
        },
        "specials": [
            None,
            None,
            [
                "Equip.BOOST_THROWS"
            ]
        ],
        "materials": [
            [
                "Items.shuriken",
                1
            ],
            [
                "Items.shuriken",
                4
            ],
            [
                "Items.shuriken",
                8,
                "Items.silver",
                3
            ],
            [
                "Items.rune",
                3,
                "Items.shuriken",
                2
            ]
        ]
    },
    "orangebauble": {
        "SID": "fierybobble",
        "type": "HAT_FEMALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            5,
            5,
            5,
            10,
            10
        ],
        "magicAttack": [
            5,
            5,
            5,
            10,
            10
        ],
        "magicDefence": [
            0,
            5,
            10,
            15,
            25
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            5,
            5,
            5,
            10,
            10
        ],
        "resistance": {
            "fire": "long50",
            "thunder": "long50",
            "holy": "long50"
        },
        "specials": [
            None,
            None,
            [
                "Equip.SUMMON",
                "Summons.GloopWood",
                0.25
            ]
        ],
        "materials": [
            [
                "Items.geode",
                1
            ],
            [
                "Items.amber",
                1
            ],
            [
                "Items.amber",
                7
            ],
            [
                "Items.magma",
                7,
                "Items.amber",
                7
            ]
        ]
    },
    "hoboclothes": {
        "SID": "hoboclothes",
        "type": "ARMOR_MALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            0,
            5,
            5,
            10,
            10
        ],
        "defence": [
            5,
            10,
            15,
            20,
            25
        ],
        "magicAttack": [
            0,
            5,
            5,
            10,
            10
        ],
        "magicDefence": [
            5,
            10,
            15,
            20,
            25
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            5,
            5,
            5,
            5,
            10
        ],
        "resistance": {
            "stun": "long100",
            "bio": "long50",
            "death": "long100"
        },
        "specials": [
            None,
            None,
            [
                "Equip.BOOST",
                "Element.EARTH"
            ],
            [
                "Equip.STEAL"
            ],
            [
                "Equip.BOOST_DEBUFFS"
            ]
        ],
        "materials": [
            [
                "Items.wool",
                1,
                "Items.turd",
                1
            ],
            [
                "Items.wool",
                4,
                "Items.turd",
                4
            ],
            [
                "Items.leather",
                12,
                "Items.virus",
                3
            ],
            [
                "Items.kevlar",
                2,
                "Items.leather",
                4
            ]
        ]
    },
    "shellarmor": {
        "SID": "shellarmor",
        "type": "ARMOR_MALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            10,
            15,
            25,
            30,
            40
        ],
        "magicAttack": [
            0,
            5,
            5,
            10,
            10
        ],
        "magicDefence": [
            10,
            20,
            25,
            30,
            40
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "holy": "long100",
            "dispel": "long100"
        },
        "specials": [
            [
                "Equip.BOOST",
                "Element.HOLY"
            ],
            None,
            [
                "Equip.DEFEND_STATUS",
                "Status.ENCHANTED",
                1
            ]
        ],
        "materials": [
            [
                "Items.gems",
                1
            ],
            [
                "Items.silver",
                1
            ],
            [
                "Items.gold",
                2,
                "Items.silver",
                1
            ],
            [
                "Items.gold",
                5,
                "Items.ruby",
                1
            ]
        ]
    },
    "coatofteeth": {
        "SID": "coatofteeth",
        "type": "ARMOR_MALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            0,
            5,
            10,
            15,
            20
        ],
        "magicAttack": [
            5,
            10,
            15,
            20,
            25
        ],
        "magicDefence": [
            0,
            5,
            10,
            15,
            20
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            10,
            10,
            10,
            10,
            10
        ],
        "resistance": {
            "dark": "long50",
            "curse": "long100",
            "death": "long100"
        },
        "specials": [
            [
                "Equip.BOOST",
                "Element.DARK"
            ],
            None,
            [
                "Equip.BOOST_DEBUFFS",
                10
            ],
            None,
            [
                "Equip.SUMMON",
                "Spells.arcadeTeeth",
                0.6
            ]
        ],
        "materials": [
            [
                "Items.claw",
                1
            ],
            [
                "Items.claw",
                2
            ],
            [
                "Items.spike",
                1,
                "Items.rune",
                1
            ],
            [
                "Items.rune",
                4
            ]
        ]
    },
    "explorersjacket": {
        "SID": "explorersjacket",
        "type": "ARMOR_MALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            10,
            15,
            20,
            25,
            30
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            10,
            15,
            20,
            25,
            30
        ],
        "accuracy": [
            20,
            25,
            30,
            40,
            50
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "poison": "long100",
            "bio": "long50",
            "wet": "long100"
        },
        "specials": [
            [
                "Equip.BOOST",
                "Element.BIO"
            ],
            None,
            [
                "Equip.BOOST_CATCH"
            ]
        ],
        "materials": [
            [
                "Items.wool",
                2
            ],
            [
                "Items.silk",
                2
            ],
            [
                "Items.kevlar",
                1,
                "Items.buckle",
                4
            ],
            [
                "Items.kevlar",
                3,
                "Items.buckle",
                4
            ]
        ]
    },
    "spaceace": {
        "SID": "spaceace",
        "type": "ARMOR_MALE",
        "HP": [
            5,
            5,
            5,
            10,
            15
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            10,
            15,
            20,
            30,
            40
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            10,
            15,
            20,
            30,
            40
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "weight": "long100",
            "stun": "long100",
            "freeze": "long100"
        },
        "specials": [
            [
                "Equip.BOOST",
                "Element.THUNDER"
            ],
            None,
            [
                "Equip.SUMMON",
                "Spells.flare",
                0.6
            ],
            None,
            [
                "Equip.DEFEND_STATUS",
                "Status.REGEN",
                3
            ]
        ],
        "materials": [
            [
                "Items.tape",
                2
            ],
            [
                "Items.plastic",
                2
            ],
            [
                "Items.kevlar",
                1,
                "Items.plastic",
                2
            ],
            [
                "Items.kevlar",
                1,
                "Items.lego",
                1,
                "Items.plastic",
                4
            ]
        ]
    },
    "spartancuirass": {
        "SID": "spartancuirass",
        "type": "ARMOR_MALE",
        "HP": [
            5,
            5,
            10,
            10,
            15
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            10,
            15,
            25,
            30,
            40
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            10,
            20,
            25,
            30,
            40
        ],
        "accuracy": [
            5,
            5,
            5,
            5,
            5
        ],
        "evade": [
            5,
            5,
            5,
            5,
            5
        ],
        "resistance": {
            "bomb": "long50",
            "weak": "long100"
        },
        "specials": [
            None,
            [
                "Equip.DEFEND_BUFF",
                "Stats.DEFENCE",
                80
            ],
            None,
            [
                "Equip.SUMMON",
                "Summons.FallenCrucified",
                0.25
            ],
            [
                "Equip.BOOST",
                "Element.FIRE"
            ]
        ],
        "materials": [
            [
                "Items.iron",
                2
            ],
            [
                "Items.silver",
                1
            ],
            [
                "Items.silver",
                2,
                "Items.gold",
                1
            ],
            [
                "Items.gold",
                6,
                "Items.buckle",
                4
            ]
        ]
    },
    "flamesuit": {
        "SID": "flamesuit",
        "type": "ARMOR_MALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            5,
            10,
            15,
            25,
            30
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            5,
            10,
            20,
            25,
            30
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "fire": "long100",
            "burn": "long100"
        },
        "specials": [
            [
                "Equip.BOOST",
                "Element.WATER"
            ],
            [
                "Equip.BOOST_STATUS"
            ],
            None,
            [
                "Equip.BOOST_BUFFS",
                10
            ],
            None
        ],
        "materials": [
            [
                "Items.tape",
                2
            ],
            [
                "Items.plastic",
                2
            ],
            [
                "Items.kevlar",
                1,
                "Items.buckle",
                2
            ],
            [
                "Items.kevlar",
                3,
                "Items.plastic",
                2
            ]
        ]
    },
    "dragonarmor": {
        "SID": "dragonarmor",
        "type": "ARMOR_MALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            5,
            10,
            10
        ],
        "defence": [
            10,
            15,
            20,
            25,
            35
        ],
        "magicAttack": [
            0,
            0,
            5,
            10,
            10
        ],
        "magicDefence": [
            10,
            15,
            20,
            25,
            35
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            5
        ],
        "evade": [
            0,
            0,
            0,
            0,
            5
        ],
        "resistance": {
            "ice": "long50",
            "thunder": "long50",
            "fire": "long50"
        },
        "specials": [
            [
                "Equip.BOOST",
                "Element.FIRE"
            ],
            [
                "Equip.STATUS",
                "Status.GOOD_LUCK",
                2,
                0.5
            ],
            None
        ],
        "materials": [
            [
                "Items.brick",
                2
            ],
            [
                "Items.brick",
                8,
                "Items.magma",
                1
            ],
            [
                "Items.gold",
                1,
                "Items.magma",
                6
            ],
            [
                "Items.scales",
                1,
                "Items.gold",
                1
            ]
        ]
    },
    "officercoat": {
        "SID": "officerscoat",
        "type": "ARMOR_MALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            0,
            5,
            5,
            10,
            10
        ],
        "defence": [
            5,
            10,
            15,
            25,
            30
        ],
        "magicAttack": [
            0,
            5,
            5,
            10,
            10
        ],
        "magicDefence": [
            5,
            10,
            20,
            25,
            30
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "dark": "long50",
            "thunder": "long50",
            "fire": "long50"
        },
        "specials": [
            [
                "Equip.BOOST",
                "Element.DARK"
            ],
            None,
            [
                "Equip.SUMMON",
                "Spells.tankgun",
                0.45
            ]
        ],
        "materials": [
            [
                "Items.wool",
                2
            ],
            [
                "Items.silk",
                1,
                "Items.bomb",
                3
            ],
            [
                "Items.satin",
                2,
                "Items.rune",
                1
            ],
            [
                "Items.satin",
                6,
                "Items.rune",
                2,
                "Items.bomb",
                6
            ]
        ]
    },
    "scottishkilt": {
        "SID": "scottishkilt",
        "type": "ARMOR_MALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            5,
            5,
            10,
            10,
            15
        ],
        "defence": [
            5,
            10,
            15,
            25,
            30
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            5,
            10,
            20,
            25,
            30
        ],
        "accuracy": [
            5,
            5,
            10,
            10,
            15
        ],
        "evade": [
            0,
            5,
            5,
            10,
            15
        ],
        "resistance": {
            "earth": "long50",
            "wet": "long100",
            "ice": "down30"
        },
        "specials": [
            None,
            [
                "Equip.STATUS",
                "Status.MORALE",
                2,
                0.5
            ],
            None,
            [
                "Equip.SUMMON",
                "Spells.rain",
                0.66
            ],
            None
        ],
        "materials": [
            [
                "Items.wool",
                2
            ],
            [
                "Items.geode",
                4
            ],
            [
                "Items.satin",
                2,
                "Items.buckle",
                4,
                "Items.geode",
                4
            ],
            [
                "Items.opal",
                2,
                "Items.buckle",
                2
            ]
        ]
    },
    "heroicarmor": {
        "SID": "heroicarmor",
        "type": "ARMOR_MALE",
        "HP": [
            0,
            0,
            0,
            5,
            10
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            10,
            20,
            40,
            50,
            65
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            10,
            15,
            20,
            30,
            45
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            -20,
            -20,
            -20,
            -20,
            -20
        ],
        "resistance": {
            "fire": "down30",
            "water": "down30",
            "thunder": "long100"
        },
        "specials": [
            [
                "Equip.BOOST",
                "Element.NONE"
            ],
            None,
            [
                "Equip.STATUS",
                "Status.DEFEND",
                1,
                0.33
            ],
            None,
            None
        ],
        "materials": [
            [
                "Items.steel",
                1
            ],
            [
                "Items.steel",
                3
            ],
            [
                "Items.silver",
                6,
                "Items.steel",
                8
            ],
            [
                "Items.titanium",
                1
            ]
        ]
    },
    "camojacket": {
        "SID": "camojacket",
        "type": "ARMOR_MALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "MP": [
            0
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            10,
            15,
            20,
            25,
            30
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            10,
            15,
            20,
            25,
            30
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            5,
            10,
            15,
            20
        ],
        "resistance": {
            "bomb": "long50",
            "stagger": "long100"
        },
        "specials": [
            [
                "Equip.BOOST",
                "Element.BOMB"
            ],
            None,
            [
                "Equip.SUMMON",
                "Spells.airstrike1",
                1
            ]
        ],
        "materials": [
            [
                "Items.turd",
                2
            ],
            [
                "Items.turd",
                2,
                "Items.cactus",
                2,
                "Items.root",
                2
            ],
            [
                "Items.kevlar",
                1,
                "Items.floppy",
                3
            ],
            [
                "Items.kevlar",
                3,
                "Items.bomb",
                4
            ]
        ]
    },
    "priesttunic": {
        "SID": "prieststunic",
        "type": "ARMOR_MALE",
        "HP": [
            5,
            5,
            5,
            5,
            10
        ],
        "attack": [
            -10,
            -10,
            -10,
            -10,
            -10
        ],
        "defence": [
            5,
            10,
            15,
            25,
            30
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            20,
            25,
            30,
            35,
            40
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            10,
            10,
            10,
            10,
            10
        ],
        "resistance": {
            "holy": "long50",
            "dark": "long50",
            "poison": "long100"
        },
        "specials": [
            [
                "Equip.BOOST_HEALING"
            ],
            [
                "Equip.BOOST",
                "Element.HOLY"
            ],
            None,
            None,
            [
                "Equip.STATUS",
                "Status.AUTOLIFE",
                1,
                0.3
            ]
        ],
        "materials": [
            [
                "Items.feather",
                2
            ],
            [
                "Items.feather",
                6,
                "Items.buckle",
                1
            ],
            [
                "Items.silk",
                4,
                "Items.silver",
                2
            ],
            [
                "Items.moonpearl",
                1,
                "Items.silver",
                4
            ]
        ]
    },
    "wizardcloak": {
        "SID": "wizardrobe",
        "type": "ARMOR_MALE",
        "HP": [
            -10,
            -10,
            -10,
            -10,
            -10
        ],
        "attack": [
            -20,
            -20,
            -20,
            -20,
            -20
        ],
        "defence": [
            0,
            5,
            10,
            15,
            20
        ],
        "magicAttack": [
            15,
            20,
            25,
            30,
            45
        ],
        "magicDefence": [
            0,
            5,
            10,
            15,
            20
        ],
        "accuracy": [
            10,
            10,
            10,
            10,
            10
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "dispel": "long100",
            "syphon": "long100"
        },
        "specials": [
            None,
            None,
            [
                "Equip.DEFEND_BUFF",
                "Stats.MAGIC_ATTACK",
                80
            ]
        ],
        "materials": [
            [
                "Items.wool",
                2
            ],
            [
                "Items.butterflywing",
                3
            ],
            [
                "Items.satin",
                2,
                "Items.gems",
                2
            ],
            [
                "Items.ruby",
                3,
                "Items.emerald",
                3,
                "Items.sapphire",
                3
            ]
        ]
    },
    "genjiarmor": {
        "SID": "genjiarmor",
        "type": "ARMOR_MALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            5,
            5,
            10,
            15,
            20
        ],
        "defence": [
            10,
            20,
            30,
            35,
            40
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            5,
            5,
            10
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "earth": "long50",
            "wind": "long50"
        },
        "specials": [
            [
                "Equip.BOOST",
                "Element.EARTH"
            ],
            None,
            [
                "Equip.DEFEND_BUFF",
                "Stats.ATTACK",
                80
            ]
        ],
        "materials": [
            [
                "Items.shuriken",
                1,
                "Items.brick",
                1
            ],
            [
                "Items.shuriken",
                4,
                "Items.brick",
                4
            ],
            [
                "Items.kevlar",
                2,
                "Items.buckle",
                4
            ],
            [
                "Items.gold",
                2,
                "Items.kevlar",
                1,
                "Items.buckle",
                2
            ]
        ]
    },
    "ninjagear": {
        "SID": "ninjagear",
        "type": "ARMOR_MALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            0,
            5,
            5,
            10,
            15
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            5,
            5,
            10,
            15
        ],
        "accuracy": [
            10,
            15,
            15,
            20,
            25
        ],
        "evade": [
            10,
            10,
            15,
            20,
            25
        ],
        "resistance": {
            "wind": "long50",
            "thunder": "long50",
            "weight": "long100"
        },
        "specials": [
            [
                "Equip.BOOST",
                "Element.WIND"
            ],
            [
                "Equip.DEFEND_STATUS",
                "Status.INVISIBLE",
                1
            ],
            None,
            [
                "Equip.BOOST_THROWS"
            ],
            None
        ],
        "materials": [
            [
                "Items.shuriken",
                1,
                "Items.bomb",
                1
            ],
            [
                "Items.shuriken",
                4,
                "Items.bomb",
                4
            ],
            [
                "Items.rune",
                1,
                "Items.bomb",
                2,
                "Items.shuriken",
                2
            ],
            [
                "Items.kevlar",
                2,
                "Items.rune",
                2
            ]
        ]
    },
    "vikingfur": {
        "SID": "vikingfur",
        "type": "ARMOR_MALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            0,
            5,
            10,
            15,
            20
        ],
        "defence": [
            10,
            15,
            20,
            25,
            30
        ],
        "magicAttack": [
            -20,
            -20,
            -20,
            -20,
            -20
        ],
        "magicDefence": [
            10,
            15,
            20,
            25,
            30
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "water": "long50",
            "ice": "long50",
            "freeze": "long100"
        },
        "specials": [
            [
                "Equip.BOOST",
                "Element.ICE"
            ],
            None,
            [
                "Equip.SUMMON",
                "Summons.BearBrown",
                0.5
            ],
            None,
            [
                "Equip.BOOST_CATCH"
            ]
        ],
        "materials": [
            [
                "Items.fur",
                1
            ],
            [
                "Items.fur",
                2,
                "Items.buckle",
                1
            ],
            [
                "Items.spike",
                2,
                "Items.fur",
                12,
                "Items.buckle",
                1
            ],
            [
                "Items.rune2",
                15,
                "Items.buckle",
                1
            ]
        ]
    },
    "santaoutfit": {
        "SID": "santaoutfit",
        "type": "ARMOR_MALE",
        "HP": [
            0,
            0,
            5,
            10,
            15
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            10,
            15,
            20,
            25,
            30
        ],
        "magicAttack": [
            0,
            5,
            5,
            10,
            15
        ],
        "magicDefence": [
            10,
            15,
            20,
            25,
            30
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            -5,
            -5,
            -5,
            -5,
            -5
        ],
        "resistance": {
            "ice": "long50",
            "freeze": "long100",
            "holy": "long50"
        },
        "specials": [
            [
                "Equip.BOOST",
                "Element.ICE"
            ],
            None,
            [
                "Equip.SUMMON",
                "Spells.present",
                2
            ]
        ],
        "materials": [
            [
                "Items.snowball",
                2,
                "Items.wool",
                1
            ],
            [
                "Items.snowball",
                8,
                "Items.wool",
                4
            ],
            [
                "Items.burger",
                1,
                "Items.leather",
                8
            ],
            [
                "Items.lego",
                1,
                "Items.burger",
                2
            ]
        ]
    },
    "turtlegi": {
        "SID": "turtlegi",
        "type": "ARMOR_MALE",
        "HP": [
            0,
            0,
            5,
            5,
            10
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            5,
            10,
            15,
            20
        ],
        "evade": [
            0,
            5,
            10,
            15,
            20
        ],
        "resistance": {
            "stun": "long100",
            "stagger": "long100",
            "dispel": "long100"
        },
        "specials": [
            [
                "Equip.RANDOM_BUFFS"
            ],
            None,
            None,
            None,
            [
                "Equip.STATUS",
                "Status.MORALE",
                1,
                1
            ]
        ],
        "materials": [
            [
                "Items.wool",
                1,
                "Items.brick",
                1
            ],
            [
                "Items.silk",
                1,
                "Items.brick",
                8
            ],
            [
                "Items.satin",
                2,
                "Items.rune2",
                2
            ],
            [
                "Items.scales",
                1,
                "Items.satin",
                2
            ]
        ]
    },
    "hipstershirt": {
        "SID": "hipstershirt",
        "type": "ARMOR_MALE",
        "HP": [
            0,
            5,
            5,
            5,
            10
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            0,
            5,
            10,
            15,
            20
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            5,
            10,
            15,
            20
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            5,
            5,
            5,
            10
        ],
        "resistance": {
            "water": "long50",
            "stun": "long100",
            "death": "long100"
        },
        "specials": [
            [
                "Equip.BOOST_FOOD"
            ],
            None,
            [
                "Equip.BOOST_BUFFS",
                10
            ]
        ],
        "materials": [
            [
                "Items.wool",
                2
            ],
            [
                "Items.coffee",
                1
            ],
            [
                "Items.coffee",
                2,
                "Items.pretzel",
                2,
                "Items.burger",
                2
            ],
            [
                "Items.burger",
                6,
                "Items.bru",
                2
            ]
        ]
    },
    "captainscoat": {
        "SID": "captainscoat",
        "type": "ARMOR_MALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "MP": [
            0
        ],
        "attack": [
            0,
            5,
            5,
            10,
            10
        ],
        "defence": [
            5,
            10,
            15,
            20,
            25
        ],
        "magicAttack": [
            0,
            5,
            5,
            10,
            10
        ],
        "magicDefence": [
            5,
            10,
            15,
            20,
            25
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            5,
            5,
            5,
            5,
            10
        ],
        "resistance": {
            "water": "long50",
            "bomb": "long50"
        },
        "specials": [
            [
                "Equip.BOOST",
                "Element.WATER"
            ],
            None,
            [
                "Equip.SUMMON",
                "Summons.SquidPink",
                0.22
            ],
            None,
            [
                "Equip.BOOST_STATUS"
            ]
        ],
        "materials": [
            [
                "Items.seashell",
                2
            ],
            [
                "Items.buckle",
                2
            ],
            [
                "Items.leather",
                8,
                "Items.sapphire",
                2
            ],
            [
                "Items.sapphire",
                5,
                "Items.leather",
                3
            ]
        ]
    },
    "magicalskirt": {
        "SID": "magicalskirt",
        "type": "ARMOR_FEMALE",
        "HP": [
            0,
            5,
            5,
            10,
            10
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            10,
            15,
            20,
            25,
            30
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            10,
            15,
            20,
            25,
            30
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "poison": "long100",
            "death": "long100",
            "curse": "long100"
        },
        "specials": [
            [
                "Equip.BOOST",
                "Element.NONE"
            ],
            [
                "Equip.STATUS",
                "Status.LOVED",
                2,
                0.15
            ],
            None,
            None,
            [
                "Equip.SUMMON",
                "Summons.SlimeBunny",
                0.5
            ]
        ],
        "materials": [
            [
                "Items.feather",
                1
            ],
            [
                "Items.silk",
                2
            ],
            [
                "Items.satin",
                2,
                "Items.gems",
                4
            ],
            [
                "Items.moonpearl",
                1,
                "Items.opal",
                1
            ]
        ]
    },
    "bluedress": {
        "SID": "bubblydress",
        "type": "ARMOR_FEMALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            10,
            15,
            20,
            25,
            30
        ],
        "magicAttack": [
            5,
            5,
            10,
            15,
            20
        ],
        "magicDefence": [
            10,
            15,
            20,
            25,
            30
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "water": "long50",
            "dispel": "long100",
            "weak": "long100"
        },
        "specials": [
            [
                "Equip.BOOST",
                "Element.WATER"
            ],
            None,
            [
                "Equip.DEFEND_STATUS",
                "Status.ENCHANTED",
                1
            ],
            None,
            [
                "Equip.SUMMON",
                "Summons.BitIce",
                0.3
            ]
        ],
        "materials": [
            [
                "Items.butterflywing",
                1
            ],
            [
                "Items.ice",
                2
            ],
            [
                "Items.ice",
                4,
                "Items.satin",
                2
            ],
            [
                "Items.sapphire",
                2,
                "Items.moonpearl",
                1
            ]
        ]
    },
    "rangerskirt": {
        "SID": "rangerskirt",
        "type": "ARMOR_FEMALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            5,
            5,
            10,
            15,
            20
        ],
        "defence": [
            0,
            5,
            10,
            15,
            20
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            5,
            10,
            15,
            20
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            5,
            10,
            15,
            20,
            25
        ],
        "resistance": {
            "earth": "long50",
            "bio": "long50",
            "weak": "long100"
        },
        "specials": [
            [
                "Equip.BOOST",
                "Element.EARTH"
            ],
            None,
            [
                "Equip.SUMMON",
                "Spells.bind",
                1
            ],
            None,
            [
                "Equip.BOOST_CATCH"
            ]
        ],
        "materials": [
            [
                "Items.herb",
                1
            ],
            [
                "Items.herb",
                2,
                "Items.leather",
                1
            ],
            [
                "Items.leather",
                10,
                "Items.buckle",
                2
            ],
            [
                "Items.kevlar",
                2,
                "Items.leather",
                6
            ]
        ]
    },
    "maidoutfit": {
        "SID": "maidoutfit",
        "type": "ARMOR_FEMALE",
        "HP": [
            0,
            5,
            5,
            10,
            10
        ],
        "attack": [
            0,
            0,
            5,
            5,
            10
        ],
        "defence": [
            10,
            15,
            20,
            25,
            30
        ],
        "magicAttack": [
            0,
            0,
            5,
            5,
            10
        ],
        "magicDefence": [
            10,
            15,
            20,
            25,
            30
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "wind": "long50",
            "earth": "long50",
            "stun": "long100"
        },
        "specials": [
            [
                "Equip.BOOST_FOOD"
            ],
            None,
            [
                "Equip.BOOST_THROWS"
            ]
        ],
        "materials": [
            [
                "Items.cupcake",
                1
            ],
            [
                "Items.coffee",
                1
            ],
            [
                "Items.coffee",
                2,
                "Items.burger",
                2
            ],
            [
                "Items.coffee",
                10,
                "Items.burger",
                5
            ]
        ]
    },
    "schooluniform": {
        "SID": "schooluniform",
        "type": "ARMOR_FEMALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "MP": [
            0
        ],
        "attack": [
            0,
            5,
            10,
            15,
            20
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            10,
            15,
            20,
            30,
            40
        ],
        "resistance": {
            "weight": "long100",
            "weak": "long100",
            "curse": "long100"
        },
        "specials": [
            None,
            None,
            [
                "Equip.DEFEND_BUFF",
                "Stats.ATTACK",
                80
            ],
            [
                "Equip.STEAL"
            ]
        ],
        "materials": [
            [
                "Items.cola",
                1
            ],
            [
                "Items.cola",
                2
            ],
            [
                "Items.satin",
                3,
                "Items.cola",
                3
            ],
            [
                "Items.satin",
                12,
                "Items.cola",
                10
            ]
        ]
    },
    "camoskirt": {
        "SID": "camoskirt",
        "type": "ARMOR_FEMALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            5,
            10,
            10,
            15,
            20
        ],
        "defence": [
            5,
            5,
            10,
            15,
            20
        ],
        "magicAttack": [
            5,
            10,
            10,
            15,
            20
        ],
        "magicDefence": [
            5,
            5,
            10,
            15,
            20
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "bomb": "long50",
            "bio": "long50",
            "stagger": "long100"
        },
        "specials": [
            [
                "Equip.BOOST",
                "Element.BOMB"
            ],
            None,
            [
                "Equip.SUMMON",
                "Spells.medipack",
                1
            ],
            None
        ],
        "materials": [
            [
                "Items.cactus",
                2
            ],
            [
                "Items.cactus",
                6
            ],
            [
                "Items.leather",
                8,
                "Items.bomb",
                10
            ],
            [
                "Items.kevlar",
                3,
                "Items.cactus",
                2
            ]
        ]
    },
    "reddress": {
        "SID": "reddress",
        "type": "ARMOR_FEMALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            0,
            5,
            10,
            15,
            20
        ],
        "magicAttack": [
            0,
            5,
            5,
            10,
            10
        ],
        "magicDefence": [
            15,
            20,
            25,
            30,
            40
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "fire": "long50",
            "thunder": "long50",
            "ice": "long50"
        },
        "specials": [
            None,
            None,
            [
                "Equip.STATUS",
                "Status.GOOD_LUCK",
                2,
                0.5
            ],
            None,
            [
                "Equip.BOOST_STATUS"
            ]
        ],
        "materials": [
            [
                "Items.butterflywing",
                1
            ],
            [
                "Items.gems",
                3
            ],
            [
                "Items.gems",
                15,
                "Items.satin",
                4
            ],
            [
                "Items.sapphire",
                2,
                "Items.topaz",
                2,
                "Items.ruby",
                2
            ]
        ]
    },
    "obsidianarmor": {
        "SID": "obsidianarmor",
        "type": "ARMOR_FEMALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            20,
            30,
            40,
            50,
            60
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            15,
            20,
            25,
            30,
            30
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            -20,
            -20,
            -20,
            -20,
            -20
        ],
        "resistance": {
            "fire": "long50",
            "burn": "long100"
        },
        "specials": [
            [
                "Equip.BOOST",
                "Element.FIRE"
            ],
            None,
            [
                "Equip.STATUS",
                "Status.BRAVE",
                2,
                0.2
            ],
            None,
            [
                "Equip.SUMMON",
                "Summons.GloopAsh",
                0.3
            ]
        ],
        "materials": [
            [
                "Items.iron",
                1
            ],
            [
                "Items.iron",
                2,
                "Items.geode",
                2
            ],
            [
                "Items.rune",
                1,
                "Items.geode",
                10
            ],
            [
                "Items.scales",
                1,
                "Items.iron",
                12
            ]
        ]
    },
    "summerkimono": {
        "SID": "summerkimono",
        "type": "ARMOR_FEMALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            5,
            10,
            15,
            20,
            25
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            5,
            10,
            15,
            20,
            25
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            5,
            10,
            15,
            20
        ],
        "resistance": {
            "wind": "long50",
            "thunder": "long50",
            "stun": "long100"
        },
        "specials": [
            [
                "Equip.BOOST",
                "Element.THUNDER"
            ],
            None,
            [
                "Equip.STATUS",
                "Status.BLESS",
                2,
                0.25
            ],
            None,
            [
                "Equip.SUMMON",
                "Spells.blossom",
                0.25
            ]
        ],
        "materials": [
            [
                "Items.wool",
                2
            ],
            [
                "Items.wool",
                8,
                "Items.shuriken",
                4
            ],
            [
                "Items.topaz",
                2,
                "Items.satin",
                2
            ],
            [
                "Items.topaz",
                4,
                "Items.opal",
                1
            ]
        ]
    },
    "popedress": {
        "SID": "popedress",
        "type": "ARMOR_FEMALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            0,
            5,
            10,
            15,
            20
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            20,
            30,
            40,
            55,
            70
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "dark": "long50",
            "holy": "long50",
            "curse": "long100"
        },
        "specials": [
            [
                "Equip.BOOST",
                "Element.HOLY"
            ],
            None,
            None,
            None,
            [
                "Equip.STATUS",
                "Status.AUTOLIFE",
                1,
                0.3
            ]
        ],
        "materials": [
            [
                "Items.flower",
                1
            ],
            [
                "Items.silk",
                2
            ],
            [
                "Items.silver",
                2,
                "Items.gold",
                1
            ],
            [
                "Items.grail",
                1
            ]
        ]
    },
    "nurseuniform": {
        "SID": "nurseuniform",
        "type": "ARMOR_FEMALE",
        "HP": [
            0,
            5,
            5,
            10,
            10
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            5,
            10,
            15,
            20,
            25
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            5,
            10,
            15,
            20,
            25
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "holy": "long50",
            "poison": "long100",
            "syphon": "long100"
        },
        "specials": [
            [
                "Equip.BOOST_HEALING"
            ],
            None,
            [
                "Equip.BOOST",
                "Element.HOLY"
            ],
            None,
            [
                "Equip.SUMMON",
                "Spells.healmore",
                0.5
            ]
        ],
        "materials": [
            [
                "Items.apple",
                2
            ],
            [
                "Items.banana",
                3
            ],
            [
                "Items.coffee",
                6,
                "Items.satin",
                2
            ],
            [
                "Items.lego",
                2,
                "Items.cupcake",
                6
            ]
        ]
    },
    "darkgown": {
        "SID": "darkgown",
        "type": "ARMOR_FEMALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "MP": [
            0
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicAttack": [
            10,
            15,
            20,
            25,
            30
        ],
        "magicDefence": [
            15,
            20,
            25,
            30,
            40
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "dark": "long50",
            "death": "long100",
            "holy": "down30"
        },
        "specials": [
            [
                "Equip.BOOST",
                "Element.DARK"
            ],
            None,
            None,
            [
                "Equip.DEFEND_BUFF",
                "Stats.MAGIC_DEFENCE",
                80
            ]
        ],
        "materials": [
            [
                "Items.flower",
                1
            ],
            [
                "Items.silk",
                2
            ],
            [
                "Items.satin",
                1,
                "Items.rune",
                1
            ],
            [
                "Items.darkmatter",
                1
            ]
        ]
    },
    "samidress": {
        "SID": "samidress",
        "type": "ARMOR_FEMALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            0,
            5,
            5,
            10,
            10
        ],
        "defence": [
            5,
            10,
            15,
            20,
            25
        ],
        "magicAttack": [
            0,
            5,
            5,
            10,
            10
        ],
        "magicDefence": [
            5,
            10,
            15,
            20,
            25
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "wind": "long50",
            "holy": "long50"
        },
        "specials": [
            [
                "Equip.BOOST",
                "Element.WIND"
            ],
            None,
            None,
            [
                "Equip.BOOST_BUFFS",
                10
            ]
        ],
        "materials": [
            [
                "Items.wool",
                1,
                "Items.feather",
                1
            ],
            [
                "Items.fur",
                2,
                "Items.feather",
                4
            ],
            [
                "Items.satin",
                4,
                "Items.fur",
                8
            ],
            [
                "Items.rune2",
                10,
                "Items.fur",
                12
            ]
        ]
    },
    "cowcostume": {
        "SID": "cowcostume",
        "type": "ARMOR_FEMALE",
        "HP": [
            5,
            5,
            10,
            15,
            20
        ],
        "MP": [
            0
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            5,
            10,
            15,
            20,
            25
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            5,
            10,
            15,
            20,
            25
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "dispel": "long100",
            "earth": "long50",
            "water": "long50"
        },
        "specials": [
            [
                "Equip.BOOST",
                "Element.EARTH"
            ],
            None,
            None,
            [
                "Equip.BOOST_DEBUFFS",
                10
            ],
            [
                "Equip.DEFEND_BUFF",
                "Stats.HP",
                20
            ]
        ],
        "materials": [
            [
                "Items.buckle",
                1
            ],
            [
                "Items.leather",
                2
            ],
            [
                "Items.silk",
                6,
                "Items.leather",
                12
            ],
            [
                "Items.burger",
                3,
                "Items.leather",
                12
            ]
        ]
    },
    "furdress": {
        "SID": "furdress",
        "type": "ARMOR_FEMALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "MP": [
            0
        ],
        "attack": [
            0,
            5,
            5,
            10,
            10
        ],
        "defence": [
            10,
            15,
            20,
            25,
            30
        ],
        "magicAttack": [
            0,
            5,
            5,
            10,
            10
        ],
        "magicDefence": [
            10,
            15,
            20,
            25,
            30
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "ice": "long50",
            "water": "long50",
            "freeze": "long100"
        },
        "specials": [
            [
                "Equip.BOOST",
                "Element.ICE"
            ],
            None,
            [
                "Equip.SUMMON",
                "Summons.MonolithViking",
                0.15
            ],
            None,
            [
                "Equip.BOOST_CATCH"
            ]
        ],
        "materials": [
            [
                "Items.fur",
                1
            ],
            [
                "Items.fur",
                2,
                "Items.buckle",
                1
            ],
            [
                "Items.spike",
                2,
                "Items.fur",
                12,
                "Items.buckle",
                1
            ],
            [
                "Items.rune2",
                15,
                "Items.buckle",
                1
            ]
        ]
    },
    "santaskirt": {
        "SID": "santaskirt",
        "type": "ARMOR_FEMALE",
        "HP": [
            0,
            5,
            5,
            10,
            10
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            10,
            15,
            20,
            25,
            30
        ],
        "magicAttack": [
            0,
            5,
            10,
            15,
            20
        ],
        "magicDefence": [
            10,
            15,
            20,
            25,
            30
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            5,
            10,
            15
        ],
        "resistance": {
            "ice": "long50",
            "freeze": "long100",
            "wet": "long100"
        },
        "specials": [
            [
                "Equip.BOOST",
                "Element.ICE"
            ],
            None,
            [
                "Equip.SUMMON",
                "Spells.candycane2",
                1
            ]
        ],
        "materials": [
            [
                "Items.snowball",
                2,
                "Items.wool",
                1
            ],
            [
                "Items.snowball",
                8,
                "Items.wool",
                4
            ],
            [
                "Items.satin",
                2,
                "Items.leather",
                8
            ],
            [
                "Items.lego",
                1,
                "Items.satin",
                2
            ]
        ]
    },
    "mechaarmor": {
        "SID": "mechasuit",
        "type": "ARMOR_FEMALE",
        "HP": [
            5,
            10,
            15,
            20,
            25
        ],
        "attack": [
            0,
            0,
            0,
            0,
            5
        ],
        "defence": [
            10,
            15,
            20,
            25,
            35
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            5
        ],
        "magicDefence": [
            10,
            15,
            20,
            25,
            35
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "bio": "long50",
            "bomb": "long50",
            "thunder": "down30"
        },
        "specials": [
            [
                "Equip.BOOST",
                "Element.BOMB"
            ],
            None,
            [
                "Equip.SUMMON",
                "Summons.CatBomber",
                0.9
            ]
        ],
        "materials": [
            [
                "Items.iron",
                2
            ],
            [
                "Items.bomb",
                2,
                "Items.steel",
                2
            ],
            [
                "Items.cpu",
                1,
                "Items.powder",
                2
            ],
            [
                "Items.gamechild",
                1
            ]
        ]
    },
    "cactusdress": {
        "SID": "cactusdress",
        "type": "ARMOR_FEMALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "MP": [
            0
        ],
        "attack": [
            5,
            10,
            10,
            15,
            20
        ],
        "defence": [
            10,
            15,
            20,
            25,
            30
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            10,
            15,
            20,
            25,
            30
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "earth": "long50",
            "bio": "long50",
            "poison": "long100"
        },
        "specials": [
            [
                "Equip.BOOST",
                "Element.BIO"
            ],
            None,
            [
                "Equip.SUMMON",
                "Spells.cactus",
                2
            ]
        ],
        "materials": [
            [
                "Items.cactus",
                2
            ],
            [
                "Items.cactus",
                8
            ],
            [
                "Items.geode",
                8,
                "Items.emerald",
                2
            ],
            [
                "Items.emerald",
                7,
                "Items.herb",
                3,
                "Items.cactus",
                3
            ]
        ]
    },
    "ninjaskirt": {
        "SID": "ninjaskirt",
        "type": "ARMOR_FEMALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            5,
            10,
            15
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            5,
            10,
            15
        ],
        "accuracy": [
            10,
            15,
            15,
            20,
            25
        ],
        "evade": [
            10,
            10,
            15,
            20,
            25
        ],
        "resistance": {
            "wind": "long50",
            "dark": "long50",
            "stun": "long100"
        },
        "specials": [
            [
                "Equip.BOOST",
                "Element.WIND"
            ],
            [
                "Equip.DEFEND_STATUS",
                "Status.INVISIBLE",
                1
            ],
            None,
            [
                "Equip.BOOST_THROWS"
            ],
            None
        ],
        "materials": [
            [
                "Items.shuriken",
                1,
                "Items.flower",
                1
            ],
            [
                "Items.shuriken",
                4,
                "Items.flower",
                2
            ],
            [
                "Items.rune",
                1,
                "Items.flower",
                2,
                "Items.shuriken",
                2
            ],
            [
                "Items.kevlar",
                2,
                "Items.rune",
                2
            ]
        ]
    },
    "casualskirt": {
        "SID": "casualskirt",
        "type": "ARMOR_FEMALE",
        "HP": [
            0,
            0,
            0,
            0,
            0
        ],
        "attack": [
            0,
            5,
            5,
            10,
            15
        ],
        "defence": [
            0,
            5,
            10,
            15,
            20
        ],
        "magicAttack": [
            0,
            5,
            5,
            10,
            15
        ],
        "magicDefence": [
            0,
            5,
            10,
            15,
            20
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            10,
            10,
            15,
            20,
            25
        ],
        "resistance": {
            "death": "long100",
            "syphon": "long100",
            "stun": "long100"
        },
        "specials": [
            [
                "Equip.BOOST_FOOD"
            ],
            None,
            [
                "Equip.BOOST_BUFFS",
                10
            ]
        ],
        "materials": [
            [
                "Items.wool",
                2
            ],
            [
                "Items.coffee",
                1
            ],
            [
                "Items.raspberries",
                4,
                "Items.pretzel",
                2,
                "Items.burger",
                2
            ],
            [
                "Items.burger",
                6,
                "Items.cola",
                2
            ]
        ]
    },
    "spidergown": {
        "SID": "spidergown",
        "type": "ARMOR_FEMALE",
        "HP": [
            0,
            5,
            5,
            10,
            10
        ],
        "attack": [
            0,
            0,
            0,
            0,
            0
        ],
        "defence": [
            10,
            15,
            20,
            25,
            35
        ],
        "magicAttack": [
            0,
            0,
            0,
            0,
            0
        ],
        "magicDefence": [
            10,
            15,
            20,
            25,
            30
        ],
        "accuracy": [
            0,
            0,
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0,
            0,
            0
        ],
        "resistance": {
            "dark": "long50",
            "fire": "long50",
            "earth": "long50"
        },
        "specials": [
            [
                "Equip.BOOST",
                "Element.DARK"
            ],
            None,
            [
                "Equip.SUMMON",
                "Summons.MirrorHaunted",
                0.5
            ],
            None,
            [
                "Equip.BOOST_DEBUFFS"
            ]
        ],
        "materials": [
            [
                "Items.shuriken",
                2
            ],
            [
                "Items.amber",
                1
            ],
            [
                "Items.rune",
                1,
                "Items.amber",
                4
            ],
            [
                "Items.rune",
                4
            ]
        ]
    },
    "swordmedal": {
        "SID": "swordmedal",
        "type": "FLAIR",
        "attack": [
            10,
            20,
            30
        ],
        "materials": [
            [
                "Items.silver",
                1,
                "Items.gold",
                1
            ],
            [
                "Items.silver",
                4,
                "Items.gold",
                4
            ]
        ],
        "HP": [
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0
        ]
    },
    "shieldmedal": {
        "SID": "shieldmedal",
        "type": "FLAIR",
        "defence": [
            10,
            20,
            30
        ],
        "materials": [
            [
                "Items.silver",
                1,
                "Items.gold",
                1
            ],
            [
                "Items.silver",
                4,
                "Items.gold",
                4
            ]
        ],
        "HP": [
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0
        ]
    },
    "goldstar": {
        "SID": "goldstar",
        "type": "FLAIR",
        "magicAttack": [
            10,
            20,
            30
        ],
        "materials": [
            [
                "Items.gold",
                1,
                "Items.gems",
                5
            ],
            [
                "Items.gold",
                5
            ]
        ],
        "HP": [
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0
        ]
    },
    "platinumstar": {
        "SID": "platinumstar",
        "type": "FLAIR",
        "magicDefence": [
            10,
            20,
            30
        ],
        "materials": [
            [
                "Items.silver",
                2,
                "Items.gems",
                5
            ],
            [
                "Items.silver",
                10
            ]
        ],
        "HP": [
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0
        ]
    },
    "chillcloud": {
        "SID": "smallcloud",
        "type": "FLAIR",
        "HP": [
            0,
            5,
            10
        ],
        "resistance": {
            "water": "short30"
        },
        "specials": [
            [
                "Equip.MORE_SP"
            ]
        ],
        "materials": [
            [
                "Items.ice",
                2,
                "Items.water",
                2
            ],
            [
                "Items.ice",
                10,
                "Items.water",
                10
            ]
        ],
        "attack": [
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0
        ]
    },
    "ironcross": {
        "SID": "ironcross",
        "type": "FLAIR",
        "resistance": {
            "bomb": "short50",
            "stagger": "short100"
        },
        "materials": [
            [
                "Items.iron",
                5,
                "Items.steel",
                5
            ],
            [
                "Items.iron",
                10,
                "Items.steel",
                10,
                "Items.silver",
                3
            ]
        ],
        "HP": [
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0
        ]
    },
    "bandage": {
        "SID": "bandage",
        "type": "FLAIR",
        "resistance": {
            "earth": "short50",
            "death": "short100"
        },
        "materials": [
            [
                "Items.silk",
                4,
                "Items.turd",
                2
            ],
            [
                "Items.silk",
                14,
                "Items.turd",
                10
            ]
        ],
        "HP": [
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0
        ]
    },
    "pentagram": {
        "SID": "goldenpentagram",
        "type": "FLAIR",
        "resistance": {
            "holy": "short50",
            "weak": "short100"
        },
        "materials": [
            [
                "Items.gold",
                1
            ],
            [
                "Items.gold",
                2,
                "Items.silver",
                1
            ]
        ],
        "HP": [
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0
        ]
    },
    "targetbadge": {
        "SID": "targetbadge",
        "type": "FLAIR",
        "resistance": {
            "wind": "short30"
        },
        "accuracy": [
            10,
            20,
            30
        ],
        "specials": [
            None,
            None,
            [
                "Equip.DEFEND_STATUS",
                "Status.TARGET",
                2
            ]
        ],
        "materials": [
            [
                "Items.plastic",
                3
            ],
            [
                "Items.plastic",
                10
            ]
        ],
        "HP": [
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0
        ]
    },
    "eyebrows": {
        "SID": "bigeyebrows",
        "type": "FLAIR",
        "resistance": {
            "death": "short100",
            "stun": "short100",
            "stagger": "short100"
        },
        "specials": [],
        "materials": [
            [
                "Items.leather",
                2
            ],
            [
                "Items.leather",
                10
            ]
        ],
        "HP": [
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0
        ]
    },
    "icebadge": {
        "SID": "frostbadge",
        "type": "FLAIR",
        "resistance": {
            "ice": "short50",
            "freeze": "short100"
        },
        "materials": [
            [
                "Items.water",
                8
            ],
            [
                "Items.sapphire",
                1,
                "Items.water",
                16
            ]
        ],
        "HP": [
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0
        ]
    },
    "hoopearings": {
        "SID": "hoopearings",
        "type": "FLAIR",
        "magicAttack": [
            0,
            5,
            10
        ],
        "resistance": {
            "thunder": "short30"
        },
        "specials": [
            [
                "Equip.STATUS",
                "Status.GOOD_LUCK",
                2,
                0.25
            ],
            None,
            [
                "Equip.DEFEND_STATUS",
                "Status.GOOD_LUCK",
                2
            ]
        ],
        "materials": [
            [
                "Items.gold",
                1
            ],
            [
                "Items.gold",
                2
            ]
        ],
        "HP": [
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0
        ]
    },
    "pearlnecklace": {
        "SID": "pearlnecklace",
        "type": "FLAIR",
        "resistance": {
            "water": "short50",
            "wet": "short100"
        },
        "materials": [
            [
                "Items.ice",
                8
            ],
            [
                "Items.sapphire",
                1,
                "Items.ice",
                16
            ]
        ],
        "HP": [
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0
        ]
    },
    "greencross": {
        "SID": "greencross",
        "type": "FLAIR",
        "magicDefence": [
            0,
            5,
            10
        ],
        "resistance": {
            "burn": "short50"
        },
        "specials": [
            [
                "Equip.STATUS",
                "Status.REGEN",
                2,
                0.3
            ],
            None,
            [
                "Equip.DEFEND_STATUS",
                "Status.REGEN",
                2
            ]
        ],
        "materials": [
            [
                "Items.silver",
                2
            ],
            [
                "Items.emerald",
                1,
                "Items.silver",
                4
            ]
        ],
        "HP": [
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0
        ]
    },
    "minidrone": {
        "SID": "minidrone",
        "type": "FLAIR",
        "accuracy": [
            0,
            5,
            10
        ],
        "resistance": {
            "bomb": "short30",
            "earth": "short30"
        },
        "specials": [
            [
                "Equip.BOOST_CATCH"
            ]
        ],
        "materials": [
            [
                "Items.spring",
                3,
                "Items.tape",
                3
            ],
            [
                "Items.cpu",
                3
            ]
        ],
        "HP": [
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0
        ]
    },
    "surgicalmask": {
        "SID": "surgicalmask",
        "type": "FLAIR",
        "resistance": {
            "bio": "short50",
            "poison": "short100"
        },
        "materials": [
            [
                "Items.silk",
                2,
                "Items.garlic",
                2
            ],
            [
                "Items.garlic",
                8,
                "Items.kevlar",
                1
            ]
        ],
        "HP": [
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0
        ]
    },
    "silvercross": {
        "SID": "silvercross",
        "type": "FLAIR",
        "resistance": {
            "dark": "short50",
            "curse": "short100"
        },
        "materials": [
            [
                "Items.silver",
                2
            ],
            [
                "Items.silver",
                6
            ]
        ],
        "HP": [
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0
        ]
    },
    "balancebadge": {
        "SID": "balancebadge",
        "type": "FLAIR",
        "resistance": {
            "dark": "short30",
            "holy": "short30"
        },
        "HP": [
            0,
            0,
            5
        ],
        "attack": [
            5,
            5,
            5
        ],
        "defence": [
            0,
            5,
            5
        ],
        "magicAttack": [
            5,
            5,
            5
        ],
        "magicDefence": [
            0,
            5,
            5
        ],
        "accuracy": [
            5,
            5,
            5
        ],
        "evade": [
            0,
            0,
            5
        ],
        "materials": [
            [
                "Items.rune",
                1,
                "Items.rune2",
                1
            ],
            [
                "Items.rune",
                1,
                "Items.rune2",
                1
            ]
        ]
    },
    "fakemustache": {
        "SID": "fakemustache",
        "type": "FLAIR",
        "resistance": {
            "ice": "short30"
        },
        "specials": [
            [
                "Equip.STEAL"
            ]
        ],
        "materials": [
            [
                "Items.fur",
                2,
                "Items.silver",
                1
            ],
            [
                "Items.fur",
                8,
                "Items.gold",
                1
            ]
        ],
        "HP": [
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0
        ]
    },
    "thunderbadge": {
        "SID": "lightningbadge",
        "type": "FLAIR",
        "resistance": {
            "thunder": "short50",
            "stun": "short100"
        },
        "materials": [
            [
                "Items.amber",
                2
            ],
            [
                "Items.amber",
                2,
                "Items.topaz",
                3
            ]
        ],
        "HP": [
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0
        ]
    },
    "chromeearings": {
        "SID": "chromeearings",
        "type": "FLAIR",
        "statusEffect": "Status.FREEZE",
        "statusChance": [
            10,
            20,
            30
        ],
        "statusDegree": [
            2,
            2,
            2
        ],
        "resistance": {
            "ice": "short30"
        },
        "specials": [
            [
                "Equip.NO_STACK"
            ]
        ],
        "materials": [
            [
                "Items.silver",
                2,
                "Items.water",
                1
            ],
            [
                "Items.silver",
                6,
                "Items.water",
                3
            ]
        ],
        "HP": [
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0
        ]
    },
    "cattail": {
        "SID": "cattail",
        "type": "FLAIR",
        "evade": [
            10,
            15,
            15
        ],
        "resistance": {
            "dark": "short30"
        },
        "specials": [
            None,
            None,
            [
                "Equip.DEFEND_BUFF",
                "Stats.EVADE",
                30
            ]
        ],
        "materials": [
            [
                "Items.fur",
                4,
                "Items.leather",
                2
            ],
            [
                "Items.fur",
                10,
                "Items.leather",
                5
            ]
        ],
        "HP": [
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0
        ]
    },
    "fatfly": {
        "SID": "fatfly",
        "type": "FLAIR",
        "statusEffect": "Status.DOOM",
        "statusChance": [
            30,
            40,
            50
        ],
        "statusDegree": [
            3,
            3,
            2
        ],
        "resistance": {
            "dark": "short30",
            "bio": "short30"
        },
        "specials": [
            [
                "Equip.NO_STACK"
            ],
            None,
            [
                "Equip.SUMMON",
                "Spells.flybomb",
                1.25
            ]
        ],
        "materials": [
            [
                "Items.virus",
                2
            ],
            [
                "Items.virus",
                10
            ]
        ],
        "HP": [
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0
        ]
    },
    "luckyclover": {
        "SID": "luckyclover",
        "type": "FLAIR",
        "resistance": {
            "bio": "short30"
        },
        "specials": [
            [
                "Equip.STATUS",
                "Status.BLESS",
                2,
                0.25
            ],
            None,
            [
                "Equip.DEFEND_STATUS",
                "Status.BLESS",
                2
            ]
        ],
        "materials": [
            [
                "Items.geode",
                4
            ],
            [
                "Items.emerald",
                3,
                "Items.geode",
                4
            ]
        ],
        "HP": [
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0
        ]
    },
    "heartpendant": {
        "SID": "heartpendant",
        "type": "FLAIR",
        "defence": [
            0,
            0,
            5
        ],
        "magicDefence": [
            0,
            0,
            5
        ],
        "resistance": {
            "death": "short100"
        },
        "specials": [
            [
                "Equip.STATUS",
                "Status.LOVED",
                2,
                0.25
            ],
            None,
            [
                "Equip.DEFEND_STATUS",
                "Status.LOVED",
                2
            ]
        ],
        "materials": [
            [
                "Items.gems",
                5
            ],
            [
                "Items.ruby",
                4
            ]
        ],
        "HP": [
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0
        ]
    },
    "crossbonepin": {
        "SID": "crossbonepin",
        "type": "FLAIR",
        "statusEffect": "Status.CURSE",
        "statusChance": [
            30,
            45,
            60
        ],
        "statusDegree": [
            4,
            5,
            6
        ],
        "resistance": {
            "death": "short50",
            "curse": "short50"
        },
        "specials": [
            [
                "Equip.NO_STACK"
            ]
        ],
        "materials": [
            [
                "Items.claw",
                4
            ],
            [
                "Items.spike",
                4
            ]
        ],
        "HP": [
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0
        ]
    },
    "battlepaint": {
        "SID": "battlepaint",
        "type": "FLAIR",
        "attack": [
            0,
            5,
            10
        ],
        "resistance": {
            "water": "short30"
        },
        "specials": [
            [
                "Equip.STATUS",
                "Status.BRAVE",
                2,
                0.2
            ],
            None,
            [
                "Equip.DEFEND_STATUS",
                "Status.BRAVE",
                4
            ]
        ],
        "materials": [
            [
                "Items.blueberries",
                6
            ],
            [
                "Items.blueberries",
                20
            ]
        ],
        "HP": [
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0
        ]
    },
    "firebadge": {
        "SID": "flamebadge",
        "type": "FLAIR",
        "resistance": {
            "fire": "short50",
            "burn": "short100"
        },
        "materials": [
            [
                "Items.magma",
                6
            ],
            [
                "Items.magma",
                2,
                "Items.ruby",
                3
            ]
        ],
        "HP": [
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0
        ]
    },
    "amethystearings": {
        "SID": "amethystearings",
        "type": "FLAIR",
        "statusEffect": "Status.DRY",
        "statusChance": [
            100,
            100,
            100
        ],
        "statusDegree": [
            2,
            3,
            4
        ],
        "resistance": {
            "dispel": "short50"
        },
        "specials": [
            [
                "Equip.NO_STACK"
            ]
        ],
        "materials": [
            [
                "Items.butterflywing",
                8
            ],
            [
                "Items.butterflywing",
                36
            ]
        ],
        "HP": [
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0
        ]
    },
    "tentacle": {
        "SID": "tentacle",
        "type": "FLAIR",
        "statusEffect": "Status.VIRUS",
        "statusChance": [
            30,
            60,
            100
        ],
        "statusDegree": [
            1,
            1,
            1
        ],
        "resistance": {
            "stun": "short50"
        },
        "specials": [
            [
                "Equip.NO_STACK"
            ],
            None,
            [
                "Equip.SUMMON",
                "Spells.tentacles",
                1.25
            ]
        ],
        "materials": [
            [
                "Items.virus",
                2
            ],
            [
                "Items.virus",
                10
            ]
        ],
        "HP": [
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0
        ]
    },
    "fairy": {
        "SID": "fairy",
        "type": "FLAIR",
        "resistance": {
            "holy": "short30"
        },
        "specials": [
            [
                "Equip.STATUS",
                "Status.AUTOLIFE",
                2,
                0.15
            ],
            None,
            [
                "Equip.DEFEND_STATUS",
                "Status.AUTOLIFE",
                1
            ]
        ],
        "materials": [
            [
                "Items.butterflywing",
                8
            ],
            [
                "Items.moonpearl",
                1,
                "Items.butterflywing",
                8
            ]
        ],
        "HP": [
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0
        ]
    },
    "triforce": {
        "SID": "thetriforce",
        "type": "FLAIR",
        "resistance": {
            "dispel": "short50",
            "syphon": "short50"
        },
        "specials": [
            [
                "Equip.STATUS",
                "Status.MORALE",
                2,
                0.25
            ],
            None,
            [
                "Equip.DEFEND_STATUS",
                "Status.MORALE",
                2
            ]
        ],
        "materials": [
            [
                "Items.gold",
                1
            ],
            [
                "Items.gold",
                3
            ]
        ],
        "HP": [
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0
        ]
    },
    "peacebadge": {
        "SID": "peacebadge",
        "type": "FLAIR",
        "statusEffect": "Status.WEAKEN",
        "statusChance": [
            30,
            45,
            60
        ],
        "statusDegree": [
            4,
            5,
            6
        ],
        "defence": [
            0,
            5,
            10
        ],
        "resistance": {
            "weak": "short50"
        },
        "specials": [
            [
                "Equip.NO_STACK"
            ]
        ],
        "materials": [
            [
                "Items.tape",
                14
            ],
            [
                "Items.tape",
                60
            ]
        ],
        "HP": [
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0
        ]
    },
    "angelpin": {
        "SID": "angelpin",
        "type": "FLAIR",
        "resistance": {
            "wind": "short50",
            "weight": "short100"
        },
        "materials": [
            [
                "Items.feather",
                2,
                "Items.silk",
                2
            ],
            [
                "Items.silver",
                6,
                "Items.feather",
                12
            ]
        ],
        "HP": [
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0
        ]
    },
    "emeraldearings": {
        "SID": "emeraldearings",
        "type": "FLAIR",
        "statusEffect": "Status.POISON",
        "statusChance": [
            50,
            80,
            100
        ],
        "statusDegree": [
            2,
            2,
            3
        ],
        "resistance": {
            "bio": "short30"
        },
        "specials": [
            [
                "Equip.NO_STACK"
            ]
        ],
        "materials": [
            [
                "Items.virus",
                2
            ],
            [
                "Items.emerald",
                2
            ]
        ],
        "HP": [
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0
        ]
    },
    "angryfaic": {
        "SID": "angryfaic",
        "type": "FLAIR",
        "defence": [
            0,
            5,
            5
        ],
        "magicDefence": [
            0,
            5,
            5
        ],
        "resistance": {
            "fire": "short30"
        },
        "specials": [
            [
                "Equip.DEFEND_STATUS",
                "Status.TARGET",
                3
            ],
            None,
            [
                "Equip.INTIMIDATE"
            ]
        ],
        "materials": [
            [
                "Items.amber",
                3
            ],
            [
                "Items.rune",
                1,
                "Items.amber",
                5
            ]
        ],
        "HP": [
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0
        ]
    },
    "pocketwatch": {
        "SID": "pocketwatch",
        "type": "FLAIR",
        "resistance": {
            "stun": "short50"
        },
        "specials": [
            [
                "Equip.STATUS",
                "Status.HASTE",
                2,
                0.2
            ]
        ],
        "materials": [
            [
                "Items.spring",
                2,
                "Items.gear",
                4
            ],
            [
                "Items.spring",
                10,
                "Items.gear",
                20
            ]
        ],
        "HP": [
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0
        ]
    },
    "coincharm": {
        "SID": "coincharm",
        "type": "FLAIR",
        "attack": [
            0,
            0,
            5
        ],
        "magicAttack": [
            0,
            5,
            5
        ],
        "specials": [
            [
                "Equip.MORE_GOLD"
            ]
        ],
        "materials": [
            [
                "Items.silver",
                2,
                "Items.map2",
                5
            ],
            [
                "Items.grail",
                1,
                "Items.map2",
                5
            ]
        ],
        "HP": [
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0
        ]
    },
    "luckyfish": {
        "SID": "luckyfish",
        "type": "FLAIR",
        "defence": [
            0,
            5,
            5
        ],
        "magicDefence": [
            0,
            0,
            5
        ],
        "specials": [
            [
                "Equip.MORE_ITEMS"
            ]
        ],
        "materials": [
            [
                "Items.gold",
                1,
                "Items.map2",
                5
            ],
            [
                "Items.scales",
                3,
                "Items.map2",
                5
            ]
        ],
        "HP": [
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0
        ]
    },
    "petrock": {
        "SID": "petrock",
        "type": "FLAIR",
        "defence": [
            0,
            5,
            5
        ],
        "magicDefence": [
            0,
            0,
            5
        ],
        "statusEffect": "Status.HEAVY",
        "statusChance": [
            100,
            100,
            100
        ],
        "statusDegree": [
            2,
            3,
            4
        ],
        "resistance": {
            "wind": "short30"
        },
        "specials": [
            [
                "Equip.NO_STACK"
            ]
        ],
        "materials": [
            [
                "Items.turd",
                5,
                "Items.rune2",
                1
            ],
            [
                "Items.turd",
                20,
                "Items.rune2",
                4
            ]
        ],
        "HP": [
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0
        ]
    },
    "narutomaki": {
        "SID": "narutomaki",
        "type": "FLAIR",
        "defence": [
            0,
            0,
            5
        ],
        "magicDefence": [
            0,
            0,
            5
        ],
        "resistance": {
            "water": "short30"
        },
        "specials": [
            [
                "Equip.REVIVE_BUFF",
                40,
                60,
                80
            ]
        ],
        "materials": [
            [
                "Items.watermelon",
                4
            ],
            [
                "Items.dragonfruit",
                8
            ]
        ],
        "HP": [
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0
        ]
    },
    "biteybadge": {
        "SID": "biteybadge",
        "type": "FLAIR",
        "HP": [
            0,
            0,
            5
        ],
        "statusEffect": "Status.TIRED",
        "statusChance": [
            100,
            100,
            100
        ],
        "statusDegree": [
            2,
            3,
            4
        ],
        "resistance": {
            "dark": "short30",
            "weak": "short50"
        },
        "specials": [
            [
                "Equip.NO_STACK"
            ]
        ],
        "materials": [
            [
                "Items.fur",
                4
            ],
            [
                "Items.fur",
                22,
                "Items.spike",
                2
            ]
        ],
        "attack": [
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0
        ]
    },
    "dinoegg": {
        "SID": "dinoegg",
        "type": "FLAIR",
        "HP": [
            0,
            0,
            5
        ],
        "evade": [
            0,
            5,
            5
        ],
        "specials": [
            [
                "Equip.MORE_AP",
                1.1,
                1.15,
                1.2
            ]
        ],
        "materials": [
            [
                "Items.feather",
                20
            ],
            [
                "Items.scales",
                3
            ]
        ],
        "attack": [
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0
        ]
    },
    "viridian": {
        "SID": "viridian",
        "type": "FLAIR",
        "resistance": {
            "wind": "short30",
            "earth": "short30",
            "weight": "short50"
        },
        "specials": [
            [
                "Equip.SKIP_HASTE"
            ]
        ],
        "materials": [
            [
                "Items.floppy",
                5,
                "Items.plastic",
                1
            ],
            [
                "Items.gamechild",
                1
            ]
        ],
        "HP": [
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0
        ]
    },
    "tetromino": {
        "SID": "tetromino",
        "type": "FLAIR",
        "accuracy": [
            0,
            5,
            10
        ],
        "evade": [
            0,
            5,
            10
        ],
        "specials": [
            [
                "Equip.TETRIS"
            ]
        ],
        "materials": [
            [
                "Items.brick",
                16
            ],
            [
                "Items.lego",
                1
            ]
        ],
        "HP": [
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0
        ]
    },
    "dogtags": {
        "SID": "dogtags",
        "type": "FLAIR",
        "attack": [
            0,
            0,
            5
        ],
        "magicAttack": [
            0,
            0,
            5
        ],
        "resistance": {
            "bomb": "short30"
        },
        "specials": [
            [
                "Equip.REVIVE_BUFF",
                40,
                60,
                80
            ]
        ],
        "materials": [
            [
                "Items.steel",
                2,
                "Items.spring",
                2
            ],
            [
                "Items.kevlar",
                3
            ]
        ],
        "HP": [
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0
        ]
    },
    "companioncube": {
        "SID": "companioncube",
        "type": "FLAIR",
        "HP": [
            0,
            0,
            5
        ],
        "resistance": {
            "thunder": "short30"
        },
        "specials": [
            [
                "Equip.REVIVE_BUFF",
                20,
                30,
                50
            ]
        ],
        "materials": [
            [
                "Items.plastic",
                4
            ],
            [
                "Items.gamechild",
                1
            ]
        ],
        "attack": [
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0
        ]
    },
    "pixelglasses": {
        "SID": "pixelglasses",
        "type": "FLAIR",
        "accuracy": [
            -10,
            -10,
            -10
        ],
        "resistance": {
            "dark": "short30",
            "holy": "short30"
        },
        "specials": [
            [
                "Equip.DEAL_WITH_IT"
            ]
        ],
        "materials": [
            [
                "Items.glass",
                8,
                "Items.plastic",
                2
            ],
            [
                "Items.glass",
                8,
                "Items.lego",
                1
            ]
        ],
        "HP": [
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0
        ]
    },
    "nanomachines": {
        "SID": "nanomachines",
        "type": "FLAIR",
        "attack": [
            0,
            0,
            5
        ],
        "magicAttack": [
            0,
            0,
            5
        ],
        "resistance": {
            "syphon": "short50",
            "poison": "short50"
        },
        "specials": [
            [
                "Equip.FAST_COOLDOWN"
            ]
        ],
        "materials": [
            [
                "Items.spring",
                12,
                "Items.gear",
                2
            ],
            [
                "Items.cpu",
                1,
                "Items.gear",
                2
            ]
        ],
        "HP": [
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0
        ]
    },
    "meowmeowbadge": {
        "SID": "meowmeowbadge",
        "type": "FLAIR",
        "attack": [
            0,
            0,
            5
        ],
        "magicAttack": [
            0,
            0,
            5
        ],
        "resistance": {
            "stun": "short50"
        },
        "specials": [],
        "materials": [
            [
                "Items.buckle",
                6
            ],
            [
                "Items.spike",
                6
            ]
        ],
        "HP": [
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0
        ]
    },
    "ramchip": {
        "SID": "ramchip",
        "type": "FLAIR",
        "resistance": {
            "dispel": "short50"
        },
        "specials": [
            [
                "Equip.MORE_MAX_SP",
                1.033,
                1.066,
                1.1
            ]
        ],
        "materials": [
            [
                "Items.cpu",
                1
            ],
            [
                "Items.gamechild",
                1
            ]
        ],
        "HP": [
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0
        ]
    },
    "babypenguin": {
        "SID": "babypenguin",
        "type": "FLAIR",
        "evade": [
            0,
            0,
            5
        ],
        "statusEffect": "Status.WET",
        "statusChance": [
            100,
            100,
            100
        ],
        "statusDegree": [
            2,
            3,
            4
        ],
        "resistance": {
            "ice": "short30"
        },
        "specials": [
            [
                "Equip.NO_STACK"
            ]
        ],
        "materials": [
            [
                "Items.snowball",
                10,
                "Items.blueberries",
                3
            ],
            [
                "Items.snowball",
                10,
                "Items.cloudberries",
                3
            ],
            []
        ],
        "HP": [
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0
        ]
    },
    "onering": {
        "SID": "onering",
        "type": "FLAIR",
        "HP": [
            10,
            10,
            10
        ],
        "attack": [
            15,
            20,
            25
        ],
        "defence": [
            15,
            20,
            25
        ],
        "magicAttack": [
            15,
            20,
            25
        ],
        "magicDefence": [
            15,
            20,
            25
        ],
        "accuracy": [
            0,
            5,
            10
        ],
        "evade": [
            0,
            5,
            10
        ],
        "resistance": {
            "ice": "short30",
            "freeze": "short50"
        },
        "specials": [
            [
                "Equip.STATUS",
                "Status.SCORCHED",
                2,
                1
            ]
        ],
        "materials": [
            [
                "Items.gold",
                1
            ],
            [
                "Items.grail",
                1
            ]
        ]
    },
    "juicybeast": {
        "SID": "juicybeast",
        "type": "FLAIR",
        "resistance": {
            "bio": "short30"
        },
        "specials": [
            [
                "Equip.SP_RECOVERY"
            ],
            [
                1.2,
                1.8,
                2.5
            ]
        ],
        "materials": [
            [
                "Items.virus",
                3,
                "Items.fur",
                3
            ],
            [
                "Items.virus",
                10,
                "Items.fur",
                10
            ]
        ],
        "HP": [
            0,
            0,
            0
        ],
        "attack": [
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0
        ]
    },
    "tooth": {
        "SID": "tooth",
        "type": "FLAIR",
        "HP": [
            10,
            15,
            15
        ],
        "resistance": {
            "holy": "short30"
        },
        "specials": [
            None,
            None,
            [
                "Equip.DEFEND_BUFF",
                "Stats.HP",
                20
            ]
        ],
        "materials": [
            [
                "Items.claw",
                5
            ],
            [
                "Items.spike",
                5
            ]
        ],
        "attack": [
            0,
            0,
            0
        ],
        "defence": [
            0,
            0,
            0
        ],
        "magicAttack": [
            0,
            0,
            0
        ],
        "magicDefence": [
            0,
            0,
            0
        ],
        "accuracy": [
            0,
            0,
            0
        ],
        "evade": [
            0,
            0,
            0
        ]
    }
}
