import QtQuick
import QtQuick.Controls

Rectangle {
    color: "#0b0f14"

    Column {
        anchors.centerIn: parent
        spacing: 12

        Text {
            text: "SECURITY CENTER"
            color: "white"
            font.pixelSize: 26
        }

        Rectangle {
            width: 300
            height: 120
            color: "#1f2937"

            Column {
                anchors.centerIn: parent

                Text {
                    text: "Session Status: Active"
                    color: "lightgreen"
                }

                Text {
                    text: "Device: Trusted"
                    color: "white"
                }

                Button {
                    text: "Revoke Session"
                }
            }
        }

        CheckBox { text: "Enable anomaly detection" }
        CheckBox { text: "Enable agent monitoring" }
    }
}