"""
Auto-Activator Plugin for Mod Organizer 2

Copyright (C) 2023 Jonathan Feenstra
"""
import mobase
from PyQt6.QtCore import qCritical
from PyQt6.QtWidgets import QApplication


class AutoActivator(mobase.IPlugin):
    def __init__(self) -> None:
        super().__init__()

    def init(self, organizer: mobase.IOrganizer) -> bool:
        self.__organizer = organizer

        if not self.__organizer.modList().onModInstalled(self.__onModInstalled):
            qCritical("Failed to install onModInstalled callback.")
            return False

        return True

    def name(self) -> str:
        return "Auto-Activator"

    def author(self) -> str:
        return "Jonathan Feenstra"

    def description(self) -> str:
        return self.__tr("Automatically activate mods after installing.")

    def version(self) -> mobase.VersionInfo:
        return mobase.VersionInfo(1, 0, 0, release_type=mobase.ReleaseType.FINAL)

    def settings(self) -> list[mobase.PluginSetting]:
        return []

    def __onModInstalled(self, mod: mobase.IModInterface) -> None:
        self.__organizer.modList().setActive(name=mod.name(), active=True)

    def __tr(self, txt: str) -> str:
        return QApplication.translate("AutoActivator", txt)


def createPlugin() -> mobase.IPlugin:
    return AutoActivator()
