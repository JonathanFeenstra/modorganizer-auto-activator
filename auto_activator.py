"""
Auto-Activator Plugin for Mod Organizer 2

Copyright (C) 2023 Jonathan Feenstra

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
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
