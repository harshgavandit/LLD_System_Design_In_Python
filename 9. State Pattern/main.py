from transport_Service import TransportService
from bike_mode import BikeMode

b = BikeMode()
transport_service = TransportService(b)
transport_service.eta()
transport_service.directions()
