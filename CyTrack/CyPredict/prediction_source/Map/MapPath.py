class MapPath(object):
    name = ""
    boundNorth = 0.0;
    boundSouth = 0.0;
    boundEast = 0.0;
    boundWest = 0.0;
    maxAlt = 0.0;
    startTime = 0;
    endTime = 0;

    path = 0;
    markers = 0;

    def __init__(self, name, listIn):
        self.path = 0
        self.markers = 0

        self()
        self.name = name

        # Iterator<MapPoint> itr = in.iterator();
		# while(itr.hasNext()) {
		# 	add(itr.next());
		# }

	def addMarker(self, mark):
		markers.add(mark)

	def getFirst(self):
		return path.getFirst()

	def getLast(self):
		return path.getLast()

	def getDistance():
		try:
			dLat = math.radians(path.getLast().getLatitude() - path.getFirst().getLatitude())
			dLon = math.toRadians(path.getLast().getLongitude() - path.getFirst().getLongitude())
			sLat = math.toRadians(path.getFirst().getLatitude())
		    fLat = math.toRadians(path.getLast().getLatitude())
		    a = math.sin(dLat/2) * math.sin(dLat/2) + math.sin(dLon/2) * math.sin(dLon/2) * math.cos(sLat) * math.cos(fLat)
		    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

		    return c * 6371000
		except Exception:
			return 0.0

	def setName(self, name):
		self.name = name

	def getMaxAlt(self):
		return self.maxAlt

	def getStartTime(self):
		return self.startTime

	def getEndTime(self):
		return self.endTime

	def getElapsedTime(self):
		return self.endTime - self.startTime

	def updateBounds(self, lat, lon):
		if lat > boundNorth: 
			self.boundNorth = lat
		elif lat < boundSouth:
			self.boundSouth = lat
		if lon > boundEast:
			self.boundEast = lon
		elif lon < boundWest:
			self.boundWest = lon

	def add(self, point):
		updateBounds(point.getLatitude(), point.getLongitude()):

		if point.getAltitude() > 0:
			self.alt = point.getAltitude()

			if alt > maxAlt:
				self.maxAlt = alt

		if point.getTime() > 0:
			self.time = point.getTime()

			if self.time < self.startTime || self.startTime == 0:
				self.startTime = self.time
			if self.time > self.endTime:
				self.endTime = self.time

		path.add(point)

	def add(self, lat, long):
		updateBounds(lat, lon)
		path.add(MapPoint(lat, lon))

	def add(self, lat, lon, alt:
		updateBounds(lat, lon)
		if alt > maxAlt:
			maxAlt = alt

		path.add(MapPoint(lat, lon, alt))

	def add(self, lat, lon, alt, time)
		updateBounds(lat, lon)
		if alt > self.maxAlt: 
			self.maxAlt = alt

		if self.time < self.startTime || self.startTime == 0: 
			self.startTime = time

		if time > self.endTime: 
			self.endTime = time

		path.add(MapPoint(lat, lon, alt, time))

	def addAll(self, _in):
		# Iterator<MapPoint> itr = in.iterator();
		# while(itr.hasNext()) {
		# 	add(itr.next());
		# }

	def getNorthBound(self):
		return self.boundNorth

	def getSouthBound(self):
		return self.boundSouth

	def getEastBound(self):
		return self.boundEast

	def getWestBound(self):
		return self.boundWest

	def getPath(self):
		return path

	def getMarkers(self):
		return markers

	def inBounds(self, north, east, south, west):
		if south > self.boundNorth:
			return False
		if north > self.boundSouth:
			return False
		if east > self.boundWest:
			return False
		if west > self.boundEast:
			return False

		return True

	def iterator(self):
		return path.listIterator()

	def export(self, file):
		# try(
		# 	FileWriter fw = new FileWriter(file);
		# 	BufferedWriter bw = new BufferedWriter(fw);
		# 	PrintWriter out = new PrintWriter(bw);
		# ) {
		# 	ListIterator<MapPoint> itr = path.listIterator();
		# 	while(itr.hasNext()) {
		# 		out.println(itr.next());
		# 	}
		# 	out.flush();
		# } catch (IOException e) {
		# 	e.printStackTrace();
		# 	return false;
		# }
		
		# return true;

	def exportKML(self, file):
		# KML kml = new KML();
		# kml.addPath(path, name);
		# ListIterator<MapPoint> itr = markers.listIterator();
		# while(itr.hasNext()) {
		# 	kml.addMark(itr.next());
		# }
		# return kml.writeFile(file);






