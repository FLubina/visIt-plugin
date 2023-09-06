AddOperator("Slice", 1)
SetActivePlots(1)
SetActivePlots(1)
SliceAtts = SliceAttributes()
SliceAtts.originType = SliceAtts.Point  # Point, Intercept, Percent, Zone, Node
SliceAtts.originPoint = (0, 0, 0)
SliceAtts.originIntercept = 0
SliceAtts.originPercent = 0
SliceAtts.originZone = 0
SliceAtts.originNode = 0
SliceAtts.normal = (0, 1, 1)
SliceAtts.axisType = SliceAtts.Arbitrary  # XAxis, YAxis, ZAxis, Arbitrary, ThetaPhi
SliceAtts.upAxis = (0, 0, 1)
SliceAtts.project2d = 1
SliceAtts.interactive = 1
SliceAtts.flip = 0
SliceAtts.originZoneDomain = 0
SliceAtts.originNodeDomain = 0
SliceAtts.meshName = "MCNP mesh"
SliceAtts.theta = 0
SliceAtts.phi = 0
SetOperatorOptions(SliceAtts, 0, 1)
DrawPlots()
RemoveAllOperators(1)
AddOperator("ThreeSlice", 1)
ThreeSliceAtts = ThreeSliceAttributes()
ThreeSliceAtts.x = 1
ThreeSliceAtts.y = 2
ThreeSliceAtts.z = 3
ThreeSliceAtts.interactive = 1
SetOperatorOptions(ThreeSliceAtts, 0, 1)
DrawPlots()
# Begin spontaneous state
View2DAtts = View2DAttributes()
View2DAtts.windowCoords = (-110, 110, -155.563, 155.563)
View2DAtts.viewportCoords = (0.2, 0.95, 0.15, 0.95)
View2DAtts.fullFrameActivationMode = View2DAtts.Auto  # On, Off, Auto
View2DAtts.fullFrameAutoThreshold = 100
View2DAtts.xScale = View2DAtts.LINEAR  # LINEAR, LOG
View2DAtts.yScale = View2DAtts.LINEAR  # LINEAR, LOG
View2DAtts.windowValid = 1
SetView2D(View2DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.53425, 0.25477, 0.80602)
View3DAtts.focus = (0, 0, 0)
View3DAtts.viewUp = (-0.0432382, 0.96049, -0.274936)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 190.526
View3DAtts.nearPlane = -381.051
View3DAtts.farPlane = 381.051
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, 0)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
# End spontaneous state

DrawPlots()
ThreeSliceAtts = ThreeSliceAttributes()
ThreeSliceAtts.x = 100
ThreeSliceAtts.y = 2
ThreeSliceAtts.z = 3
ThreeSliceAtts.interactive = 1
SetOperatorOptions(ThreeSliceAtts, 0, 1)
OpenDatabase("localhost:/home/imenko_prezimenovic/visit/bin/MCNPplugin/testData/meshtal.mcnp", 0)
# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.0196365, 0.217799, 0.975796)
View3DAtts.focus = (0, 0, 0)
View3DAtts.viewUp = (-0.0540895, 0.974324, -0.218559)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 190.526
View3DAtts.nearPlane = -381.051
View3DAtts.farPlane = 381.051
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, 0)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.679732, 0.198232, 0.706165)
View3DAtts.focus = (0, 0, 0)
View3DAtts.viewUp = (-0.0536601, 0.973645, -0.221666)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 190.526
View3DAtts.nearPlane = -381.051
View3DAtts.farPlane = 381.051
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, 0)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.560283, 0.219748, 0.79862)
View3DAtts.focus = (0, 0, 0)
View3DAtts.viewUp = (-0.0542516, 0.971831, -0.229348)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 190.526
View3DAtts.nearPlane = -381.051
View3DAtts.farPlane = 381.051
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, 0)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
# End spontaneous state

RemoveOperator(0, 1)
AddOperator("SphereSlice", 1)
SphereSliceAtts = SphereSliceAttributes()
SphereSliceAtts.origin = (0, 100, 50)
SphereSliceAtts.radius = 150
SetOperatorOptions(SphereSliceAtts, 0, 1)
DrawPlots()
OpenDatabase("localhost:/home/imenko_prezimenovic/visit/bin/MCNPplugin/testData/meshtal.mcnp", 0)
# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.462578, -0.777058, 0.426852)
View3DAtts.focus = (0, 0, 0)
View3DAtts.viewUp = (0.564356, 0.629398, 0.534191)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 190.526
View3DAtts.nearPlane = -381.051
View3DAtts.farPlane = 381.051
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, 0)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.375227, -0.926637, -0.0234297)
View3DAtts.focus = (0, 0, 0)
View3DAtts.viewUp = (0.555095, 0.204391, 0.806284)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 190.526
View3DAtts.nearPlane = -381.051
View3DAtts.farPlane = 381.051
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, 0)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.262692, -0.962072, -0.0735552)
View3DAtts.focus = (0, 0, 0)
View3DAtts.viewUp = (0.586056, 0.0985318, 0.804257)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 190.526
View3DAtts.nearPlane = -381.051
View3DAtts.farPlane = 381.051
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, 0)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
# End spontaneous state

PseudocolorAtts = PseudocolorAttributes()
PseudocolorAtts.scaling = PseudocolorAtts.Log  # Linear, Log, Skew
PseudocolorAtts.skewFactor = 1
PseudocolorAtts.limitsMode = PseudocolorAtts.OriginalData  # OriginalData, CurrentPlot
PseudocolorAtts.minFlag = 0
PseudocolorAtts.min = 0
PseudocolorAtts.useBelowMinColor = 0
PseudocolorAtts.belowMinColor = (0, 0, 0, 255)
PseudocolorAtts.maxFlag = 0
PseudocolorAtts.max = 1
PseudocolorAtts.useAboveMaxColor = 0
PseudocolorAtts.aboveMaxColor = (0, 0, 0, 255)
PseudocolorAtts.centering = PseudocolorAtts.Natural  # Natural, Nodal, Zonal
PseudocolorAtts.colorTableName = "Default"
PseudocolorAtts.invertColorTable = 0
PseudocolorAtts.opacityType = PseudocolorAtts.FullyOpaque  # ColorTable, FullyOpaque, Constant, Ramp, VariableRange
PseudocolorAtts.opacityVariable = ""
PseudocolorAtts.opacity = 1
PseudocolorAtts.opacityVarMin = 0
PseudocolorAtts.opacityVarMax = 1
PseudocolorAtts.opacityVarMinFlag = 0
PseudocolorAtts.opacityVarMaxFlag = 0
PseudocolorAtts.pointSize = 0.05
PseudocolorAtts.pointType = PseudocolorAtts.Point  # Box, Axis, Icosahedron, Octahedron, Tetrahedron, SphereGeometry, Point, Sphere
PseudocolorAtts.pointSizeVarEnabled = 0
PseudocolorAtts.pointSizeVar = "default"
PseudocolorAtts.pointSizePixels = 2
PseudocolorAtts.lineType = PseudocolorAtts.Line  # Line, Tube, Ribbon
PseudocolorAtts.lineWidth = 0
PseudocolorAtts.tubeResolution = 10
PseudocolorAtts.tubeRadiusSizeType = PseudocolorAtts.FractionOfBBox  # Absolute, FractionOfBBox
PseudocolorAtts.tubeRadiusAbsolute = 0.125
PseudocolorAtts.tubeRadiusBBox = 0.005
PseudocolorAtts.tubeRadiusVarEnabled = 0
PseudocolorAtts.tubeRadiusVar = ""
PseudocolorAtts.tubeRadiusVarRatio = 10
PseudocolorAtts.tailStyle = PseudocolorAtts.None  # None, Spheres, Cones
PseudocolorAtts.headStyle = PseudocolorAtts.None  # None, Spheres, Cones
PseudocolorAtts.endPointRadiusSizeType = PseudocolorAtts.FractionOfBBox  # Absolute, FractionOfBBox
PseudocolorAtts.endPointRadiusAbsolute = 0.125
PseudocolorAtts.endPointRadiusBBox = 0.05
PseudocolorAtts.endPointResolution = 10
PseudocolorAtts.endPointRatio = 5
PseudocolorAtts.endPointRadiusVarEnabled = 0
PseudocolorAtts.endPointRadiusVar = ""
PseudocolorAtts.endPointRadiusVarRatio = 10
PseudocolorAtts.renderSurfaces = 1
PseudocolorAtts.renderWireframe = 0
PseudocolorAtts.renderPoints = 0
PseudocolorAtts.smoothingLevel = 0
PseudocolorAtts.legendFlag = 1
PseudocolorAtts.lightingFlag = 1
PseudocolorAtts.wireframeColor = (0, 0, 0, 0)
PseudocolorAtts.pointColor = (0, 0, 0, 0)
SetPlotOptions(PseudocolorAtts)
PseudocolorAtts = PseudocolorAttributes()
PseudocolorAtts.scaling = PseudocolorAtts.Linear  # Linear, Log, Skew
PseudocolorAtts.skewFactor = 1
PseudocolorAtts.limitsMode = PseudocolorAtts.OriginalData  # OriginalData, CurrentPlot
PseudocolorAtts.minFlag = 0
PseudocolorAtts.min = 0
PseudocolorAtts.useBelowMinColor = 0
PseudocolorAtts.belowMinColor = (0, 0, 0, 255)
PseudocolorAtts.maxFlag = 0
PseudocolorAtts.max = 1
PseudocolorAtts.useAboveMaxColor = 0
PseudocolorAtts.aboveMaxColor = (0, 0, 0, 255)
PseudocolorAtts.centering = PseudocolorAtts.Natural  # Natural, Nodal, Zonal
PseudocolorAtts.colorTableName = "Default"
PseudocolorAtts.invertColorTable = 0
PseudocolorAtts.opacityType = PseudocolorAtts.FullyOpaque  # ColorTable, FullyOpaque, Constant, Ramp, VariableRange
PseudocolorAtts.opacityVariable = ""
PseudocolorAtts.opacity = 1
PseudocolorAtts.opacityVarMin = 0
PseudocolorAtts.opacityVarMax = 1
PseudocolorAtts.opacityVarMinFlag = 0
PseudocolorAtts.opacityVarMaxFlag = 0
PseudocolorAtts.pointSize = 0.05
PseudocolorAtts.pointType = PseudocolorAtts.Point  # Box, Axis, Icosahedron, Octahedron, Tetrahedron, SphereGeometry, Point, Sphere
PseudocolorAtts.pointSizeVarEnabled = 0
PseudocolorAtts.pointSizeVar = "default"
PseudocolorAtts.pointSizePixels = 2
PseudocolorAtts.lineType = PseudocolorAtts.Line  # Line, Tube, Ribbon
PseudocolorAtts.lineWidth = 0
PseudocolorAtts.tubeResolution = 10
PseudocolorAtts.tubeRadiusSizeType = PseudocolorAtts.FractionOfBBox  # Absolute, FractionOfBBox
PseudocolorAtts.tubeRadiusAbsolute = 0.125
PseudocolorAtts.tubeRadiusBBox = 0.005
PseudocolorAtts.tubeRadiusVarEnabled = 0
PseudocolorAtts.tubeRadiusVar = ""
PseudocolorAtts.tubeRadiusVarRatio = 10
PseudocolorAtts.tailStyle = PseudocolorAtts.None  # None, Spheres, Cones
PseudocolorAtts.headStyle = PseudocolorAtts.None  # None, Spheres, Cones
PseudocolorAtts.endPointRadiusSizeType = PseudocolorAtts.FractionOfBBox  # Absolute, FractionOfBBox
PseudocolorAtts.endPointRadiusAbsolute = 0.125
PseudocolorAtts.endPointRadiusBBox = 0.05
PseudocolorAtts.endPointResolution = 10
PseudocolorAtts.endPointRatio = 5
PseudocolorAtts.endPointRadiusVarEnabled = 0
PseudocolorAtts.endPointRadiusVar = ""
PseudocolorAtts.endPointRadiusVarRatio = 10
PseudocolorAtts.renderSurfaces = 1
PseudocolorAtts.renderWireframe = 0
PseudocolorAtts.renderPoints = 0
PseudocolorAtts.smoothingLevel = 0
PseudocolorAtts.legendFlag = 1
PseudocolorAtts.lightingFlag = 1
PseudocolorAtts.wireframeColor = (0, 0, 0, 0)
PseudocolorAtts.pointColor = (0, 0, 0, 0)
SetPlotOptions(PseudocolorAtts)
RemoveOperator(0, 1)
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/home/imenko_prezimenovic/.visit/crash_recovery.16193.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
DrawPlots()
