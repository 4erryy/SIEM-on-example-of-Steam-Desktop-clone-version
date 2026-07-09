import QtQuick
import QtQuick.Controls
import QtQuick.Dialogs

Rectangle {
    id: settingsRoot
    anchors.fill: parent
    color: "#1b2838"

    FileDialog {
        id: fileDialog
        title: "Выберите файл .maFile или .json"
        currentFolder: "_" 
        nameFilters: ["Steam Authenticator files (*.maFile *.json)"]
        onAccepted: {
            statusText.text = "🔄 Отправка файла..."
            authHandler.upload_mafile(fileDialog.selectedFile.toString())
        }
    }

    Column {
        anchors.centerIn: parent
        spacing: 20
        width: parent.width * 0.8

        Text {
            text: "УПРАВЛЕНИЕ STEAM GUARD (.MAFILE)"
            color: "#66c0f4"
            font.pointSize: 16
            font.bold: true
            anchors.horizontalCenter: parent.horizontalCenter
        }

        Button {
            text: "📁 Загрузить .maFile в систему"
            width: 250
            anchors.horizontalCenter: parent.horizontalCenter
            onClicked: fileDialog.open()
        }

        Text {
            id: statusText
            text: "Выберите файл для импорта логов и привязки"
            color: "#c7d5e0"
            font.pointSize: 11
            wrapMode: Text.Wrap
            width: parent.width
            horizontalAlignment: Text.AlignHCenter
        }

        Button {
            text: "Проверить статус безопасности бэкенда"
            width: 250
            anchors.horizontalCenter: parent.horizontalCenter
            onClicked: authHandler.check_secure_status()
        }

        Text {
            id: backendStatusText
            text: "Статус соединения не проверен"
            color: "#8aa3b4"
            anchors.horizontalCenter: parent.horizontalCenter
        }
    }

    Connections {
        target: authHandler
        
        function onCheckResult(msg) {
            backendStatusText.text = msg
        }

        function onUploadStatus(statusMessage) {
            statusText.text = statusMessage
        }
    }
}
