import QtQuick
import QtQuick.Controls

Rectangle {
    id: libraryRoot
    anchors.fill: parent
    color: "#1b2838"

    ListModel {
        id: eventsModel
    }

    Column {
        anchors.fill: parent
        anchors.margins: 20
        spacing: 15

        Text {
            text: "AGENT MONITORING LOGS (LIBRARY)"
            color: "#66c0f4"
            font.pointSize: 18
            font.bold: true
        }

        // Список для вывода событий
        ListView {
            id: listView
            width: parent.width
            height: parent.height - 80
            model: eventsModel
            clip: true
            spacing: 5

            delegate: Rectangle {
                width: listView.width
                height: 45
                color: "#171a21"
                radius: 4
                border.color: model.status === "error" ? "#ff4d4d" : "#2a475e"

                Row {
                    anchors.verticalCenter: parent.verticalCenter
                    anchors.left: parent.left
                    anchors.leftMargin: 15
                    spacing: 20

                    Text {
                        text: "[" + model.type.toUpperCase() + "]"
                        color: model.status === "error" ? "#ff4d4d" : "#66c0f4"
                        font.bold: true
                    }

                    Text {
                        text: model.message
                        color: "#c7d5e0"
                    }
                }
            }
        }
    }

    // Таймер автоматического запроса данных раз в 2 секунды
    Timer {
        interval: 2000
        running: true
        repeat: true
        triggeredOnStart: true
        onTriggered: {
            if (window.isAuthorized) { // Запрашиваем только если авторизованы
                authHandler.fetch_events()
            }
        }
    }

    Connections {
        target: authHandler

        function onEventsReceived(jsonString) {
            eventsModel.clear()
            try {
                var data = JSON.parse(jsonString)
                for (var i = 0; i < data.length; i++) {
                    eventsModel.append({
                        "type": data[i].event_type || "info",
                        "status": data[i].status || "normal",
                        "message": data[i].message || ""
                    })
                }
            } catch(e) {
                console.log("Error parsing events JSON")
            }
        }
    }
}
