# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'parameter_configuration.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ConfigurationDialog(object):
    def setupUi(self, ConfigurationDialog):
        ConfigurationDialog.setObjectName("ConfigurationDialog")
        ConfigurationDialog.resize(900, 593)
        font = QtGui.QFont()
        font.setPointSize(10)
        ConfigurationDialog.setFont(font)
        self.GridLayout = QtWidgets.QGridLayout(ConfigurationDialog)
        self.GridLayout.setVerticalSpacing(22)
        self.GridLayout.setObjectName("GridLayout")
        self.fgw_slider_value = QtWidgets.QSlider(ConfigurationDialog)
        self.fgw_slider_value.setMinimum(1)
        self.fgw_slider_value.setMaximum(6)
        self.fgw_slider_value.setSingleStep(1)
        self.fgw_slider_value.setPageStep(1)
        self.fgw_slider_value.setProperty("value", 4)
        self.fgw_slider_value.setSliderPosition(4)
        self.fgw_slider_value.setOrientation(QtCore.Qt.Horizontal)
        self.fgw_slider_value.setObjectName("fgw_slider_value")
        self.GridLayout.addWidget(self.fgw_slider_value, 1, 2, 1, 1)
        self.gpspwr_checkBox = QtWidgets.QCheckBox(ConfigurationDialog)
        self.gpspwr_checkBox.setObjectName("gpspwr_checkBox")
        self.GridLayout.addWidget(self.gpspwr_checkBox, 10, 0, 1, 1)
        self.apst_label_parameter = QtWidgets.QLabel(ConfigurationDialog)
        self.apst_label_parameter.setObjectName("apst_label_parameter")
        self.GridLayout.addWidget(self.apst_label_parameter, 3, 8, 1, 1)
        self.label_4 = QtWidgets.QLabel(ConfigurationDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.GridLayout.addWidget(self.label_4, 8, 0, 1, 1)
        self.afrsf_label_parameter = QtWidgets.QLabel(ConfigurationDialog)
        self.afrsf_label_parameter.setObjectName("afrsf_label_parameter")
        self.GridLayout.addWidget(self.afrsf_label_parameter, 4, 0, 1, 1)
        self.gppl_label_parameter = QtWidgets.QLabel(ConfigurationDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gppl_label_parameter.sizePolicy().hasHeightForWidth())
        self.gppl_label_parameter.setSizePolicy(sizePolicy)
        self.gppl_label_parameter.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.gppl_label_parameter.setObjectName("gppl_label_parameter")
        self.GridLayout.addWidget(self.gppl_label_parameter, 9, 2, 1, 1)
        self.gppl_spinBox = QtWidgets.QSpinBox(ConfigurationDialog)
        self.gppl_spinBox.setMaximum(2)
        self.gppl_spinBox.setProperty("value", 1)
        self.gppl_spinBox.setObjectName("gppl_spinBox")
        self.GridLayout.addWidget(self.gppl_spinBox, 9, 4, 1, 1)
        self.afrsf_label_display = QtWidgets.QLabel(ConfigurationDialog)
        self.afrsf_label_display.setObjectName("afrsf_label_display")
        self.GridLayout.addWidget(self.afrsf_label_display, 4, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.GridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.apbt_slider_value = QtWidgets.QSlider(ConfigurationDialog)
        self.apbt_slider_value.setMinimum(2)
        self.apbt_slider_value.setMaximum(50)
        self.apbt_slider_value.setSingleStep(2)
        self.apbt_slider_value.setPageStep(2)
        self.apbt_slider_value.setProperty("value", 10)
        self.apbt_slider_value.setOrientation(QtCore.Qt.Horizontal)
        self.apbt_slider_value.setObjectName("apbt_slider_value")
        self.GridLayout.addWidget(self.apbt_slider_value, 4, 10, 1, 1)
        self.line_2 = QtWidgets.QFrame(ConfigurationDialog)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.GridLayout.addWidget(self.line_2, 7, 0, 1, 5)
        self.apbt_label_parameter = QtWidgets.QLabel(ConfigurationDialog)
        self.apbt_label_parameter.setObjectName("apbt_label_parameter")
        self.GridLayout.addWidget(self.apbt_label_parameter, 4, 8, 1, 1)
        self.afafp_label_parameter = QtWidgets.QLabel(ConfigurationDialog)
        self.afafp_label_parameter.setObjectName("afafp_label_parameter")
        self.GridLayout.addWidget(self.afafp_label_parameter, 6, 0, 1, 1)
        self.apbt_label_display = QtWidgets.QLabel(ConfigurationDialog)
        self.apbt_label_display.setObjectName("apbt_label_display")
        self.GridLayout.addWidget(self.apbt_label_display, 4, 12, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.GridLayout.addItem(spacerItem1, 1, 11, 1, 1)
        self.apfp_label_display = QtWidgets.QLabel(ConfigurationDialog)
        self.apfp_label_display.setObjectName("apfp_label_display")
        self.GridLayout.addWidget(self.apfp_label_display, 6, 12, 1, 1)
        self.apfp_slider_value = QtWidgets.QSlider(ConfigurationDialog)
        self.apfp_slider_value.setMinimum(1)
        self.apfp_slider_value.setMaximum(100)
        self.apfp_slider_value.setPageStep(1)
        self.apfp_slider_value.setProperty("value", 10)
        self.apfp_slider_value.setOrientation(QtCore.Qt.Horizontal)
        self.apfp_slider_value.setObjectName("apfp_slider_value")
        self.GridLayout.addWidget(self.apfp_slider_value, 6, 10, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.GridLayout.addItem(spacerItem2, 1, 9, 1, 1)
        self.afsw_label_parameter = QtWidgets.QLabel(ConfigurationDialog)
        self.afsw_label_parameter.setObjectName("afsw_label_parameter")
        self.GridLayout.addWidget(self.afsw_label_parameter, 5, 0, 1, 1)
        self.fgw_label_display = QtWidgets.QLabel(ConfigurationDialog)
        self.fgw_label_display.setObjectName("fgw_label_display")
        self.GridLayout.addWidget(self.fgw_label_display, 1, 4, 1, 1)
        self.afsw_slider_value = QtWidgets.QSlider(ConfigurationDialog)
        self.afsw_slider_value.setMinimum(5)
        self.afsw_slider_value.setMaximum(60)
        self.afsw_slider_value.setSingleStep(5)
        self.afsw_slider_value.setPageStep(5)
        self.afsw_slider_value.setProperty("value", 20)
        self.afsw_slider_value.setOrientation(QtCore.Qt.Horizontal)
        self.afsw_slider_value.setObjectName("afsw_slider_value")
        self.GridLayout.addWidget(self.afsw_slider_value, 5, 2, 1, 1)
        self.afm_label_parameter = QtWidgets.QLabel(ConfigurationDialog)
        self.afm_label_parameter.setObjectName("afm_label_parameter")
        self.GridLayout.addWidget(self.afm_label_parameter, 2, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.GridLayout.addItem(spacerItem3, 1, 3, 1, 1)
        self.apst_label_display = QtWidgets.QLabel(ConfigurationDialog)
        self.apst_label_display.setObjectName("apst_label_display")
        self.GridLayout.addWidget(self.apst_label_display, 3, 12, 1, 1)
        self.label_2 = QtWidgets.QLabel(ConfigurationDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.GridLayout.addWidget(self.label_2, 0, 8, 1, 5)
        self.afrsf_slider_value = QtWidgets.QSlider(ConfigurationDialog)
        self.afrsf_slider_value.setMinimum(5)
        self.afrsf_slider_value.setMaximum(80)
        self.afrsf_slider_value.setSingleStep(5)
        self.afrsf_slider_value.setPageStep(5)
        self.afrsf_slider_value.setProperty("value", 25)
        self.afrsf_slider_value.setSliderPosition(25)
        self.afrsf_slider_value.setOrientation(QtCore.Qt.Horizontal)
        self.afrsf_slider_value.setObjectName("afrsf_slider_value")
        self.GridLayout.addWidget(self.afrsf_slider_value, 4, 2, 1, 1)
        self.afa_checkBox = QtWidgets.QCheckBox(ConfigurationDialog)
        self.afa_checkBox.setChecked(True)
        self.afa_checkBox.setObjectName("afa_checkBox")
        self.GridLayout.addWidget(self.afa_checkBox, 3, 0, 1, 1)
        self.apsw_label_display = QtWidgets.QLabel(ConfigurationDialog)
        self.apsw_label_display.setObjectName("apsw_label_display")
        self.GridLayout.addWidget(self.apsw_label_display, 2, 12, 1, 1)
        self.aphbw_label_parameter = QtWidgets.QLabel(ConfigurationDialog)
        self.aphbw_label_parameter.setObjectName("aphbw_label_parameter")
        self.GridLayout.addWidget(self.aphbw_label_parameter, 1, 8, 1, 1)
        self.line_3 = QtWidgets.QFrame(ConfigurationDialog)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.GridLayout.addWidget(self.line_3, 7, 8, 1, 5)
        self.apsw_slider_value = QtWidgets.QSlider(ConfigurationDialog)
        self.apsw_slider_value.setMinimum(6)
        self.apsw_slider_value.setMaximum(30)
        self.apsw_slider_value.setSingleStep(2)
        self.apsw_slider_value.setPageStep(2)
        self.apsw_slider_value.setProperty("value", 10)
        self.apsw_slider_value.setOrientation(QtCore.Qt.Horizontal)
        self.apsw_slider_value.setObjectName("apsw_slider_value")
        self.GridLayout.addWidget(self.apsw_slider_value, 2, 10, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.GridLayout.addItem(spacerItem4, 1, 7, 1, 1)
        self.aphbw_slider_value = QtWidgets.QSlider(ConfigurationDialog)
        self.aphbw_slider_value.setMinimum(20)
        self.aphbw_slider_value.setMaximum(140)
        self.aphbw_slider_value.setSingleStep(4)
        self.aphbw_slider_value.setPageStep(4)
        self.aphbw_slider_value.setProperty("value", 40)
        self.aphbw_slider_value.setOrientation(QtCore.Qt.Horizontal)
        self.aphbw_slider_value.setObjectName("aphbw_slider_value")
        self.GridLayout.addWidget(self.aphbw_slider_value, 1, 10, 1, 1)
        self.fgw_label_parameter = QtWidgets.QLabel(ConfigurationDialog)
        self.fgw_label_parameter.setObjectName("fgw_label_parameter")
        self.GridLayout.addWidget(self.fgw_label_parameter, 1, 0, 1, 1)
        self.apst_slider_value = QtWidgets.QSlider(ConfigurationDialog)
        self.apst_slider_value.setMinimum(1)
        self.apst_slider_value.setMaximum(30)
        self.apst_slider_value.setPageStep(5)
        self.apst_slider_value.setProperty("value", 5)
        self.apst_slider_value.setOrientation(QtCore.Qt.Horizontal)
        self.apst_slider_value.setObjectName("apst_slider_value")
        self.GridLayout.addWidget(self.apst_slider_value, 3, 10, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.GridLayout.addItem(spacerItem5, 1, 5, 1, 1)
        self.apfp_label_parameter = QtWidgets.QLabel(ConfigurationDialog)
        self.apfp_label_parameter.setObjectName("apfp_label_parameter")
        self.GridLayout.addWidget(self.apfp_label_parameter, 6, 8, 1, 1)
        self.afafp_slider_value = QtWidgets.QSlider(ConfigurationDialog)
        self.afafp_slider_value.setMinimum(3)
        self.afafp_slider_value.setMaximum(30)
        self.afafp_slider_value.setSingleStep(3)
        self.afafp_slider_value.setPageStep(3)
        self.afafp_slider_value.setProperty("value", 6)
        self.afafp_slider_value.setOrientation(QtCore.Qt.Horizontal)
        self.afafp_slider_value.setObjectName("afafp_slider_value")
        self.GridLayout.addWidget(self.afafp_slider_value, 6, 2, 1, 1)
        self.afsw_label_display = QtWidgets.QLabel(ConfigurationDialog)
        self.afsw_label_display.setObjectName("afsw_label_display")
        self.GridLayout.addWidget(self.afsw_label_display, 5, 4, 1, 1)
        self.gpwptf_checkBox = QtWidgets.QCheckBox(ConfigurationDialog)
        self.gpwptf_checkBox.setChecked(True)
        self.gpwptf_checkBox.setObjectName("gpwptf_checkBox")
        self.GridLayout.addWidget(self.gpwptf_checkBox, 9, 0, 1, 1)
        self.afafp_label_display = QtWidgets.QLabel(ConfigurationDialog)
        self.afafp_label_display.setObjectName("afafp_label_display")
        self.GridLayout.addWidget(self.afafp_label_display, 6, 4, 1, 1)
        self.apsw_label_parameter = QtWidgets.QLabel(ConfigurationDialog)
        self.apsw_label_parameter.setObjectName("apsw_label_parameter")
        self.GridLayout.addWidget(self.apsw_label_parameter, 2, 8, 1, 1)
        self.afm_comboBox = QtWidgets.QComboBox(ConfigurationDialog)
        self.afm_comboBox.setCurrentText("")
        self.afm_comboBox.setMaxVisibleItems(2)
        self.afm_comboBox.setObjectName("afm_comboBox")
        self.GridLayout.addWidget(self.afm_comboBox, 2, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(ConfigurationDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.GridLayout.addWidget(self.label_8, 5, 8, 1, 2)
        self.label = QtWidgets.QLabel(ConfigurationDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.GridLayout.addWidget(self.label, 0, 0, 1, 5)
        self.aphbw_label_display = QtWidgets.QLabel(ConfigurationDialog)
        self.aphbw_label_display.setObjectName("aphbw_label_display")
        self.GridLayout.addWidget(self.aphbw_label_display, 1, 12, 1, 1)
        self.gpbl_label_parameter = QtWidgets.QLabel(ConfigurationDialog)
        self.gpbl_label_parameter.setObjectName("gpbl_label_parameter")
        self.GridLayout.addWidget(self.gpbl_label_parameter, 10, 2, 1, 1)
        self.gpbl_spinBox = QtWidgets.QSpinBox(ConfigurationDialog)
        self.gpbl_spinBox.setMaximum(4)
        self.gpbl_spinBox.setObjectName("gpbl_spinBox")
        self.GridLayout.addWidget(self.gpbl_spinBox, 10, 4, 1, 1)
        self.line = QtWidgets.QFrame(ConfigurationDialog)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.GridLayout.addWidget(self.line, 0, 6, 12, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(ConfigurationDialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.GridLayout.addWidget(self.buttonBox, 11, 10, 1, 3)
        self.restore_standard_values = QtWidgets.QPushButton(ConfigurationDialog)
        self.restore_standard_values.setObjectName("restore_standard_values")
        self.GridLayout.addWidget(self.restore_standard_values, 10, 10, 1, 3)
        self.spp_checkBox = QtWidgets.QCheckBox(ConfigurationDialog)
        self.spp_checkBox.setObjectName("spp_checkBox")
        self.GridLayout.addWidget(self.spp_checkBox, 11, 0, 1, 2)
        self.gpif_label_parameter = QtWidgets.QLabel(ConfigurationDialog)
        self.gpif_label_parameter.setObjectName("gpif_label_parameter")
        self.GridLayout.addWidget(self.gpif_label_parameter, 11, 2, 1, 1)
        self.gpif_comboBox = QtWidgets.QComboBox(ConfigurationDialog)
        self.gpif_comboBox.setObjectName("gpif_comboBox")
        self.GridLayout.addWidget(self.gpif_comboBox, 11, 4, 1, 1)
        self.GridLayout.setColumnStretch(0, 5)

        self.retranslateUi(ConfigurationDialog)
        self.afm_comboBox.setCurrentIndex(-1)
        self.aphbw_slider_value.valueChanged['int'].connect(self.aphbw_label_display.setNum)
        self.afrsf_slider_value.valueChanged['int'].connect(self.afrsf_label_display.setNum)
        self.apsw_slider_value.valueChanged['int'].connect(self.apsw_label_display.setNum)
        self.apbt_slider_value.valueChanged['int'].connect(self.apbt_label_display.setNum)
        self.apfp_slider_value.valueChanged['int'].connect(self.apfp_label_display.setNum)
        self.afsw_slider_value.valueChanged['int'].connect(self.afsw_label_display.setNum)
        self.afafp_slider_value.valueChanged['int'].connect(self.afafp_label_display.setNum)
        QtCore.QMetaObject.connectSlotsByName(ConfigurationDialog)

    def retranslateUi(self, ConfigurationDialog):
        _translate = QtCore.QCoreApplication.translate
        ConfigurationDialog.setWindowTitle(_translate("ConfigurationDialog", "Parameter Configuration"))
        self.gpspwr_checkBox.setToolTip(_translate("ConfigurationDialog", "Check if for each job the corresponding protocol section should be stored along with the stacked image."))
        self.gpspwr_checkBox.setText(_translate("ConfigurationDialog", "Store protocol with results"))
        self.apst_label_parameter.setToolTip(_translate("ConfigurationDialog", "In the automatic construction of alignment point grids, points are discarded if there is too little local structure.\n"
"Higher values result in more points to be discarded. If the value is too low, unreliable alignment points are included."))
        self.apst_label_parameter.setText(_translate("ConfigurationDialog", "Minimum structure"))
        self.label_4.setToolTip(_translate("ConfigurationDialog", "With these parameters parts of the computing workflow can be skipped."))
        self.label_4.setText(_translate("ConfigurationDialog", "Workflow Parameters"))
        self.afrsf_label_parameter.setToolTip(_translate("ConfigurationDialog", "Only for \"Surface\" mode: Size of the stabilization patch relative to the frame size."))
        self.afrsf_label_parameter.setText(_translate("ConfigurationDialog", "Stabilization patch size\n"
"(% of frame size)"))
        self.gppl_label_parameter.setToolTip(_translate("ConfigurationDialog", "Level of detail of protocol: 0 for nothing, 1 for major steps only, 2 for detailed info."))
        self.gppl_label_parameter.setText(_translate("ConfigurationDialog", "Protocol detail level"))
        self.afrsf_label_display.setText(_translate("ConfigurationDialog", "TextLabel"))
        self.apbt_label_parameter.setToolTip(_translate("ConfigurationDialog", "In the automatic construction of alignment point grids, points are discarded if no pixels in the surrounding box are bright enough.\n"
"Higher values result in more points to be discarded. If the value is too low, unreliable alignment points are included."))
        self.apbt_label_parameter.setText(_translate("ConfigurationDialog", "Minimum brightness"))
        self.afafp_label_parameter.setToolTip(_translate("ConfigurationDialog", "The reference frame for the multipoint alignment is computed as the average of the best frames. This value specifies the number of frames to be used."))
        self.afafp_label_parameter.setText(_translate("ConfigurationDialog", "Percentage of best frames for\n"
"reference frame computation"))
        self.apbt_label_display.setText(_translate("ConfigurationDialog", "TextLabel"))
        self.apfp_label_display.setText(_translate("ConfigurationDialog", "TextLabel"))
        self.afsw_label_parameter.setToolTip(_translate("ConfigurationDialog", "Only for \"Surface\" mode: Maximum allowed shift of consecutive frames per coordinate direction in pixels."))
        self.afsw_label_parameter.setText(_translate("ConfigurationDialog", "Stabilization search width\n"
"(pixels)"))
        self.fgw_label_display.setText(_translate("ConfigurationDialog", "TextLabel"))
        self.afm_label_parameter.setToolTip(_translate("ConfigurationDialog", "All frames have to be globally aligned with each other before stacking. Two modes are supported: \"Surface\" and \"Planetary\".\n"
"In \"Surface\" mode (moon, sun) a patch with sufficient local contrast is used for image registration.\n"
"In \"Planetary\" mode, the \"centers of gravity\" of all frames are registered with each other."))
        self.afm_label_parameter.setText(_translate("ConfigurationDialog", "Frame stabilization  mode"))
        self.apst_label_display.setText(_translate("ConfigurationDialog", "TextLabel"))
        self.label_2.setToolTip(_translate("ConfigurationDialog", "Parameters used in the second (fine-tuning) phase. In each pixel the color image\n"
"is warped such that it exactly matches the B/W image."))
        self.label_2.setText(_translate("ConfigurationDialog", "Multipoint Alignment Parameters"))
        self.afa_checkBox.setToolTip(_translate("ConfigurationDialog", "Only for \"Surface\" mode: Identify frame stabilization patch automatically."))
        self.afa_checkBox.setText(_translate("ConfigurationDialog", "Automatic frame stabilization"))
        self.apsw_label_display.setText(_translate("ConfigurationDialog", "TextLabel"))
        self.aphbw_label_parameter.setToolTip(_translate("ConfigurationDialog", "Size of the quadratic box around an alignment point used to measure the local shift.\n"
"Smaller values result in better resolution of locality, but shift detection can fail if local contrast is low."))
        self.aphbw_label_parameter.setText(_translate("ConfigurationDialog", "Alignment box width\n"
"(pixels)"))
        self.fgw_label_parameter.setToolTip(_translate("ConfigurationDialog", "In the presence of noise in the image, shift detection between frames can be misled by spurious local minima.\n"
"Gaussian blur can help finding the global optimum. Try higher values for noisy images."))
        self.fgw_label_parameter.setText(_translate("ConfigurationDialog", "Noise level (add Gaussian blur)"))
        self.apfp_label_parameter.setToolTip(_translate("ConfigurationDialog", "At each alignment point the same number of frames are stacked.\n"
"This value specifies this number relative to the total number of frames."))
        self.apfp_label_parameter.setText(_translate("ConfigurationDialog", "Percentage of best frames\n"
"to be stacked"))
        self.afsw_label_display.setText(_translate("ConfigurationDialog", "TextLabel"))
        self.gpwptf_checkBox.setToolTip(_translate("ConfigurationDialog", "Append a protocol of this program execution to the text file \"PlanetarySystemStacker.log\" in the user\'s home directory."))
        self.gpwptf_checkBox.setText(_translate("ConfigurationDialog", "Write protocol to file"))
        self.afafp_label_display.setText(_translate("ConfigurationDialog", "TextLabel"))
        self.apsw_label_parameter.setToolTip(_translate("ConfigurationDialog", "Maximum allowed local warp per coordinate direction."))
        self.apsw_label_parameter.setText(_translate("ConfigurationDialog", "Max. alignment search\n"
"width (pixels)"))
        self.label_8.setText(_translate("ConfigurationDialog", "Stacking Parameters"))
        self.label.setToolTip(_translate("ConfigurationDialog", "Parameters used in the first matching phase. In this phase, the color image\n"
"is rotated, shifted and stretched to match the B/W image."))
        self.label.setText(_translate("ConfigurationDialog", "Frame-related Parameters"))
        self.aphbw_label_display.setText(_translate("ConfigurationDialog", "TextLabel"))
        self.gpbl_label_parameter.setToolTip(_translate("ConfigurationDialog", "Level of data buffering, 0 for no buffering, 4 for buffering all frames and intermediate results."))
        self.gpbl_label_parameter.setText(_translate("ConfigurationDialog", "Data buffering level"))
        self.restore_standard_values.setToolTip(_translate("ConfigurationDialog", "Reset parameters to original values. In most cases they should give satisfactory results."))
        self.restore_standard_values.setText(_translate("ConfigurationDialog", "Restore standard values"))
        self.spp_checkBox.setToolTip(_translate("ConfigurationDialog", "Postprocess the stacked image immediately after stacking,\n"
"rather than in a separate job"))
        self.spp_checkBox.setText(_translate("ConfigurationDialog", "Stacking plus postprocessing"))
        self.gpif_label_parameter.setToolTip(_translate("ConfigurationDialog", "Stacked and postprocessed images can be written either in \"tiff\" or \"fits\" format."))
        self.gpif_label_parameter.setText(_translate("ConfigurationDialog", "Write images as"))

