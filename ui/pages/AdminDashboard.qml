import QtQuick
import QtQuick.Controls

Rectangle {
    color: "#0a0e12"

    Column {
        anchors.fill: parent
        anchors.margins: 20
        spacing: 10

        Text {
            text: "ADMIN DASHBOARD"
            color: "white"
            font.pixelSize: 26
        }

        Rectangle {
            width: parent.width
            height: 200
            color: "#111827"

            Column {
                anchors.centerIn: parent
                spacing: 8

                Text { text: "Active Users: 1"; color: "white" }
                Text { text: "Events Logged: 128"; color: "white" }
                Text { text: "Security Alerts: 3"; color: "red" }
            }
        }

        Button { text: "View Logs" }
        Button { text: "Manage Users" }
        Button { text: "System Audit" }
    }
}