# thai-river-web-scraping
Script for scraping data from https://tiwrm.hii.or.th/DATA/REPORT/php/chart/chaopraya/small/chaopraya.php


Node-Red flow
```
[
    {
        "id": "0f746ec73085280d",
        "type": "inject",
        "z": "ab4bb3ba14295947",
        "name": "ดึงข้อมูลทุกๆ 10 นาที",
        "props": [
            {
                "p": "payload"
            },
            {
                "p": "topic",
                "vt": "str"
            }
        ],
        "repeat": "600",
        "crontab": "",
        "once": false,
        "onceDelay": 0.1,
        "topic": "",
        "payloadType": "date",
        "x": 580,
        "y": 140,
        "wires": [
            [
                "417d580878d66055"
            ]
        ]
    },
    {
        "id": "417d580878d66055",
        "type": "exec",
        "z": "ab4bb3ba14295947",
        "command": "python3 /home/kunyaiadmin/test.py",
        "addpay": "",
        "append": "",
        "useSpawn": "false",
        "timer": "",
        "winHide": false,
        "oldrc": false,
        "name": "ดึงข้อมูลจากแผนที่ลุ่มน้ำ",
        "x": 800,
        "y": 160,
        "wires": [
            [
                "63507a1685d32b4c"
            ],
            [],
            []
        ]
    },
    {
        "id": "63507a1685d32b4c",
        "type": "json",
        "z": "ab4bb3ba14295947",
        "name": "",
        "property": "payload",
        "action": "obj",
        "pretty": false,
        "x": 990,
        "y": 140,
        "wires": [
            [
                "f6359ed1281116da",
                "c275fc66e824fe49",
                "2f077e03a5109fbd",
                "6ec7db5f924a6287"
            ]
        ]
    },
    {
        "id": "f6359ed1281116da",
        "type": "debug",
        "z": "ab4bb3ba14295947",
        "name": "",
        "active": false,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "statusVal": "",
        "statusType": "auto",
        "x": 1170,
        "y": 140,
        "wires": []
    },
    {
        "id": "c275fc66e824fe49",
        "type": "switch",
        "z": "ab4bb3ba14295947",
        "name": "เกณฑ์ระดับน้ำปัจจุบัน",
        "property": "payload.tele[34].percent",
        "propertyType": "msg",
        "rules": [
            {
                "t": "lt",
                "v": "80",
                "vt": "str"
            },
            {
                "t": "btwn",
                "v": "80",
                "vt": "num",
                "v2": "100",
                "v2t": "num"
            },
            {
                "t": "gt",
                "v": "100",
                "vt": "num"
            }
        ],
        "checkall": "true",
        "repair": false,
        "outputs": 3,
        "x": 1060,
        "y": 220,
        "wires": [
            [
                "2b580971a3e08f7a"
            ],
            [
                "8ed8a3f80d7fb08a"
            ],
            [
                "d4abff49f499f3be"
            ]
        ]
    },
    {
        "id": "a6ee637746200dd7",
        "type": "debug",
        "z": "ab4bb3ba14295947",
        "name": "เฝ้าระวัง",
        "active": false,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "payload",
        "targetType": "msg",
        "statusVal": "",
        "statusType": "auto",
        "x": 1540,
        "y": 240,
        "wires": []
    },
    {
        "id": "2b580971a3e08f7a",
        "type": "debug",
        "z": "ab4bb3ba14295947",
        "name": "ปกติ",
        "active": false,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "payload",
        "targetType": "msg",
        "statusVal": "",
        "statusType": "auto",
        "x": 1530,
        "y": 200,
        "wires": []
    },
    {
        "id": "8ed8a3f80d7fb08a",
        "type": "function",
        "z": "ab4bb3ba14295947",
        "name": "ประกาศระดับน้ำเฝ้าระวัง",
        "func": "var station_name = msg.payload.tele[34].name;\nvar n_current = msg.payload.tele[34].water1;\nvar bank = msg.payload.tele[34].bank;\nvar percent = msg.payload.tele[34].percent;\nn_left = bank - n_current;\nmsg.payload = \"ระดับน้ำปัจจุบันประจำสถานีวัดน้ำ \" + station_name + \" มีระดับต่ำกว่าตลิ่งอยู่ที่ \" + n_left + \" เมตร โดยคิดเป็น \" + percent +\" แนะนำควรเตรียมพร้อมและติดตามสถานการณ์น้ำอย่างใกล้ชิด\"\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "initialize": "",
        "finalize": "",
        "libs": [],
        "x": 1340,
        "y": 240,
        "wires": [
            [
                "a6ee637746200dd7"
            ]
        ]
    },
    {
        "id": "2f077e03a5109fbd",
        "type": "function",
        "z": "ab4bb3ba14295947",
        "name": "ดึงชื่อสถานีโทรมาตร",
        "func": "var n=0\nvar stack = []\nwhile(n<50){\n    var name = msg.payload.tele[n].code\n    stack.push(name)\n    n++\n}\nmsg.payload = stack\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "initialize": "",
        "finalize": "",
        "libs": [],
        "x": 1170,
        "y": 60,
        "wires": [
            [
                "89e0a22e71ef2c16"
            ]
        ]
    },
    {
        "id": "89e0a22e71ef2c16",
        "type": "debug",
        "z": "ab4bb3ba14295947",
        "name": "",
        "active": false,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "statusVal": "",
        "statusType": "auto",
        "x": 1370,
        "y": 60,
        "wires": []
    },
    {
        "id": "d4abff49f499f3be",
        "type": "function",
        "z": "ab4bb3ba14295947",
        "name": "ประกาศระดับน้าอันตราย",
        "func": "var station_name = msg.payload.tele[34].name;\nvar n_current = msg.payload.tele[34].water1;\nvar bank = msg.payload.tele[34].bank;\nvar percent = msg.payload.tele[34].percent;\nn_left = n_current - bank;\nmsg.payload = \"ระดับน้ำปัจจุบันประจำสถานีวัดน้ำ\" + station_name + \" มีระดับสูงกว่าตลิ่งอยู่ที่ \" + n_left.toFixed(1) + \" เมตร โดยคิดเป็น \" + percent.toFixed() +\" เปอร์เซ็นต์ แนะนำควรทำการอพยพโดยทันที\"\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "initialize": "",
        "finalize": "",
        "libs": [],
        "x": 1340,
        "y": 280,
        "wires": [
            [
                "d91ac766ae44e9d9"
            ]
        ]
    },
    {
        "id": "d91ac766ae44e9d9",
        "type": "debug",
        "z": "ab4bb3ba14295947",
        "name": "",
        "active": false,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "statusVal": "",
        "statusType": "auto",
        "x": 1550,
        "y": 280,
        "wires": []
    },
    {
        "id": "04a41cc753f87161",
        "type": "ui_chart",
        "z": "ab4bb3ba14295947",
        "name": "",
        "group": "063fefe75592dd27",
        "order": 1,
        "width": 0,
        "height": 0,
        "label": "สถานีโทรมาตรอุทัยธานี",
        "chartType": "line",
        "legend": "false",
        "xformat": "HH:mm:ss",
        "interpolate": "linear",
        "nodata": "",
        "dot": true,
        "ymin": "",
        "ymax": "",
        "removeOlder": "3",
        "removeOlderPoints": "",
        "removeOlderUnit": "3600",
        "cutout": 0,
        "useOneColor": false,
        "useUTC": false,
        "colors": [
            "#1f77b4",
            "#aec7e8",
            "#ff7f0e",
            "#2ca02c",
            "#98df8a",
            "#d62728",
            "#ff9896",
            "#9467bd",
            "#c5b0d5"
        ],
        "outputs": 1,
        "useDifferentColor": false,
        "className": "",
        "x": 1180,
        "y": 360,
        "wires": [
            []
        ]
    },
    {
        "id": "6ec7db5f924a6287",
        "type": "change",
        "z": "ab4bb3ba14295947",
        "name": "",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "payload.tele[34].water1",
                "tot": "msg"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 920,
        "y": 280,
        "wires": [
            [
                "04a41cc753f87161",
                "73e5f2fe0e735047"
            ]
        ]
    },
    {
        "id": "73e5f2fe0e735047",
        "type": "debug",
        "z": "ab4bb3ba14295947",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "statusVal": "",
        "statusType": "auto",
        "x": 1230,
        "y": 320,
        "wires": []
    },
    {
        "id": "063fefe75592dd27",
        "type": "ui_group",
        "name": "สถานการณ์น้ำ",
        "tab": "3d723297982455ad",
        "order": 1,
        "disp": false,
        "width": "6",
        "collapse": false,
        "className": ""
    },
    {
        "id": "3d723297982455ad",
        "type": "ui_tab",
        "name": "Flood detector",
        "icon": "dashboard",
        "disabled": false,
        "hidden": false
    }
]
```
