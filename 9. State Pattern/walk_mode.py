from transport_mode import TransportMode


class WalkMode(TransportMode):
    def eta(self):
        print("Walk will take 30 mins")

    def directions(self):
        print("Walk right to the road and then left")
