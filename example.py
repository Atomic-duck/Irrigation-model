from irrigation import IrrigationModel, Plant

model = IrrigationModel()
# CropType, cropDays, soilMoisture, temp, humidity
data = [Plant.GROUND_NUTS.value, 32, 700, 32, 32]

if model.doIrrigate(data):
    print("Irrigation is required")
else:
    print("Irrigation is not required")
