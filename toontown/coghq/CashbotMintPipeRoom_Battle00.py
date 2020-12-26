from toontown.coghq.SpecImports import *
GlobalEntities = {1000: {'type': 'levelMgr',
        'name': 'LevelMgr',
        'comment': '',
        'parentEntId': 0,
        'cogLevel': 0,
        'farPlaneDistance': 1500,
        'modelFilename': 'phase_10/models/cashbotHQ/ZONE13a',
        'wantDoors': 1},
 1001: {'type': 'editMgr',
        'name': 'EditMgr',
        'parentEntId': 0,
        'insertEntity': None,
        'removeEntity': None,
        'requestNewEntity': None,
        'requestSave': None},
 0: {'type': 'zone',
     'name': 'UberZone',
     'comment': '',
     'parentEntId': 0,
     'scale': 1,
     'description': '',
     'visibility': []},
 10001: {'type': 'battleBlocker',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 0,
         'pos': Point3(135.90512085, -2.06722736359, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0),
         'cellId': 0,
         'radius': 10.0},
 10003: {'type': 'battleBlocker',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 0,
         'pos': Point3(-86.7350921631, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': Vec3(0.378204703331, 2.94127488136, 2.80858683586),
         'cellId': 1,
         'radius': 10},
 10005: {'type': 'model',
         'name': 'farLeft',
         'comment': '',
         'parentEntId': 10004,
         'pos': Point3(45.6502952576, 31.8647651672, 0.228899106383),
         'hpr': Vec3(333.434936523, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0),
         'collisionsOnly': 0,
         'loadType': 'loadModelCopy',
         'modelPath': 'phase_10/models/cashbotHQ/pipes_C.bam'},
 10006: {'type': 'model',
         'name': 'farRight',
         'comment': '',
         'parentEntId': 10004,
         'pos': Point3(50.0559577942, -32.7609710693, 0.228899106383),
         'hpr': Vec3(206.565048218, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0),
         'collisionsOnly': 0,
         'loadType': 'loadModelCopy',
         'modelPath': 'phase_10/models/cashbotHQ/pipes_C.bam'},
 10008: {'type': 'model',
         'name': 'nearLeft',
         'comment': '',
         'parentEntId': 10004,
         'pos': Point3(-47.9696311951, 31.8647651672, 0.228899106383),
         'hpr': Vec3(26.5650520325, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0),
         'collisionsOnly': 0,
         'loadType': 'loadModelCopy',
         'modelPath': 'phase_10/models/cashbotHQ/pipes_D1.bam'},
 10009: {'type': 'model',
         'name': 'nearRight',
         'comment': '',
         'parentEntId': 10004,
         'pos': Point3(-43.6387481689, -36.8883552551, 0.228899106383),
         'hpr': Vec3(154.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0),
         'collisionsOnly': 0,
         'loadType': 'loadModelCopy',
         'modelPath': 'phase_10/models/cashbotHQ/pipes_D1.bam'},
 10000: {'type': 'nodepath',
         'name': 'cogs',
         'comment': '',
         'parentEntId': 0,
         'pos': Point3(102.420700073, 0.0, 0.0),
         'hpr': Point3(270.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0)},
 10002: {'type': 'nodepath',
         'name': 'frontCogs',
         'comment': '',
         'parentEntId': 0,
         'pos': Point3(-94.4453353882, 0.0, 0.0),
         'hpr': Vec3(270.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0)},
 10004: {'type': 'nodepath',
         'name': 'props',
         'comment': '',
         'parentEntId': 0,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': 1},
 10007: {'type': 'nodepath',
         'name': 'leftCogs',
         'comment': '',
         'parentEntId': 0,
         'pos': Point3(0.0, 40.9584655762, 0.0),
         'hpr': Vec3(270.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0)},
 10010: {'type': 'nodepath',
         'name': 'rightCogs',
         'comment': '',
         'parentEntId': 0,
         'pos': Point3(0.0, -40.9599990845, 0.0),
         'hpr': Vec3(270.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0)}}
Scenario0 = {}
levelSpec = {'globalEntities': GlobalEntities,
 'scenarios': [Scenario0]}
