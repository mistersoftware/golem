import sys
import os
import logging
import logging.config

sys.path.append( os.environ.get( 'GOLEM' ) )

from tools.UiGen import genUiFiles
genUiFiles( "ui" )

from RenderingAdmApplicationLogic import RenderingAdmApplicationLogic
from GNRstartApp import startRenderingApp

from examples.gnr.ui.AdministrationMainWindow import AdministrationMainWindow
from examples.gnr.Application import GNRGui
from examples.gnr.customizers.RenderingAdmMainWindowCustomizer import RenderingAdmMainWindowCustomizer


def main():

    logging.config.fileConfig('logging.ini', disable_existing_loggers=False)

    logic   = RenderingAdmApplicationLogic()
    app     = GNRGui( logic, AdministrationMainWindow )
    gui     = RenderingAdmMainWindowCustomizer

    startRenderingApp( logic, app, gui )

main()