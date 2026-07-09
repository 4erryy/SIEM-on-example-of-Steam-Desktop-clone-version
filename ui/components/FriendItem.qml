import QtQuick
import QtQuick.Controls

Rectangle {
    width: parent.width
    height: 50
    color: "#1f2937"

    property string name: "Friend"
    property bool online: true

    Text {
        anchors.centerIn: parent
        text: name + (online ? " • online" : " • offline")
        color: online ? "lightgreen" : "gray"
    }
}