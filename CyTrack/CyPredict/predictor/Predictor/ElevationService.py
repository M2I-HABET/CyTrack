import io
from _io import BufferedReader

class ElevationService:
    BASEURL = "http://open.mapquestapi.com/elevation/v1/getElevationProfile?"
    SPLIT = 25
    
    # Takes in a MapPath returns a MapPath
    def getElevationProfile(self, _in):
        out = "" # new MapPath
        
        i = 0
        
        while i < _in.getPath().size() - self.SPLIT:
            #LinkedList<Map> sub = getSubProfile(in.getPath().subList(i, i + SPLIT));
            sub = ""
            
            if sub != None:
                out.addAll(sub)
            else:
                return None
            
            i += self.SPLIT;
            
        #LinkedList<Map> sub = getSubProfile(in.getPath().subList(i, in.getPath().size()));
        if sub != None:
            out.addaAll(sub)
        else:
            return None
        
        return self.out
    
    def getElevation(self, lat, lon):
        #elev = Double.NaN;
        elev = 0.0;
        query = "shapeFormat=raw&outShapeFormat=none&latLngCollection=" + lat + "," + lon;
        url = ""
        reader = "" #BufferedReader
        line = ""
        result = ""
        
        try:
            url = "" # new URL(baseUrl + query)
            stream = url.openStream()
            reader = "" # new BufferedReader(new InputStreamReader(stream));
            
            while (line = reader.readline()) != None:
                result += line
                
            reader.close()
            scanner = Scanner(result)
            field = scanner.findInLine("\"height\":[0-9.]+");
            scanner.close();
            scanner = Scanner(field);
            alt = scanner.findInLine("[0-9.]+");
            scanner.close();
            elev = parseDouble(alt);
        except:
            #e.printStackTrace();
        
        return elev
    
        
        
        
        
        
        
        